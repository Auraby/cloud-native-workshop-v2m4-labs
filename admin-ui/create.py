from flask import Blueprint, render_template, url_for,request
import requests
import os

create = Blueprint('create',__name__)

# VM_URL = os.getenv("VM_URL",default="coolstore-admin.southeastasia.cloudapp.azure.com")

@create.route('/')
def home():
    return render_template('create.html')

@create.route('/check_connection', methods=['GET'])
def check_connection_vm():
    if request.method == "GET":
        try:
            vmResponse = requests.get("http://coolstore-admin.southeastasia.cloudapp.azure.com/Health")
            responseMsg = vmResponse.text
        except Exception as e:
            responseMsg = f"Error checking connection: {e}"

    return render_template('create.html',responseMsg=responseMsg)