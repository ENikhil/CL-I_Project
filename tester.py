import os
import string
import sys
import codecs
#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")
#Globally declaring all variables to be used
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

fdict=open("features.txt", 'r')
ens=(en.rstrip() for en in fdict)
ens=(en for en in ens if en)
feature=[]
for en in ens:
	feature.append(en)

bist=open("BIS.txt", 'r')
featno=0

for k, sentence in enumerate(llw): #Iterating through sentences
	for j, w in enumerate(sentence): #Iterating through word entries
		flag=0
		featno=0
		bist.seek(0,0)
		for line in bist:
			if (flag==0) * (line.split()[0]==w[0]): #Checking 'test' list with dictionary of words from closed class
				flag=1
				if (line.split()[1]==w[1]):
					if(w[2]==0):
						match+=1
				elif (w[2]==1):
					match+=1
					break
			else:
				continue
		if (flag==1):
			continue
		else:
			call=0
			call2=0
			tag=""
			f1=-1
			f2=-1
			f3=-1
			f4=-1
			f5=-1
			f6=-1
			f7=-1
			i=0
			print("ojo")
			flag=0
			while i<len(feature): #Iterating through feature dictionary
				call+=1
				if (flag==1):
					call2+=1 #Keep track of feature number
				if (feature[i].split()[0]==w[0]) * (flag==0):
					print("ok")
					tag=feature[i].split()[1]
					flag=1
					pos=call
					i+=1
					continue
				elif (flag==1) * (feature[i].split()[0]==w[0]):
					if (call2%7==1) * (f1==-1):
						print("xd")
						if (j==0):
							if(feature[i].split()[1]=="<start>"):
								f1=1
								i=pos+1
								call2=1
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f1=0
									i=pos+1
									call2=1
									i+=1
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]):
							f1=1
							i=pos+1
							call2=1
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f1=0
								i=pos+1
								call2=1
								i+=1
								continue
					elif (call2%7==2) * (f2==-1):
						print("xd")
						if (j==0):
							if(feature[i].split()[1]=="<start>") * (feature[i].split()[2]=="<start>"):
								f2=1
								i=pos+2
								call2=2
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f2=0
									i=pos+2
									call2=2
									i+=1
									continue
						if (j==1):
							if(feature[i].split()[1]==sentence[j-1][0]) * (feature[i].split()[2]=="<start>"):
								f2=1
								i=pos+2
								call2=2
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f2=0
									i=pos+2
									call2=2
									i+=1
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]) * (sentence[j-2][0]==feature[i].split()[2]):
							f2=1
							i=pos+2
							call2=2
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f2=0
								i=pos+2
								call2=2
								i+=1
								continue
					elif (call2%7==3) * (f3==-1):
						print("xd")
						if (j==0):
							if(feature[i].split()[1]=="<start>") * (feature[i].split()[2]=="none"):
								f3=1
								i=pos+3
								call2=3
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f3=0
									i=pos+3
									call2=3
									i+=1
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]) * (sentence[j-1][1]==feature[i].split()[2]):
							f3=1
							i=pos+3
							call2=3
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f3=0
								i=pos+3
								call2=3
								i+=1
								continue
					elif (call2%7==4) * (f4==-1):
						print("xd")
						if (j==0):
							if(feature[i].split()[1]=="<start>") * (feature[i].split()[2]=="<start>"):
								f4=1
								i=pos+4
								call2=4
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f4=0
									i=pos+4
									call2=4
									i+=1
									continue
						elif (j==1):
							if(feature[i].split()[1]==sentence[j-1][0]) * (feature[i].split()[2]=="<start>"):
								f4=1
								i=pos+4
								call2=4
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f4=0
									i=pos+4
									call2=4
									i+=1
									continue
						elif (j==(len(sentence)-2)):
							if(feature[i].split()[3]==sentence[j+1][0]) * (feature[i].split()[4]=="<end>"):
								f4=1
								i=pos+4
								call2=4
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f4=0
									i=pos+4
									call2=4
									i+=1
									continue
						elif (j==(len(sentence)-1)):
							if(feature[i].split()[3]=="<end>") * (feature[i].split()[4]=="<end>"):
								f4=1
								i=pos+4
								call2=4
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f4=0
									i=pos+4
									call2=4
									i+=1
									continue
						elif (sentence[j-1][0]==feature[i].split()[1]) * (sentence[j-2][0]==feature[i].split()[2]) * (sentence[j+1][0]==feature[i].split()[3]) * (sentence[j+2][0]==feature[i].split()[4]):
							f4=1
							i=pos+4
							call2=4
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f4=0
								i=pos+4
								call2=4
								i+=1
								continue
					elif (call2%7==5) * (f5==-1):
						print("xd")
						if (j==0):
							if(feature[i].split()[1]=="none") * (feature[i].split()[2]==sentence[j+1][1]):
								f5=1
								i=pos+5
								call2=5
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f5=0
									i=pos+5
									call2=5
									i+=1
									continue
						elif (j==len(sentence)-1):
							if(feature[i].split()[1]==sentence[j-1][1]) * (feature[i].split()[2]=="none"):
								f5=1
								i=pos+5
								call2=5
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f5=0
									i=pos-5
									call2=5
									i+=1
									continue
						elif (sentence[j-1][1]==feature[i].split()[2]) * (sentence[j+1][1]==feature[i].split()[3]):
							f5=1
							i=pos+5
							call2=5
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f5=0
								i=pos+5
								call2=5
								i+=1
								continue
					elif (call2%7==6) * (f6==-1):
						print("xd")
						if (j==len(sentence)-1):
							if(feature[i].split()[1]=="<end>"):
								f6=1
								i=pos+6
								call2=6
								i+=1
								continue
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f6=0
									i=pos+6
									call2=6
									i+=1
									continue
						elif (sentence[j+1][0]==feature[i].split()[1]):
							f6=1
							i=pos+6
							call2=6
							i+=1
							continue
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f6=0
								i=pos+6
								call2=6
								i+=1
								continue
					elif (call2%7==0) * (f7==-1):
						print("xd")
						if (j==len(j)-1):
							if(feature[i].split()[1]=="<end>") * (feature[i].split()[2]=="none"):
								f7=1
								break
							else:
								call+=7
								i=call
								if(feature[i].split()[0]==w[0]):
									call-=1
									call2-=1
									continue
								else:
									f7=0
									break
						elif (sentence[j+1][0]==feature[i].split()[1]) * (sentence[j+1][1]==feature[i].split()[2]):
							f7=1
							break
						else:
							call+=7
							i=call
							if (w[0]==feature[i].split()[1]):
								call-=1
								call2-=1
								continue
							else:
								f7=0
								break
			fsum=f1+f2+f3+f4+f5+f6+f7
			print("lol")
			if (fsum>=4) * (flag==1):
				if(w[1]==tag) * (w[2]==0):
					match+=1
				elif (w[2]==1) * (w[1]!=tag):
					match+=1
			if (flag==0):
				if(w[1]=="NN_N") * (w[2]==0):
					match+=1
				elif (w[1]!="NN_N") * (w[2]==1):
					match+=1
print(match)
print(count)