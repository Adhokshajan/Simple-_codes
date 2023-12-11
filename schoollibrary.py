import pickle as p
import random as r
f=open("Books.dat","rb+")
f1=open("register.dat","rb+")
f2=open("cart.dat","wb+")
f3=open("feedback.txt","w+")

def search():
    print("Search Menu")
    z=int(input("Press 1 to Search by Book Name \nPress 2 to Search by Author Name "))
    if z==1:

        pt=input("Enter book name ")
        c=0
        try:
            f.seek(0)
            while True:
                d=p.load(f)
                if d["Name"]==pt:
                    print(d)
                    c+=1
                    m=input("Would you like to order the book(Y/N) ")
                    if m=="Y":
                        order()


        except:
            print(c,"Matches Found")
    elif z==2:
        pt=input("Enter Author Name ")
        c=0
        try:
            f.seek(0)
            while True:
                d=p.load(f)
                if d["Author Name"]==pt:
                    print(d)
                    c+=1
                    m=input("Would you like to order this book(Y/N) ")
                    if m=="Y":
                        order()


        except:
            print(c,"Matches Found")
def order():
        
        x=True
        while x:
            r=input("Enter the book name you would like to order  ")
            try:
                f.seek(0)
                while True:
                    d=p.load(f)
                   
                    if d['Name']==r:
                        print(d)
                        p.dump(d,f2)

            except:
            
                t=input("Would You like to order any other book(Yes/No)  ")
                if t=="No": 
                   cart()
                   break
def update():
    No=int(input("Enter Number of Books to be added"))
    for i in range(No):
        d={}
        d["name"]=input("Enter Book Name").lower
        d["author"]=input("Enter Author Name").lower
        d["genre"]=input("Enter Genre").lower
        d["cost"]=int(input("Enter Cost"))
def payment():
    c=0
    try:
        f2.seek(0)
        while True:
            d=p.load(f2)
            c+=int(d["Cost"])

    except:
        print("Total Cost is ", c)
        print()
        print()
        print("Robot Verification")
        l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        l1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        l2=["1","2","3","4","5","6","7","8","9","0"]
        l3=["!","@","$","#","%","^","&","*"]
        z=True
        while z:
            captcha=""
            captcha=r.choice(l)+r.choice(l1)+r.choice(l2)+r.choice(l3)
            print(captcha)
            user=input("Enter above Message to proceed for payment") 

            if user==captcha:
                z=False


                print('''What mode of Payment would you like to continue
                Press 1 for UPI
                Press 2 for Net Banking
                Press 3 for Cards
                ''')
                z=int(input("Enter your Option"))
                if z ==1:
                    print("NOTE:You need to have a registerd UPI ID or else it will be created")
                    v=input("Enter your UPI ID")
                   
                    b=bool(v)
                    if b==1:
                        print("Payment Succesfull")
                        print("Redirecting to home page")
                        home()
                        break
                elif z==2:
                    print('''Available Banks
                    1.SBI
                    2.HDFC
                    3.AXIS
                    4.ICICI''')
                    v=input("Enter Your Bank Name")
                    if v=="SBI":
                        k=input("Enter Acc. No.")
                        l=bool(k)
                        if l==1:
                            print("Payment Succesfull")
                            print("Redirecting to home page")
                            home()
                            break
                    elif v=="HDFC":
                        k=input("Enter Acc. No.")
                        l=bool(k)
                        if l==1:
                            print("Payment Succesfull")
                            print("Redirecting to home page")
                            home()
                            break

                    elif v=="AXIS":
                        k=input("Enter Acc. No.")
                        l=bool(k)
                        if l==1:
                            print("Payment Succesfull")
                            print("Redirecting to home page")
                            home()
                            break
                    elif v=="ICICI":
                        k=input("Enter Acc. No.")
                        l=bool(k)
                        if l==1:
                            print("Payment Succesfull")
                            print("Redirecting to home page")
                            home()
                            break

                elif z==3:
                    print("According to the new guidelines of RBI , We do not store your card information")
                    t=float(input("Enter your Card No.  "))
                    g=int(input("Enter CVV  "))
                    l=bool(t)
                    k=bool(g)
                    if l==1 and k==1 :
                        print("Payment Succesfull")
                        print("Redirecting to home ")
                        home()


            else:
                z=True
                print("Try again")          
