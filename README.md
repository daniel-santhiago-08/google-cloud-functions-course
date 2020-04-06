# Google Cloud Functions Course
## Iniciando um projeto
To start a new project in Google Cloud, we can create it from Google Cloud Platform Console
## Instalando o Pip
Faça o download usando o seguinte código no terminal:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Execute o comando para instalar o Pip:
```
python get-pip.py
```

Caso o Python não seja encontrado utilize o caminho completo em:
```
C:\\Users\daniel.santhiago\AppData\Local\Programs\Python\Python37\python get-pip.py
```
## Criando um ambiente virtual
Precisamos instalar `virtualenv` com o seguinte comando:
```
pip install virtualenv
```
Dentro da pasta de seu projeto digite o comando para criar o ambiente virtual com o 
nome `gcloud-venv` :
``` 
virtualenv gcloud-venv
```

Uma pasta será criada na raíz do seu projeto com o mesmo nome.
Para ativá-la digite o comando no Windows:
```
gcloud-venv\Scripts\activate
```

Você verá no terminal antes de cada comando ``(gcloud-venv)``
indicando que o ambiente virtual está ativado.


##Pacotes
Para fazer a instalação de pacotes do Python é criado um arquivo chamado `requirements.txt`
que irá conter os nomes dos pacotes a serem instalados através do comando:
```
pip install -r requirements.txt
```

## Fazendo o deploy da função
Primeiro devemos definir o ID do nosso projeto com o seguinte comando:
```
gcloud config set project [PROJECT_ID]
```

Então faremos o deploy de nossa função com o comando:
```
gcloud functions deploy [FUNCTION_NAME] --runtime python37 --triger-http
```

###Considerações importantes
* Caso o gcloud não tenha sido adicionado ao PATH de sua máquina, é possível executá-lo
 passando o caminho completo ou o caminho relativo até a pasta 
 `.google-cloud-sdk\bin\gcloud` desta forma teremos por exemplo o comando:
 ```
 ..\..\gcloud functions deploy [FUNCTION_NAME] --runtime python37 --triger-http
 ```
 * Para fazer o deploy de uma função é preciso executar o comando de dentro da pasta onde está o arquivo `main.py`
 utilize o comando:
 ```
cd [FOLDER_NAME]
```

