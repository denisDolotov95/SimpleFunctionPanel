A simple interface for our containers. If you want to check your services/data bases/monitors/queues. The flexible asynchronous FastAPI framework and the Jinja2 template engine make it so easy.
***
config.py - a configue module in which you specify the services that should be monitored
***
Check in on your own machine:
    ***uvicorn app:app --reload***

Deployment on your docker host (Image must be in the registry: localhost:5000):
    ***docker compose up -d***

If you have Gitlab CI/CD then there's a .gitlab-ci.yml file
***
![Main panel](MainPage.png)