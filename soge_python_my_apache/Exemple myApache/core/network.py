import sys
from threading import Thread
import socket

from api import parse_request, HTTPResponse, HTTPStatus, format_response

def handle_request(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    input = conn.recv(MAX_BUFFER_SIZE).decode('utf8').rstrip()
    parsed_request = False

    try:
        parsed_request = parse_request(input)
    except Exception as e:
        print('Error while parsing request:', e)
    finally:
        print(vars(parsed_request))
        response = HTTPResponse(
            version=parsed_request.version,
            headers=parsed_request.headers,
            body='OKKK',
            status=HTTPStatus.Status.OK
        )
        conn.send(format_response(response).encode())
        conn.close()

        return parsed_request


class NetworkServer(object):
    def __init__(self):        
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print('Socket created')

        try:
            self.conn.bind(('localhost', 8080))
        except socket.error as message:
            print('Bind failed. Error : ', message)

            return

        self.conn.listen(2)

        print('Socket now listening')

    def start(self):
        while True:
            conn, addr = self.conn.accept()
            ip, port = str(addr[0]), str(addr[1])

            print('Accepting connection from', ip, ':', port)
            
            try:
                Thread(target=handle_request, args=(conn, ip, port)).start()
            except Exception as message:
                print('Can\'t create client, error:', message)