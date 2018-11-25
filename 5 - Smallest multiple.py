found = True
num = 20
while found:
    matched = True
    for x in range(1, 21):
        if num % x > 0:
            matched = False
            break

    if matched == True:
        found = False
    num = num+1
print (num-1)
