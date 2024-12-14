---
title: "An Obsidian based blog system"

date: 2023-12-13

draft: false

tags: ["how_to", "obsidian", "blog"]

categories: ["tutorials"]

series: ["getting-started"]
---

## from: Vault's folder, to: Blog's feed 
This is my personal Blogging pipeline that whas thankfulli founded in the hands of the content creator NetWorkChuck, and can be found at this follow [link](https://www.youtube.com/watch?v=dnE7c0ELEH8&list=PLazumvohNo-2qvB49-9RL4karLMmqBDas&index=18). I hope it could find you to well, and help you too on express beter ideias to the word.

It serves well if you to like to have the control you publications and to have some code-based-automation fun!

What is happening here is that some obsidian valt is feeding the content of thouse publications that you are seeing now. In a process that thake a minimal effort once it have started.

And down below is how i made it.

## Why do it?
The CEO of [Anthropic](https://www.anthropic.com/) (a startup founded by former OpenAI members) and [Daniel Miessler](https://danielmiessler.com/) have some interesting ideas about AI, the future, and how it will affect our lives. In my view, this one seems particularly reasonable:  
![[daniel_miessler_x_post.png]]
From what I understand, as AI becomes more decentralized, it will become more efficient for people around the world to share ideas and create goods. And whether or not it’s currently hyped in the tech market, the benefits of open dialogue on improving the economy are widely recognized.

So, if we could use a Zettelkasten-like note system to extract our thoughts and then have an application that can draw directly from a vault to quickly and easily produce blog posts, that would be very helpful.

Like many discoveries throughout history, it all starts with just a few letters.

## How it works
The following chart demonstrates how it should be done:
![[blog_system.png]]
Is expected to:
- A post folder is feeded.
- Its content is "robocopyed" to the respective folder of the site's project.
- An frame work called Hugo transfers it Mardows to HTML files (And fome images to...)
- Is all uload to an remote repository's branch
- An host provider deliver it all!

## The Setup
- [Dowload](https://obsidian.md/download) and install Obsidian.
- On your regular Vault os Choice, Create a Folder called ==posts==. Here wil be where all your expressions can live!
- Make your Go acessible. If still dont, [dowload](https://go.dev/dl/) and install. It is necessary to make the Hugo work.
- [Dowload](https://gohugo.io/installation/) and install Hugo. It make possible to convert Markdown into HTML files when called. Use the lastest releases on the Prebuilt binaries section. Look up for a match on your OS.
- Extract hugo.exe. Copy and paste it on a new folder call ==Hugo==. Add this path to your Sistem Variable PATH.
- Make your Git acessible. If still dont, [dowload](https://git-scm.com/downloads) and install. It can handle diferent versions of you files.
- Iniciate a new empty repository where you create you new site with hugo. Configure you email and name for this git.
- Go to the [hugo themes](https://themes.gohugo.io/themes/) list and get one. Use one with ==Install theme as a submodule== on you terminal from the same directory for cloning it.
- Open the local hugo.toml and paste here the configurations that your chosen theme provide. Ignore module and so sections.

## Starting
- Navegate to where you whant to store you site files. Fron there in the terminal use: ==hugo new site [your_site_name]===.
- Inicialize hit repository in the roo of the site projetc, add name and email configs, and find your the theme. Here i chise the terminal:
```
  
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com" 
#Find a theme ---> https://themes.gohugo.io/ and clone it:
git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal
```
- paste inside hugo.toml file the configurations founded at the theme description site. Is att some "how to configure section". Make sure to skip module and so parts.
- Run ==hugo server -T [your_chosen_theme]== to see if it is working locally. Acess the server and celebrate! =]
- Open the content folder inside the site directory. Create a ==posts== folder. Inside content folder  use: ==robocopy "[source_path]" "[destination_path]" /mir==. 
- Back to the site's root and use ==hugo server== for your eyes only. =]. Inside ==public/post== are the html versions of  Obsidian's Markdown files.
- Go to the Obsidian's source mode on your note. Lets take some FrontMater | Metadata | Proprieties to it. Insert between --- and --- the title, date, draft(false) and some tags(this onde on -|bullets). If you like to, You can have some templater on and so... Use robocopy inside contents & hugo server inside root to see the efects!

## Images Attachments
- On you vault, put all your blog images inside an Attachments deficades folder
- Now i will put an totally perfect and precise image in this note. 
	![[smile.png]]
	If just do so, it wil be not consider like one to hugo. It need some temper. Spycy! =]
- Paste this script in a imgs.py file on the root of your site. Remember to replace the directories variables (I made some alterations, becose when i did use the Chuck's one, it modifies the original path):
```
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

```
- And create a ==static/images== folder. Run the python file and see if the image whas transfer!

## Test one
- You can save an automation, so when called, it can update and run all:
```
# update_blog.py
import os
import subprocess

# Diretório base do projeto
base_dir = r"my_blog_directori\matosdatascienceblog"

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
```

- I have also done a centralized run file to update all:
```
# update_blog.py
import os
import subprocess

# Diretório base do projeto
base_dir = r"my_blog_directori\matosdatascienceblog"

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
```

## Git and Github actions
- Now you need to autenticate your self at the github account. At ==cd ~/== find the ==.ssh== folder.  
- If is not your first time you wil find some files here, like a ==id_rsa== like a private one and a ==id_rsa.pub== like a public one. The public is what we gona upload to git hub.
- If is your firts time use to generate some: ==bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"==. The one thar you use to config this git. 
- If you have more than one, use: ==cat [key.pub]== or open as a text to get it SHA copy.
- Go to you git hub accont. Create blank private repo. Go to Settings. Register new pair off keys.
- Test if you are in, from inside .ssh folder, use: ==ssh -T git@github.com== and you should get a welcome mensage. 
- Now, from you repo root, use ==git remote add origin git@github.com:[your_username/repo_name.git]==.
- Use ==hugo== again.
- git add .
- git commit
- Only puplic folder is fot the host only. So thrn we need do take it to another branch. Use: 
```
git subtree split --prefix public -b hostinger-deploy
git push origin hostinger-deploy:hostinger --force
git branch -D hostinger-deploy
```

- And also put all inside a big one:
```
import os
import re
import shutil
import subprocess
from datetime import datetime

# Paths
base_dir = r"my_blog_directori\matosdatascienceblog"
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

    # Executar robocopy
    if not execute_robocopy():
        print("Erro crítico no robocopy")
        return False

    # Processar imagens
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

- Implement the repo manualy to someserver. Here i used a blck php one on hostinger. until make your self familiar to it.
## Host it
- Put your git URL by the folling steps on the form dependig it is private or public. this is a public one. So i used a ==https://github.com/my_git_user/my_repo.git==.
- Once is all working, Implemet manualy. If is working, click on the auto-implement button. A modal will appear, explanning a webhook URL(copy this one), and a link to configure it on you github account. acces id and paste onde the correspondenting field. Make no other chages and save it. It is done! It should work just fine as this one here is.
- You can also insert all by the python plugin! Confire as show in the Python Scripter!
- start blogging! =]

## Styling Your Blog - Custom Styles
To improve the visual appearance of your blog, especially for images, create a `layouts/partials/extended_head.html` file:
```
<style>
/* Estilo global para todas as imagens em posts e páginas */
.post-content img,
.page-content img,
.post img,
.page img {
    display: block;
    margin: 2rem auto;
    max-width: 100%;
    height: auto;
    width: 600px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

/* Hover effect suave */
.post-content img:hover,
.page-content img:hover,
.post img:hover,
.page img:hover {
    transform: scale(1.02);
}

/* Ajuste para imagens menores (como logos) */
.post-content img[alt*="logo"],
.page-content img[alt*="logo"],
.post img[alt*="logo"],
.page img[alt*="logo"] {
    width: 300px;
    box-shadow: none;
}

/* Ajuste para imagens de perfil */
.post-content img[alt*="profile"],
.page-content img[alt*="profile"],
.post img[alt*="profile"],
.page img[alt*="profile"] {
    width: 250px;
    border-radius: 50%;
    border: 3px solid #333;
}
</style>
```

Now, when posting an image, just ==| logo or profile== input in the description for the style you want on it:
```
<!-- Now you can use the first word to determinate the style! -->
<!-- normal images -->
![Description](/images/image.png)
<!-- To use it on vault -->
![[imagem.png]]

<!-- for logo -->
![logo Description](/images/logo.png)
<!-- To use it on vault -->
![[logo_imagem.png|logo]]

<!-- for profile images -->
![profile Description](/images/photo.jpg)
<!-- To use it on vault -->
![[perfil.jpg|profile]]
```
Select and use you favorite...
Make sure to get ==[markup.goldmark.renderer] unsafe = true== on the hugo.toml file.

### Creating About Page
Create a new file `content/about.md`:
```
---

title: "About"

date: 2023-12-13

draft: false

---
# About Me

!(profile Description)[profile_photo.png]

Hi! I'm [Your Name], a Data Scientist and Python Developer.

## Professional Background

I specialize in:

- Data Science

- Machine Learning

- Python Development

- Data Analysis

## Skills

### Programming Languages

- Python

- R

- SQL

### Tools & Technologies

- Pandas

- Scikit-learn

- TensorFlow

- Git

## Contact

You can find me on:

- GitHub

- LinkedIn
```


### Creating Projects Page
Create a new file `content/projects.md`:
```

---

title: "Projects"

date: 2023-12-13

draft: false

---

# Data Science Projects

## 🤖 Machine Learning Projects

### Blog Pipeline Automation

!project logo

- Tech Stack: Python, Hugo, Git

- Description: Automated blog deployment pipeline that converts Obsidian notes to Hugo posts

- Key Features:

- Automatic image processing

- Git integration

- Markdown conversion

- Automated deployment

### Other Project Name

- Tech Stack: Python, Pandas, Scikit-learn

- Description: Brief description of your project

- Key Features:

- Feature 1

- Feature 2

- Feature 3

## 📊 Data Analysis Projects

### Project Name

- Dataset: Description of data source

- Tools: Python, Pandas, Matplotlib

- Outcome: Key findings or results

## 📫 Interested in Collaboration?

Feel free to reach out if you're interested in collaborating on any projects:

- LinkedIn

- GitHub
```

## Auto run an update
- Install the Python scripter plugin. 
- Put you update.py inside .obsidian/scripts/python folder and point you global python version on python version
- reload obsidian an now you can run it from the Ctrl + P comands.
## Common Issues
- **Images not showing:** Check image path and case sensitivity
- **Styles not applying:** Verify extended_head.html location
- **Git errors:** Check SSH key configuration
- **Hugo server errors:** Verify Hugo version compatibility

## Regular Tasks
- Backup your Obsidian vault
- Update Hugo and theme versions
- Check Git repository size
- Monitor server logs

## Considerations
It was verry fun and joyfull to see this blog being construct. I hope you to do it, so you can also spread this ideias and help others!

## References
[I started a blog.....in 2024 (why you should too)](https://www.youtube.com/watch?v=dnE7c0ELEH8&list=PLazumvohNo-2qvB49-9RL4karLMmqBDas&index=18))

