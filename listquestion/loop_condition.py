#Looping & Conditions
#Write a loop that goes through a list of numbers and prints "even" or "odd" next to each number.

num = [2,20,16,98,45,37,78,99,2,88]
for n in num:
    if n % 2 == 0:
        print("even",n)
    else:
        print("odd",n)