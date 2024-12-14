import os
import re
import shutil
import subprocess
from datetime import datetime

# Paths
base_dir = r"D:\MyBlogStufs\matosdatascienceblog"
posts_dir = r"D:\Google Drive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\Google Drive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = os.path.join(base_dir, "content", "posts")
static_images_dir = os.path.join(base_dir, "static", "images")

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

def execute_robocopy():
    cmd = f'robocopy "{posts_dir}" "{hugo_posts_dir}" /mir'
    print(f"Executando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode <= 7

def execute_command(cmd):
    print(f"Executando: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {cmd}: {e}")
        return False

def git_commands():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [
        'git add .',
        f'git commit -m "Blog atualizado em {current_time}"',
        'git push origin master',
        'git subtree split --prefix public -b hostinger',
        'git push origin hostinger --force',
        'git branch -D hostinger'
    ]

def main():
    # Mudar para o diretório do projeto
    os.chdir(base_dir)

    # Processar imagens (sem robocopy)
    if not process_images():
        print("Erro ao processar imagens")
        return False

    # Gerar site Hugo
    if not execute_command('hugo --cleanDestinationDir'):
        return False

    # Executar comandos git
    for cmd in git_commands():
        if not execute_command(cmd):
            return False

    print("Blog atualizado com sucesso!")
    return True

if __name__ == "__main__":
    main()