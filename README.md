# Detecção de Imagens

Este projeto tem dois arquivos .py de simples funcionamento onde um serve para fazer detecção de rostos(camera.py), e outro arquivo capaz de observar o número feito com os dedos e retornar o número como saída(contar_mãos.py), este projeto foi desenvolvido e preparado para sistema Windows.

## Requisitos

- Python 3.10
- Câmera acoplada a seu computador

## Configuração do Ambiente

Siga os passos abaixo para configurar corretamente o ambiente de desenvolvimento:

### 1. Clonar o repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/Leonardo-snts/Detec-o-de-Imagens.git
cd Detec-o-de-Imagens
```

### 2. Instalar o CMake

Baixe e instale o [CMake](https://cmake.org/download/).
Certifique-se de marcar a opção "Add CMake to system PATH", para que ele possa ser usado diretamente no terminal.

### 3. Instalar o Visual Studio Community Edition

Baixe e instaler o [Visual Studio Community Edition](https://visualstudio.microsoft.com/pt-br/vs/community/).
Durante a instalação, certifique-se de selecionar a opção "Desenvolvimento para desktop com C++". Isso vai garantir que você tenha as ferramentas de compilação necessárias.
Certifique-se de instalar o "Build Tools for Visual Studio", que inclui o compilador e outras ferramentas necessárias. Eles podem ser encontrados como uma opção dentro da instalação do Visual Studio.

### 4. Criar e ativar um ambiente virtual (venv)

Criação de uma venv:

```bash
python -m venv venv
```

Ativação de uma venv:

```bash
.\venv\Scripts\activate
```

### 5. Instalar dependências dentro da venv

Digite o seguinte comando no seu terminal com a venv ativa:

```bash
pip install -r requirements.txt
```

### 6. Rodar o projeto

No terminal dê o seguinte comando para rodar o projeto:

```bash
#para detectar rosto
python camera.py

#para contar números
python contar_mãos.py
```
Pressione "CTRL + C" no terminal para encerrar

### 7. Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```






