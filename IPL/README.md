# IPL Points Table Project ( A djnago-model based project )

Welcome to the IPL Points Table Project! This project demonstrates how to create an IPL points table using Django models and display it in an HTML template through views functions, leveraging Jinja for templating.

## Project Overview

This project aims to help students learn how to:
- Define and use Django models to represent data.
- Create views to process data and send it to templates.
- Use Jinja templating language to display data in HTML.
- Set up URL routing to connect views and templates.

## Project Flow

1. **URL Routing:**
   - When a user visits a URL (e.g., `/points-table/`), Django's URL dispatcher (`urls.py`) maps the URL to the corresponding view function.

2. **View Processing:**
   - The view function associated with the URL processes the request.
   - It interacts with the Django models to fetch data from the database.

3. **Data Processing:**
   - The view processes the fetched data as per the business logic.
   - It may perform calculations, sorting, or filtering on the data.

4. **Rendering Template:**
   - After processing, the view passes the processed data to an HTML template.
   - The HTML template uses Jinja templating to dynamically render the data in the desired format.

5. **Displaying Result:**
   - The rendered HTML page, containing the IPL points table, is sent back as the HTTP response.
   - Users can see the updated points table on their web browser.

## Database Configuration

To use this project with your own database, follow these steps:
1. Open the `settings.py` file in your Django project (`iplpoints/`) directory.
2. Update the database settings in the `DATABASES` dictionary according to your database credentials.
   Example:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }


## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/siddharthjena/learn-django-web-development.git
    cd learn-django-web-development/ipl
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the project:**
    ```sh
    python manage.py runserver
    ```
