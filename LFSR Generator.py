from collections import deque

loop = int(input("How many iterations of the lfsr would you like to see : "))
seed = input("Enter a 4 bit seed(eg: 1101):\t ")
LFSRfile = open("LFSR.txt", "w+")

seedQueue = deque(seed)
print("The seed entered is:\t\t", seed)

#xor function performs an XOR operation on the 1st and 3rd values inputted, and returns the output of the operation 
def xor(que):
    if(que[0] == que[2]):
        return 0
    else:
        return 1
#Loop to show the desired number of iterations of the LFSR   
def lfsrLoop():
    for j in range(0, loop):
        x = xor(seedQueue)
        seedQueue.pop()
        seedQueue.appendleft(x)
        lfsrList = (list(seedQueue))
        lfsrStr = ''.join(map(str,lfsrList))
        q = str(j + 1)
        print("Iteration", j + 1, "of the seed is:\t", lfsrStr)
        LFSRfile.write("Iteration " + q + " of the seed is:\t" + lfsrStr + "\n")

if(len(seed) != 4):
    print("You have entered a seed that is not of the correct size")
    exit()
else:
    lfsrLoop()
input()
