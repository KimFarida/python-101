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
        return False
    else:
        return contact

def update(name, phone_numbers, emails=None):
    contact = search(name)

    if not contact:
        return
    else:
        if phone_numbers:
            saved_phone_numbers = contact.get("phone_numbers", [])
            saved_phone_numbers.extend(phone_numbers)
        if emails:
            saved_emails = contact.get("emails", [])
            saved_emails.extend(emails)

        return f"""
        We have successfully updated {name} with
         Phone Numbers : {'|'.join(phone_numbers)}
         Emails : {'|'.join(emails) if emails else 'No email added'}
         Updated Contact : {contact}
         """


def delete(name):
    contact = search(name)
    if not contact:
        return f"Could not delete"
    contact_details = phone_book.pop(name)
    return f"Successfully deleted {contact_details}"

add_contact("Aisha", ["08033124903", "09023467908"], ["aisha@gmail.com","aisha@yahoo.com"])
add_contact("Olamide", ["08033124903", "09023467908"], ["olamide@gmail.com","olamide@yahoo.com"])
print(search("Aisha"))
print(update("Aisha", ["09137000975"], ["aisha@icloud.com"]))
print(delete("Olamide"))
print(phone_book)