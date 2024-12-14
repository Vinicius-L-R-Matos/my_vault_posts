import os
import re
import shutil
import subprocess
from datetime import datetime
import sys

# Paths
base_dir = r"D:\MyBlogStufs\matosdatascienceblog"
posts_dir = r"D:\Google Drive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\Google Drive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = os.path.join(base_dir, "content", "posts")
static_images_dir = os.path.join(base_dir, "static", "images")

# Verificar se está sendo executado pelo Obsidian
if len(sys.argv) > 2:
    python_script = sys.argv[0]  # caminho do script
    vault_path = sys.argv[1]     # caminho do vault
    file_path = sys.argv[2]      # arquivo atual
else:
    print("Executando fora do Obsidian")

def process_images():
    print("Processando imagens...")
    # Criar diretórios se não existirem
    for dir_path in [hugo_posts_dir, static_images_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Processar cada arquivo markdown
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            source_path = os.path.join(posts_dir, filename)
            with open(source_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Encontrar e processar imagens
            pattern = r'!\[\[([^]]*\.(png|jpg|jpeg|gif))(\|[^]]*?)?\]\]'
            images = re.findall(pattern, content)
            
            # Criar cópia modificada para o Hugo
            hugo_content = content
            for image_path, ext, style in images:
                # Determinar o estilo
                if style and '|logo' in style:
                    prefix = 'logo'
                elif style and '|profile' in style:
                    prefix = 'profile'
                else:
                    prefix = 'Image'
                
                # Construir o padrão original exato
                original_pattern = f"![[{image_path}{style}]]"
                markdown_image = f"![{prefix} Description](/images/{image_path.replace(' ', '%20')})"
                
                # Substituir no conteúdo
                hugo_content = hugo_content.replace(original_pattern, markdown_image)
                
                # Copiar imagem
                image_source = os.path.join(attachments_dir, image_path)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)
            
            # Salvar arquivo processado
            hugo_path = os.path.join(hugo_posts_dir, filename)
            with open(hugo_path, "w", encoding="utf-8") as file:
                file.write(hugo_content)
    
    return True

def execute_command(cmd):
    print(f"Executando: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {cmd}: {e}")
        return False

def execute_robocopy():
    """Executa robocopy para copiar posts"""
    cmd = f'robocopy "{posts_dir}" "{hugo_posts_dir}" /mir'
    print(f"\nExecutando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode <= 7  # Robocopy success codes are 0-7

def reset_and_update_site():
    """Reseta o Git e atualiza o site"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Limpar diretório public
    public_dir = os.path.join(base_dir, "public")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.makedirs(public_dir)
    
    # Primeiro: Executar robocopy
    if not execute_robocopy():
        print("Erro ao executar robocopy")
        return False
    
    commands = [
        # Segundo: Reset completo do repositório
        'git checkout --orphan temp_branch',
        'git add -A',
        f'git commit -m "Reset do blog em {current_time}"',
        'git branch -D master || true',
        'git branch -m master',
        'git push -f origin master',
        
        # Terceiro: Gerar o site Hugo
        'hugo',  # Gerar o site
        'hugo --minify',  # Minificar o site
        
        # Quarto: Verificar e commitar o site gerado
        'git add public -f',
        f'git commit -m "Site gerado em {current_time}"',
        'git push -f origin master',
        
        # Quinto: Atualizar branch hostinger
        'git subtree split --prefix public -b hostinger',
        'git push -f origin hostinger',
        
        # Sexto: Limpeza
        'git checkout master',
        'git branch -D hostinger',
        'git gc --aggressive --prune=now'
    ]
    
    for cmd in commands:
        print(f"\nExecutando: {cmd}")
        if not execute_command(cmd):
            print(f"Erro ao executar: {cmd}")
            return False
            
    # Verificar se index.html foi gerado
    index_path = os.path.join(public_dir, "index.html")
    if not os.path.exists(index_path):
        print("ERRO: index.html não foi gerado!")
        return False
        
    return True

def main():
    # Mudar para o diretório do projeto
    os.chdir(base_dir)

    # Processar imagens
    if not process_images():
        print("Erro ao processar imagens")
        return False

    # Reset Git e atualizar site
    if not reset_and_update_site():
        print("Erro ao atualizar site")
        return False

    print("Blog atualizado com sucesso!")
    return True

if __name__ == "__main__":
    main()