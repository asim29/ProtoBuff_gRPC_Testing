from concurrent import futures
import time
import math

import grpc

import addressbook_pb2
import addressbook_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

filename = "addressbook"

class AddressBookComServicer(addressbook_pb2_grpc.AddressBookComServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.db = addressbook_pb2.AddressBook()

    def WriteToBook(self, request, context):
        print "In write to book"
        addressbook = self.db
        addressbook.people.extend([request])
        f = open(filename, "wb")
        f.write(addressbook.SerializeToString())
        f.close
        
        response = addressbook_pb2.Response()
        response.reply = "OK"
        return response

    def ReadFromBook(self, request, context):
        print "In read from book"
        addressbook = self.db
        if request.reply == "Send all":
            f = open(filename, "rb")
            addressbook.ParseFromString(f.read())
            f.close

            for person in addressbook.people:
                print person.name
                yield person




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressbook_pb2_grpc.add_AddressBookComServicer_to_server(
        AddressBookComServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
