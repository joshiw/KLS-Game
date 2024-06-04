import socket

def main():
    host = '127.0.0.1'
    port = 5555

    server_connection = socket.socket()
    server_connection.bind((host, port))

    server_connection.listen(2)
    player1 = server_connection.accept()
    player2 = server_connection.accept()