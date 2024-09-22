import requests

jira_url = ''
username = ''
password = ''

endpoint = f'{jira_url}/rest/api/2/field'
headers = {
    'Content-Type': 'application/json'
}
auth = (username, password)
response = requests.get(endpoint, headers=headers, auth=auth)
if response.status_code == 200:
    custom_fields = response.json()
    for field in custom_fields:
        print(f'Name custom field: {field["name"]}')
        print(f'ID custom field: {field["id"]}')
else:
    print(f'Error: {response.status_code} - {response.text}')
