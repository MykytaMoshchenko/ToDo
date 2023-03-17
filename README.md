# ToDo

Django project for managing ToDo list.


## Installation

Python3 must be already installed.

```shell
git clone https://github.com/MykytaMoshchenko/ToDo.git
cd ToDo_list
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

For the matter of security, ".env" file was created for storing SECRET_KEY.
```.env file
Steps:

1) Create a .env file in your base directory (where manage.py is).

YourDjangoProject
├───project
│   ├───__init__.py
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───.env
├───manage.py
└───db.sqlite3

2) Updating settings.py:
    import dotenv
    import os
    
    # Add .env variables anywhere before SECRET_KEY
    dotenv_file = os.path.join(BASE_DIR, ".env")
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)

    # UPDATE secret key
    SECRET_KEY = os.environ["SECRET_KEY"] # Instead of your actual secret key

3)  Add .env to your .gitignore file

4) Inside of your .env file add:
    SECRET_KEY=qolwvjicds5p53gvod1pyrz*%2uykjw&a^&c4moab!w=&16ou7 # <- Example key, SECRET_KEY=yoursecretkey
```


## Features

* Managing tasks directly from the website, creating tasks, setup deadlines, update complete status of the tasks.
* Powerful admin panel for advanced managing


## Demo

![Website interface](demo.png)
