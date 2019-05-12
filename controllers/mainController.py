from app import app
from flask import session,render_template,redirect,url_for, request
import models.mainModel as mainModel

@app.route("/")
def index(): 
    modelResponse = mainModel.index()
    controllerResponse = "This is the model"
    return render_template('index.html',modelResponse = modelResponse,controllerResponse = controllerResponse)

# Here You create the new routes