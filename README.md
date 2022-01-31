# Calculator
Practicing software development building a simple calculator from components to microservices and UI


# Installation
* [Python 3](https://www.python.org/downloads/)
* [PIP](https://packaging.python.org/tutorials/installing-packages/)
* [Pytest](https://docs.pytest.org)
* [Pytest Cov](https://pypi.org/project/pytest-cov/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [Flask](https://flask.palletsprojects.com/)
* [Flask_restful](https://github.com/flask-restful/flask-restful)

# Start Api  
From VS Code: `Api.py -> Run`  
From terminal: `python3 Api.py`  

# Azure App Deployment
- Tutorial https://docs.microsoft.com/nl-nl/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask
- Open the Azure CLI via portal.azure.com.
- Execute git clone https://github.com/eskape/calculator
- cd ./calculator/
- From Azure CLI: az webapp up --sku B1 --name eskape-calculator-app
- After deployment openen: https://eskape-calculator-app.azurewebsites.net/add