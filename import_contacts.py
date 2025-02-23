import os
import django
import json

# Django Umgebung einrichten
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joinbackend.settings")  # Ersetze mit deinem Projekt
django.setup()


from joinbackend_app.models import Contact


# JSON-Daten
contacts = [
    {
        "firstName": "Anton",
        "lastName": "Mayer",
        "email": "antom@gmail.com",
        "phoneNumber": "235325325",
        "profileColor": "#FF7A00",
    },
    {
        "firstName": "Anja",
        "lastName": "Schulz",
        "email": "anjaschulz@gmail.com",
        "phoneNumber": "235325325",
        "profileColor": "#FFC700",
    },
    {
        "firstName": "Benedikt",
        "lastName": "Ziegler",
        "email": "ziegler@gmx.com",
        "phoneNumber": "235325325",
        "profileColor": "#9327FF",
    },
    {
        "firstName": "David",
        "lastName": "Eisenberg",
        "email": "eisenberg@googlemail.com",
        "phoneNumber": "235325325",
        "profileColor": "#6E52FF",
    },
    {
        "firstName": "Eva",
        "lastName": "Fischer",
        "email": "fischer_eva@gmail.com",
        "phoneNumber": "235325325",
        "profileColor": "#FC71FF",
    },
    {
        "firstName": "Emanuel",
        "lastName": "Mauer",
        "email": "e.mauer@gmail.com",
        "phoneNumber": "235325325",
        "profileColor": "#6E52FF",
    },
    {
        "firstName": "Tatjana",
        "lastName": "Wolf",
        "email": "wolf@gmail.com",
        "phoneNumber": "+49 2 2 2222 222 2",
        "profileColor": "#FF7A00",
    },
    {
        "firstName": "Marcel",
        "lastName": "Bauer",
        "email": "bauer@gmail.com",
        "phoneNumber": "+49 2 2 2222 222 2",
        "profileColor": "#1FD7C1",
    },
]

# Kontakte in die Datenbank speichern


def import_contacts():
    for contact in contacts:
        Contact.objects.create(
            first_name=contact["firstName"],
            last_name=contact["lastName"],
            # Default-Wert, falls kein E-Mail vorhanden ist
            email=contact.get("email", "default@gmx.de"),
            # Falls keine Telefonnummer vorhanden ist
            phone_number=contact.get("phoneNumber", ""),
            profileColor=contact.get("profileColor", "#1FD7C1"),
        )
    print("Import abgeschlossen!")


def delete_contacts():
    Contact.objects.all().delete()
    print("Alles löschen abgeschlossen!")



# Funktion ausführen
if __name__ == "__main__":
    delete_contacts()
    import_contacts()
