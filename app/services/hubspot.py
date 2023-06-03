import requests
import os
from dotenv import load_dotenv

load_dotenv()


class HubSpotAPI():
    def __init__(self):
        self.HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")
        self.api = "https://api.hubspot.com/crm/v3"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.HUBSPOT_TOKEN}",
        }

    def get_contacts(self):
        url = f"{self.api}/objects/contacts"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def create_contact(self, payload):
        url = f"{self.api}/objects/contacts"
        response = requests.post(url, headers=self.headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
