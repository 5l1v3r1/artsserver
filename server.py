import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_content():
    
    key             = request.form['key']
    content_type    = request.form['content_type']
    content_data    = request.form['content_data']
    
    return str(key)+" "+str(content_type)+" "+str(content_data)

if __name__ == "__main__":
    app.run()
