from tkinter import *     #learnt in 11th Std
import mysql.connector as sqltor     #learnt in 12th Std
mycon=sqltor.connect(host='localhost',user='root',passwd='MySQL@Class12',database='CSProject')

#Registration
def register_window():
    global register_screen
    register_screen= Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x250")
    global username_entry
    global password_entry
    Label(register_screen, text="Please enter details below",bg="yellow").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen,show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="yellow", command = register_user).pack()

def register_user():
    username_info = username_entry.get()
    password_info= password_entry.get()
    cursor1=mycon.cursor()
    cursor1.execute("select * from credentials")
    data=cursor1.fetchall()
    for i in data:
        if i[0]==username_info:
            Label(register_screen,text="Username already exists! Please close app and try again",font=('calibri',11)).pack()
            break
    else:
        query="insert into credentials values('{}','{}')".format(username_info,password_info)
        cursor2=mycon.cursor()
        cursor2.execute(query)
        Label(register_screen, text="Registration Success!", fg="black", font=("calibri", 11)).pack()
        Label(register_screen, text="Go to front page and login ",fg="black", font=("calibri", 11)).pack()
        Label(register_screen, text="with same username & password", fg="black", font=("calibri", 11)).pack()
        mycon.commit()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
#Login
def login_window():
    global login_screen
    login_screen= Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x250")
    Label(login_screen, text='Please enter details below to login').pack()
    Label(login_screen, text="").pack()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username").pack()
    username_login_entry= Entry(login_screen)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen,show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command =login_verify).pack()

def login_verify():
    username=username_login_entry.get()
    password=password_login_entry.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    cursor1=mycon.cursor()
    cursor1.execute("select * from credentials")
    data=cursor1.fetchall()
    for i in data:
        if i[0]==username:
            if i[1]==password:
                login_success()
                break
            else:
                password_not_recognised()
                break
    else:
        user_not_found()

def login_success():
    login_screen.destroy()
    main_screen.destroy()
    graphing()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen= Toplevel(login_screen)
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.title("Error!")
    Label(password_not_recog_screen, text="Invalid Password!").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen= Toplevel(login_screen)
    user_not_found_screen.title("Error!")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

#Plotting the Graph
def graphing():
    import matplotlib.pyplot as plt #from w3schools.com
    print('Login Successful!')
    print('Do you want to:')
    print('1. Read and plot data from a csv files')
    print('2. Plot a graph of a given equation')
    print('3. See stock prices')
    print('4. Exit')
    s=True
    while s==True:
        print()
        choice=input('Enter 1, 2, 3 or 4: ')
        if choice=='1':
            import csv
            filename=input('Enter file name(Ex: File.csv) ')
            x2=[]
            y2=[]
            with open(filename,'r') as f:
                c=csv.reader(f)
                for i in c:
                    [x,y]=i
                    x2.append(float(x))
                    y2.append(float(y))
                xaxis=input('Enter x axis label ')
                yaxis=input('Enter y axis label ')
                title=input('Enter title ')
                labl=input('Enter label for the line ')
                print('If u want to save the figure, click save button option in bottom part of MatPlotLib screen')
                plt.plot(x2,y2, label=labl,marker='o')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                plt.title(title)
                plt.legend([labl])
                plt.show()
        elif choice=='2':
            n=int(input('Enter no.of equations to be plotted '))
            import numpy as np #from www.geeksforgeeks.org
            a=eval(input('Enter starting point of x axis '))
            b=eval(input('Enter ending point of x axis '))
            print('Enter RHS of the equation in terms of x')
            print('Instructions: use ** for raising exponents,* for multiplication,/ for division, np.sin(x), np.cos(x), etc. for trigonometric functions, np.exp(x) for e^x and np.pi for pi')
            for i in range(0,n):
                x=np.arange(a,b,0.1)
                #print(x)
                y=eval(input('Enter Equation y='))
                ls=input("Enter the line's style(solid/dashed/dotted/dashdot) ")
                lw=float(input("Enter the line's width "))
                c=input("Enter the line's colour(blue/green/red/magenta/yellow/black/cyan/white/brown) ")
                labl=input('Enter label for the equation ')
                plt.plot(x, y, label=labl, color=c, linestyle=ls, linewidth= lw)
                y=None
            xaxis=input('Enter x axis label ')
            yaxis=input('Enter y axis label ')
            title=input('Enter title ')
            print('If u want to save the figure, click save button option in bottom part of MatPlotLib screen')
            plt.grid()
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)
            plt.legend()
            plt.title(title)
            plt.show()
        elif choice=='3':
            import datetime as dt
            import yfinance as yf
            import pandas as pd
            tname=input('Enter ticker name of the company(ex., AAPL for apple, MSFT for microsoft) \nSearch on the web for ticker names if you do not know ')
            dd1=int(input('Enter start day '))
            mm1=int(input('Enter start month '))
            yyyy1=int(input('Enter start year(yyyy) '))
            dd2=int(input('Enter end day '))
            mm2=int(input('Enter end month '))
            yyyy2=int(input('Enter end year(yyyy) '))
            print('If u want to save the figure, click save button option in bottom part of MatPlotLib screen')
            start_date=dt.date(yyyy1, mm1, dd1)
            end_date=dt.date(yyyy2,mm2,dd2)
            title=tname+' '+'Closing Prices'
            #print(start_date,end_date,tname)
            data = pd.DataFrame(yf.download(tname, start=start_date, end=end_date));
            #print(data)
            close = data['Close']
            #print(close)
            plt.plot(close)
            plt.grid()
            plt.xlabel('Dates')
            plt.ylabel('Closing Prices')
            plt.legend([tname])
            plt.title(title)
            plt.show()
        elif choice=='4':
            print("Exit!")
            s=False
        else:
            print('Invalid choice')
        continue

def main_account_screen():
    global main_screen
    main_screen= Tk()
    main_screen.geometry("500x250")
    main_screen.title("Login Page")
    Label(text="Please Login to Continue", bg="yellow", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command =login_window).pack()
    Label(text="").pack()
    Label(text="New User? Register with us:-",width="300", height="2", font=("Calibri", 8)).pack()
    Button(text="Register", height="2", width="30", command=register_window).pack()
    main_screen.mainloop()

#Initialsising the program
main_account_screen()