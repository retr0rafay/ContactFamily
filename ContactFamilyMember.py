# In order to use this program, you must have a CSV file that contains the names and phone numbers of your friends and family. For example, I have the
# name of the person in the first column and the enumber in the second column, so something like name,number and then you can fill the values in the columns.

# You'll first need to create a Twilio trial account, and you should receive an account sid and auth token. Do not put it out in public (like how I did)
# since people can steal them, but these current ones are expired so it's fine for now. 

# You can host your PY and CSV files in a server, so for example I have it hosted on Python Anywhere. The server runs every day at about 1 PM EST since I
# have it set up that way, but you can choose your own time on when you want this program run.

# Have any questions? Reach out to me!

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
