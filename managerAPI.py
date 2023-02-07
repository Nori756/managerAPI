# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import urllib
import json

app = Flask(__name__)

CORS(
    app,
    supports_credentials=True
)


@app.route("/",methods=["GET","POST"])
def test():
    result = "Welcome."
    return result


@app.route("/transmit/",methods=["GET","POST"])
def transmit():
    
    if request.method == "GET":

       params = request.args
       response = {}

       if 'text' in params:
            response.setdefault('res', 'text is : ' + params.get('text'))

       return make_response(jsonify(response))
   
    elif request.method == "POST":

         # URLパラメータ
        params = request.args
        
        response = {}
        if 'text' in params: 
            text = params.get('text')
            url = ''
    
            data = { 'text': text}
            url = url % urllib.parse.urlencode(data)

            try:

                with urllib.request.urlopen(url) as res:
                    text = res.read()
                    response = text
            except urllib.error.HTTPError as err:
                print(err.code)
            except urllib.error.URLError as err:
                print(err.reason)
    
        return response       



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=, threaded=True, debug=True)
