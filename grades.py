print("Grades")
print("---------------")

try:
    nilai = float(input("Enter your score :"))

    if nilai <= 0.3 :
        print("final grade: E")
    elif nilai <= 0.5 : 
        print("final grade: D")
    elif nilai <= 0.65 :    
        print("final grade: C")
    elif nilai <= 0.85 :    
        print("final grade: B")
    elif nilai <= 1.0 : 
        print("final grade: A") 
    else: 
        print("invalid input")

except ValueError:
        print('ada salah gan')


