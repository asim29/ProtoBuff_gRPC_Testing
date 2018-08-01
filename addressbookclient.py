from __future__ import print_function

import random

import grpc

import addressbook_pb2
import addressbook_pb2_grpc


def Write(stub):
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = "Asim"
    person.email = "asimwaheed@gmail.com"
    phone_number = person.phones.add()
    phone_number.number = "5138008"
    phone_number.type = addressbook_pb2.Person.HOME 
    # PromptForAddress(person)
    response = stub.WriteToBook(person)
    if response.reply == "OK":
        print("Person added into address book")
    else:
        print("Something went wrong")

def Read(stub):
    tosend = addressbook_pb2.Response(reply = "Send all")
    persons = stub.ReadFromBook(tosend)
    for person in persons:
        print(person.id)
        print(person.name)
        print(person.email)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = addressbook_pb2_grpc.AddressBookComStub(channel)
    print("-------------- Writing --------------")
    Write(stub)
    print("-------------- Reading --------------")
    Read(stub)
    # print("-------------- RecordRoute --------------")
    # guide_record_route(stub)
    # print("-------------- RouteChat --------------")
    # guide_route_chat(stub)


if __name__ == '__main__':
    run()
