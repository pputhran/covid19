import boto3

comprehend_client = boto3.client('comprehend')

ESCALATION_INTENT_MESSAGE = "Sorry for the trouble. Let me transfer you to one of our specialists"

def lambda_handler(event, context):
    response = comprehend_client.detect_sentiment(Text=event["inputTranscript"],LanguageCode='en')
    
    sentiment = response["Sentiment"]
    
    if sentiment == 'NEGATIVE':
        
        result= {
            "sessionAttributes": {
                "sentiment": sentiment
            },
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": ESCALATION_INTENT_MESSAGE
                }
            }
        }
    
    else:
        
        result= {
            "sessionAttributes": {
                "sentiment": sentiment
            },
            "dialogAction": {
                "type": "Delegate",
                "slots": event["currentIntent"]["slots"]
            }
        }
    
    return result

