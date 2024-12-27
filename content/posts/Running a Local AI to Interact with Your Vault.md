---
title: Running a Local AI to Interact with Your Vault
date: 2023-12-20
draft: false
tags:
  - how_to
  - obsidian
  - AI
categories:
  - tutorials
series:
  - Local
---

## From: Ollama Installation. To: AI Integration

Inspired once more by [NetworkChuck](https://www.youtube.com/watch?v=Wjrdr0NU4Sk), this guide walks you through setting up Ollama on your system, integrating various AI models, and enhancing your workflow with ==Stable Diffusion== and ==BMO== or ==Smart Connections== on obsidian. Whether you're a developer or an AI enthusiast, this step-by-step tutorial will help you harness the power of local AI models effectively.

If you also enjoy configuring your AI environment and exploring different models, this approach will provide you with the control and flexibility you need!

What’s happening here is that you’re setting up a local AI server using Ollama, complemented by a web UI for easier interaction and additional tools like Stable Diffusion for image generation. Once everything is configured, maintaining and expanding your AI capabilities requires minimal effort.

Below, I’ll show you how to set up Ollama, integrate various AI models, and enhance your setup with additional tools. You can follow these steps to create your personalized AI environment.

## Did you ever run an Ollama?
![logo Description](/images/ollama.png)
[Ollama](https://github.com/ollama/ollama/tree/main/docs) is a lightweight, extensible framework for building and running language models on the local machine. It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a variety of applications.

To get started right away, do the following:

1. **Visit Ollama's Website**
    - Go to [ollama.com](https://ollama.com/).

2. **Install WSL on Windows**
    
    - Open the Windows Command Prompt (CMD) and execute:
        ```
        wsl --install
        ```
    - If is the first time, create some auth there.

3. **Upgrade and Update Packages**
    - In your WSL terminal, run:
        ```
        sudo apt update
        sudo apt upgrade -y
        ```
        
4. **Download the Linux Version**
    - Copy and run the following command from ollama in your terminal:
        ```bash
        curl -fsSL https://ollama.com/install.sh | sh
        ```
        
5. **Verify Ollama is Running**
    - Open your web browser and navigate to:
        ```
        localhost:11434
        ```
    - You should see a message indicating that Ollama is running!
	- *Note: I think "11434" can be transleted as "llama" if you to bend 90º you neek. Once you to figure it out, maybe it won't come back...*

6. **Take care of you llamas**
	- To view all the AI models currently installed in your Ollama setup, use the following command:
        ```
		ollama list
        ```
	- If you don't what one of those anymore, you can always eliminate whit:
        ```
		ollama rm model_name
        ```

9. **Add an AI Model to Ollama**
    - Pull the Llama2 model:
        ```bash
        ollama pull model_name
        ```
        
7. **Run and Test the Model**
    - Execute the following command to test:
        ```bash
        ollama run model_name
        ```
        
    - You can interact with the model here. Press `Ctrl+C` to stop the response and type `/bye` to close the session.

## Web UI

The [Web UI](https://github.com/open-webui/open-webui) provides an interface to interact with your AI models more conveniently. There are several options available, and for this guide, we'll set up **Open Web UI** using Docker.

### Installing Docker

1. **Add Docker's Official GPG Key and Repository**
    ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

2. **Install Docker**
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

### Running the Web UI Container

1. **Start the Container**
    ```bash
    sudo docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```
	- If you need to stop it:
	```
	sudo docker stop open-webui
	sudo docker rm open-webui
	sudo docker stop $(sudo docker ps -q)
	
	```
1. **Verify the Container is Running**
    ```bash
    sudo docker ps
    ```
    - You should see a list of running containers, indicating that the Web UI is available at:
        ```
        http://localhost:8080/auth
        ```
    - Create a local access credential. The first login uses the `admin` account.
    - Connection settings can be found under `Settings` -> `Connections`.
    
## Adding More Models

1. **Pull Additional Models via Ollama**
    ```bash
    ollama pull codegen
    ```
    - After installation, the model will be available in the Web UI's selection box.

## Managing Access

You can manage user access through the admin panel:
1. **Access the Admin Panel**
    - Click on the bottom-left logo and navigate to the admin section.
2. **Manage Users and Groups**
    - In the `Users` section, create and assign users to specific groups to control access permissions.

## Creating Custom Models
To create your own models:
1. **Access the Workspace**
    - Navigate to the workspace and click the `+` button on the top-right corner to add a new model.

## Using AI into the Vault
### Adding AI to Smart Connections
1. **Configure Local AI in Chat Settings**
    - Select the `Local` option and choose the desired model name from the chat configuration settings.

### BMO option
Installing the BMO plugin will enable the default chosen model. The available commands are:
#### General Commands

- `/clear` or `/c` - Clear chat history.
- `/ref on` - Turn on "reference current note".
- `/ref off` - Turn off "reference current note".
- `/maxtokens [VALUE]` - Set max tokens.
- `/temp [VALUE]` - Change temperature range from 0 to 2.

#### Profile Commands

- `/profile` - List profiles.
- `/profile [PROFILE-NAME] or [VALUE]` - Change profile.

#### Model Commands
- `/model` - List models.
- `/model [MODEL-NAME] or [VALUE]` - Change model.

#### Prompt Commands
- `/prompt` - List prompts.
- `/prompt [PROMPT-NAME] or [VALUE]` - Change prompts.
- `/prompt clear` - Clear prompt.

#### Editor Commands
- `/append` - Append current chat history to the current active note.
- `/save` - Save current chat history to a note.
- `/load` - List or load a chat history into view.

#### Response Commands
- `/stop` or `/s` - Stop fetching response. **Warning:** Anthropic models cannot be aborted. Use with caution.

### Call queries from Python Scripter
If you like to play some hard code, you can to try to run the script direct from the control painel, or even from the cmd. This is what i come trougth:

```bash
"""
Script de Atualização de Blog Hugo
=================================

Este script automatiza o processo de atualização de um blog Hugo, realizando as seguintes tarefas:
1. Processamento de imagens do Obsidian para o formato Hugo
2. Geração do site Hugo
3. Atualização do repositório Git

Requisitos
----------
- Python 3.6+
- Hugo instalado e configurado
- Git instalado e configurado
- Acesso aos diretórios necessários

Estrutura de Diretórios
----------------------
- posts_dir: Diretório contendo os posts do Obsidian
- attachments_dir: Diretório com as imagens do Obsidian
- hugo_posts_dir: Diretório de posts do Hugo
- static_images_dir: Diretório de imagens estáticas do Hugo

Uso
---
O script pode ser executado de duas formas:

1. Via Python Scripter (Obsidian):
   O plugin fornecerá automaticamente os argumentos:
   - sys.argv[1]: Caminho do vault
   - sys.argv[2]: Caminho do arquivo

2. Via linha de comando:
   ```
   python update_blog.py
   ```

Funcionalidades Principais
------------------------
process_images():
    Processa as imagens do Obsidian para o formato Hugo:
    - Converte links de imagem do formato Obsidian (![Image Description](/images/imagem.png)) para Markdown
    - Copia as imagens para o diretório estático do Hugo
    - Suporta estilos especiais (logo, profile)

execute_command(cmd):
    Executa comandos do sistema de forma segura

git_commands():
    Lista de comandos Git para atualização do repositório:
    - Adiciona alterações
    - Realiza commit com timestamp
    - Push para branch master
    - Atualiza branch hostinger

main():
    Função principal que orquestra todo o processo de atualização

Configurações
------------
Paths principais (podem ser modificados conforme necessário):
- base_dir: D:\MyBlogStufs\matosdatascienceblog
- posts_dir: D:\Google Drive\DriveSyncFiles\Vault\posts
- attachments_dir: D:\Google Drive\DriveSyncFiles\Vault\Attachments

Observações
----------
- O script assume uma estrutura específica de diretórios
- Necessário ter permissões de escrita nos diretórios
- Git deve estar configurado com as credenciais corretas
- Hugo deve estar instalado e acessível via linha de comando

Tratamento de Erros
-----------------
- Verifica existência de diretórios
- Valida execução de comandos
- Fornece feedback sobre operações realizadas
"""

"""
python 3.12.7
pip freeze:
asttokens==3.0.0
bitsandbytes==0.45.0
certifi==2024.12.14
charset-normalizer==3.4.0
colorama==0.4.6
contourpy==1.3.1
cycler==0.12.1
decorator==5.1.1
et_xmlfile==2.0.0
executing==2.1.0
filelock==3.16.1
fonttools==4.55.3
fsspec==2024.12.0
fuzzywuzzy==0.18.0
huggingface-hub==0.27.0
idna==3.10
ipython==8.31.0
jedi==0.19.2
Jinja2==3.1.4
jsonpickle==4.0.1
kiwisolver==1.4.7
Levenshtein==0.26.1
MarkupSafe==3.0.2
matplotlib==3.10.0
matplotlib-inline==0.1.7
mpmath==1.3.0
networkx==3.4.2
numpy==2.2.0
openpyxl==3.1.5
packaging==24.2
pandas==2.2.3
parso==0.8.4
pillow==11.0.0
prompt_toolkit==3.0.48
pure_eval==0.2.3
Pygments==2.18.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
python-Levenshtein==0.26.1
python-louvain==0.16
pytz==2024.2
pyvis==0.3.2
PyYAML==6.0.2
RapidFuzz==3.11.0
regex==2024.11.6
requests==2.32.3
safetensors==0.4.5
scipy==1.14.1
setuptools==75.6.0
six==1.17.0
stack-data==0.6.3
sympy==1.13.1
tokenizers==0.21.0
torch==2.5.1
tqdm==4.67.1
traitlets==5.14.3
transformers==4.47.1
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
wcwidth==0.2.13
"""
import os
import re
import shutil
import subprocess
from datetime import datetime
import sys

# Define valores padrão para os caminhos
DEFAULT_VAULT_PATH = r"D:\Google Drive\DriveSyncFiles\Vault"
DEFAULT_FILE_PATH = ""

# Tenta obter argumentos do Obsidian, se não existirem usa os valores padrão
try:
    python_script = sys.argv[0]  # caminho do script
    vault_path = sys.argv[1]     # caminho do vault
    file_path = sys.argv[2]      # caminho do arquivo
except IndexError:
    vault_path = DEFAULT_VAULT_PATH
    file_path = DEFAULT_FILE_PATH

 
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
```

This whay i can ask some question, make conection to some ideias an talk whit you data. All by your self. It work fine.In my case better than any plugin. 
The last created file on the self_questions folder is anwsered in the self_grahs one. If some graphs are out put, they are stored at self_graphs. Like this one bellow:
![logo Description](/images/self_graph.png)
## Summary
This guide provides a comprehensive walkthrough for setting up Ollama on your local machine, integrating various AI models, managing user access, and enhancing your setup with tools like Stable Diffusion and BMO. By following these steps, you can create a robust and flexible AI environment tailored to your specific needs.

### Common Issues
- **Ollama not running:** Ensure the installation script executed without errors and that WSL is properly installed.
- **Docker issues:** Verify Docker is installed correctly and that the Docker daemon is running.
- **Model not appearing in Web UI:** Ensure the model was pulled successfully using `ollama pull [model_name]`.
- **Stable Diffusion installation errors:** Check that all prerequisites are installed and that Pyenv is configured correctly.

### Regular Tasks
- **Update AI models:** Regularly pull updates for your AI models using Ollama.
- **Backup configurations:** Keep backups of your Docker configurations and AI models.
- **Monitor system resources:** Ensure your system can handle the resource demands of running multiple AI models.

### Considerations
Setting up a local AI environment provides greater control over your data and models. It allows for customization and integration with various tools, enhancing productivity and enabling advanced functionalities. While the initial setup requires technical knowledge, the long-term benefits make it a worthwhile investment for AI enthusiasts and professionals alike.

## References
- [Host All Your AI Locally](https://www.youtube.com/watch?v=Wjrdr0NU4Sk)
