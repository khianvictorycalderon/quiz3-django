# Django Quiz 3 Hands On
**Read the `LICENSE.md` FIRST BEFORE ANYTHING (*You cannot copy this code for academic purpose, otherwise there would be legal consequences!*)**

### Preview
![Preview](preview.png)

### Prerequisites:
1. Python (with pip installer)

### Setup:
1. Generate a safe key using this command in your python interpreter:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
2. Create your virtual environment by running `python -m venv venv`.
3. Activate your virtual environment with `.\venv\Scripts\activate` (for Windows).
4. Install all the necessary dependencies with `pip install -r requirements.txt`
5. Run `python manage.py migrate` (if using database) for database migration.
6. Run the server via `python manage.py runserver`. 
    *(Note: If existing port is used, used another port, example: `python manage.py runserver 7000`, `7000` is the port to run the server.)*

---

### Additional Notes:
- If database is modified from the previous schema, always run `python manage.py makemigrations` then `python manage.py migrate`.
- If installing additional dependencies, run `pip freeze > requirements.txt`.
- Always set `DEBUG=False` on production.

### Dependencies
- All package dependencies are in `requirements.txt` file.