import os
import string
import sys
import codecs
count=0
match=0
llw=[] #List of sentences/list_of_words (Contains test data)
lw=[] #List of words (Sentences in test data)

testfile=open("test-conll-040419-token-with-replaced-tags.txt", 'r')
lines=(line.rstrip() for line in testfile)
lines=(line for line in lines if line) #Removes empty lines from file

#Initializing lists with words, tags and truth values from test data
for line in lines:
	count+=1 #Number of words in test data
	line=line.split()
	word=line[0]
	ttag=line[1]
	val=line[2]
	lw.append([word,ttag,val]) #Adding word entry to the sentence list
	if word == '।':
		llw.append(lw) #Adding sentence to the list of sentences
		lw=[]

#Adding the feature dictionary to a list of lists
fdict=open("features.txt", 'r')
ens=(en.rstrip() for en in fdict)
ens=(en for en in ens if en)
feature=[]
feat=[]
for i,en in enumerate(ens):
	if(i==0):
		k=en.split()[0]
		feature.append(en)
	else:
		if en.split()[0]==k:
			feature.append(en)
		else:
			feat.append(feature)
			feature=[]
			k=en.split()[0]
			feature.append(en)

bist=open("BIS.txt", 'r')

for k, sentence in enumerate(llw): #Iterating through sentences
	for j, w in enumerate(sentence): #Iterating through word entries
		flag=0
		featno=0
		bist.seek(0,0)
		for line in bist:
			if (flag==0) and (line.split()[0]==w[0]): #Checking 'test' list with dictionary of words from closed class
				flag=1
				if (line.split()[1]==w[1]):
					if(int(w[2])==0):
						match+=1
				elif (int(w[2])==0):
					match+=1
					break
			else:
				continue
		if (flag==1):
			continue
		else:
			tag=""
			#Initializing all features
			f1=-1
			f2=-1
			f3=-1
			f4=-1
			f5=-1
			f6=-1
			f7=-1
			i=0
			flag=0
			found=0
			while (i<len(feat)) * (found==0): #Checking if the word can be found in the feature dictionary
				if (w[0]==feat[i][0].split()[0]):
					feature=feat[i]
					found=1
					tag=feat[i][0].split()[1]
					break
				else:
					i+=1
					continue
			if(found==0): #Giving a default N_NN tag to the word in case it can't be found in the feature dictionary
				if(w[1]=="NN_N") * (int(w[2])==0):
					match+=1
				elif (w[1]!="NN_N") * (int(w[2])==1):
					match+=1
				continue
			i=1
			while (i<len(feature)) * (found==1): #Iterating through features of the specific word
					if (i%7==1) * (f1==-1): #Feature 1
						if (j==0):
							if(feature[i].split()[1]=="<start>"):
								f1=1
								i=2
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f1=0
									i=2
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]):
							f1=1
							i=2
							continue
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f1=0
								i=2
								continue
					elif (i%7==2) * (f2==-1): #Feature 2
						if (j==0):
							if(feature[i].split()[1]=="<start>") * (feature[i].split()[2]=="<start>"):
								f2=1
								i=3
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f2=0
									i=3
									continue
						if (j==1):
							if(feature[i].split()[1]==sentence[j-1][0]) * (feature[i].split()[2]=="<start>"):
								f2=1
								i=3
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f2=0
									i=3
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]) * (sentence[j-2][0]==feature[i].split()[2]):
							f2=1
							i=3
							continue
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f2=0
								i=3
								continue
					elif (i%7==3) * (f3==-1): #Feature 3
						if (j<=1):
							if(feature[i].split()[1]=="<start>"):
								f3=1
								i=4
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f3=0
									i=4
									continue
						elif (sentence[j-2][0]==feature[i].split()[1]):
							f3=1
							i=4
							continue
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f3=0
								i=4
								continue
					elif (i%7==4) * (f4==-1): #Feature 4
						if (j==0):
							if(feature[i].split()[1]=="<start>") * (feature[i].split()[2]=="<start>"):
								f4=1
								i=5
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f4=0
									i=5
									continue
						elif (j==1):
							if(feature[i].split()[1]==sentence[j-1][0]) * (feature[i].split()[2]=="<start>"):
								f4=1
								i=5
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f4=0
									i=5
									continue
						elif (j==(len(sentence)-2)):
							if(feature[i].split()[3]==sentence[j+1][0]) * (feature[i].split()[4]=="<end>"):
								f4=1
								i=5
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f4=0
									i=5
									continue
						elif (j==(len(sentence)-1)):
							if(feature[i].split()[3]=="<end>") * (feature[i].split()[4]=="<end>"):
								f4=1
								i=5
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f4=0
									i=5
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]) * (sentence[j-2][0]==feature[i].split()[2]) * (sentence[j+1][0]==feature[i].split()[3]) * (sentence[j+2][0]==feature[i].split()[4]):
							f4=1
							i=5
							continue
						else:
							i+=7							
							if (i<len(feature)):
								continue
							else:
								f4=0
								i=5
								continue
					elif (i%7==5) * (f5==-1): #Feature 5
						if (j==len(sentence)-1):
							if(feature[i].split()[1]=="<end>") * (feature[i].split()[2]=="<end>"):
								f5=1
								i=6
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f5=0
									i=6
									continue
						if (j==len(sentence)-2):
							if(feature[i].split()[1]==sentence[j+1][0]) * (feature[i].split()[2]=="<end>"):
								f5=1
								i=6
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f5=0
									i=6
									continue
						elif (sentence[j+1][0]==feature[i].split()[1]) * (sentence[j+2][0]==feature[i].split()[2]):
							f5=1
							i=6
							continue
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f5=0
								i=6
								continue
					elif (i%7==6) * (f6==-1): #Feature 6
						if (j==len(sentence)-1):
							if(feature[i].split()[1]=="<end>"):
								f6=1
								i=7
								continue
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f6=0
									i=7
									continue
						elif (sentence[j+1][0]==feature[i].split()[1]):
							f6=1
							i=7
							continue
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f6=0
								i=7
								continue
					elif (i%7==0) * (f7==-1): #Feature 7
						if (j>=len(sentence)-2):
							if(feature[i].split()[1]=="<end>"):
								f7=1
								break
							else:
								i+=7
								if (i<len(feature)):
									continue
								else:
									f7=0
									break
						elif (sentence[j+2][0]==feature[i].split()[1]):
							f7=1
							break
						else:
							i+=7
							if (i<len(feature)):
								continue
							else:
								f7=0
								break
			fsum=f1+f2+f3+f4+f5+f6+f7 #Checking if the feature sum is more than half the features
			if (fsum>=3):
				if(w[1]==tag) and (int(w[2])==0):
				elif (int(w[2])==1) and (w[1]!=tag):
					match+=1
print("Number of accurate tags: "+str(match))
print("Total number of words in testing data: "+str(count))
print("Accuracy= "+str(match*100/count)+" %")