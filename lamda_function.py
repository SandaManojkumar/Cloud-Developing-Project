import json
import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:your-region:your-account-id:SmartHomeAlerts"

table = dynamodb.Table('SmartHomeData')

def lambda_handler(event, context):
    print("Received event: ", event)
    if "devices" in event:
        for device in event["devices"]:
            store_device_action(device)
            send_notification(device)
    else:
        store_device_action(event)
        send_notification(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Actions processed and notifications sent successfully!')
    }

def store_device_action(device):
    """ Stores device action in DynamoDB """
    device_id = device.get("device_id", "unknown")
    device_type = device.get("device_type", "unknown")
    action = device.get("action", "unknown")

    table.put_item(
        Item={
            'device_id': device_id,
            'device_type': device_type,
            'action': action
        }
    )
    print(f"Stored: {device_id} - {action}")

def send_notification(device):
    """ Sends an SMS or email notification via SNS """
    device_id = device.get("device_id", "unknown")
    action = device.get("action", "unknown")
    
    message = f"🔔 Smart Home Alert: {device_id} performed action {action}."
    
    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message
    )
    
    print(f"Notification sent for {device_id} - {action}")
