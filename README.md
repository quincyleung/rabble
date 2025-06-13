# CS 220 Homework: Rabble Web Application

This repository contains the code for a Reddit-style web application I built in **Django** for [CMSC 22000 – Introduction to Software Development](https://uchicago-cs.github.io/cmsc22000/) at the University of Chicago.

## 🛠️ Features Implemented
- Full CRUD functionality for posts and comments
- Threaded reply support on post detail pages
- Private and public subRabbles
- Anonymous posting and commenting
- Session-based authentication
- User settings and profile features
- RESTful API endpoints for post interactions
- Permissions enforcement for user-generated content

## 🧪 Testing & Improvements
- Added unit tests for custom views and APIs using `pytest`
- Structured app for modularity and clarity
- Additional improvements to UI responsiveness and frontend usability

## 🚀 How to Run
Clone the repository and set up the Django environment:

```bash
git clone https://github.com/quincyleung/rabble.git
cd rabble
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
