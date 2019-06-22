from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "--address",
    help="the address to host application, default is 'localhost'",
    default="localhost",
)
parser.add_argument(
    "-p", "--port", help="The port of the server application default is '5532'", default="5532"
)


def accept_incoming_connections():

    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Digite seu username para o chat", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = "Ben vindo %s para sair digite {quit}." % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s Entrou na sala!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s Saiu da sala." % name, "utf8"))
            break


def broadcast(msg, prefix=""):

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

args = parser.parse_args()

HOST = args.address
PORT = int(args.port)

BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Aguardando conexão no endereço {} porta {}".format(HOST, PORT))
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
