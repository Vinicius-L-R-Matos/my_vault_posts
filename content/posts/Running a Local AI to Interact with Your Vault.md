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

Inspired by [NetworkChuck](https://www.youtube.com/watch?v=Wjrdr0NU4Sk), this guide walks you through setting up Ollama on your system, integrating various AI models, and enhancing your workflow with ==Stable Diffusion== and ==BMO== or ==Smart Connections== on obsidian. Whether you're a developer or an AI enthusiast, this step-by-step tutorial will help you harness the power of local AI models effectively.

If you enjoy configuring your AI environment and exploring different models, this approach will provide you with the control and flexibility you need!

What’s happening here is that you’re setting up a local AI server using Ollama, complemented by a web UI for easier interaction and additional tools like Stable Diffusion for image generation. Once everything is configured, maintaining and expanding your AI capabilities requires minimal effort.

Below, I’ll show you how to set up Ollama, integrate various AI models, and enhance your setup with additional tools. You can follow these steps to create your personalized AI environment.

## Did you ever run an Ollama?
![Image Description](/images/ollama.png)
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
		ollama remove model_name
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

## Adding AI to Smart Connections
1. **Configure Local AI in Chat Settings**
    - Select the `Local` option and choose the desired model name from the chat configuration settings.

## About Stable Diffusion
For working with images, setting up Stable Diffusion can enhance your AI capabilities.

### Stable Diffusion Install
#### Prerequisites

1. **Install Pyenv Prerequisites**
    ```bash
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git
    ```

2. **Install Pyenv**
    ```bash
    curl https://pyenv.run | bash
    ```

3. **Install Python 3.10*
    ```bash
    pyenv install 3.10
    ```

4. **Set Python 3.10 as Global Version**
    ```bash
    pyenv global 3.10
    ```

### Install Stable Diffusion
1. **Download the Web UI Script**
    ```bash
    wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
    ```

2. **Make the Script Executable**
    ```bash
    chmod +x webui.sh
    ```

3. **Run the Script**
    ```bash
    ./webui.sh --listen --api
    ```

## BMO
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
