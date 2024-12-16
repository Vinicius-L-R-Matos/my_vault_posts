---
title: "An Obsidian based blog system"

date: 2023-12-13

draft: false

tags: ["how_to", "obsidian", "blog"]

categories: ["tutorials"]

series: ["getting-started"]
---

## From: Vault's folder. To: Blog's feed 
aaaaaaaaaaaaaaaa
This is my personal blogging pipeline, which I thankfully discovered through the content creator [NetWorkChuck](https://www.youtube.com/watch?v=dnE7c0ELEH8&list=PLazumvohNo-2qvB49-9RL4karLMmqBDas&index=18). I hope this pipeline also proves useful to you, helping you express better ideas to the world.

If you enjoy maintaining control over your publications and having some code-based automation fun, this approach should serve you well!

What’s happening here is that an Obsidian vault is feeding the content of the posts you’re reading right now. Once everything is set up, the process requires minimal effort to keep running smoothly.

I’ve used a [fastpages](https://vinicius-l-r-matos.github.io/-Repositorio-DS/) blog for the last 3 years. While it was very functional, it became a bit annoying not having full control over all the errors that occurred in Jekyll. And since it officially migrated to [Quarto](https://quarto.org/), I no longer had my familiar framework for transcribing my markdown files into posts. However, I had a great experience using Obsidian and decided to share what I learned.

Below, I’ll show you how I built this blog and how everything works.

## Why do it?
The CEO of [Anthropic](https://www.anthropic.com/)—a startup founded by former OpenAI members— mister [Daniel Miessler](https://danielmiessler.com/) have shared some interesting perspectives on AI, the future, and how these technologies will shape our lives. In my view, this particular idea seems especially reasonable one:
![Image Description](/images/daniel_miessler_x_post.png)
From my understanding, as AI becomes more decentralized, it will become increasingly efficient for people around the world to share ideas and create goods. Regardless of whether it’s currently hyped in the tech market, the benefits of open dialogue on improving the economy are widely recognized.

So, if we could use a Zettelkasten-like note system to capture our thoughts and then have an application draw directly from a vault to quickly and easily produce blog posts, that would be incredibly helpful and productive.

As with many discoveries throughout history, it all starts with just a few letters.
## How it works
The following chart demonstrates how it’s done:
![Image Description](/images/blog_system.png)
Putting it into a few words, it is expected that:

- A post folder is provided.
- Its content is “robocopied” to the appropriate folder in the site’s project.
- A framework called Hugo transforms the Markdown files (and some images, too) into HTML.
- Everything is uploaded to a branch of a remote repository.
- A hosting provider delivers it all!

## The Materials
The following are needed and will be explained—along with their downloads, installations, and setups—in the next sections:
- Obsidian
- Git
- Git hub
- Hugo
- Host site
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
- Run ==hugo server -r [your_chosen_theme]== to see if it is working locally. Acess the server and celebrate! =]
- Open the content folder inside the site directory. Create a ==posts== folder. Inside content folder  use: ==robocopy "[source_path]" "[destination_path]" /mir==. 
- Back to the site's root and use ==hugo server== for your eyes only. =]. Inside ==public/post== are the html versions of  Obsidian's Markdown files.
- Go to the Obsidian's source mode on your note. Lets take some FrontMater | Metadata | Proprieties to it. Insert between --- and --- the title, date, draft(false) and some tags(this onde on -|bullets). If you like to, You can have some templater on and so... Use robocopy inside contents & hugo server inside root to see the efects!

## Images Attachments
- On you vault, put all your blog images inside an Attachments deficades folder
- Now i will put an totally perfect and precise image in this note. 
	![Image Description](/images/smile.png)
	If just do so, it wil be not consider like one to hugo. It need some temper. Spycy! =]
- Paste this script in a imgs.py file on the root of your site. Remember to replace the directories variables (I made some alterations, becose when i did use the Chuck's one, it modifies the original path):
```
import os
import re
import shutil

# Paths
posts_dir = r"D:\Google Drive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\Google Drive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = r"D:\MyBlogStufs\matosdatascienceblog\content\posts"  # New directpry for Hugo
static_images_dir = r"D:\MyBlogStufs\matosdatascienceblog\static\images"

# Create if not exists
for dir_path in [hugo_posts_dir, static_images_dir]:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Process every mardown file
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        # Read original file from Obsidian
        source_path = os.path.join(posts_dir, filename)
        with open(source_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Find and process images
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Make hugo on each one
        hugo_content = content
        for image in images:
            # Replace links only for Hugo's one
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            hugo_content = hugo_content.replace(f"[[{image}]]", markdown_image)
            
            # Copy image for static on Hugo
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
        
        # Save in the hupo dir
        hugo_path = os.path.join(hugo_posts_dir, filename)
        with open(hugo_path, "w", encoding="utf-8") as file:
            file.write(hugo_content)

print("Files processed end copy!")
```
- And create a ==static/images== folder. Run the python file and see if the image whas transfer!

## Test one
- You can save an automation, so when called, it can update and run all:
```
# update_blog.py
import os 
import subprocess 

# Base directory of the project 
base_dir = r"my_blog_directory\my_data_science_blog" 

# Commands to execute commands = [ 
	f'robocopy "D:\\GoogleDrive\\DriveSyncFiles\\Vault\\posts" "{base_dir}\\content\\posts" /mir', 
	'python imgs.py', 
	'hugo server -t terminal' 
] 

# Change to the project directory 
os.chdir(base_dir) 

# Execute commands in sequence 
for cmd in commands:
	print(f"Executing: {cmd}") subprocess.run(cmd, shell=True)
```

- And also do a centralized run file to update all:
```
# update_blog.py
import os
import subprocess

# Base directory of the project
base_dir = r"my_blog_directory\my_data_science_blog"

# Commands to be executed
commands = [
    f'robocopy "D:\\Google Drive\\DriveSyncFiles\\Vault\\posts" "{base_dir}\\content\\posts" /mir',
    'python imgs.py',
    'hugo server -t terminal'
]

# Change to the project directory
os.chdir(base_dir)

# Execute commands in sequence
for cmd in commands:
    print(f"Executing: {cmd}")
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

- And also put all inside a the big one:
```
import os
import re
import shutil
import subprocess
from datetime import datetime

# Paths
base_dir = r"my_blog_directory\my_data_science_blog"
posts_dir = r"D:\GoogleDrive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\GoogleDrive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = os.path.join(base_dir, "content", "posts")
static_images_dir = os.path.join(base_dir, "static", "images")

def process_images():
    print("Processing images...")
    # Create directories if they do not exist
    for dir_path in [hugo_posts_dir, static_images_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Process each markdown file
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            # Read the original Obsidian file
            source_path = os.path.join(posts_dir, filename)
            with open(source_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Find and process images
            images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
            
            # Create a modified copy for Hugo
            hugo_content = content
            for image in images:
                # Replace links in the Hugo version only
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                hugo_content = hugo_content.replace(f"[[{image}]]", markdown_image)
                
                # Copy image to the Hugo static directory
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)
            
            # Save the modified version in the Hugo directory
            hugo_path = os.path.join(hugo_posts_dir, filename)
            with open(hugo_path, "w", encoding="utf-8") as file:
                file.write(hugo_content)
    
    print("Files processed and copied successfully!")
    return True

def execute_robocopy():
    cmd = f'robocopy "{posts_dir}" "{hugo_posts_dir}" /mir'
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode <= 7

def execute_command(cmd):
    print(f"Executing: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing {cmd}: {e}")
        return False

def git_commands():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [
        'git add .',
        f'git commit -m "Blog updated at {current_time}"',
        'git push origin master',
        'git subtree split --prefix public -b hostinger',
        'git push origin hostinger --force',
        'git branch -D hostinger'
    ]

def main():
    # Change to the project directory
    os.chdir(base_dir)

    # Execute robocopy
    if not execute_robocopy():
        print("Critical error in robocopy")
        return False

    # Process images
    if not process_images():
        print("Error processing images")
        return False

    # Generate the Hugo site
    if not execute_command('hugo --cleanDestinationDir'):
        return False

    # Execute git commands
    for cmd in git_commands():
        if not execute_command(cmd):
            return False

    print("Blog successfully updated!")
    return True

if __name__ == "__main__":
    main()
```

- Implement the repo manualy to someserver. Until make your self familiar to it. Then you can host it. Here i used a blank php one on hostinger. 
## Host it
- Put your git URL by the folling steps on the form dependig it is private or public. this is a public one. So i used a ==https://github.com/my_git_user/my_repo.git==.
- Once is all working, Implemet manualy. If is working, click on the auto-implement button. A modal will appear, explanning a webhook URL(copy this one), and a link to configure it on you github account. acces id and paste onde the correspondenting field. Make no other chages and save it. It is done! It should work just fine as this one here is.
- You can also insert all by the python plugin! Confire as show in the Python Scripter!
- start blogging! =]

## Styling Your Blog - Custom Styles
To improve the visual appearance of your blog, especially for images, create a `layouts/partials/extended_head.html` file:
```
<style>
/* Global style for all images in posts and pages */
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

/* Smooth hover effect */
.post-content img:hover,
.page-content img:hover,
.post img:hover,
.page img:hover {
    transform: scale(1.02);
}

/* Adjustments for smaller images (such as logos) */
.post-content img[alt*="logo"],
.page-content img[alt*="logo"],
.post img[alt*="logo"],
.page img[alt*="logo"] {
    width: 300px;
    box-shadow: none;
}

/* Adjustments for profile images */
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
<!-- Now you can use the first word in the Vault image call to determinate the style! -->

<!-- normal images in the blog -->
![Description](/images/image.png)
<!-- use it on vault -->
![Image Description](/images/imagem.png)

<!-- for logo in the blog -->
![logo Description](/images/logo.png)
<!-- use it on vault -->
![logo Description](/images/logo_imagem.png)

<!-- for profile images in the blog -->
![profile Description](/images/photo.jpg)
<!-- use it on vault -->
![profile Description](/images/perfil.jpg)
```
Select and use you favorite. Make sure to get ==[markup.goldmark.renderer] unsafe = true== on the hugo.toml file.

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

Hi! 

<!-- All other stuffs -->
```
### Creating Projects Page
Create a new file `content/projects.md`:
```

---

title: "Projects"

date: 2023-12-13

draft: false

---

#  Projects

<!-- All other stuffs -->
```

## Auto run an update
- Install the Python scripter plugin. 
- Put you update.py inside .obsidian/scripts/python folder and point you global python version on python version. And here is my contribuition to it:
```
import os
import re
import shutil
import subprocess
from datetime import datetime
import sys

# Receive arguments from Obsidian
python_script = sys.argv[0]  # script path
vault_path = sys.argv[1]     # vault path
file_path = sys.argv[2]      # file path

# Paths
base_dir = r"D:\MyBlogDirectory\my_data_science_blog"
posts_dir = r"D:\GoogleDrive\DriveSyncFiles\Vault\posts"
attachments_dir = r"D:\GoogleDrive\DriveSyncFiles\Vault\Attachments"
hugo_posts_dir = os.path.join(base_dir, "content", "posts")
static_images_dir = os.path.join(base_dir, "static", "images")

def process_images():
    print("Processing images...")
    # Create directories if they do not exist
    for dir_path in [hugo_posts_dir, static_images_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Process each markdown file
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            source_path = os.path.join(posts_dir, filename)
            with open(source_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Find and process images
            pattern = r'!\[\[([^]]*\.(png|jpg|jpeg|gif))(\|[^]]*?)?\]\]'
            images = re.findall(pattern, content)
            
            # Create a modified copy for Hugo
            hugo_content = content
            for image_path, ext, style in images:
                # Determine style
                if style and '|logo' in style:
                    prefix = 'logo'
                elif style and '|profile' in style:
                    prefix = 'profile'
                else:
                    prefix = 'Image'
                
                # Build the exact original pattern
                original_pattern = f"![[{image_path}{style}]]"
                markdown_image = f"![{prefix} Description](/images/{image_path.replace(' ', '%20')})"
                
                # Replace in the Hugo content
                hugo_content = hugo_content.replace(original_pattern, markdown_image)
                
                # Copy the image
                image_source = os.path.join(attachments_dir, image_path)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)
            
            # Save the processed file
            hugo_path = os.path.join(hugo_posts_dir, filename)
            with open(hugo_path, "w", encoding="utf-8") as file:
                file.write(hugo_content)
    
    return True

def execute_command(cmd):
    print(f"Executing: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing {cmd}: {e}")
        return False

def git_commands():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [
        'git add .',
        f'git commit -m "Blog updated at {current_time}"',
        'git push origin master',
        'git subtree split --prefix public -b hostinger',
        'git push origin hostinger --force',
        'git branch -D hostinger'
    ]

def main():
    # Change to the project directory
    os.chdir(base_dir)

    # Process images (without robocopy)
    if not process_images():
        print("Error processing images")
        return False

    # Generate the Hugo site
    if not execute_command('hugo --cleanDestinationDir'):
        return False

    # Execute git commands
    for cmd in git_commands():
        if not execute_command(cmd):
            return False

    print("Blog successfully updated!")
    return True

if __name__ == "__main__":
    main()
```
- reload obsidian an now you can run it from the Ctrl + P comands.
## Common Issues
- **Images not showing:** Check image path and case sensitivity
- **Styles not applying:** Verify extended_head.html location
- **Git errors:** Check SSH key configuration
- **Hugo server errors:** Verify Hugo version compatibility
- **Slowness in finishing:** Consider re-running the Hugo process. After all, the content mirrors the Vault! Delete everything except your content. Fewer updates will make it as fast as before.
## Regular Tasks
- Backup your Obsidian vault
- Update Hugo and theme versions
- Check Git repository size
- Monitor server logs
## Considerations
It was verry fun and joyfull to see this blog being construct. I hope you to do it, so you can also spread this ideias and help others!

## References
[I started a blog.....in 2024 (why you should too)](https://www.youtube.com/watch?v=dnE7c0ELEH8&list=PLazumvohNo-2qvB49-9RL4karLMmqBDas&index=18))
