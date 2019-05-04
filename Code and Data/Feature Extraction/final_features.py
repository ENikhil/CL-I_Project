# TO STORE OUTPUT OF CODE, RUN THE FOLLOWING COMMAND IN THE TERMINAL:
# python3 final_features.py | tee "name of file".txt


import math


morphemes = dict()


def feature(tags):
    m = len(tags)
    n = m
    n = n + 4
    a = [["0", "0"] for i in range(n)]
    for i in range(n):
        
        a[0][0] = "<start>"
        a[0][1] = "none"
        a[1][0] = "<start>"
        a[1][1] = a[n-2][1] = a[n-1][1]= "none"
        a[n-1-1][0] = a[n-1][0] = "<end>"
        for i in range(2, n-2):
            a[i][0] = tags[i-2][0]
            a[i][1] = tags[i-2][1]
                
    final = [0] * m *  8
    arr = [[" " for i in range(5)] for j in range(m * 8)] 

    x = 1
    for i in range(m):
        for j in range(i*8, i*8+8):
            if a[i+2][1] != "CC_CCD" and a[i+2][1] != "CC_CCS" and a[i+2][1] != "PR_PRF" and a[i+2][1] != "PR_PRL" and a[i+2][1] != "PR_PRP" and a[i+2][1] != "PR_PRQ" and a[i+2][1] != "RD_PUNC" and a[i+2][1] != "RD_SYM" : 
                arr[j][0] = a[i+2][0]
    for i in range(m):
        if a[i+2][1] != "CC_CCD" and a[i+2][1] != "CC_CCS" and a[i+2][1] != "PR_PRF" and a[i+2][1] != "PR_PRL" and a[i+2][1] != "PR_PRP" and a[i+2][1] != "PR_PRQ" and a[i+2][1] != "RD_PUNC" and a[i+2][1] != "RD_SYM" : 
            for j in range(i*8, i*8+1):

            
                arr[j][x] = a[i+2][1]
                j+=1
                x = 1
                arr[j][x] = a[i+1][0]
                j+=1
                x = 1
                arr[j][x] = a[i+1][0]
                x+=1
                arr[j][x] = a[i][0]
                j+=1
                x = 1
                arr[j][x] = a[i][0]
                j+=1
                x = 1
                arr[j][x] = a[i+1][0]
                x+=1
                arr[j][x] = a[i+3][0]
                j+=1
                x = 1
                arr[j][x] = a[i+3][0]
                x+=1
                arr[j][x] = a[i+4][0]
                j+=1
                x = 1
                arr[j][x] = a[i+3][0]
                j+=1
                x = 1
                arr[j][x] = a[i+4][0]
                x = 1
    k = 1

    for i in range(m*8):
        s = int(math.floor(i/8))
        if a[s +2][1] != "CC_CCD" and a[s +2][1] != "CC_CCS" and a[s +2][1] != "PR_PRF" and a[s +2][1] != "PR_PRL" \
                and a[s +2][1] != "PR_PRP" and a[s +2][1] != "PR_PRQ" and a[s +2][1] != "RD_PUNC" and a[s +2][1] != "RD_SYM" : 
            if (i % 8 == 0):
                currentMorpheme = (arr[i][0], arr[i][1])
            else:
                if currentMorpheme not in morphemes: morphemes[currentMorpheme] = []
                morphemes[currentMorpheme].append(arr[i])
    
        # for line in morpheme:
        #     for item in line:
        #         f.write(item)
        #     f.write('\n')
            
    #print(arr)       
    f.write("\n")

def read(fl):
    for line in fl:
        tags = []
        for line in fl:
            line = line.strip()
            if len(line) <= 0:
                feature(tags)
                break
            tags.append((line.split()[0], line.split()[1]))
    
    
xx = open("train_data.txt", "r", encoding = 'utf-8')
read(xx)  

for morpheme in morphemes:
    print('\n', morpheme[0] + '  ' + morpheme[1], '\n')
    for line in morphemes[morpheme]:
        print(line[0], line[1], line[2], line[3], line[4])
