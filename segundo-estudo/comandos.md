## Comandos para utilizar python 3.6 no comando python ou pip 
alias python=python3.6
alias pip=pip3

## Instalando VirtualEnv
pip install virtualenv
virtualenv ambvir --python=python3.6

## Inicializando e desativando Ambiente 
source ambvir/bin/activate
deactivate

## Instalando dependências
pip install Flask
pip install Flask-Restful
pip install flask-pymongo
pip install python-dotenv
pip install Flask-JWT-Extended

## Listar dependências
pip freeze


