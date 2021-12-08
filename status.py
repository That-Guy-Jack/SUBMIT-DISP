#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)
#app.config['SERVER_NAME']= 'caroline.local'

def submit() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("aaa", 1)
    mylcd.lcd_display_string("aaa", 2)
    mylcd.lcd_display_string("Send your message:", 3)
    mylcd.lcd_display_string("ThatGuyJack.co.uk/FF", 4)
    sleep(1)

    


def switchClear() :
    mylcd.lcd_clear()
    sleep(1)

# API submit
@app.route('/api/submit', methods=['GET','POST'])
def apiSubmit() :
    #message = request.args.get('message')
   return '''<form method="POST"><div><label>Message: <input type="text" name="message"></label>< div><input type="submit" value="Submit"></form>'''
    #submit()
    #return jsonify({})

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
