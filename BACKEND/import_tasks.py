from joinbackend_app.models import Task
import os
import django
import json

# Django Umgebung einrichten
# Ersetze mit deinem Projekt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joinbackend.settings")
django.setup()

tasks = [
    {
        "type": "User Story",
        "title": "User registry",
        "description": "As a user I want to be able to register myself",
        "subtasks": [
            {
                "subtaskText": "Formular",
                "complete": True
            },
            {
                "subtaskText": "Privacy Policy",
                "complete": False
            }
        ],
        "finishedSubtasks": 1,
        "assignedTo": [
            {
                "firstName": "Anton",
                "lastName": "Mayer",
                "profileColor": "#FF7A00"
            },
            {
                "firstName": "Benedikt",
                "lastName": "Ziegler",
                "profileColor": "#9327FF"
            }
        ],
        "category": "feedback",
        "priority": "Low",
        "dueDate": "2024-09-23"
    },
    {
        "type": "User Story",
        "title": "Tasks on board",
        "description": "As a user I want to see my tasks on the board",
        "subtasks": [
            {
                "subtaskText": "design",
                "complete": False
            },
            {
                "subtaskText": "add tasks on board",
                "complete": False
            }
        ],
        "finishedSubtasks": 0,
        "assignedTo": [
            {
                "firstName": "Christoph",
                "lastName": "Völker",
                "profileColor": "#FF7A00"
            }
        ],
        "category": "todo",
        "priority": "Urgent",
        "dueDate": "2025-01-01"
    },
    {
        "type": "Technical Task",
        "title": "Responsiveness with CSS",
        "description": "Support for several viewports",
        "subtasks": [
            {
                "subtaskText": "Desktop view",
                "complete": False
            },
            {
                "subtaskText": "Mobile view",
                "complete": True
            }
        ],
        "finishedSubtasks": 1,
        "assignedTo": [
            {
                "firstName": "Anton",
                "lastName": "Mayer",
                "profileColor": "#FF7A00"
            },
            {
                "firstName": "Benedikt",
                "lastName": "Ziegler",
                "profileColor": "#9327FF"
            }
        ],
        "category": "todo",
        "priority": "Urgent",
        "dueDate": "2024-12-03"
    },
    {
        "type": "User Story",
        "title": "Contacts",
        "description": "As a user I want to see my contacts",
        "subtasks": [
            {
                "subtaskText": "order alphabetically",
                "complete": False
            },
            {
                "subtaskText": "add users to tasks",
                "complete": False
            }
        ],
        "finishedSubtasks": 0,
        "assignedTo": [
            {
                "firstName": "Anton",
                "lastName": "Mayer",
                "profileColor": "#FF7A00"
            },
            {
                "firstName": "Benedikt",
                "lastName": "Ziegler",
                "profileColor": "#9327FF"
            }
        ],
        "category": "done",
        "priority": "Medium",
        "dueDate": "2024-08-04"
    },
    {
        "type": "User Story",
        "title": "Legal Notice etc.",
        "description": "As a user I want to know what happens with my data",
        "subtasks": [
            {
                "subtaskText": "Legal notice",
                "complete": False
            },
            {
                "subtaskText": "Privacy Policy",
                "complete": False
            }
        ],
        "finishedSubtasks": 0,
        "assignedTo": [
            {
                "firstName": "Anton",
                "lastName": "Mayer",
                "profileColor": "#FF7A00"
            },
            {
                "firstName": "Benedikt",
                "lastName": "Ziegler",
                "profileColor": "#9327FF"
            }
        ],
        "category": "progress",
        "priority": "Low",
        "dueDate": "2024-11-03"
    }
]


# Tasks in die Datenbank speichern


def import_tasks():
    for task in tasks:
        Task.objects.create(

        )
    print("Import abgeschlossen!")


def delete_tasks():
    Task.objects.all().delete()
    print("Alles löschen abgeschlossen!")


# Funktion ausführen
if __name__ == "__main__":
    delete_tasks()
    import_tasks()
