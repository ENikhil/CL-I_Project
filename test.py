import os
import string
import sys

count = 0
global lol_o_w
lol_o_w = []
global t
global l_o_w
l_o_w = []
global match
match = 0
file = open("test-conll-040419-token-with-replaced-tags.txt", 'r')
lines = (line.rstrip() for line in file)
lines = (line for line in lines if line)
for line in lines:
	count+=1
	line=line.split()
	word=line[0]
	tag = line[1]
	val = line[2]
	l_o_w.append([word, tag, val])
	if word == "।":
	    lol_o_w.append(l_o_w)
	    l_o_w = []

#featf = open("BIS.txt", 'r')
#lines = (line.rstrip() for line in featf)
#lines = (line for line in lines if line)
flag = 0

bist = open("BIS.txt", 'r')
lines = (line.rstrip() for line in bist)
lines = (line for line in lines if line)

featf = open("store.txt", 'r')
books = (book.rstrip() for book in featf)
books = (book for book in books if book)
flag = 0
feat = 0
for i, sentence in enumerate(lol_o_w):
	print(sentence)
	for j, w in enumerate(sentence):
		flag=0
		feat=0
	    for line in lines:
	        if(flag == 0 and line.split()[0] == w[0]):
	            flag = 1
	            t = line.split()[1]
	            if(t == w[1]):
	                binary = 1
	                if(binary == w[2]):
	                    match += 1
	            elif(w[2]==0):
	                    match+=1
	        elif(flag == 1):
	            break
	        else:
	            continue
		    if(flag == 1):
		        flag = 0
		        continue
		    else:
		        for book in books:
		            if(flag == 0 and book.split()[0] == w):
		                flag = 1
		                t = book.split()[1]
		            elif(flag == 0):
		              continue
		            elif(flag == 2):
		                    break
		            elif(flag == 1):
		                if(feat == 0):
		                    arg1 = book.split()[2]
		                    if(arg1 == "<start>" and j == 0):
		                        feat = 1
		                        continue
		                    elif(arg1 == sentence[j-1][0]):
		                        feat = 1
		                        continue
		                    else:
		                        flag = 2
		                        continue
		                elif(feat == 1):
		                    arg1 = book.split()[2]
		                    arg2 = book.split()[3]
		                    if(arg1 == "<start>" and j == 0):
		                            feat = 2
		                            continue
		                    elif(arg1 == sentence[j-1][0] and arg2 == "<start>" and j == 1):
		                        feat = 2
		                        continue
		                    elif(arg1 == sentence[j-1][0] and arg2 == sentence[j-2][0]):
		                        feat = 2
		                        continue
		                    else:
		                        flag = 2
		                        continue
		                elif(feat==2):
		                    arg1 = book.split()[2] 
		                    arg2 = book.split()[3]
		                    if(arg1 == "<start>"):
		                        feat = 3
		                        continue
		                    elif(arg1 == sentence[j-1][0] and arg2==sentence[j-1][1]):
		                        feat = 3
		                        continue
		                    else:
		                        flag = 2
		                        continue
		                elif(feat==3):
		                    arg1 = book.split()[2]
		                    arg2 = book.split()[3]
		                    arg3 = book.split()[4]
		                    if(arg1 == "<start>" and j == 0):
		                            feat = 4
		                            continue
		                    elif(arg1 == sentence[j-1][0] and arg2 == "<start>" and j == 1 and arg3 == sentence[j-1][0]):
		                        feat = 4
		                        continue
		                    elif(arg1 == sentence[j-1][0] and arg2 == sentence[j-2][0] and j == len(sentence)-1 and arg3 == "<end>"):
		                        feat = 4
		                        continue
		                    elif(arg1 == sentence[j-1][0] and arg2 == sentence[j-2][0] and arg3 == sentence[j+1][0]):
		                        feat = 4
		                        continue
		                    else:
		                        flag = 4
		                        continue
		                elif(feat==4):
		                    flag = 5
		                    continue
		                elif(feat==5):
		                    arg1 = book.split()[2]
		                    arg2 = book.split()[3]
		                    if(arg1 == "<end>" and j == len(sentence)-1):
		                        feat = 6
		                        continue
		                    elif(arg1 == sentence[j+1][0]):
		                        feat = 6
		                        continue
		                    else:
		                        flag = 2
		                        continue
		                elif(feat == 6):
		                    if(t == w[1]):
		                            binary=1
		                            if(binary == w[2]):
		                                    match+=1
		                    elif( w[2]==0):
		                            match+=1
	print(str(match*100/count)+"% accuracy")
