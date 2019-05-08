__author__ = 'RemonIbrahim'

import socket
import json 
import sys
from tkinter import *
from PIL import ImageTk,Image
import os 

HOST = '127.0.0.1'
PORT = 3000

def main(): 

    while True :
        os.system('clear')
        print("\t\tWelcom to our Grocery Shop")
        response = int(input("[-] Enter (1) for CMD , (2) for GUI : "))
        if response == 1 :
            TUI()
        elif response == 2 :
            GUI()
        else :
            print("Sorry you enterd wrong number")
        again = int(input("[-] Do you want to try again Enter (1) for Yes , (2) for No : "))
        if again != 1 :
            break 
#Text User Interface
def TUI():
    s = socket.socket()
# try to open port in server 
    try:
        s.connect((HOST, PORT))
        print("[-] socket connect to port " + str(PORT))
    except socket.error as msg:
        print("Bind Failed."+str(msg))
        sys.exit()
# recieve the prices from the server 
    data = s.recv(1024)
    data = data.decode("UTF-8")
    data = json.loads(data)
# display the prices on the screen
    print("[-] Prices of today are ")
    print("[-] Orange Price is : ", str(data['Orange_Price']))
    print("[-] Apple  Price is : ", str(data['Apple_Price']))
    print("[-] Banana Price is : ", str(data['Banana_Price']))

# ask for the order 
    print("[-] Now you can tell me what do you want ")
    
    orange_num = input('[-] How many Oranges  do you want : ')
    orange_num = int(orange_num)

    apple_num = input('[-] How many Apples  do you want  : ')
    apple_num = int(apple_num)

    banana_num = input('[-] How many Bananas do you want  : ')
    banana_num = int(banana_num)
# construct the order as dictionry type and  send to server 
    mydict = {"orange_num": orange_num , "apple_num":apple_num , "banana_num":banana_num }
    
    data_byte = json.dumps(mydict).encode('UTF-8')
    s.sendall(data_byte)
# recieve the final price from the server 
    data = s.recv(1024)
    data = data.decode('UTF-8')
    print("[-] total price is "+ str(data))
    s.close()



def GUI():
    window = Tk()
    app(window)

class app():
    def __init__(self , root ):
        self.currency = 'LE/KG'
        self.total = ''
        self.default = '##'
        self.status = 'Disconnected' 
        self.error = ''
       
        self.s = socket.socket()
       
        self.window = root
        self.window.geometry('700x700+500+270')
        self.window.resizable(0,0)
        self.window.title('Grocery Shop') 
        
        self.applePrice = StringVar(self.window)
        self.applePrice.set(self.default+self.currency)

        self.orangePrice = StringVar(self.window)
        self.orangePrice.set(self.default+self.currency)

        self.bananaPrice = StringVar(self.window)
        self.bananaPrice.set(self.default+self.currency)

        self.totalPrice = StringVar(self.window)
        self.totalPrice.set('Total Price : '+self.default+self.currency)

        self.statusText = StringVar(self.window)
        self.statusText.set("You are "+self.status)

        self.errorText = StringVar(self.window)
        

        self.orangeNum = StringVar()
        self.appleNum = StringVar()
        self.bananaNum = StringVar()

    # place the images 
        self.canvas0 = Canvas(self.window, width = 300, height = 300)
        self.canvas0.place(x=10,y=10)
        self.img0 = ImageTk.PhotoImage(Image.open("apple.jpg").resize((150, 150), Image.ANTIALIAS))  
        self.canvas0.create_image(0, 0, anchor=NW, image=self.img0) 

        self.canvas1 = Canvas(self.window, width = 300, height = 300)
        self.canvas1.place(x=170,y=10)
        self.img1 = ImageTk.PhotoImage(Image.open("orange.jpeg").resize((150, 150), Image.ANTIALIAS))  
        self.canvas1.create_image(0, 0, anchor=NW, image=self.img1) 

        self.canvas2 = Canvas(self.window, width = 300, height = 300)
        self.canvas2.place(x=330,y=10)
        self.img2 = ImageTk.PhotoImage(Image.open("banana.jpg").resize((150, 150), Image.ANTIALIAS))  
        self.canvas2.create_image(0, 0, anchor=NW, image=self.img2)

# place the connect to server button 
        self.connectButton = Button(text="ConnectToServer",command=self.connect,bg='grey', fg='green',font=('Comic Sans MS',18) ).place(x=490,y=90)
   
