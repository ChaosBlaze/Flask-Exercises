from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/calculate', methods=['get'])
def calc():

    number = request.args.get('number')
    msg = ''
    try:

        if int(number)%2==0:
            msg='even'
        elif int(number)%2!=0:
            msg='odd'
    except:
        if (number) == "":
            msg='No number provided!'
        
        else:
            msg='not an integer!'


    return render_template('calculate.html', msg=msg, number=number)

