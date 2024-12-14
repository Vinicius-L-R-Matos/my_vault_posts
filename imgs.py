import os
import re
import shutil

# Paths
posts_dir = r"D:\Google Drive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\Google Drive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = r"D:\MyBlogStufs\matosdatascienceblog\content\posts"  # Novo diretório para os posts do Hugo
static_images_dir = r"D:\MyBlogStufs\matosdatascienceblog\static\images"

# Criar diretórios se não existirem
for dir_path in [hugo_posts_dir, static_images_dir]:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Processar cada arquivo markdown
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        # Ler arquivo original do Obsidian
        source_path = os.path.join(posts_dir, filename)
        with open(source_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Encontrar e processar imagens
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Criar cópia modificada para o Hugo
        hugo_content = content
        for image in images:
            # Substituir links apenas na cópia para o Hugo
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            hugo_content = hugo_content.replace(f"[[{image}]]", markdown_image)
            
            # Copiar imagem para o diretório static do Hugo
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
        
        # Salvar versão modificada no diretório do Hugo
        hugo_path = os.path.join(hugo_posts_dir, filename)
        with open(hugo_path, "w", encoding="utf-8") as file:
            file.write(hugo_content)

print("Arquivos processados e copiados com sucesso!")