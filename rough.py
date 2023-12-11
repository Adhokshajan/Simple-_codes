import pickle as p 
#import json as j
f=open("Books.dat","rb+")
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
        f.close()


display()