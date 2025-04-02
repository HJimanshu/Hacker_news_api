# Hacker_news_api

# About The Project 
"""
Create the custom api using django for 
fetching the top 10 stories and 
its integrated with frontend using
 react.js"""

<!--This project is divided into two sections: Backend and Frontend.  -->
# Q:how to set up?

Follow is for:
# Backend
# Setting Up the Environment

First, set up the environment and install all dependencies for the project. Use the following commands:
> python -m venv myenv


Activate the virtual environment and install the required dependencies:
pip install django requests dotenv django-cors-headers

All dependencies are listed in the requirements.txt file.

# Creating a Django Project

After setting up the environment, create a Django project using:
> django-admin startproject project_name

For creating an app within the project, run:
>django-admin startapp app_name


For further details, you can refer to the Django documentation:
[Official Django Documentation](https://docs.djangoproject.com/en/5.1/)

# Creating an API for Fetching HackerNews Data

To create an API that fetches data from the HackerNews API, update the [settings.py] file:

Add the app to the [INSTALLED_APPS] section.

Configure [CORS-middleware] for API integration by adding django-cors-headers.                                                                                               
# Q:How to run?

Go to main directory
1.Activate the Environment:
   >myenv/Scripts/activate
2.Install dependencies:
   >pip install requirenements.txt
3.Run the server:      
   >python manage.py runserver

[You get the data of the api](' http://127.0.0.1:8000/api/fetch_hacker_news')

[You see the api's end points using this ]('http://127.0.0.1:8000')
[Note:]->you change the port using:(python manage.py runserver port_number)
>python manage.py runserver 8888


_______________________________________________________________________________________________________________


# Frontend
**Setting Up the React Environment**

To set up the frontend using React, follow these steps:

>npx create-react-app reactfrontapp
>cd reactfrontapp
>npm install axios react-router-dom

**Running the Frontend**

Start the React app using:
>npm start run

**Note**
For the both You can firstly different folders
Backend/
Frontend/
And then follow the setup and how to run applicationa and test the api.
The frontend integrates with the Django backend API.
Uses [axios] for API requests.
Implements [react-router-dom] for navigation.
For the testing you run both backend and frontend file.
You see the api responce on frontend [using react UI]


**Other Resources**

For Logging :
[django-logging](https://docs.djangoproject.com/en/5.1/topics/logging/#topic-logging-parts-loggers)

