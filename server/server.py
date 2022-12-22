import time
import socket

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
print(extract_ip())
time.sleep(1)

HOST = extract_ip() #Sets the HOST variable to the IP address of current local network
PORT = 32323 #PORT can be anything as long as it's not occupied by some other program

print(HOST)
time.sleep(1)

#Create a socket object from the socket module, AF_INET = IPv4 addresses, SOCK_STREAM = TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind our socket to the HOST and PORT tuple

server.bind((HOST, PORT))

#Listen for incoming connections (we set maximum queue size to 1)

while True:
    server.listen(1)
    print("[SERVER] Server is listening...")

    #Accept incoming client, this function returns the client and their address

    client, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    while True: #forever loop unless broken

        try:
            data = client.recv(1024)
        except:
            break
        data = data.decode('UTF-8')
        print(f"{addr}: {data}")

