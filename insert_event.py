import boto3
import ontario_combine
import sys
sys.setrecursionlimit(20000)#cause I write shit code

db = boto3.resource('dynamodb',region_name='us-east-1')
table = db.Table('Events')

event_list = ontario_combine.combined()

counter = 1
with table.batch_writer() as batch:
    for event in event_list:
        batch.put_item(Item={
            "province":event.province,
            "id":event.id,
            "Info":{
                "title":event.title,
                "party":event.party,
                "date":event.date,
                "link":event.link,
                "location":event.location
        }
        })
        print("%s event added"%counter)
        counter += 1