import json

NO_SYMPTOMS = "Thanks for the details. You have no symptoms of COVID 19."
SYMPTOMS = "Thanks for the details. You have some symptoms of COVID 19. I would suggest speaking to your doctor for next steps."

def lambda_handler(event, context):

    print(event['inputTranscript'])

    if event['inputTranscript'] == 'No Symptoms':

        result = {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                            "contentType": "PlainText",
                            "content": NO_SYMPTOMS
                    }
                }
            }
    
    else:
        result = {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                            "contentType": "PlainText",
                            "content": SYMPTOMS
                    }
                }
            }
        
    
    return result