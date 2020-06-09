import time


def loading():
    for x in range(3):
        for y in range (4):
            print('Loading' + "." * y)    
            time.sleep(0.5) 

def list():
    Verena={
        "Name"  : "Name      : Verena Andrea",
        "Age"   : "Age       : 16",
        "Crime" : "Crime     : makan dikelas"
           }
    Pilip={
        "Name"  : "Name      : Pilip",
        "Age"   : "Age       : 17",
        "Crime" : "Crime     : bobo dikelas"
           }
    Vannes={
        "Name"  : "Name      : Vannes",
        "Age"   : "Age       : 17",
        "Crime" : "Crime     : maen hp"
           }
    VW={
        "Name"  : "Name      : VW",
        "Age"   : "Age       : 16",
        "Crime" : "Crime     : ngupil"
           }
    
    dicts=[Verena,Pilip,Vannes,VW]
    print(len(dicts), "KETAUAN")
    for dict in dicts:
        print(dict["Name"])
        print(dict["Age"])
        print(dict["Crime"])

while True:
    password=input("Password:")
    password1=password
    if password1=="vwjamet":
        print("---------------")
        print("DPO INDONESIA")
        print("---------------")
        time.sleep(0.5)
        loading()
        time.sleep(0.5)
        list()
        break

    else :
        print("salah password")