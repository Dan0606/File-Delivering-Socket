import socket
HOST = '127.0.0.1'
PORT = 52472 


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    resp = s.recv(10).decode()
    filesize = int(resp)
    data = s.recv(filesize)
    while len(data) < filesize:
        print("downloading..." + str(len(data)/filesize*100) + "%")
        data += s.recv(filesize - len(data))
    filename2 = "C:\\Users\\danda\\OneDrive\\שולחן העבודה\\download des\\ draw.png"
    f2 = open(filename2, "wb")
    f2.write(data)
    f2.close()
    s.close()

main()