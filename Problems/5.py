cont = True
N = 1
while(cont):
    for i in range(1,21):
        if N%i != 0:
            N+=1
            break
    else:
        print(N)
        break
