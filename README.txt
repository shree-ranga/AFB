1. CD to AFB path from CLI.

2. Assuming Python 3 and venv are installed, create a virtual environment with the following bash command
    "python3 -m venv venv"

3. Run the following command tpo activate the virtual environment
    "source venv/bin/activate"

4. Install the necessary python packages with the following bash command
    "pip install -r requirements.txt"

5. Create migrations with the following commands
    "python manage.py makemigrations"
    "python manage.py migrate"

6. Run the tests with the following command
    "python manage.py test"

7. Run server
    "python manage.py runserver"

8. API documentation at the following URL
    "http://127.0.0.1:8000/documentation/"
