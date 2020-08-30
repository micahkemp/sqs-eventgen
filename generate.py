import time
import boto3

# TODO move this to a configuration or argument
sqs_name = "vaultsync_demo"
message_delay_sec = 5

sqs = boto3.resource('sqs')
#queue = sqs.Queue(sqs_url)
queue = sqs.get_queue_by_name(QueueName=sqs_name)

while True:
    message_body = "Hello!"
    print(f"Send message: {message_body}")
    queue.send_message(MessageBody=message_body)
    time.sleep(message_delay_sec)
