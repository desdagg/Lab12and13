
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

import settings

def addMessageToQueue(name, message):
	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
	m = Message()

	try:
		q=conn.get_queue(name)
		m.set_body(message)
		q.write(m)
		return "The following message has been posted: " + message

	except:
		return "Could not write the message to queue, or queue does not exist"
