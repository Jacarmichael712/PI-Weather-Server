import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = (sys.argv[1], 6000)
print("Connecting to {} port {}".format(server_addr[0], server_addr[1]), file=sys.stderr)
sock.connect(server_addr)

try:
    #message = input("Input the location you want the current weather for\nformat: 'city, state, country, unit' where unit is metric or imperial\n")
    message = 'Greenville, SC, US, imperial'
    msg_arr = message.split(", ")

    print("Getting weather data for: {}, {}, {} in {} units".format(msg_arr[0], msg_arr[1], msg_arr[2], msg_arr[3]), file=sys.stderr)

    sock.sendall(message.encode())
    weather = ""

    while True:
        try:
            data = sock.recv(16)
        except:
            break
        else:
            weather += data.decode('utf-8')

            if(len(data.decode()) < 16):
                break
            
    print(weather, file=sys.stderr)

finally:
    print("Closing socket...", file=sys.stderr)
    sock.close()