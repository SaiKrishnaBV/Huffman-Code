import math
import sys
global prob
prob= []

def findpos(val, i):
    for j in range(len(prob)):
        if(val >= prob[j]):
            return j
    return i-1 
            

def dispFeatures(code, prob):
    length = [len(k) for k in finalCode]
    
    mean = sum([a*b for a,b in zip(length,prob)])
    
    var = 0
    for k in range(len(length)):
        var = var + ((length[k]-mean)**2)*P[k]

    entropy = 0
    for j in prob:
        entropy = entropy + j*(math.log(1/j))/math.log(2)
    print finalCode
    print("Average length of the code: %f" %mean)

    print("Entropy of the system: %f" %entropy)

    print("Variance of the code: %f" %var)

    print("Efficiency of the code: %f" %(entropy/mean))

        
    
    
prob = input("Enter probabilities: ")
if(sum(prob) != 1):
    print("Entered probabilities dont add upto 1")
    sys.exit()
prob = sorted(prob, reverse = True)
P = prob

n = len(prob)
code = ['']*n
for i in range(n-2):
    val = prob[n-i-1]+ prob[n-i-2]
    if(code[n-i-1] != '' and code[n-i-2] != ''):
        code[-1] = ['1' + k for k in code[-1]]
        code[-2] = ['0' + k for k in code[-2]]
    elif(code[n-i-1] != ''):
        code[n-i-2] = '0'
        code[-1] = ['1' + k for k in code[-1]]
    elif(code[n-i-2] != ''):
        code[n-i-1] = '1'
        code[-2] = ['0' + k for k in code[-2]]
    else:
        code[n-i-1] = '1'
        code[n-i-2] = '0'
       
    pos = findpos(val, i)
    prob = prob[0:(len(prob) - 2)]
    prob.insert(pos, val)
    if(isinstance(code[n-i-2], list) and isinstance(code[n-i-1], list)):
        cumulative = code[n-i-1] + code[n-i-2]
        
    elif(isinstance(code[n-i-2], list)):
        cumulative = code[n-i-2] +[code[n-i-1]]
        
    elif(isinstance(code[n-i-1], list)):
        cumulative = code[n-i-1] + [code[n-i-2]]
        
    else:
        cumulative = [code[n-i-2],code[n-i-1]]
    code = code[0:(len(code)-2)]
    code.insert(pos,cumulative)

code[0] = ['0' + k for k in code[0]]
code[1] = ['1' + k for k in code[1]]
if(len(code[1]) == 0):
    code[1] = '1'
print("The minimum variance Huffman code for the given system is:")
count = 0
finalCode = ['']*n
for i in range(2):
    for j in range(len(code[i])):
        finalCode[count] = code[i][j];
        count +=1
finalCode = sorted(finalCode, key = len)

dispFeatures(finalCode, P)

