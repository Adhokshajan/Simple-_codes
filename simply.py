import pickle as p 
e=input("enter your choice ")
z=open("flowers.dat","rb+")
"""this is simmply done to check git push"""


if e=="flowers":
    try:
        z.seek(0)
        while True:
            d=p.load(z)
            print(d)

    except:
        z.close()