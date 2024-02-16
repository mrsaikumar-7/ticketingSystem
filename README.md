# Ticketing System

## Description

Ticketing System is a Django-based web application for managing tickets, notes, and user profiles.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django installed (`pip install django`)
- Additional Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrsaikumar-7/ticketingSystem.git
2. Navigate to the project directory:

   ```bash
   cd ticketingSystem
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
4. Activate the virtual environment:

   ```bash
   venv\Scripts\activate   #windows
   source venv/bin/activate  #macOS/Linux
5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
7. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
8. Run the development server:

   ```bash
   python manage.py runserver
9. Access the application at http://127.0.0.1:8000/ in your web browser.


## Usage
  
  - Create a new ticket, view, update, and close tickets.
  - Add notes to tickets.
  - Access user profile and update information.
## Project Structure
  - ticket/: Django app containing the main application logic.
  - accounts/: Django app handling user authentication and profiles.
  - static/: Static files (CSS, images, etc.).
  - templates/: HTML templates.
    
## Technologies Used
  - Django
  - HTML
  - CSS
  - Javascript
  - Chart.js
  - bootstrap5
   
   
   
