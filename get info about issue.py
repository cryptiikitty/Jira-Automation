from jira import JIRA

jira_url = ''
username = ''
password = ''

jira = JIRA(server=jira_url, basic_auth=(username, password))

issue_key = 'Project-1'

issue = jira.issue(issue_key)

print(f'Issue {issue.key}:')
print(f'Type: {issue.fields.issuetype.id}')
print(f'Desc: {issue.fields.summary}')
print(f'Status: {issue.fields.status.name}')
print(f'Priority: {issue.fields.priority.id}')





