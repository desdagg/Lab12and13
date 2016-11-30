from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

#IMPORTS Boto files / libraries
from list_aws_queues import getAllQueues
from create_aws_queue import createNewQueue
from delete_aws_queue import deleteExistingQueue
from count_msg_queue import getQueueCount
from write_aws_queue import addMessageToQueue
from read_msg_queue import readQueueMessage
from consume_aws_queue import consumeQueueMessage

app = Flask(__name__)


#INDEX ROUTE
@app.route('/')
def index():
    return "This is an example of SQS Management Flask Application"


#ERROR CHECKING
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#SHOW ALL QUEUES
@app.route('/queues')
def get_queues():
    return jsonify({'queues': getAllQueues()})


#ADD NEW QUEUE
@app.route('/queues', methods=['POST'])
def add_queue():
    if not request.json or not 'name' in request.json:
        abort(400)
    return createNewQueue(request.json['name'])


#DELETE QUEUE
@app.route('/queues/<queue_name>', methods=['DELETE'])
def delete_queue(queue_name):
    return deleteExistingQueue(queue_name)


#GET MESSAGES COUNT
@app.route('/queues/<queue_name>/msgs/count', methods=['GET'])
def get_queue_count(queue_name):
    return getQueueCount(queue_name)


#ADD NEW MESSAGE TO QUEUE
@app.route('/queues/<queue_name>/msgs', methods=['POST'])
def add_message_to_queue(queue_name):
    if not request.json or not 'content' in request.json:
        abort(400)
    return addMessageToQueue(queue_name, request.json['content'])


#READ MESSAGE IN QUEUE
@app.route('/queues/<queue_name>/msgs', methods=['GET'])
def read_message_from_queue(queue_name):
    return readQueueMessage(queue_name)


#CONSUME MESSAGE IN QUEUE
@app.route('/queues/<queue_name>/msgs', methods=['DELETE'])
def consume_message_from_queue(queue_name):
    return consumeQueueMessage(queue_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)
