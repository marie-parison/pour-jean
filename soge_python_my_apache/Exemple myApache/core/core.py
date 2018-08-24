from .network import NetworkServer

def start():
    server = NetworkServer()
    server.start()