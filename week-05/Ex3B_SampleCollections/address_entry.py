# Exercise 3.B Lab 3 - Address Entry

# Create a dictionary with contact information
contact_info = {
    "name": "Jamie Smith",
    "address": "123 Main Street",
    "city": "Wilmington",
    "state": "DE",
    "zip": "19801"
}

# Display original mailing address
print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

# Remove the original name
contact_info.pop("name")

# Create a new name dictionary
full_name = {
    "first name": "Jamie",
    "last name": "Smith"
}

# Add an honorific
full_name.update({"honorific": "Mx."})

# Add the name dictionary to contact_info
contact_info.update({"full_name": full_name})

# Display updated mailing address
print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")