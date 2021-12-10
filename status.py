#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template
from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(17)
buzzer.off()
app = Flask(__name__)

mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)
#app.config['SERVER_NAME']= 'thatguyjack.co.uk/SM/'

def submit(message) :
    mylcd.lcd_clear()
    mylcd.lcd_display_string(message, 1)
    mylcd.lcd_display_string("", 2)
    mylcd.lcd_display_string("Send your message:  ", 3)
    mylcd.lcd_display_string("ThatGuyJack.co.uk/SM", 4)
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

    


def switchClear() :
    mylcd.lcd_clear()
    sleep(1)

# API submit
@app.route('/api/submit', methods=['POST'])
def apiSubmit() :
    #message = request.args.get('message')
        message = request.form.get('message')
        submit(message)
        return '''
                  <h1>Your Message has been sent!: {}</h1>'''.format(message)

# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    switchClear()
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/')
def index():
    #url_for('html', filename='lcd.html')
    return render_template('lcd.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
