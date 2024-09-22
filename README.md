# Jira Automation

## Description:

- `comment_to_project.py`: Transfers all comments from subtasks to the parent task. Works for all tasks in the project.

- `comment_to_project_once_a_day.py`: Transfers all comments from subtasks to the parent task. Works for all tasks in the project (for the last 24 hours).

- `create_task_project.py`: Creates a task based on an Excel spreadsheet.

- `project_task_to_another_project.py`: Based on a project task, creates a task in another project.

- `jira.xlsx`: Basic spreadsheet.

## Priority
- Lowest: 5
- Low: 4
- Medium: 3
- High: 2
- Highest: 1
- Critical: 10000
- Blocker: 10001

## Mandatory Fields in jira.xlsx
- `create_task_project.py`: Title, Priority, Category, Description
- `project_task_to_another_project.py`: Executor's Project, Root Task (created by the previous script)

## Notes on project_task_to_another_project.py
The task may not be created if the executor's project has mandatory custom fields. The error response shows the field's ID or name.
If it's the name, look up the ID in `customfield.md` and fill it in the code (suitable for fields with a drop-down list, entered in "Group" in jira.xlsx).

For the execution date field, there is a separate field - "Execution Date" in jira.xlsx.

## How to Use:

### Task Creation Scripts:
Creating a task in our project:
1. Open the attached `jira.xlsx` file and clear it (an example filled spreadsheet is provided in the repository).
2. Fill in the fields according to our project: Title, Priority, Category, Description.
3. Run the `create_task_project.py` script.

Creating a task for the executor:
1. Fill in the mandatory field: Executor's Project.
2. Fill in other fields.
   - If the executor is known, you can write their JIRA id (e.g., IvanovII). In this case, a comment will be created in the task mentioning this user and asking them to take on the task.
3. Run the `project_task_to_another_project.py` script.

Note: If the project not listed above has mandatory fields, you need to find out its ID, add it to the code in the `project_dict` dictionary in the format `'Project': 'id(customfield_...)`.
You can find the ID of this field in the response.

## Jira.xlsx
| Executor's Project | Title       | Priority | Category | Description       | Root Task  | Task        | Team | Period of Execution | Responsible |
|--------------------|-------------|----------|----------|-------------------|------------|-------------|------|----------------------|--------------|
| Project            | Bug fix #1  | 3        |          | Please fix bug    | Project-1  | ProjectDev-2 | Dev  | 07.07.2023           |              |