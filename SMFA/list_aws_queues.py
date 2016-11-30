import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2
import settings

# URL which returns a KEY which can be used to access SQS

def getAllQueues():

    mylist = []
    conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    rs = conn.get_all_queues()
    for q in rs:
        mylist.append(q.id)

    return mylist
