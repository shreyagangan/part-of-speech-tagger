from __future__ import division
import math
#from __future__ import multiplication
from collections import defaultdict
A={} #transition probabilities
Alist = defaultdict(list) #transition maps
B={} #emission probabilities
Blist = defaultdict(list) #emission maps
input_path="hmmmodel.txt"

hmmmodel=open(input_path, "r")
lists=hmmmodel.read()
twolists=lists.split('\n*****\n',1)
rawA=twolists[0].split("\n")
rawB=twolists[1].split("\n")

#print(twolists)
#print(rawA)


for line in rawA:
 if(line!=" " and line!=""):
 	(key1, key2, val) = line.split(" ",2)    
 	if(key2 not in Alist[key1]):   
 		Alist[key1].append(key2)
 		A[key1,key2] = map(float,val.split())
    #print(key1+" "+key2+" "+str(M[key1,key2]))

#print(A)  
#print(Alist)
#print(rawB)

for line in rawB:
	if(line!=" " and line!=""):
 		(key1, key2, val) = line.split(" ",2)    
 		if(key2 not in Blist[key1]):   
 			Blist[key1].append(key2)
 			B[key1,key2] = map(float,val.split())

#print(B)  
#print(Blist)

import sys

#input_path="example_test.txt"
hmmoutput=open("hmmoutput.txt", "w+")
input_path="train/catalan_corpus_dev_raw.txt"
with open(input_path, "r")  as test:
		for line in test:
			#initializing
			viterbi_prob={}
			vlist=defaultdict(list) #list of all possible tags for the word at position count
			backptr={}
			vlist[0]={'q0'}
			#viterbi_prob[0,'q0']=1.0  
			viterbi_prob[0,'q0']=0.0  
			#print(vlist)
			#print(viterbi_prob)
			#initialize lines
			tokens=line.split()
			#print(tokens)
			prev_tags=vlist[0]
			count=1;
			for word in tokens:
				print(word)
				current_taglist=[]
				if(Blist.has_key(word)):  #word seen in training set
					#print(Maplist[word])
					#print("Maplist")
					current_taglist=Blist[word]
				else: #new word      
					for prev_tag in prev_tags:
						for ctag in Alist[prev_tag]:   
							if(ctag not in current_taglist and ctag!='qX'):
								current_taglist.append(ctag)
								#print ctag
				print(current_taglist)    
				for current_tag in current_taglist:
						maxprob=float('-inf')
						maxtag=""
						#print(current_tag)
						for prev_tag in prev_tags:
							#print(prev_tag)
							##if M.has_key((prev_tag,current_tag)) and M.has_key((word,current_tag)) and viterbi_prob.has_key((count-1,prev_word,prev_tag)):
							p1=[]
							if A.has_key((prev_tag,current_tag)):
								p1=A[prev_tag,current_tag]
							else:
								p1=A[prev_tag,'qX']  
							p2=[]
							if B.has_key((word,current_tag)):
								p2=B[word,current_tag] 
							else:
								p2=[1.0]
							p3=viterbi_prob[count-1,prev_tag] #has to be true
							#print(p1[0])
							#print(p2[0])
							#print(p3)
							#prob=p1[0]*p2[0]*p3  
							prob=math.log(p1[0])+math.log(p2[0])+p3  
							#print(prob)
							#print(maxprob)
							if(prob>maxprob):
								#print("Hey!")
								maxprob=prob
								maxtag=prev_tag
						#print(current_tag,word,maxprob)    
						
						vlist[count].append(current_tag)
						viterbi_prob[count,current_tag]=maxprob
						backptr[count,current_tag]=maxtag
				
				prev_tags=vlist[count]
				count=count+1
			
			#print(vlist)
			#print(viterbi_prob)
			
			vlen=len(vlist)-1
			#print(vlen)

			#print("last vlist:")
			maxprob=float('-inf')
			maxtag=""
			for tag in vlist[vlen]:
				#print tag
				if(viterbi_prob[vlen,tag]>maxprob):
					maxprob=viterbi_prob[vlen,tag]
					maxtag=tag
			#print("end of last vlist")
			#print("maxtag:"+maxtag)  
			#print("start tagging")  
			taglist={}
			for i in range(vlen,0,-1):
				taglist[tokens[i-1]]=maxtag
				maxtag=backptr[i,maxtag]
			#print("end tagging!")  
			
			for word in tokens:
				hmmoutput.write(word)
				hmmoutput.write("/")
				hmmoutput.write(taglist[word])
				hmmoutput.write(" ")
			hmmoutput.write("\n")  

hmmoutput.close()

#import sys
##print sys.float_info.max
##print sys.float_info.min
#minfloat=sys.float_info.min
#minnegfloat=-(sys.float_info.min)
##print minnegfloat
#if(minfloat<0):
#  #print "thank god!"
#if(minnegfloat<0):
#  #print "oh thank god!"  
	##print (str(M[]))
	#viterbi['start']=[tag,]



