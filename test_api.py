import json
import requests

def test_endpoint(endpoint: str, method: str = "GET", body: dict = None):
    url = 'http://localhost:9000/2015-03-31/functions/function/invocations'
    
    # Define the request payload to simulate an API Gateway event
    payload = {
        "resource": endpoint,
        "path": endpoint,
        "httpMethod": method.upper(),
        "headers": {
            "Content-Type": "application/json"
        },
        "multiValueQueryStringParameters": None,
        "queryStringParameters": None,  # Include this to avoid KeyError
        "body": json.dumps(body) if body else None,
        "isBase64Encoded": False,
        "requestContext": {
            "resourcePath": endpoint,
            "httpMethod": method.upper(),
            "path": endpoint,
        },
        "pathParameters": None,  # Include this to avoid potential KeyErrors
        "stageVariables": None,  # Include this to avoid potential KeyErrors
        "wsgi.url_scheme": "http",  # Include this to specify the URL scheme
    }
    
    # Make the request to the local Lambda runtime emulator
    response = requests.post(url, json=payload)
    
    # Optionally parse the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        data = response.text
    
    return data


if __name__ == "__main__":
    # Test the root endpoint
    response = test_endpoint("/")
    print("Response from '/':", response)
    
    # Test a POST endpoint with a body
    response = test_endpoint("/predictdata", method="POST", body={
        "gender": "male",
        "ethnicity": "group B",
        "parental_level_of_education": "bachelor's degree",
        "lunch": "standard",
        "test_preparation_course": "none",
        "reading_score": 72,
        "writing_score": 74
    })
    print("Response from '/predictdata':", response)
