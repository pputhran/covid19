NO_SYMPTOMS = "Thanks for the details. You have no symptoms of COVID 19."
SYMPTOMS = "Thanks for the details. You have some symptoms of COVID 19. I would suggest speaking to your doctor for next steps."

def dispatch(text):
    
    result = {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": {
                            "contentType": "PlainText",
                            "content": text
                    }
                }
            }
    
    return result


def lambda_handler(event, context):

    if event['inputTranscript'] == 'No Symptoms':
        lex_response = dispatch(NO_SYMPTOMS)
    else:
        lex_response = dispatch(SYMPTOMS)
    
    return lex_response