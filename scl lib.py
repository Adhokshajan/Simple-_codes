import pickle as p
f=open("scl lib.dat","wb+")
d={}
#Create Function
def create():
    x=int(input("Enter No.of Books to be Entered"))
    for i in range(x):
        name=input("Enter Book name")
        no=int(input("Enter Book No"))
        cost=int(input("Enter the cost"))
        d["name"]=name
        d["no"]=no
        d["cost"]=cost
        p.dump(d,f)
    f.close()

#Display Function'''
f=open("scl lib.dat","rb+")
def display():
    try:
        while True:
            d=p.load(f)
            print(d)
    except:
        f.close()


#Search Function'''
f=open("scl lib.dat","rb+")
def search():
    e=input("Enter Book No.")
    try:
        z=True
        while z :
            d=p.load(f)
            if d["no"]==e:
                print(d)
                z=False
    except:
        f.close()



#Modify Function
f=open("scl lib.dat","rb+")
def modify():
    try:
        z=True
        while z:
            x=f.tell()
            d=p.load(f)
            if d["no"]==1500:
                f.seek(x)
                d["cost"]+=150
                z=False
                p.dump(d,f)

    except:
        
        f.close()
















print("Welcome to Library")
print('''1.create a book record
      2.Display All Book
      3.search a book
      4.Modify A record''')
b=True

    
s=int(input("Enter your option"))
if s==1:
    create()
elif s==2:
    display()
elif s==3:
    search()
else:
    modify()

while b:
    
    

    c=input("Would you like to continue(Yes/No")
    if c=="Yes"or c=="yes":
        
           
        s=int(input("Enter your option"))
        if s==1:
            create()
        elif s==2:
            display()
        elif s==3:
            search()
        else:
            modify()


    else:
        b=False
           




    
            
    

