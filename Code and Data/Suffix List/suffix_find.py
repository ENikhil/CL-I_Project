import math
suf = open("suffix.txt", "a+", encoding = 'utf-8')
def find_suff(tags):
    m = len(tags)
    n = m
    n = n + 4
    a = [["0", "0"] for i in range(m)]
    for i in range(m):
        x = str(tags[i][0])
        a[i][0] = x[-3:]
        a[i][1] = tags[i][1]
                
    final = [0] * m *  8
    arr = [[" " for i in range(5)] for j in range(m * 8)] 

    x = 1
    # for i in range(m):
    #     for j in range(i*8, i*8+8):
    #         if a[i+2][1] != "CC_CCD" and a[i+2][1] != "CC_CCS" and a[i+2][1] != "PR_PRF" and a[i+2][1] != "PR_PRL" and a[i+2][1] != "PR_PRP" and a[i+2][1] != "PR_PRQ" and a[i+2][1] != "RD_PUNC" and a[i+2][1] != "RD_SYM" : 
    #             arr[j][0] = a[i+2][0]
    for i in range(m):
        if a[i][1] != "CC_CCD" and a[i][1] != "CC_CCS" and a[i][1] != "PR_PRF" and a[i][1] != "PR_PRL" and a[i][1] != "PR_PRP" and a[i][1] != "PR_PRQ" and a[i][1] != "RD_PUNC" and a[i][1] != "RD_SYM" : 
            suf.write(a[i][0] + " " + a[i][1] + "\n")

def read(fl):
    for line in fl:
        tags = []
        for line in fl:
            line = line.strip()
            if len(line) <= 0:
                find_suff(tags)
                break
            tags.append((line.split()[0], line.split()[1]))
    
    
xx = open("train_data.txt", "r", encoding = 'utf-8')
read(xx)  
