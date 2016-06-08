import os
from bson.objectid import ObjectId

from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient


client = MongoClient("mongodb://artsadmin:bssquad@ds011314.mlab.com:11314/artsdb")

content = client.artsdb.content

app = Flask(__name__)

@app.route('/content/setContent', methods=['POST'])
def setContent():
	
	contentType     = request.form['contentType']
	contentData     = request.form['contentData']
	
	key = content.insert(
		{
			"contentType" : contentType,
			"contentData" : contentData,
		}
	)

	response = {
		"key":str(key)
	}

	return str(response)

@app.route('/content/getContent/<key>')
def getContent(key):

	document = content.find_one({"_id": ObjectId(key)})
	
	return str(document)

if __name__ == "__main__":
	app.run()