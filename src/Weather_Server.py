import socket
import sys
import API_Calls

# create a TCP/IP socket using IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the TCP/IP socket to the pi's address with a port you choose
# I chose port 6000 for simplicity, but you could change it
server_name = sys.argv[1]
server_addr = (server_name, 6000)

# print start up message to stderr and bind server address to socket
print("Starting up pi-weather-server on {} port {}".format(server_addr[0], server_addr[1]), file=sys.stderr)
sock.bind(server_addr)

# listen on this socket for a connection
sock.listen(1)

while True:
    print("Waiting for a connection...", file=sys.stderr)
    conn, client_addr = sock.accept()

    try:
        input = ""
        print("client connected: {}".format(client_addr), file=sys.stderr)
        while True:
            try:
                data = conn.recv(16)
            except:
                break
            else:
                print("received {}".format(data), file=sys.stderr)
                input += data.decode('utf-8')

                if(len(data.decode()) < 16):
                    print("No more data to receive", file=sys.stderr)
                    break

        print("Data received from client\nClient request: {}".format(input), file=sys.stderr)
        # make an array of city, state, country by splitting loc data
        data_split = input.split(", ")
        message = API_Calls.getWeatherInfo(data_split[0], data_split[1], data_split[2], data_split[3])

        conn.sendall(message.encode())

    finally:
        # close connection when finished
        conn.close()