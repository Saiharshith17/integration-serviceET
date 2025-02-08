from flask import Flask, request, jsonify
from service.messageService import MessageService
from confluent_kafka import Producer, Consumer
import json
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()
kafka_host = os.getenv('KAFKA_HOST', 'localhost')
kafka_port = os.getenv('KAFKA_PORT', '9092')
kafka_bootstrap_servers = f"{kafka_host}:{kafka_port}"
print("Kafka server is " + kafka_bootstrap_servers)

producer = Producer({'bootstrap.servers': kafka_bootstrap_servers})

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    user_id = request.headers.get('x-user-id')
    if not user_id:
        return jsonify({'error': 'x-user-id header is required'}), 400

    message = request.json.get('message')
    result = messageService.process_message(message)

    if result is not None:
        serialized_result = result
        serialized_result['user_id'] = user_id
        producer.produce('expense_service', key=user_id, value=json.dumps(serialized_result).encode('utf-8'))
        producer.flush()  # Ensure messages are sent
        return jsonify(serialized_result)
    else:
        return jsonify({'error': 'Invalid message format'}), 400

@app.route('/', methods=['GET'])
def handle_get():
    return 'hello world'

@app.route('/health', methods=['GET'])
def handle_check():
    return 'OK'

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
