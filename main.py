
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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
     
    def count(self):
        x = int(self.numberDisplay.text)
        x += 10
        self.numberDisplay.text = str(x)
    
    def sendToServer(self):
        x = self.numberDisplay.text
        x = x.encode('UTF-8')
        client.send(x)




class HelloWorld(App):
    
    def build(self):
        return MyRoot()


HelloWorld = HelloWorld()

HelloWorld.build()
HelloWorld.run()
print(HOST)