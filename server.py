import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/content/setContent', methods=['POST'])
def setContent():
    
    key             = request.form['key']
    contentType     = request.form['contentType']
    contentData     = request.form['contentData']
    
    print "hello world"

    return 'Key: %s \nContent type: %s \nContent data: %s' % (key, contentType, contentData)

@app.route('/content/getContent/<int:key>')
def getContent(key):
    
    return 'Key: %d \nContent type: %d \nContent data: %d' % (key, key, key)

if __name__ == "__main__":
    app.run()