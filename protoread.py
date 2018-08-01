import addressbook_pb2
import sys

def ListPeople(address_book):
	for person in address_book.people:
		print "Person ID:", person.id
		print "  Name:", person.name
		if person.email != "":
			print "  Email:", person.email

		for phone_number in person.phones:
			if phone_number.type == addressbook_pb2.Person.MOBILE:
				print "  Mobile Phone #: "
			elif phone_number.type == addressbook_pb2.Person.HOME:
				print "  Home Phone #: "
			elif phone_number.type == addressbook_pb2.Person.WORK:
				print "  WORK Phone #: "
			print "  ", phone_number.number

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
	sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)

