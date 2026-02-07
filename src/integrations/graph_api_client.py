# Microsoft Graph API Client for Outlook Integration

This client allows for integration with Microsoft Graph API to interact with Outlook functionalities such as sending emails, retrieving calendar events, and managing contacts.

## Installation

To use this client, ensure that you have the necessary permissions and the `requests` library installed:

```bash
pip install requests
```

## Usage Example
```python
class GraphApiClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://graph.microsoft.com/v1.0/'

    def send_email(self, recipient, subject, body):
        url = f'{self.base_url}me/sendMail'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        email_data = {
            'message': {
                'subject': subject,
                'body': {
                    'contentType': 'Text',
                    'content': body
                },
                'toRecipients': [
                    {'emailAddress': {'address': recipient}}
                ]
            }
        }
        response = requests.post(url, headers=headers, json=email_data)
        return response.status_code

# Example usage
# client = GraphApiClient('<ACCESS_TOKEN>')
# client.send_email('example@domain.com', 'Test Subject', 'Test Body')
```
