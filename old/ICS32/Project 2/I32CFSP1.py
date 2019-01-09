from collections import namedtuple
import socket

ConnectFourConnection = namedtuple('ConnectFourConnection',
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

def start_connection(host: str, port: int) -> ConnectFourConnection:
    I32CFSP_socket = socket.socket()
    I32CFSP_socket.connect((host, port))

    I32CFSP_socket_in = I32CFSP_socket.makefile('r')
    I32CFSP_socket_out = I32CFSP_socket.makefile('w')

    return ConnectFourConnection(
        socket = I32CFSP_socket,
        socket_in = I32CFSP_socket_in,
        socket_out = I32CFSP_socket_out)
    
def hello(connection: ConnectFourConnection, username: str) -> None:
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    _expect_line(connection, 'I32CFSP_HLLO')

def send_move(connection: ConnectFourConnection, move: ConnectFourMove):
    pass
    

def close_connection(connection: ConnectFourConnection) -> None:
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()

def _read_line(connection: ConnectFourConnection) -> str:
    return connection.socket_in.readline()[:-1]

def _expect_line(connection: ConnectFourConnection, expected: str) -> None:
    line = _read_line(connection)
    if line != expected:
        raise I32CFSPError()

def _write_line(connection: ConnectFourConnection, line: str) -> None:
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()

