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

```
import requests
from datetime import datetime
import os
import json
import re
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Set, Tuple
import yaml
from yaml import SafeLoader
from fuzzywuzzy import fuzz
import pickle
from datetime import datetime, timedelta, date
import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network
import pandas as pd
import traceback

class ObsidianAssistant:
    def __init__(self, vault_path: str, cache_duration: int = 24):
        """
        Inicializa o assistente com o caminho do vault e configurações
        
        Args:
            vault_path: Caminho para o vault do Obsidian
            cache_duration: Duração do cache em horas
        """
        self.vault_path = Path(vault_path)
        self.cache_file = self.vault_path / ".cache" / "summaries.pkl"
        self.cache_duration = timedelta(hours=cache_duration)
        self.load_cache()
        
        # Dicionário de comandos
        self.command_handlers = {
            "resuma": self.handle_summary,
            "consulte": self.handle_query,
            "relacione": self.handle_relationships,
            "esquematize": self.handle_outline,
            "busque": self.handle_search,
            "visualize": self.handle_visualization
        }
    
    def visualize_knowledge_graph(self, G: nx.Graph, title: str = "Grafo de Conhecimento"):
        """Visualiza o grafo de conhecimento em HTML interativo"""
        try:
            # Criar diretório self_graphs se não existir
            output_dir = self.vault_path / "self_graphs"
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            html_path = output_dir / f"graph_{timestamp}.html"
            data_path = output_dir / f"graph_data_{timestamp}.json"
            
            # Criar visualização
            net = Network(
                height="750px", 
                width="100%", 
                bgcolor="#ffffff", 
                font_color="black",
                select_menu=True,
                filter_menu=True,
                cdn_resources='remote'  # Usar CDN remoto
            )

            # Configurar cabeçalho HTML personalizado
            net.html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                
                <!-- Vis.js CDN -->
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
                <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
                
                <!-- Bootstrap CDN -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous" />
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>

                <!-- Tom Select CDN -->
                <link href="https://cdn.jsdelivr.net/npm/tom-select@2.2.2/dist/css/tom-select.css" rel="stylesheet">
                <script src="https://cdn.jsdelivr.net/npm/tom-select@2.2.2/dist/js/tom-select.complete.min.js"></script>

                <style type="text/css">
                    #mynetwork {
                        width: 100%;
                        height: 750px;
                        background-color: #ffffff;
                        border: 1px solid lightgray;
                        position: relative;
                        float: left;
                    }
                </style>
            </head>
            <body>
                <div class="container-fluid">
                    <div id="mynetwork"></div>
                </div>
                <script type="text/javascript">
            """

            net.set_options("""
            {
                "nodes": {
                    "font": {"size": 16, "strokeWidth": 2},
                    "borderWidth": 2,
                    "shadow": true,
                    "scaling": {
                        "min": 20,
                        "max": 60
                    }
                },
                "edges": {
                    "color": {
                        "inherit": false,
                        "color": "#666666",
                        "opacity": 0.8
                    },
                    "smooth": {"type": "continuous"},
                    "length": 200,
                    "width": 1.5
                },
                "physics": {
                    "barnesHut": {
                        "gravitationalConstant": -2000,
                        "centralGravity": 0.3,
                        "springLength": 200,
                        "springConstant": 0.04,
                        "damping": 0.09
                    },
                    "solver": "barnesHut",
                    "stabilization": {
                        "enabled": true,
                        "iterations": 1000,
                        "updateInterval": 25
                    }
                },
                "interaction": {
                    "hover": true,
                    "tooltipDelay": 200,
                    "zoomView": true,
                    "dragView": true,
                    "navigationButtons": true
                }
            }
            """)

            # Adicionar nós e arestas aqui
            nodes_data = []
            edges_data = []

            # Adicionar nós ao Network
            for node in G.nodes():
                node_data = G.nodes[node]
                node_label = str(node).split('/')[-1]  # Usar apenas o nome do arquivo como label
                
                net.add_node(
                    str(node),
                    title=node_data.get('title', str(node)),
                    color=node_data.get('color', '#4287f5'),
                    size=node_data.get('size', 30),
                    label=node_label,
                    physics=True,
                    shape='dot'
                )
                
                # Guardar dados do nó para JSON
                nodes_data.append({
                    'id': str(node),
                    'type': node_data.get('type', 'file'),
                    'label': node_label,
                    'full_path': str(node)
                })

            # Adicionar arestas com propriedades específicas
            for edge in G.edges():
                net.add_edge(
                    str(edge[0]), 
                    str(edge[1]),
                    physics=True,
                    smooth={'type': 'continuous'},
                    color={'color': '#666666', 'opacity': 0.8}
                )
                
                # Guardar dados da aresta para JSON
                edges_data.append({
                    'from': str(edge[0]),
                    'to': str(edge[1])
                })

            # Adicionar código de fechamento do HTML
            net.html += """
                    // Inicializar o grafo
                    var network = new vis.Network(container, data, options);
                </script>
            </body>
            </html>
            """
            # Salvar HTML
            with open(str(html_path), 'w', encoding='utf-8') as f:
                f.write(net.html)

            # Salvar dados do grafo
            graph_data = {
                'timestamp': timestamp,
                'nodes': nodes_data,
                'edges': edges_data,
                'stats': {
                    'total_nodes': len(G.nodes()),
                    'total_edges': len(G.edges()),
                    'directory': title.replace("Estrutura do Diretório: ", "")
                }
            }
            
            with open(data_path, 'w', encoding='utf-8') as f:
                json.dump(graph_data, f, indent=2, ensure_ascii=False)

            # Salvar visualização
            print(f"\nSalvando visualização em: {html_path}")
            print(f"Salvando dados do grafo em: {data_path}")
            
            return str(html_path)

        except Exception as e:
            print(f"Erro na visualização: {e}")
            traceback.print_exc()
            raise

    def handle_outline(self, prompt: str, config: dict) -> str:
        """Cria um esquema estruturado ou grafo de diretório"""
        print("\nDebug handle_outline:")
        print(f"Prompt recebido: {prompt}")
        print(f"Config: {config}")
        
        if "diretório" in prompt.lower():
            try:
                # Extrair o nome do diretório do prompt
                parts = prompt.lower().split("diretório")
                if len(parts) > 1:
                    # Pegar a última parte após "diretório" e limpar
                    directory = parts[-1].strip()
                    # Remover palavras comuns que podem aparecer no prompt
                    directory = directory.replace("como é o", "").replace("do", "").replace("da", "").strip()
                else:
                    directory = config.get('context_notes', [''])[0]
                
                print(f"Diretório encontrado: {directory}")
                
                if not directory:
                    return "Erro: Especifique um diretório no prompt ou em context_notes"
                
                print("Construindo grafo...")    
                G = self.build_directory_graph(directory)
                print(f"Grafo construído com {len(G.nodes())} nós e {len(G.edges())} arestas")
                
                print("Visualizando grafo...")
                self.visualize_knowledge_graph(G, f"Estrutura do Diretório: {directory}")
                
                return f"Grafo da estrutura do diretório '{directory}' gerado com sucesso!"
                
            except Exception as e:
                print(f"Erro detalhado ao gerar grafo: {str(e)}")
                traceback.print_exc()
                return f"Erro ao gerar grafo do diretório: {str(e)}"
        
        # Se não for visualização de diretório, criar esquema normal
        context = f"""Crie um esquema estruturado sobre o tema, com:
        - Tópicos principais
        - Subtópicos
        - Pontos-chave
        - Conexões entre conceitos
        
        Tema: {prompt}"""
        return self.query_ollama(config['model'], context)

    def build_directory_graph(self, directory_path: str) -> nx.Graph:
        """Constrói um grafo representando a estrutura de diretórios"""
        G = nx.Graph()
        base_path = self.vault_path / directory_path.strip('/')
        
        if not base_path.exists():
            raise ValueError(f"Diretório não encontrado: {directory_path}")
        
        def add_directory_to_graph(path: Path, parent: Optional[str] = None):
            current = str(path.relative_to(self.vault_path))
            
            if path.is_dir():
                G.add_node(current, type='directory')
            else:
                G.add_node(current, type='file')
                
            if parent:
                G.add_edge(parent, current)
                
            if path.is_dir():
                for item in path.iterdir():
                    if item.is_dir() or item.suffix.lower() == '.md':
                        add_directory_to_graph(item, current)
        
        add_directory_to_graph(base_path)
        return G

    def generate_graph_report(self) -> str:
        """Gera relatório básico do grafo"""
        return f"""# Relatório do Grafo
    Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """

    def load_cache(self):
        """Carrega o cache de resumos"""
        self.cache = {}
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'rb') as f:
                    self.cache = pickle.load(f)
            except Exception as e:
                print(f"Erro ao carregar cache: {e}")

    def save_cache(self):
        """Salva o cache de resumos"""
        self.cache_file.parent.mkdir(exist_ok=True)
        try:
            with open(self.cache_file, 'wb') as f:
                pickle.dump(self.cache, f)
        except Exception as e:
            print(f"Erro ao salvar cache: {e}")

    def get_latest_config_from_vault(self) -> dict:
        """
        Busca a configuração mais recente na pasta self_questions
        
        Returns:
            Dict com configurações encontradas no YAML mais recente
        """
        try:
            config_path = self.vault_path / "self_questions"
            
            latest_file = None
            latest_time = 0
            
            for file in config_path.glob("*.md"):
                file_time = file.stat().st_mtime
                if file_time > latest_time:
                    latest_time = file_time
                    latest_file = file
            
            if not latest_file:
                raise ValueError("Nenhum arquivo de configuração encontrado em self_questions/")
                
            with open(latest_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.startswith('---'):
                raise ValueError(f"Arquivo {latest_file.name} não contém metadados YAML")
                
            yaml_end = content.index('---', 3)
            yaml_content = content[3:yaml_end]
            config = yaml.safe_load(yaml_content)
            
            prompt = content[yaml_end + 3:].strip()
            
            required_fields = ['model', 'temperature']
            missing_fields = [field for field in required_fields if field not in config]
            if missing_fields:
                raise ValueError(f"Campos obrigatórios faltando: {missing_fields}")
                
            final_config = {
                'model': config.get('model', 'tinyllama'),
                'temperature': float(config.get('temperature', 0.1)),
                'context_notes': config.get('context_notes', []),
                'tags': config.get('tags', []),
                'prompt': prompt,
                'max_tokens': int(config.get('max_tokens', 2000)),
                'previous_context': config.get('previous_context', True),
                'file_path': latest_file,
                'data': config.get('data', datetime.now().strftime('%d/%m/%Y')),
                'hora': config.get('hora', datetime.now().strftime('%H:%M:%S'))
            }
            
            return final_config
            
        except Exception as e:
            print(f"Erro ao ler configuração: {str(e)}")
            raise

    def get_notes_from_path(self, path_or_note: str) -> List[Tuple[Path, str]]:
        """
        Obtém notas de um caminho ou nome de nota específico
        
        Args:
            path_or_note: Caminho da pasta ou nome da nota
        Returns:
            Lista de tuplas (caminho, conteúdo)
        """
        notes = []
        base_path = self.vault_path / path_or_note.strip('/')
        
        # Se é um caminho de diretório
        if ('/' in path_or_note) or ('\\' in path_or_note):
            if base_path.is_dir():
                # Busca recursivamente todos os arquivos .md no diretório
                for file_path in base_path.rglob("*.md"):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            notes.append((file_path, content))
                    except Exception as e:
                        print(f"Erro ao ler {file_path}: {e}")
            else:
                # Tenta encontrar arquivo específico
                if base_path.with_suffix('.md').exists():
                    try:
                        with open(base_path.with_suffix('.md'), 'r', encoding='utf-8') as f:
                            content = f.read()
                            notes.append((base_path.with_suffix('.md'), content))
                    except Exception as e:
                        print(f"Erro ao ler {base_path}: {e}")
        else:
            # Busca fuzzy por nome de nota
            matches = self.fuzzy_find_note(path_or_note)
            if matches:
                file_path = matches[0][0]
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        notes.append((file_path, content))
                except Exception as e:
                    print(f"Erro ao ler {file_path}: {e}")
        
        return notes

    def query_ollama(self, model: str, prompt: str, context: Optional[str] = None, previous_context: str = "") -> str:
        """
        Consulta o modelo Ollama
        
        Args:
            model: Nome do modelo
            prompt: Prompt principal
            context: Contexto adicional
            previous_context: Contexto prévio
        """
        url = "http://127.0.0.1:11434/api/generate"

        prompt = f"""Responda somente em português, de forma clara, estruturada e detalhada. 
    Inclua exemplos sempre que possível. 
    Pergunta: {prompt}
    """

        if previous_context:
            prompt += f"\n\nContexto prévio:\n{previous_context}"

        if context:
            prompt += f"\n\nContexto adicional:\n{context}"

        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": 0.1
        }

        try:
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_line = line.decode("utf-8")
                        data = json.loads(json_line)
                        full_response += data.get("response", "")
                        if data.get("done"):
                            break
                    except json.JSONDecodeError:
                        continue
            return self.validate_output(full_response.strip())
        except Exception as e:
            return f"Erro na consulta: {str(e)}"

    def build_knowledge_graph(self) -> nx.Graph:
        """Constrói um grafo de conhecimento baseado nas notas"""
        G = nx.Graph()
        
        # Percorre todas as notas markdown
        for file_path in self.vault_path.rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Adiciona nó para a nota atual
                current_node = str(file_path.relative_to(self.vault_path))
                G.add_node(current_node)
                
                # Procura links para outras notas
                links = re.findall(r'\[\[(.*?)\]\]', content)
                for link in links:
                    if '|' in link:
                        link = link.split('|')[0]
                    G.add_edge(current_node, link)
                    
            except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
        return G

    def validate_output(self, response: str) -> str:
        """Valida e corrige a saída do modelo"""
        if not response:
            return "Nenhuma resposta gerada."

        common_words = ["o", "a", "é", "de", "que", "e", "do", "da"]
        if not any(word in response.lower() for word in common_words):
            return "Erro: Resposta gerada não está em português."

        corrections = {
            "fomulário": "formulário",
            "resutados": "resultados",
            "armazeinar": "armazenar"
        }
        for wrong, correct in corrections.items():
            response = response.replace(wrong, correct)

        return response.strip()

    def identify_command(self, prompt: str) -> tuple[str, str]:
        """
        Identifica o comando no prompt
        
        Args:
            prompt: Texto do prompt
        Returns:
            Tupla com (comando, resto do prompt)
        """
        words = prompt.lower().split()
        for word in words:
            if word in self.command_handlers:
                remaining_prompt = prompt.replace(word, "", 1).strip()
                return word, remaining_prompt
        return "consulte", prompt

    def handle_summary(self, prompt: str, config: dict) -> str:
        """Gera um resumo conciso do conteúdo"""
        try:
            # Extrair nome da nota do prompt
            note_name = None
            if "nota" in prompt.lower():
                parts = prompt.lower().split("nota")
                if len(parts) > 1:
                    note_name = parts[1].strip()
            
            if not note_name:
                return "Erro: Nome da nota não encontrado no prompt"

            # Buscar a nota no vault
            matches = self.fuzzy_find_note(note_name)
            if matches:
                file_path = matches[0][0]
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        prompt_text = f"""Sintetize em UMA única frase curta o assunto principal desta nota:

    {content}

    IMPORTANTE: Responda APENAS com uma frase direta, sem bullets ou listas."""

                        return self.query_ollama(config['model'], prompt_text)
                        
                except Exception as e:
                    print(f"Erro ao ler {file_path}: {e}")
                    return f"Erro ao ler a nota: {str(e)}"
            else:
                return f"Erro: Nota '{note_name}' não encontrada"

        except Exception as e:
            print(f"Erro ao gerar resumo: {e}")
            return f"Erro ao gerar resumo: {str(e)}"

    def handle_query(self, prompt: str, config: dict) -> str:
        """Consulta padrão"""
        return self.query_ollama(config['model'], prompt)

    def handle_relationships(self, prompt: str, config: dict) -> str:
        """Analisa relações entre conceitos"""
        context = f"""Analise as relações e conexões entre os conceitos mencionados.
        Identifique padrões, dependências e influências mútuas.
        
        Conceitos: {prompt}"""
        response = self.query_ollama(config['model'], context)
        
        if "visualize" in prompt.lower():
            G = self.build_knowledge_graph()
            self.visualize_knowledge_graph(G, "Grafo de Relações")
        
        return response

    def handle_outline(self, prompt: str, config: dict) -> str:
        """Cria um esquema estruturado"""
        context = f"""Crie um esquema estruturado sobre o tema, com:
        - Tópicos principais
        - Subtópicos
        - Pontos-chave
        - Conexões entre conceitos
        
        Tema: {prompt}"""
        return self.query_ollama(config['model'], context)

    def handle_search(self, prompt: str, config: dict) -> str:
        """Busca em notas específicas"""
        tags = re.findall(r'#(\w+)', prompt)
        if tags:
            notes = self.find_notes_by_tags(tags)
            context = "\n".join([content for _, content in notes])
            return self.query_ollama(config['model'], f"Baseado nas notas encontradas com as tags {tags}, {prompt}")
        return self.query_ollama(config['model'], prompt)
    
    def analyze_vault_data(self, directory_path: Path) -> pd.DataFrame:
        """Analisa os dados do diretório e retorna um DataFrame estruturado"""
        try:
            data = {
                'path': [],
                'name': [],
                'dir': [],
                'tags': [],
                'links': [],
                'n_tags': [],
                'n_links': []
            }
            
            print(f"\nAnalisando diretório: {directory_path}")

            def extract_yaml_and_content(content):
                """Extrai YAML frontmatter e conteúdo do arquivo"""
                yaml_data = {}
                if content.startswith('---'):
                    try:
                        # Encontrar o fim do bloco YAML
                        end_pos = content.find('---', 3)
                        if end_pos != -1:
                            yaml_text = content[3:end_pos].strip()
                            yaml_data = yaml.safe_load(yaml_text) or {}
                            content = content[end_pos + 3:].strip()
                    except:
                        pass
                return yaml_data, content

            def extract_tags(content, yaml_data):
                """Extrai tags do conteúdo e do YAML"""
                # Tags do conteúdo (formato #tag)
                content_tags = set(re.findall(r'#([\w/-]+)', content))
                
                # Tags do YAML
                yaml_tags = set()
                if 'tags' in yaml_data:
                    if isinstance(yaml_data['tags'], list):
                        yaml_tags.update(str(tag) for tag in yaml_data['tags'] if tag)
                    elif isinstance(yaml_data['tags'], str):
                        yaml_tags.add(yaml_data['tags'])
                
                # Combinar e limpar tags
                all_tags = content_tags.union(yaml_tags)
                return {tag.strip() for tag in all_tags if tag.strip()}

            def extract_links(content):
                """Extrai links do conteúdo"""
                links = re.findall(r'\[\[(.*?)\]\]', content)
                clean_links = set()
                for link in links:
                    if '|' in link:
                        link = link.split('|')[0]
                    if link.strip():
                        clean_links.add(link.strip())
                return clean_links

            # Processar cada arquivo no diretório especificado
            for file_path in directory_path.rglob('*.md'):
                try:
                    # Converter caminhos para lowercase para consistência
                    relative_path = str(file_path.relative_to(self.vault_path)).lower()
                    file_name = file_path.name.lower()
                    dir_path = str(file_path.parent.relative_to(self.vault_path)).lower()
                    
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Extrair YAML e conteúdo
                    yaml_data, clean_content = extract_yaml_and_content(content)
                    
                    # Extrair tags e links
                    tags = extract_tags(clean_content, yaml_data)
                    links = extract_links(clean_content)
                    
                    # Debug para verificar tags encontradas
                    if tags:
                        print(f"\nTags encontradas em {file_path.name}:")
                        print(f"- Do YAML: {yaml_data.get('tags', [])}")
                        print(f"- Do conteúdo: {set(re.findall(r'#([\w/-]+)', clean_content))}")
                        print(f"- Tags finais: {tags}")

                    # Adicionar dados ao dicionário
                    data['path'].append(relative_path)
                    data['name'].append(file_name)
                    data['dir'].append(dir_path)
                    data['tags'].append(','.join(sorted(tags)))
                    data['links'].append(','.join(sorted(links)))
                    data['n_tags'].append(len(tags))
                    data['n_links'].append(len(links))

                except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
                    continue

            # Criar DataFrame
            df = pd.DataFrame(data)
            
            print(f"\nTotal de arquivos processados: {len(df)}")
            print(f"Diretórios encontrados: {df['dir'].nunique()}")
            print(f"Total de tags únicas: {len(set(','.join(df['tags'].dropna()).split(',')))}")
            
            return df
            
        except Exception as e:
            print(f"Erro na análise dos dados: {e}")
            traceback.print_exc()
            return pd.DataFrame()

    def handle_visualization(self, prompt: str, config: dict) -> str:
        try:
            # Extrair o diretório do prompt
            target_dir = "Notas/Tratados"  # valor padrão
            if "diretório" in prompt.lower():
                parts = prompt.lower().split("diretório")
                if len(parts) > 1:
                    target_dir = parts[-1].strip()
                    target_dir = target_dir.replace("como é o", "").replace("do", "").replace("da", "").strip()
            
            # Primeiro, localizar o diretório base (Notas/Tratados ou configurado)
            base_path = self.vault_path / "Notas" / "Tratados"
            if not base_path.exists():
                return f"Erro: Diretório base não encontrado: Notas/Tratados"
            
            # Depois, procurar o subdiretório especificado DENTRO do diretório base
            target_dir_lower = target_dir.lower()
            found_dir = None
            
            # Buscar apenas nos subdiretórios do diretório base
            for path in base_path.rglob("*"):
                if path.is_dir() and path.name.lower() == target_dir_lower:
                    # Verificar se este diretório é um subdiretório do base_path
                    try:
                        path.relative_to(base_path)
                        found_dir = path
                        break
                    except ValueError:
                        continue
                    
            if not found_dir:
                return f"Erro: Subdiretório '{target_dir}' não encontrado dentro de {base_path}"
                
            target_path = found_dir
            print(f"\nAnalisando diretório: {target_path}")
            
            if not target_path.exists():
                return f"Erro: Diretório não encontrado: {target_dir}"

            # Criar diretório e nomes de arquivo
            output_dir = self.vault_path / "self_graphs"
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            html_path = output_dir / f"graph_{timestamp}.html"
            excel_path = output_dir / f"graph_{timestamp}.xlsx"
            
            # Passar o target_path correto para analyze_vault_data
            df = self.analyze_vault_data(target_path)
            
            if df.empty:
                return "Nenhum arquivo encontrado"

            # Salvar Excel
            try:
                excel_data = {
                    'Arquivo': df['name'],
                    'Caminho': df['path'],
                    'Diretório': df['dir'],
                    'Tags': df['tags'],
                    'Links': df['links'],
                    'Qtd Tags': df['n_tags'],
                    'Qtd Links': df['n_links']
                }
                
                excel_df = pd.DataFrame(excel_data)
                excel_df.to_excel(excel_path, index=False, sheet_name='Dados do Vault')
                print(f"Excel salvo em: {excel_path}")
            except Exception as e:
                print(f"Erro ao salvar Excel: {e}")

            # Criar grafo
            G = nx.Graph()
            
            # Definir cores
            file_color = '#4287f5'  # Azul
            tag_color = '#f54242'   # Vermelho
            
            # Primeiro passo: adicionar todos os nós de arquivo com IDs mais amigáveis
            print("Adicionando nós de arquivo...")
            for _, row in df.iterrows():
                # Criar ID amigável usando o nome do arquivo e diretório (em lowercase)
                friendly_id = f"{row['dir']}/{row['name']}".lower()
                
                # Criar tooltip rico com informações detalhadas
                tooltip = f"""<div style='background-color: white; padding: 10px; border-radius: 5px;'>
                    <b>Arquivo:</b> {row['name']}<br>
                    <b>Caminho:</b> {row['dir']}<br>
                    <b>Tags:</b> {row['tags']}<br>
                    <b>Links:</b> {row['links']}<br>
                    <a href='file:///{str(self.vault_path / row['path'])}' target='_blank'>Abrir arquivo</a>
                </div>"""

                # Criar string de busca em lowercase
                search_string = f"{row['name']} {row['dir']}".lower()
                
                G.add_node(
                    friendly_id,
                    title=tooltip,
                    label=row['name'],  # Manter label original para visualização
                    color=file_color,
                    size=20,
                    group='file',
                    searchable=search_string
                )

            # Segundo passo: adicionar tags e conexões
            print("Adicionando tags e conexões...")
            for _, row in df.iterrows():
                friendly_id = f"{row['dir']}/{row['name']}"  # Usar mesmo ID amigável
                tags = row['tags'].split(',') if row['tags'] else []
                
                for tag in tags:
                    if tag.strip():
                        tag_node = f"#{tag.strip()}".lower()
                        
                        # Tooltip rico para tags
                        tag_tooltip = f"""<div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <b>Tag:</b> {tag.strip()}<br>
                            <b>Tipo:</b> Tag
                        </div>"""
                        
                        if tag_node not in G:
                            G.add_node(
                                tag_node,
                                title=tag_tooltip,  # Tooltip rico para tags
                                label=f"#{tag.strip()}",
                                color=tag_color,
                                size=15,
                                group='tag',
                                searchable=tag_node
                            )
                        G.add_edge(friendly_id, tag_node)

            # Criar visualização otimizada
            print("Gerando visualização...")
            net = Network(
                height="750px",
                width="100%",
                bgcolor="#ffffff",
                font_color="black",
                select_menu=True,
                filter_menu=True,
                cdn_resources='remote'
            )

            # Configurações otimizadas com busca melhorada
            net.set_options("""
            {
                "nodes": {
                    "font": {"size": 12},
                    "scaling": {"min": 10, "max": 30}
                },
                "edges": {
                    "color": {"inherit": "both"},
                    "smooth": false
                },
                "physics": {
                    "barnesHut": {
                        "gravitationalConstant": -2000,
                        "centralGravity": 0.3,
                        "springLength": 95
                    },
                    "solver": "barnesHut",
                    "stabilization": {
                        "iterations": 50
                    }
                },
                "interaction": {
                    "hover": true,
                    "tooltipDelay": 100,
                    "hideEdgesOnDrag": true,
                    "multiselect": true
                }
            }
            """)

            # Converter grafo NetworkX para Pyvis
            print("Finalizando grafo...")
            net.from_nx(G)
            net.save_graph(str(html_path))
            
            print("Visualização concluída!")
            return f"""Análise concluída:
            - Grafo: {html_path}
            - Excel: {excel_path}
            - Total de arquivos: {len(df)}
            - Total de tags: {df['n_tags'].sum()}
            - Total de links: {df['n_links'].sum()}"""
                
        except Exception as e:
            print(f"Erro: {str(e)}")
            traceback.print_exc()
            return f"Erro ao gerar grafo: {str(e)}"

    def process_prompt(self, config: dict) -> str:
        """
        Processa o prompt baseado no comando identificado
        """
        try:
            print("\nDebug process_prompt:")
            print(f"Prompt recebido: {config['prompt']}")
            
            command, remaining_prompt = self.identify_command(config['prompt'])
            print(f"Comando identificado: {command}")
            print(f"Prompt restante: {remaining_prompt}")
            
            handler = self.command_handlers.get(command, self.handle_query)
            print(f"Handler selecionado: {handler.__name__}")
            
            response = handler(remaining_prompt, config)
            print(f"Resposta do handler obtida: {response[:100]}...")
            
            # Salva a resposta
            self.save_to_md(config['prompt'], response)
            return response
            
        except Exception as e:
            print(f"Erro ao processar prompt: {str(e)}")
            return f"Erro: {str(e)}"

    def save_to_md(self, prompt: str, response: str) -> str:
        """Salva a interação em arquivo markdown"""
        folder_name = self.vault_path / "self_talks" / datetime.now().strftime("%Y/%m/%d")
        file_name = f"{datetime.now().strftime('%H-%M-%S')}.md"
        file_path = folder_name / file_name

        folder_name.mkdir(parents=True, exist_ok=True)

        content = f"# Consulta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n## Pergunta:\n{prompt}\n\n## Resposta:\n{response}\n"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Arquivo salvo em: {file_path}")
        return content

    def find_notes_by_tags(self, tags: List[str], content_filter: Optional[str] = None) -> List[Tuple[Path, str]]:
        """Busca notas por tags e conteúdo"""
        matching_notes = []
        tags = [tag.strip('#') for tag in tags]

        for file_path in self.vault_path.rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    yaml_data = {}
                    if content.startswith('---'):
                        try:
                            end_yaml = content.index('---', 3)
                            yaml_content = content[3:end_yaml]
                            yaml_data = yaml.safe_load(yaml_content)
                            content = content[end_yaml + 3:]
                        except:
                            pass

                    found_tags = re.findall(r'#[\w/]+', content)
                    found_tags = [tag.strip('#') for tag in found_tags]
                    
                    if yaml_data.get('tags'):
                        found_tags.extend(yaml_data['tags'])

                    if any(tag in found_tags for tag in tags):
                        if content_filter:
                            if content_filter.lower() in content.lower():
                                matching_notes.append((file_path, content))
                        else:
                            matching_notes.append((file_path, content))
            except Exception as e:
                print(f"Erro ao ler {file_path}: {e}")

        return matching_notes

    def fuzzy_find_note(self, query: str) -> List[Tuple[Path, float]]:
        """Busca notas usando correspondência fuzzy"""
        matches = []
        for file_path in self.vault_path.rglob("*.md"):
            ratio = fuzz.ratio(query.lower(), file_path.stem.lower())
            if ratio > 60:
                matches.append((file_path, ratio))
        return sorted(matches, key=lambda x: x[1], reverse=True)

    def summarize_note(self, model: str, content: str, max_length: int = 500) -> str:
        """Gera um resumo da nota"""
        content_hash = hash(content)
        if content_hash in self.cache:
            cache_time, summary = self.cache[content_hash]
            if datetime.now() - cache_time < self.cache_duration:
                return summary

        prompt = f"""Faça um resumo conciso do seguinte texto, destacando os pontos principais:

{content}

Limite o resumo a aproximadamente {max_length} caracteres."""

        summary = self.query_ollama(model, prompt)
        
        self.cache[content_hash] = (datetime.now(), summary)
        self.save_cache()
        
        return summary

def main():
    vault_path = Path.cwd().parent.parent.parent
    assistant = ObsidianAssistant(vault_path)
    
    try:
        # Lê configuração do último arquivo em self_questions
        config = assistant.get_latest_config_from_vault()
        
        # Processa o prompt
        response = assistant.process_prompt(config)
        print("\nResposta processada com sucesso!")
        
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
```
T
his whay i can ask some question, make conection to some ideias an talk whit you data. All by your self. It work fine.In my case better than any plugin. 
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
