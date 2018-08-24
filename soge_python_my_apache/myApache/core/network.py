from api import parse_request, HTTPResponse, HTTPStatus, HTTPDuplex, format_response
import socket
import threading
import yaml
import os.path

def handle_request(conn, addr):
    print("test")
    request = conn.recv(1024).decode('utf8').rstrip()
    parsed_request = parse_request(request)

    print(conn)

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../configs/core.yml")

    file = open(path)

    addonsList = yaml.load(file)

    file.close()

    print(addonsList['addons'])

    duplex = HTTPDuplex()

    duplex.request = parsed_request
    duplex.response = None
    duplex.socket = conn

    List = []

    for addon in addonsList['addons']:
        try:
           List.append(getattr(getattr(__import__('addons.' + addon), addon), addon))
           print("Bien importé : ", addon, '.')
        except ImportError:
           print("Erreur en important ", addon, '.')

    for addon in List:
        this_addon = addon(addon)
        this_addon.execute(duplex)

    conn.send(format_response(duplex.response).encode())
    conn.close()

    return parsed_request


class Server(object):

    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.conn.bind(('127.0.0.1', 8080))

        self.conn.listen(2)

    def start(self):
        while True:
            conn, addr = self.conn.accept() #Tupple
            Thread = threading.Thread(target=handle_request, args=(conn, addr))
            Thread.deamon = True # ?
            Thread.start()
