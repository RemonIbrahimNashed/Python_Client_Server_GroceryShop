from tkinter import *

def main():
    window = Tk()
    app(window)

class app():
    def __init__(self ,rootWindow):
        self.window = rootWindow 

        self.appWidth = 650 
        self.appHeight = 300 
        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHight = self.window.winfo_screenheight()

        self.xToCenterTheApp = self.screenWidth/2 - self.appWidth/2
        self.yToCenterTheApp = self.screenHight/2 - self.appHeight/2
        
        self.window.geometry('%dx%d+%d+%d' % (self.appWidth, self.appHeight, self.xToCenterTheApp, self.yToCenterTheApp))
        self.window.resizable(0,0)
        self.window.title('Simple Tkinter Calculator')
        
        
        self.welcomLabel= Label(self.window, text="Welcom to our simple calculator", fg='blue', font=('Comic Sans MS',20)).place(x=100,y=30) 
        self.num1Label= Label(self.window, text="Enter First  Number : ", fg='black', font=('Comic Sans MS',15)).place(x=30,y=100) 
        self.num2Label= Label(self.window, text="Enter Second Number : ", fg='black', font=('Comic Sans MS',15)).place(x=30,y=130) 

        self.num1Text = StringVar(self.window)
        self.num2Text = StringVar(self.window)
        self.num1Entry = Entry(self.window,textvariable = self.num1Text ,font=('Comic Sans MS',15)).place(x=245,y=100,width=200)
        self.num2Entry = Entry(self.window,textvariable = self.num2Text,font=('Comic Sans MS',15)).place(x=245,y=130,width=200)

        self.operationLabel= Label(self.window, text="Choose an operation : ", fg='black', font=('Comic Sans MS',15)).place(x=30,y=170) 
        self.sumButton = Button(text="+",command=lambda:self.get_result('+'),bg='green', fg='black',font=('Comic Sans MS',15) ).place(x=250,y=170)
        self.difButton = Button(text="-",command=lambda:self.get_result('-'),bg='green', fg='black',font=('Comic Sans MS',15) ).place(x=300,y=170)
        self.mulButton = Button(text="*",command=lambda:self.get_result('*'),bg='green', fg='black',font=('Comic Sans MS',15) ).place(x=350,y=170)
        self.divButton = Button(text="/",command=lambda:self.get_result('/'),bg='green', fg='black',font=('Comic Sans MS',15) ).place(x=400,y=170)

        self.ResultLabel= Label(self.window, text="Result is : ", fg='black', font=('Comic Sans MS',18)).place(x=30,y=210) 
        self.outputResult = StringVar(self.window)
        self.outputResult.set('')
        self.outputLabel= Label(self.window, textvariable=self.outputResult, fg='brown', font=('Comic Sans MS',18)).place(x=150,y=210) 

        self.error = StringVar(self.window)
        self.errorLabel= Label(self.window, textvariable=self.error, fg='red', font=('Comic Sans MS',20)).place(x=230,y=240) 

        self.window.mainloop()
    def get_result(self,op):
        result = ''
        try :
            num1 = float(self.num1Text.get())
            num2 = float(self.num2Text.get())
        except ValueError :
            result = ''
            self.outputResult.set(result)
            self.error.set("wrong numbers")
            return 
        if(op == '+') :
            result = num1 + num2 
        elif(op == '-') : 
            result = num1 - num2
        elif(op == '*') :
            result = num1 * num2
        elif(op == '/') :
            if( num2 != 0 ):
                result = num1 / num2
            else :
                result = ''
                self.outputResult.set(result)
                self.error.set("you can't divide by 0")
                return 
        self.error.set("")
        self.outputResult.set(result)
        


if __name__ == '__main__':
    main()