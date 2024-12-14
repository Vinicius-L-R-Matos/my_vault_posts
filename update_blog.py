# update_blog.py
import os
import subprocess

# Diretório base do projeto
base_dir = r"D:\MyBlogStufs\matosdatascienceblog"

# Comandos a serem executados
commands = [
    f'robocopy "D:\Google Drive\DriveSyncFiles\Vault\posts" "{base_dir}\content\posts" /mir',
    'python imgs.py',
    'hugo server -t terminal'
]

# Mudar para o diretório do projeto
os.chdir(base_dir)

# Executar comandos em sequência
for cmd in commands:
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True)