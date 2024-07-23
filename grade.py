print("Enter marks obtained in 5 subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int (input())


tot = markOne + markTwo + markThree + markFour + markFive
avg = tot/5
print("Average=%.5f",avg)
if avg>=70 and avg<=100:
    print("Your grade is A")
elif avg>=60 and avg <=69:
    print("Your grade is B")
elif avg>=50 and avg<= 59:
    print("Your grade is C")
elif avg>=40 and avg <= 49:
    print("your gade is D")
else:
    print("Invalid input")