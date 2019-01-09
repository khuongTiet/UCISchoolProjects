from collections import namedtuple
import socket

I32CFSP = namedtuple('I32CFSP',
                     ['socket', 'socket_in', 'socket_out'])

ConnectFourMove = namedtuple('ConnectFourMove',
                             ['command', 'column'])

class I32CFSPError(Exception):
    pass

def select_host() -> str:
    while True:
        host = input('Host: ').strip()
        
        if len(host) == 0:
            print('Please specify a host (either a name or an IP address)')
        else:
            return host


def select_port() -> int:
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
            
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def start_connection(host: str, port: int) -> I32CFSP:
    I32CFSP_socket = socket.socket()
    I32CFSP_socket.connect((host,port))

    I32CFSP_socket_in = I32CFSP_socket.makefile('r')
    I32CFSP_socket_out = I32CFSP_socket.makefile('w')

    return I32CFSP(
        socket = I32CFSP_socket,
        socket_in = I32CFSP_socket_in,
        socket_out = I32CFSP_socket_out)
    
def I32CFSP_hello(connection: I32CFSP, username: str) -> None:
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    _expect_line(connection, 'I32CFSP_HLLO')

def _read_line(connection: I32CFSP) -> str:
    return connection.socket_in.readline()[:-1]

def _expect_line(connection: I32CFSP, expected: str) -> None:
    line = _read_line(connection)
    if line != expected:
        raise I32CFSPError()

def _write_line(connection: I32CFSP, line: str) -> None:
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()
            
"""
def connect_to_server(host: str, port: int) -> None:
    server_socket = socket.socket()
    try:
        print('Connecting to server ...')
        server_socket.connect((host,port))
        server_socket_in = server.socket.makefile('r')
        server_socket_out = server.socket.makefile('w')
        print('Connected successfully!')


        return ConnectFourConnection(socket = server_socket,
            socket_in = server_socket_in,
            socket_out = server_socket_out)


def I32CFSP_HELLO(connection: ConnectFourConnection, username: str) -> None:
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    _expect_line(connection, 'I32CFSP_HELLO')
"""

if __name__ == '__main__':
    k = select_host()
    j = select_port()
    start_connection(k,j)
