import os
import json
from bson.objectid import ObjectId

from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from flask.ext.cors import CORS


client = MongoClient("mongodb://artsadmin:bssquad@ds011314.mlab.com:11314/artsdb")

content = client.artsdb.content

app = Flask(__name__)
CORS(app)

@app.route('/content/setContent', methods=['POST'])
def setContent():

	contentType     = request.get_json().get("contentType")
	contentData     = request.get_json().get("contentData")
	contentSize     = request.get_json().get("contentSize")
	
	key = content.insert(
		{
			"contentSize" : contentSize,
			"contentType" : contentType,
			"contentData" : contentData,
		}
	)

	return str(key)

@app.route('/content/getContent/<key>')
def getContent(key):

	document = content.find_one({"_id": ObjectId(key)})
	
	document.pop("_id", None)

	document["key"] = key

	return json.dumps(document)

if __name__ == "__main__":
	app.run()