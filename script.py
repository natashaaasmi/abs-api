#importing flask dependencies
import flask
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
from flask_cors import CORS
#--------------------------------
#langchain code
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0.6)

def define(term):
    template = """Define {term}"""
    prompt = PromptTemplate(input_variables=["term"], template=template)
    respond = (llm(prompt.format(term=term)))
    return respond

#--------------------------------

#initalizing app
app = Flask(__name__)
CORS(app)
api = Api(app)

#home page
@app.route('/', methods=['GET','POST'])
def page_home():
    if request.method == 'POST':
    #form.get allows for private (browser) API access from HTML form
        #term = request.form.get("termy")
    #args allows for public (postman) API access
        term = request.args.get('termy')
        return define(term)
    return flask.render_template('index.html')

#this is the api endpoint
@app.route('/define/', methods=['GET','POST'])
def define_api():
    if request.method == 'POST':
        term = request.args.get('term')
        return define(term)
    else: 
        return "get"

#running the app
if __name__ == '__main__':
    app.run(port=8000, debug=True)

