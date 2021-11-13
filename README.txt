1. Unzip the AFB folder.

2. CD into AFB.

3. Assuming Python 3 and venv is installed, create a virtual environment with the following bash command
    "python3 -m venv venv"

4. Activate the virtual environment with the following bash command
    "source venv/bin/activate"

5. Install the necessary python packages with the following bash command
    "pip install -r requirements.txt"

6. Create migrations with the following commands
    "python manage.py makemigrations"
    "python manage.py migrate"

7. Run the tests with the following command
    "python manage.py test"

8. Run server
    "python manage.py runserver"

9. API documentation at the following URL
    "http://127.0.0.1:8000/documentation/"
