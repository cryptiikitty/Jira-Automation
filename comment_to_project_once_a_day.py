from jira import JIRA
from datetime import datetime, timedelta
import calendar
import time
import datetime
import requests

jira_url = ''
username = ''
password = ''
project_key = 'Project name'
board_name = ''

auth = (username, password)
url = f'{jira_url}/rest/api/2/search?jql=project={project_key}'
tasks_list = []

start_at = 0
max_results = 50
while True:
    session = requests.Session()
    response = session.get(f'{url}&startAt={start_at}&maxResults={max_results}', auth=auth)
    if response.status_code == 200:
        issues = response.json().get('issues')
        if not issues:
            break
        for issue in issues:
            issue_key = issue['key']
            tasks_list.append(issue_key)
        start_at += max_results
    else:
        print(f'Error: {response.status_code} - {response.text}')
        break
    session.close()



jira = JIRA(server='', basic_auth=(username, password))

currentYear = datetime.datetime.now().year
currentMonth = datetime.datetime.now().month
currentDay = datetime.datetime.now().day
date = datetime.datetime(currentYear,currentMonth,currentDay)
one_day_ago = date - timedelta(days=1)
one_day_ago = str(one_day_ago.date())


for main_issue_key in tasks_list:
    main_issue = jira.issue(main_issue_key, expand='issuelinks')
    issuelinks = main_issue.fields.issuelinks
    for link in issuelinks:
        if hasattr(link, 'inwardIssue'):
            sub_issue = link.inwardIssue.key
            comments = jira.comments(sub_issue)
            if comments:
                for comment in comments:
                    created_date = comment.created.split('T')[0]
                    print(created_date, one_day_ago)
                    if created_date == one_day_ago:
                        comment_body = f"Moved from subtask {sub_issue}:\n{comment.author.displayName}: {comment.body}"
                        jira.add_comment(main_issue_key, body=comment_body)

        elif hasattr(link, 'outwardIssue'):
            sub_issue = link.outwardIssue.key
            comments = jira.comments(sub_issue)
            if comments:
                for comment in comments:
                    created_date = comment.created.split('T')[0]
                    print(created_date, one_day_ago)
                    if created_date == one_day_ago:
                        comment_body = f"Moved from subtask {sub_issue}:\n{comment.author.displayName}: {comment.body}"
                        jira.add_comment(main_issue_key, body=comment_body)

jira.close()


