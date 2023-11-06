import socket


def run():

  if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080

    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect((host, port))

    while True:
      file = open("Selected_User.txt","r")
      filename = (file.read)
      try:
        fi = open(filename, "r")
        data = fi.read
        if not data:
          break
        while data:
          sock.send(str(data).encode())
          data = fi.read()
          fi.close()

      except IOError :
          print('Error 01: requested file not found')





#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#client.connect(('0.0.0.0',8080))
#client.send("I am CLIENT\n".encode())
#from_server = client.recv(4096)
#client.close()
#print(from_server.decode)
