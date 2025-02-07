from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService


app=Flask(__name__)
app.config.from_pyfile('config.py')


messageService=MessageService()

@app.route('/v1/ds/message/', methods=['POST'])
def handle_message():
    message=request.json.get('message')
    result=messageService.process_message(message)
    if result is None:
        return jsonify({"error": "Message not recognized"}), 400

    return jsonify(result) 

@app.route('/',methods=['GET'])
def handle_get():
    return 'hello world'


if __name__=="__main__":
    app.run(host="localhost",port=5000,debug=True)