# place the names 
        self.appleLabel = Label(self.window , text="Apple", fg='red',bg='grey', font=('Comic Sans MS',30)).place(x=30,y=180) 
        self.orangeLabel = Label(self.window , text="Orange", fg='orange',bg='grey',font=('Comic Sans MS',30)).place(x=190,y=180)
        self.bananaLabel = Label(self.window , text="Banana", fg='yellow',bg='grey',font=('Comic Sans MS',30)).place(x=350,y=180)
    
# place the prices 
        self.applePriceLabel = Label(self.window , textvariable=self.applePrice , fg='black', font=('Comic Sans MS',20)).place(x=30,y=240)
        self.orangePriceLabel = Label(self.window, textvariable=self.orangePrice , fg='black', font=('Comic Sans MS',20)).place(x=190,y=240)
        self.bananaPriceLabel = Label(self.window , textvariable=self.bananaPrice , fg='black', font=('Comic Sans MS',20)).place(x=350, y=240) 

# place the spinBoxes 
        self.appleSpinBox = Spinbox(self.window, from_=0, to=100 ,textvariable = self.appleNum, font=('Comic Sans MS',20), width=7)
        self.appleSpinBox.place(x=30,y=280)

        self.orangeSpinBox = Spinbox(self.window, from_=0, to=100, textvariable = self.orangeNum,font=('Comic Sans MS',20), width=7)
        self.orangeSpinBox.place(x=190,y=280)

        self.bananaSpinBox = Spinbox(self.window, from_=0, to=100, textvariable = self.bananaNum,font=('Comic Sans MS',20), width=7)
        self.bananaSpinBox.place(x=350,y=280)
# place the check total price button and label  
        self.totalPriceLabel = Label(self.window , textvariable = self.totalPrice ,fg='black', font=('Comic Sans MS',25)).place(x=348,y=360)
        self.checkButton = Button(text="CheckOut",command=self.checkTotalPriceFromServer,bg='grey', fg='blue',font=('Comic Sans MS',30) ).place(x=150,y=350) 
    
# place server client status 
        self.statusLabel = Label(self.window , textvariable = self.statusText ,fg='brown', font=('Comic Sans MS',25)).place(x=150,y=450)
        self.statusLabel = Label(self.window , textvariable = self.errorText ,fg='red', font=('Comic Sans MS',25)).place(x=80,y=490)
# place disconnect button 
        # self.disConnectButton = Button(text="Disconnect",command=self.disconnect,bg='grey', fg='red',font=('Comic Sans MS',18) ).place(x=490,y=130)

        self.window.mainloop()
    def connect(self):
    # try to open port in server 
        if self.error != '':
            self.error = ""
            self.errorText.set(self.error)
            
        if self.status == "Connected":
            self.error = "You are already connected"
            self.errorText.set(self.error)
            return 
        try:
            self.s.connect((HOST, PORT))
            print("[-] socket connect to port " + str(PORT))
        except socket.error as msg:
            print("Bind Failed."+str(msg))
            sys.exit()
        self.status = 'Connected'
        self.statusText.set('You are '+self.status)
# recieve the prices from the server 
        data = self.s.recv(1024)
        data = data.decode("UTF-8")
        data = json.loads(data)
        self.orangePrice.set(str(data['Orange_Price'])+self.currency )
        self.applePrice.set(str(data['Apple_Price'])+self.currency)
        self.bananaPrice.set(str(data['Banana_Price'])+self.currency)
    
    def disconnect(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
        self.orangePrice.set(default+currency)
        self.applePrice.set(default+currency)
        self.bananaPrice.set(default+currency)
        self.totalPrice.set("Total Price : "+default+currency)
        self.status = 'Disconnected'
        self.statusText.set('You are '+status)
        self.orangeSpinBox.delete(0,"end")
        self.appleSpinBox.delete(0,"end")
        self.bananaSpinBox.delete(0,"end")

    def checkTotalPriceFromServer(self):
        if self.status == "Disconnected":
            self.error = "ERROR , you are disconnected ,\n you can't CheckOut"
            self.errorText.set(self.error)
            rerturn 
        self.error = ""
        self.errorText.set(self.error)
        mydict = {'orange_num':int(self.orangeSpinBox.get())  , 'apple_num': int(self.appleSpinBox.get()) , 'banana_num':int(self.bananaSpinBox.get()) }
        data_byte = json.dumps(mydict).encode('UTF-8')
        self.s.sendall(data_byte)
    # recieve the final price from the server 
        data = self.s.recv(1024)
        data = data.decode('UTF-8')
        self.total = data
        self.totalPrice.set("Total Price : "+self.total+self.currency)
        
        
    
if __name__ == '__main__':
    main()