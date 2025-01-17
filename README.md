# Personal Artificial Intelligence Operating System (pAI-OS)

## Getting Started

### Users

An easy to use release is coming soon, but for now you can follow the instructions below to get started.


> 💡 **Tip:** Download and install [Python](https://www.python.org/downloads/) if you can't run it from the terminal.


Setup and run the server:

# Alembic

Alembic is used to manage database versioning using migrations.

## Upgrade schema

`alembic upgrade head`

## Downgrade schema

`alembic downgrade -1`

## Update schema

Update backend/models.py then run:

`alembic revision --autogenerate -m "added asset table"`

** NOTE: If you get an error about an already existing table, you may want to drop the table and run 'alembic upgrade head' again. **


## Setup the project
Clone the entire repository

```sh
git clone https://github.com/Kwaai-AI-Lab/assistant
```

### Setting up the ```.env``` file

1. Create a ```.env``` file
    In the root directory of your project, create a new file named ```.env```   

2. Add your environment variables    
    Open the ```.env``` file in a text editor and add the required environment variables. Each variable should be on a new line in the format:

Example of ```.env```:

```
PAIOS_ALLOW_ORIGINS='http://localhost:5173,https://0.0.0.0:8443,https://localhost:3000'
PAIOS_DB_ENCRYPTION_KEY=''
CHUNK_SIZE='2000'
CHUNK_OVERLAP='400'
ADD_START_INDEX='True'
EMBEDDER_MODEL='llama3:latest'
SYSTEM_PROMPT='You are a helpful assistant for students learning needs.'
MAX_TOKENS='200'
TEMPERATURE='0.2'
TOP_K='40'
TOP_P='0.9'
 
PAIOS_SCHEME='https'
PAIOS_HOST='0.0.0.0'
PAIOS_EXPECTED_RP_ID='localhost'
PAIOS_PORT='8443'
PAIOS_URL='https://localhost:8443'
 
PAI_ASSISTANT_URL='https://localhost:3000'
PAIOS_JWT_SECRET=''

#Eleven labs
XI_API_URL='https://api.elevenlabs.io'
XI_API_KEY=''
XI_CHUNK_SIZE='1024'

#Ollama
OLLAMA_LOCAL_MODELS_URL='http://0.0.0.0:11434/api/tags'
OLLAMA_MODELS_DESCRIPTION_URL='https://ollama.com/library/'
```
__PAIOS_URL__: Url where is hosted the PAIOS

__PAI_ASSISTANT_URL__: Url where is hosted the PAIAssistant

__TEMPERATURE__: 
The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)

__TOP_K__: Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative.

__TOP_P__: Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)

__CHUNK_SIZE__: The maximum size of a chunk.
__CHUNK_OVERLAP__: Target overlap between chunks. Overlapping chunks helps to mitigate loss of information when context is divided between chunks.

__ADD_START_INDEX__: We set add_start_index=True so that the character index at which each split Document starts within the initial Document is preserved as metadata attribute “start_index”.

__EMBEDDER_MODEL__: Check the final ❗ note.

__XI_CHUNK_SIZE__:Size of chunks to read/write at a time

__MAX_TOKENS__: Maximum number of tokens to predict when generating text. (Default: 128, -1 = infinite generation, -2 = fill context). Common lengths might be:

    - A maximum of 50 tokens for very concise answers
    - A maximum of 200 tokens for more substantial responses

### Instructions to Obtain an Eleven Labs API Key
Follow these steps to get an API key from Eleven Labs:
1. Create an Eleven Labs Account

    If you don't already have an account, go to [Eleven Labs](https://elevenlabs.io/app/sign-up) and sign up for a free or paid plan. You'll need an active account to access the API.

2. Log In to Your Account

    Once you have an account, log in to the Eleven Labs dashboard using your credentials.

3. Navigate to the API Section

    After logging in, go to the API section of the dashboard. You can typically find this in the main navigation or giving click on your User name and then on API Keys option.

4. Generate and copy Your API Key 

    In the API section, you'll see an option to generate or view your API key. Click the button to generate a new API key if one isn’t already created. Once generated, your API key will be displayed. Copy it and store it securely, because you will not be able to display it again.

5. Store the API Key in Your Project’s ```.env``` File
    To securely use the API key in your project, add it to your ```.env``` file like this:
    ```
    XI_API_KEY="sk_******"
    ```

### Install Ollama
In order to create an assistant, you will need to download [Ollama](https://ollama.com/download)

__macOS__

[Download](https://ollama.com/download/Ollama-darwin.zip)

__Windows preview__

[Download](https://ollama.com/download/OllamaSetup.exe)

__Linux__

```
curl -fsSL https://ollama.com/install.sh | sh
```

[Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md)


After installing Ollama, Ollama will run in the background and the `ollama` command line is available in `cmd`, `powershell` or your favorite terminal application. As usual the Ollama api will be served on
`http://localhost:11434`.

You should see the message:  "_Ollama is running_"

#### Common Ollama comands

__Download a model__

```
ollama run llama3.2
```
__Pull a model__

This command can also be used to update a local model. Only the diff will be pulled.
```
ollama pull llama3.2
```

__List all the installed models__

This list contains the available models for you to choose from and set as the Large Language Model (LLM) for your Assistant.
```
ollama list
```
__Remove a model__

Keep in mind that once you delete a model from your computer, it will no longer be available for setting up with your Assistant.
```
ollama rm llama3.2
```

#### Model library

Ollama supports a list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library')

Here are some example models that can be downloaded:

| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| Llama 3.2          | 3B         | 2.0GB | `ollama run llama3.2`          |
| Llama 3.2          | 1B         | 1.3GB | `ollama run llama3.2:1b`       |
| Llama 3.1          | 8B         | 4.7GB | `ollama run llama3.1`          |
| Llama 3.1          | 70B        | 40GB  | `ollama run llama3.1:70b`      |
| Llama 3.1          | 405B       | 231GB | `ollama run llama3.1:405b`     |
| Phi 3 Mini         | 3.8B       | 2.3GB | `ollama run phi3`              |
| Phi 3 Medium       | 14B        | 7.9GB | `ollama run phi3:medium`       |
| Gemma 2            | 2B         | 1.6GB | `ollama run gemma2:2b`         |
| Gemma 2            | 9B         | 5.5GB | `ollama run gemma2`            |
| Gemma 2            | 27B        | 16GB  | `ollama run gemma2:27b`        |
| Mistral            | 7B         | 4.1GB | `ollama run mistral`           |
| Moondream 2        | 1.4B       | 829MB | `ollama run moondream`         |
| Neural Chat        | 7B         | 4.1GB | `ollama run neural-chat`       |
| Starling           | 7B         | 4.1GB | `ollama run starling-lm`       |
| Code Llama         | 7B         | 3.8GB | `ollama run codellama`         |
| Llama 2 Uncensored | 7B         | 3.8GB | `ollama run llama2-uncensored` |
| LLaVA              | 7B         | 4.5GB | `ollama run llava`             |
| Solar              | 10.7B      | 6.1GB | `ollama run solar`             |



|❗ Note: Currently, the Assistant's embbeder model cannot be configured through the Assistant's UI. This means that whatever model you specify in the ```.env``` file under the variable name __EMBEDDER_MODEL__ must already be installed on your computer. You can verify the models installed by running the command ```ollama list``` |
|--|

## Run the project
```sh
docker build -t assistant .
docker run -p 8443:8443 assistant
```

Visit [https://localhost:8443/](https://localhost:8443/)
