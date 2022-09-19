import boto3
from botocore.exceptions import ClientError
import datetime
import json
import random
import time

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

product_first_name = ('Mobile','TV','AC')
product_last_name = ('Samsung','TCL','LG')

email=('deepakv75@gmail.com', 'vijay.singh.verma@gmail.com', 'deepak@carzso.com')

try:
        # Here we assign our aws clients/resources to use
        sqs = boto3.resource(service_name = 'sqs', region_name="us-east-1", endpoint_url='https://sqs.us-east-1.amazonaws.com')

        # Get the queue
        queue = sqs.get_queue_by_name(QueueName='orders')

        product_id=1000
        while True:
                try :
                        product_id+=1
                        order=  {
                                        'customer_name': random.choice(first_names)+" "+random.choice(last_names),
                                        'email_id': random.choice(email),
                                        'product _id': product_id,
                                        'product_name': random.choice(product_first_name)+" "+random.choice(product_last_name),
                                        'price': round(random.uniform(100.5, 7500.5),2),
                                        'timestamp': str(datetime.datetime.now())
                                }
                        # Create a new message
                        response = queue.send_message(MessageBody=json.dumps(order))
                        print(response.get('MessageId'))
                        print(response.get('MD5OfMessageBody'))
                        time.sleep(10)
                except KeyboardInterrupt:
                        break
                
                

except ClientError as e:
        print("deer")
