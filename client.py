# Description: Asks the user for their name, then establishes a socket with
# the server, once attatched, it opens the GUI and terminal.py takes over
# from there.

import socket, os, terminal

# PORT NUMBER TO USE
PORT = 6111


# Main client function, asks for the users, name, spins up a socket and then
# loads the GUI for the duration of execution. Closes the socket after the GUI
# closes.
def client():

    # Make sure the port gets passed down from the global scope
    global PORT

    os.system("stty sane")
    name = input("What is your name: ")
    print("Hello {}!".format(name))

    # Create the socket
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the host
    sender_socket.connect((socket.gethostname(), PORT))

    # Set a flag for the duration of the program running
    sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Send a signal identifying the client
    id = "{}".format(name)
    sender_socket.send(bytes(id, 'utf-8'))
    
    # Run the GUI
    terminal.loader(sender_socket, name)

    # Close the socket when we are done
    sender_socket.close()

if __name__ == "__main__":
    client()