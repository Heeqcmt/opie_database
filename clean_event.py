import boto3


db = boto3.resource('dynamodb',region_name='us-east-1')
table = db.Table('Events')
events = table.scan()
with table.batch_writer() as batch:
    for event in events['Items']:
        batch.delete_item(
            Key={
                "province":event["province"],
                "id":event["id"]
            }
        )
        print("event deleted")