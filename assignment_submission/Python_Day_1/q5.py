# accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.  

marks = int(input("Enter the marks you scored out of 100 : "))

if marks > 90:
    print("Distinction !")
elif marks > 80:
    print("First Class")
elif marks > 70:
    print("Second Class")
elif marks > 40:
    print("Third Class")
else:
    print("Fail")