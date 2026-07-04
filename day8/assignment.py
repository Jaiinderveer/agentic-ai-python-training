"""  
WhatsApp

Classes / Objects:

1. User
---------------------
user_id
name
phone
email
gender
bio
profile_image
availability_status
addresses[]
contacts[]
stories[]
groups[]
communities[]

2. Contact
---------------------
contact_id
name
phone
email
gender
bio
profile_image
availability_status
addresses[]

3. Message
---------------------
message_id
sender
receiver
message
message_type        
time
status              
length

4. Story
---------------------
story_id
media
caption
aspect_ratio
visibility          // Everyone, Contacts, Selected Contacts
upload_time
expiry_time
views
likes

5. Group
---------------------
group_id
group_name
group_icon
description
members[]
admins[]
messages[]
typing_status

6. Community
---------------------
community_id
community_name
community_icon
description
admins[]
members[]
groups[]

Relationships
---------------------
1 User → Many Contacts
1 User → Many Stories
1 User → Many Groups
1 User → Many Communities

1 Group → Many Users (Members)
1 Group → Many Admins
1 Group → Many Messages

1 Community → Many Groups
1 Community → Many Members
1 Community → Many Admins

1 User → Sends Many Messages
1 User → Receives Many Messages
    
"""

class User:

    # Constructor
    def __init__(self, user_id, name, phone, email):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = None
        self.bio = ""
        self.profile_image = None
        self.availability_status = "Online"

        self.contacts = []
        self.stories = []
        self.groups = []
        self.communities = []


class Contact:

    def __init__(self, contact_id, name, phone):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = None
        self.gender = None
        self.bio = ""
        self.profile_image = None
        self.availability_status = "Offline"


class Message:

    def __init__(self, sender, receiver, content, message_type):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.message_type = message_type 
        self.time = None
        self.status = "Sent"                
        self.length = len(content)


class Story:

    def __init__(self, media):
        self.media = media
        self.aspect_ratio = "9:16"
        self.visibility = "Contacts"
        self.views = 0
        self.likes = 0
        self.upload_time = None
        self.expiry_time = None


class Group:

    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.admins = []
        self.messages = []
        self.typing_status = {}


class Community:

    def __init__(self, community_name):
        self.community_name = community_name
        self.members = []
        self.admins = []
        self.groups = []


# User
user = User(1, "Jai", "9876543210", "jai@gmail.com")
user.name = "Jaiinder"

# Contacts
contact1 = Contact(101, "Rahul", "9876500000")
contact2 = Contact(102, "Anil", "9876504000")
contact3 = Contact(103, "Yash", "9876505000")

user.contacts = [contact1, contact2, contact3]

# Story
story = Story("my_photo.jpg")
user.stories.append(story)

# Messages
message1 = Message(user, contact1, "Hello!", "Text")
message2 = Message(user, contact2, "Hello Bhambri!", "Text")
message3 = Message(user, contact3, "Hello Jai!", "Text")

# Group
group = Group("Python Learners")
group.members = [user, contact1, contact2, contact3]
group.admins = [user]
group.messages = [message1, message2, message3]

user.groups.append(group)

# Community
community = Community("GNDEC Students")
community.admins = [user]
community.members = [user, contact1, contact2, contact3]
community.groups = [group]

user.communities.append(community)
print('~~~~~~~~~~~~~~~~~~~~~~')
print('User:',user)
print('contact1:',contact1)
print('contact2:',contact2)
print('contact3:',contact3)
print('Message1:',message1)
print('Message2:',message2)
print('Message3:',message3)
print('~~~~~~~~~~~~~~~~~~~~~~')
print('data in User:',vars(user))
print('data in contact1:',vars(contact1))
print('data in contact2:',vars(contact2))
print('data in contact3:',vars(contact3))
print('data in Message1:',vars(message1))
print('data in Message2:',vars(message2))
print('data in Message3:',vars(message3))
print('~~~~~~~~~~~~~~~~~~~~~~')