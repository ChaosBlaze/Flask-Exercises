from datetime import datetime

from flask import Flask, render_template
    
app = Flask(__name__)

@app.get("/")
def date():
    DandT =  datetime.today().strftime("%A, %B %d %Y %H:%M:%S") 
    return render_template('index.html', DandT=DandT)





