# Nourish - Calorie Counter

## Project Overview

Nourish is a Django-based calorie tracking web application that helps users keep track of the food they consume throughout the day.

Users can create an account, log in securely, add food items with their calorie information, view their daily food entries, delete food entries, calculate their total daily calorie intake, and reset their daily calorie count.

The application provides a clean, responsive, and user-friendly interface built with Tailwind CSS and uses PostgreSQL for persistent data storage

## Features

### User Authentication

* User registration
* User login and logout
* Password validation using Django's built-in authentication system
* User-specific food records

### Calorie Tracking

* Add food items
* Specify calorie amounts
* Specify meal types
* View all food items logged for the day
* Calculate total daily calories
* Delete food entries
* Reset the daily calorie count

### User Interface

* Responsive design
* Tailwind CSS styling
* Reusable Django template inheritance
* Clean and modern Nourish-themed interface
* Responsive navigation
* Mobile-friendly layouts

## Technologies Used

### Backend

* Python 3.14
* Django
* Django Authentication
* PostgreSQL

### Frontend

* HTML5
* CSS3
* Tailwind CSS
* Django Templates

### Development Tools

* Git
* GitHub
* Visual Studio Code

## Project Structure

```text
Nourish/
│
├── calorie_tracker/
│   ├── migrations/
│   ├── templates/
│   │   └── calorie_tracker/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── add_food.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── nourish/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Database

Nourish uses PostgreSQL as its database management system.

The database stores user authentication information and food entries associated with individual users.

Each food entry contains information such as:

* Food name
* Calories
* Meal type
* User
* Date added

## Authentication and Security

The project uses Django's built-in authentication system for user management.

Security practices implemented include:

* CSRF protection on POST forms
* Django password hashing
* Login protection for authenticated pages
* User-specific food records
* Server-side form validation
* Database queries handled through Django's ORM
* Sensitive configuration values excluded from version control where applicable

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AbbieJonnes/Nourish.git
```

### 2. Navigate Into the Project

```bash
cd Nourish
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

On Windows using Git Bash:

```bash
source myenv/Scripts/activate
```

On Windows PowerShell:

```powershell
myenv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure PostgreSQL

Create a PostgreSQL database and configure the database credentials in `nourish/settings.py`.

Example configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

For production deployment, database credentials should be stored using environment variables rather than directly in the settings file.

### 7. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

### 9. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## Usage

### Creating an Account

Navigate to the registration page and provide:

* Username
* Email address
* Password
* Password confirmation

After successful registration, log in to access the dashboard.

### Adding Food

From the dashboard, select the option to add food and provide:

* Food name
* Calorie amount
* Meal type

The food item will then appear in the daily food log.

### Viewing Calories

The dashboard displays the total number of calories consumed for the current day.

### Deleting Food

Each food entry has a delete option. Deleting an entry removes it from the daily food log and updates the calorie total.

### Resetting Daily Calories

The reset option removes the food entries for the current day and resets the daily calorie total.

## Deployment

The application is intended to be deployed using a hosting platform such as Render.

The production deployment should use:

* PostgreSQL
* Environment variables for sensitive settings
* A production WSGI server
* Appropriate Django production security settings

### Live Application

The live application will be available here after deployment:

```text
[Add Render URL after deployment]
```

## Version Control

Git is used for version control throughout the development of Nourish.

Example Git commands:

```bash
git status
git add .
git commit -m "Add calorie tracking functionality"
git push origin main
```

Meaningful commit messages are used to document the development process.

## Future Improvements

Possible future improvements include:

* Nutritional information beyond calories
* Weekly and monthly calorie statistics
* Food search and recommendations
* Personalized calorie goals
* Progress charts
* Profile customization

## Author

### Abigael Mwangi

GitHub: https://github.com/AbbieJonnes

Email: [abigaelmwangi534@gmail.com]

## License

This project is licensed under the MIT License.
