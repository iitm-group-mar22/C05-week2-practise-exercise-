import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    #print(event)
    snsmsg=json.loads(event['Records'][0]['Sns']['Message'])
    email_id=snsmsg['email_id']
    #print(email_id)
    sub=f"Order Successfully placed for {snsmsg['product_name']}"
    msg=f"Hi {snsmsg['customer_name']},<br />"
    msg+=f"<br />"
    msg+=f"Your order of product id : {snsmsg['product _id']} and product name : {snsmsg['product_name']} "
    msg+=f"has been succesfully placed<br />"
    msg+=f"<br />"
    msg+=f"Your total bill amoint is : {snsmsg['price']}.<br />"
    msg+=f"<br />"
    msg+=f"Warm Regards<br />"
    msg+=f"Carzso Team"
    
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name="us-east-1")
    response = client.send_email(
        Destination={
            'ToAddresses': [
                email_id,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Data': msg,
                },
                
            },
            'Subject': {
                'Data': sub,
            },
        },
        Source='deepak@carzso.com',
        )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