def register():
    m={}
    i=int(input("Are You a New Member \n 1.Yes \n 2.No \n Enter 1 or 2 "))
    x=True
    if i==1:
        
        m["email"]=input("enter email id")
        password=input("Enter a valid password \n Length Should Be 8 or more \n  One digit is necessary")
        m["password"]=password
        while x :

            if len(password)<8 or password.isalnum()==False :
                 print("please read the restrictions")
                 password=input("Enter a valid password \n Length Should Be 8 or more \n One special character is necssary \n One digit is necessary")
            else:
                x=False
            
                  
        else:
            print("succesfully registered")
            p.dump(m,f1)
            f1.seek(0)
            
            
    elif i==2:
        email=input("enter your email id ")
        pwd=input("Enter your Password")
        try:
            f1.seek(0)
            while True:
                d=p.load(f1)
                if d["email"]==email and d["password"]==pwd:
                    print("Succesfull Login")
                    break
        except:
           f1.close()
           
           display()
def display():
    try:
       f.seek(0)
       while True:
           d=p.load(f)
           print("Name :",d["Name"],end="  ,  ")
           print("Genre:",d["Genre"],end="  ,  ")
           print("Cost:",d["Cost"],end="  ,  ")
           print("Author Name:",d["Author Name"])
           print()
           print()
    except:
        e=input("Would you like to order any book(Yes/No)  ")
        if e=="Yes":
            order()
        else:
            print("Redirecting to home page")
            home()
def cart():
    print("Your Cart")
    try:
        f2.seek(0)
        while True:
            d=p.load(f2)
            print(d)

    except:
        g=input("Would you like to continue to payment(Yes/No)  ")
        if g=="Yes":
            payment()
        else:
            print("Redirecting to home page")
            home()
def feedback():
    e=input("Enter your feedback  ")
    f3.writelines(e)
    print("Thank You for your Valueable Feedback")
    n=input("Would you like to continue shopping (Y/N)  ")
    if n=="Y":
        home()
    else:
        print("Thanks For Shopping")
        exit()
def contact():
    print("Instagram:                 ")
    print("Facebook:           " )
    print("Email(For Promotions):          ")
def home():

    while True:
        x=int(input(("Enter \n 1.TO DISPLAY BOOKS AND THEIR DETAILS \n 2.Cart \n 3.Payment \n 4.Contact Us 5.Feedback\n 6.register\n7.exit\n8.Search a Book")))
        if x==1:
            display()
        elif x==2:
            cart()
        elif x==3:
            payment()
        elif x==4:
            contact()
        elif x==5:
            feedback()
        elif x==6:
            register()
        elif x==7:
            print("Thanks For Shopping")
            exit()
        elif x==8:
            search()
        else:
            cont=input("Enter \n 1 TO CONTINUE SHOPPING \n 2 TO BREAK ")
            if cont==1:
                pass
            else:
                break
def edit(file):
    i=int(input(" Press 1 to Edit Book Name \n Press 2 to Edit Cost \n Press 3 to Edit Genre \n Press 4 to Edit Author Name"))
    if i==1:
        v=input("ENter Author Name")
        z=input("Enter the correct name of the book ")
        try:
            f.seek(0)
            while True:
                c=f.tell()
                d=p.load(f)
                if d["Author Name"]==v:
                    f.seek(c)
                    d["Name"]=z
        except:
            print("Book Name Edited")


    elif i==2:
        v=input("Enter Book Name")
        z=input("Enter the correct cost of the book ")
        try:
            f.seek(0)
            while True:
                c=f.tell()
                d=p.load(f)
                if d[" Name"]==v:
                    f.seek(c)
                    d["Cost"]=z
        except:
            print("Cost Edited")

    elif i==3:
        v=input("Enter Book Name")
        z=input("Enter the correct genre of the book ")
        try:
            f.seek(0)
            while True:
                c=f.tell()
                d=p.load(f)
                if d["Name"]==v:
                    f.seek(c)
                    d["Genre"]=z
        except:
            print("Genre Edited")



    elif i==4:
        v=input("Enter Book Name")
        z=input("Enter the correct author of the book ")
        try:
            f.seek(0)
            while True:
                c=f.tell()
                d=p.load(f)
                if d["Name"]==v:
                    f.seek(c)
                    d["Author Name"]=z
        except:
            print("Author Name Edited")
home()
f.close()
f1.close()
f2.close()
f3.close()


    
    

            
       








    

