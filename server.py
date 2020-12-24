import socket
HOST = '127.0.0.1'
PORT = 52472 


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create TCP socket
    s.bind((HOST, PORT)) 
    s.listen() # open the socket for client connections
    print("waiting for clients...")
    client_connection1, addr = s.accept() 
    filename1 = "C:\\Users\\danda\\OneDrive\\שולחן העבודה\\download src\\draw.png"
    f1 = open(filename1, "rb")
    x = f1.read()
    filesize = str(len(x))
    while len(filesize) < 10:
        filesize = "0" + filesize
    client_connection1.send(filesize.encode())
    client_connection1.send(x)
    f1.close()
    s.close()

main()