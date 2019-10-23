i = int(input("type some number 1 to 100: "))

if i%15==0: 
    print("fizzbuzz")

elif i%3==0 :
    print("buzz")
elif i%5==0 :
    print("fizzbuzz")
else:
    print(i)

