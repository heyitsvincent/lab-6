total=0
print "how many are you adding"
userinput= raw_input()
for x in range(userinput):
    print "what is the number"
    total = total + userinput 
    print total 
    
total2 =[]
for x in range(3):
    print "input a number"
    userinput = int(raw_input())
    total2.append(userinput)
print sum(total2)

total3=1
userinput = int(raw_input())
for x in range((1, userinput+1, 1)):
    total=total * x 
print total3

# hello!!