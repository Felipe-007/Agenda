
<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=E51C44&labelColor=0A1033">

 <img src="https://img.shields.io/static/v1?label=NLW&message=06&color=E51C44&labelColor=0A1033" alt="NLW 06" />
</p>


![cover](.github/cover.png?style=flat)


## 💻 Projeto
O projeto tem a finalidade de criar agendas (ainda incompleto) feito com Django 3.1.7 e Python 3.9.1.

## ✨ Tecnologias

-   [ ] Python
-   [ ] Django
-   [ ] Html
-   [ ] Css
-   [ ] JavaScript
-   [ ] Mysql
-   [ ] Django Crispy Forms
-   [ ] Gunicorn


## 🔖 Deploy

Você pode visualizar o Deploy do projeto através [desse link](https://github.com/Felipe-007/Agenda).


## Tutorial para iniciantes

Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
git clone https://github.com/Felipe-007/Agenda.git
```

- Para **Windows**:

```
cd agenda
python -m venv Myenv
Myenv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Para **Linux**:

```
cd agenda
python3.7 -m venv Myenv
. Myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Para **Mac**

```
cd agenda
python -m venv Myenv
. Myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## :hammer_and_wrench: Mysql 
Caso apresente erro durante a migração "python manage.py migrate", crie o arquivo local_settings.py na pasta \Agenda\agenda.
Com a seguintes configurações:

```
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agenda_mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Realize a configuração do seu banco de dados, referenciando as configurações acima.

Pronto!


## 📄 Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

<br />

<div align="center">
  <small>Agradecimentos ao professor Luiz Otávio Miranda</small>  
</div>
