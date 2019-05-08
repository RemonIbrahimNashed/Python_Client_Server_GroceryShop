__author__ = "RemonIbrahim"

import socket
import json 
import sys
from _thread import start_new_thread

HOST = '127.0.0.1'
PORT = 3000

# define a dictionary to hold the prices of every item in our shop 
prices = {'Apple_Price':20 , "Orange_Price":10 , "Banana_Price":30 }

def client_thread(conn, addr):

    client_id =  str(addr[0]) + ":" + str(addr[1])
    print("[-] Sending prices to " + client_id)
# conver the dictionry prices into JSON STRING then into Byte Object 
    data_byte = json.dumps(prices).encode('UTF-8')
# send the prices Byte Object to the Client 
    conn.sendall(data_byte)
    
    print("[-] All Prices are sent to "+ client_id)
    print("[-] Waiting order from  "+  client_id)
# recieve the Order from the client as Byte Object  
    while True :
        data = conn.recv(1024)
        if not data :
            break 
# convert the order to JSON STRING 
        data = data.decode('UTF-8')
# then finally convert the Order to DICTIONARY 
        data = json.loads(data)
        print("[-] Order recived from "+  client_id)
        
# collect info from the order 
        orange_num = data['orange_num']
        apple_num = data['apple_num']
        banana_num = data['banana_num']
# calculate the final price 
        final_price = orange_num * prices["Orange_Price"] + apple_num * prices['Apple_Price'] + banana_num * prices['Banana_Price'] 
# send the final Price 
        print("[-] Sending total Price to "+ client_id)
        conn.send(str(final_price).encode())
# close the connection with the client 
    conn.close()
    print("[-] connection finished with "+ client_id)



def main():
    s = socket.socket()
# try to open port in server 
    try:
        s.bind((HOST, PORT))
        print("[-] Socket Bound to port " + str(PORT))
    except socket.error as msg:
        print("Bind Failed.")
        sys.exit()
# server can listen to 10 clients at same time 
    
    s.listen(10)
    while True:
        
        conn, addr = s.accept()
        print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
        start_new_thread(client_thread, (conn,addr))

    conn.close()
    s.close()
    

if __name__ == '__main__':
    main()