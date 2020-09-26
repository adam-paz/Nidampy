# Nidampy
To install Python dependencies:
1) Creat virtual environment with "python3 -m venv env"
2) Activate environment with "venv/Scripts/activate" (add source command in bash)
3) Install packages with "pip install --user -r requirements.txt"

To install Node dependencies:
1) Navigate to "ReactDjango/backend/templates/frontend"
2) Install modules with "npm install"

# Run
env 1) source ReactDjango/env/Scripts/activate
backend 2) cd ReactDjango/backend && python manage.py runserver
frontend 3) cd ReactDjango/backend/templates/frontend && npm start