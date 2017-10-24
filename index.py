import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=4))
    x = int(event['queryStringParameters']['x'])
    y = int(event['queryStringParameters']['y'])
    print("x = " + str(x))
    print("y = " + str(y))
    retval = {"result" : x / y}
    return {
        'statusCode' : 200,
        'headers' : {
            'content-type' : 'text/html'
        },
        'body' : '<html><body>OK</body></html>'
    }
