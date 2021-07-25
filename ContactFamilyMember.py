import csv
from twilio.rest import Client
import random

contacts_names = []
contacts_numbers = []
with open('contacts.csv', mode='r', newline='') as contacts:
    reader = csv.DictReader(contacts)
    for row in reader:
        contacts_names.append(row['name'])
        contacts_numbers.append(row['number'])

account_sid = 'AC8dec5cd2d7a53061645615fd0a1bb899'
auth_token = '849f361c952d94568c8af44958060b70'
client = Client(account_sid, auth_token)
contact_to_call = random.choice(contacts_names)
index_for_contact = contacts_names.index(contact_to_call)
message = client.messages.create(
    from_='+18305496084',
    body=f'You should call {contact_to_call} today. The number is {contacts_numbers[index_for_contact]}',
    to='+17702352270'
)