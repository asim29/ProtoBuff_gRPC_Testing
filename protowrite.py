#! /user/bin/python

import addressbook_pb2
import sys

# This function fills in a Person message based on the user input.
def PromptForAddress(person):
	person.id = int(raw_input("Enter person ID number: "))
	person.name = raw_input("Enter Name: ")

	email = raw_input("Enter email address (blank for none): ")
	if email != "":
		person.email = email

	while True:
		number = raw_input("Enter a phone number (or leave blank to finish): ")
		if number == "":
			break

		phone_number = person.phones.add()
		phone_number.number = number

		phonetype = raw_input("Is this a mobile, home, or work phone? ")
		if phonetype == "mobile":
			phone_number.type = addressbook_pb2.Person.MOBILE
		elif phonetype == "home":
			phone_number.type = addressbook_pb2.Person.HOME 
		elif phonetype == "work":
			phone_number.type = addressbook_pb2.Person.WORK
		else:
			print "Unknown phone type: Leaving as default value."


# Main Procedure: Reads the entire address book from a file,
# 	adds one person based on user input, then writes it back to the same
	# file
# if len(sys.argv) != 2:
# 	print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
# 	sys.exit(-1)

# address_book = addressbook_pb2.AddressBook()

# # Read the existing address book.
# try:
# 	f = open(sys.argv[1], "rb")
# 	address_book.ParseFromString(f.read())
# 	f.close()
# except IOError:
# 	print sys.argv[1] + ": Could not open file. Creating a new one"

# # Add an address
# person = addressbook_pb2.Person() 
# PromptForAddress(person)
# address_book.people.extend([person])
# # Write the new address book back to the disk
# f = open(sys.argv[1], "wb")
# f.write(address_book.SerializeToString())
# f.close