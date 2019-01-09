from collections import namedtuple
import connectfour
import I32CFSP
import ConnectFourGame
import socket

def _run_user_interface() -> None:
    host = I32CFSP.select_host()
    port = I32CFSP.select_port()
    connection = I32CFSP.start_connection(host, port)
    username = _ask_for_username()
    try:
        I32CFSP.hello(connection, username)
        I32CFSP.send(connection, 'AI_GAME')
        

    finally:
        I32CFSP.close_connection(connection)




def _handle_command(connection: I32CFSP.ConnectFourConnection) -> bool:
    command = input('[D]rop or [P]op ').strip().upper()

    if command == 'D':
        pass
    
def _handle_drop_command(connection: I32CFSP.ConnectFourConnection) -> None:
    column_to_drop = input('Column to drop in: ').strip()

    if column_to_drop == 0:
        pass



def _ask_for_username() -> str:
    while True:
        username = input('Username: ')
        if len(username) > 1:
            return username
        else:
            print('That username is not valid')



if __name__ == '__main__':
    _run_user_interface()
