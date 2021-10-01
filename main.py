
from flask import Flask , jsonify, request, render_template
from selenium import webdriver
from selenium.webdriver.common import keys
from waitress import serve
from CentralDiApiCode import Centdi
import json
import os



username = "carpool1"
password = "Autohaul1!"
Url = "https://www.google.com"
Url1 = "https://www.centraldispatch.com/protected/cargo/sample-prices-lightbox?num_vehicles=1&ozip="
Url2 ="&dzip="    
Url3 = "&enclosed=0&inop=0&vehicle_types="
Url4 = "&miles="
Url5 = ""        
data = {}
ozip = "77449"
dzip = "11386"
types1 = ""
filePath = "Key.json"



app = Flask(__name__)


@app.route('/login')
def login_main():
    if os.path.exists(filePath):
        os.remove(filePath)
        print ("yes")
    else:
        print("Can not delete the file as it doesn't exists")
        
    Di = Centdi(Url,username,password)
    global driver2
    driver2 = Di.login()

    key = input("Token : ")
    print(key)

    data = {'Key' : key}
        

    with open('Key.json', 'w') as outfile:
        print ("writing")
        json.dump(data, outfile)
    outfile.close()

    return "Value = " + key

   
@app.route('/getdata/<ozip>/<dzip>/<types1>')
def getinstance(ozip,dzip,types1):
    with open('Key.json', 'r') as outfile:
         data = json.load(outfile)
         Key = data["Key"]
    Di = Centdi(Url,username,password)
    Di.getdata(ozip,dzip,types1, Key, driver2)
    return "Sucess"
   


 



if __name__ == "__main__":
    app.run( host='0.0.0.0', port=5000, debug=True)

