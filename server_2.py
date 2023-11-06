import socket
import os


def run():
      if __name__ == '__main__':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', 8080))
            sock.listen(5)
            connections = []
            print({"initiating clients"})
            for i in range (5):
                  conn = sock.accept()
                  connections.append(conn)
                  print('connectected to client', i+1)

            index = 0
            filenumber= 0 
            for conn in connections:
                  index += 1 
                  data = conn[0].recv(1024).decode()
                  if not data:
                        continue
                  os.chdir('(',str(filenumber),',)')
                  filename = 'output'+str(filenumber)+'.txt'
                  filenumber = filenumber+1
                  fo = open(filename, "w")
                  while data:
                        if not data:
                              break
                        else:
                              fo.write(data)
                              data = conn[0].recv(1024).decode()

                  print()
                  print('recieving data from client', index)
                  print()
                  print("transfer complete new filename = ", filename)

            for conn in connections:
                  conn[0].close()
                                