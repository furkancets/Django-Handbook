# Virtual environment oluşturma

# Django Local Process for VsCode

 **Create project directory**

```bash
mkdir djangoprojects
# open that folder with vscode or any IDE
# open IDE terminal
pwd
# ../djangoprojects
mkdir buildDjango
# ../djangoprojects/buildDjango
```

 **Create virtual environment(venv)**

- **`shift + command + p`**  >> and create interpretter >> Venv or Conda

```bash
# it will generate some .venv folder in your directory
# check directory **ls -al**
source .venv/bin/activate
#download django
pip3 install django
#check version
python3 -m django version 
#nowadays 4.1.3 or 4< (from 24.11.2022)

```

**Create virtual environment(virtualenv)**

```bash
virtualenv -p /opt/homebrew/bin/python3.10 django-env
source django-env/bin/activate
pip3 install django
```

**Create Django project**

```bash
#chefsTable is an example
django-admin startproject <your project name>
cd <your project name>
```

**Create Django App project**

```bash
python manage.py startapp <your app name>
```

**Check your server**

```bash
python3 manage.py runserver
# then visit http://localhost:8000/
```