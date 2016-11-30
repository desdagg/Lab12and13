#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

import settings

def createNewQueue(name):
    conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    try:
        q=conn.create_queue(name)
        return name + " queue has been created or already exists"
    except:
        return "Could not create queue. possible too soon since deletion, wait 60 seconds"
