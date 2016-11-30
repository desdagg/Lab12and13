
import boto.sqs
import boto.sqs.queue
from boto.sqs.attributes import Attributes
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

import settings

def consumeQueueMessage (name):

	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
	q = conn.get_queue(name)
	result = ""

	try:
		m = Message()
		m = q.read(60)
		str1 = m.get_body()
		result = "Message read = " + str1 + " \n"
	except:
		result = result + "Could not read message\n"

	try:
		q.delete_message(m)
		result = result + "message deleted from the queue\n"
	except:
		result = result + "Could not delete message\n"

	return result
