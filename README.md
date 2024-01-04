# e-commerce
</div>
```

--> Move into the directory where we have the project files : 
```bash
cd e-commerce

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> make migrations :
```bash
py manage.py makemigrations

```

--> migrate :
```bash
py manage.py migrate

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#
