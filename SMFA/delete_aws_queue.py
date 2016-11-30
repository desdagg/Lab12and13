
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

import settings

def deleteExistingQueue(name):

	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

	try:
		q=conn.get_queue(name)

	except:
		result = "Failed to find queue " + name
		return result

	try:
		conn.delete_queue(q,True)
		result = name + " queue has been deleted"
		return result

	except:
		return "Could not delete the queue, or it does not exist"
