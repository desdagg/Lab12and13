
import boto.sqs
import boto.sqs.queue
from boto.sqs.attributes import Attributes
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

import settings

def readQueueMessage(name):

	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
	q = conn.get_queue(name)

	try:
		m = Message()
		m = q.read(60)
		str1 = m.get_body()
		result = "Message read = " + str1
		return result

	except:
		return "Could not read message"
