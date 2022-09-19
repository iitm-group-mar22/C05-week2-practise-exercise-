import boto3
from botocore.exceptions import ClientError
import json
import time

try:
        # Here we assign our aws clients/resources to use
        sqs = boto3.resource(service_name = 'sqs', region_name="us-east-1", endpoint_url='https://sqs.us-east-1.amazonaws.com')
        sns = boto3.client('sns', region_name="us-east-1")
        # Get the queue
        queue = sqs.get_queue_by_name(QueueName='orders')
        while True:
                try :
                    # Process messages by printing out body and optional author name
                    for sqsmessage in queue.receive_messages():

                        # Print out the body and author (if set)
                        message=json.loads(sqsmessage.body)
                        print(message)
                        # Let the queue know that the message is processed
                        response = sns.publish(
                                        TargetArn='arn:aws:sns:us-east-1:848880885953:testing',
                                        Message=json.dumps({'default': json.dumps(message)}),
                                        MessageStructure='json',
                                        Subject='a short subject for your message',
                                        )
                        sqsmessage.delete()
                        time.sleep(10)
                except KeyboardInterrupt:
                        break
                
                

except ClientError as e:
        print("deer")
