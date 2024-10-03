'''
Add new contacts.
Search contacts by name.
Update contact information (like phone number or email).
Delete contacts.

'''

phone_book = {}
#Name, Phonenumbers and emails

def add_contact(name, phone_numbers, emails=None):
    phone_book[name] = {}

    contact = phone_book.get(name)

    contact['phone_numbers'] = phone_numbers
    contact['emails'] = emails

    print("Contact saved Successfully")
#     print(f"""
#         Name: {name},
#         Phone Numbers : {'|'.join(phone_numbers)}
#         Emails : {'|'.join(emails)}
# """)

def search(name):
    contact = phone_book.get(name)
    if contact is None:
        print(f"This person is not available in your contacts")
    else:
        print(name)
        print(contact)


add_contact("Aisha", ["08033124903", "09023467908"], ["aisha@gmail.com","aisha@yahoo.com"])
add_contact("Olamide", ["08033124903", "09023467908"], ["olamide@gmail.com","olamide@yahoo.com"])
search("Aisha")