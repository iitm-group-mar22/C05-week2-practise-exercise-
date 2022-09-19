import boto3
from botocore.exceptions import ClientError
import datetime
import json
import random

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

product_first_name = ('Mobile','TV','AC')
product_last_name = ('Samsung','TCL','LG')

email=('deepakv75@gmail.com', 'vijay.singh.verma@gmail.com', 'deepak@carzso.com')

try:
        # Here we assign our aws clients/resources to use
        sqs_client = boto3.client("sqs", region_name="us-east-1", endpoint_url='https://sqs.us-east-1.amazonaws.com')

        queue_url = "https://sqs.us-east-1.amazonaws.com/848880885953/orders"

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
                        response = sqs_client.send_message(QueueUrl=queue_url, MessageBody=json.dumps(order))
                        print(response.get('MessageId'))
                        print(response.get('MD5OfMessageBody'))
                        
                except KeyboardInterrupt:
                        break
                
                

except ClientError as e:
        print("deer")
