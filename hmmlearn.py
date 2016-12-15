from __future__ import division
from collections import defaultdict
A={} #Transition counts
Q={"q0":0} #tags...counts of all tags
last={} #counts of last tags...to be subtracted to calculate transmission
Qlist = defaultdict(list) #list of all possible transitions

V = defaultdict(list) #list of observations for each tags 
B={} #Emmision counts


input_path="train/catalan_corpus_train_tagged.txt"
with open(input_path, "r")  as training_data:
    for line in training_data:
    	tokens = line.split()
    	##print(tokens)
    	prev="q0"
       	Q['q0']=Q['q0']+1
       	for token in tokens:
          no_of_letters=len(token)
          ##print(token)
          ##print(no_of_letters)
          tag=token[no_of_letters-2:no_of_letters]
          obs=token[0:no_of_letters-3]
          #(obs,tag)=token.split("/",1)
          ##print(obs)
          ##print(tag)
          if obs not in V[tag]:
       			V[tag].append(obs)
       	  if tag not in Qlist[prev]:
            Qlist[prev].append(tag)
       	  if Q.has_key(tag):
       			Q[tag]=Q[tag]+1	
       	  else:
       			Q[tag] = 1
       		#pair=tag+","+obs;	
       	  if B.has_key((tag,obs)):
       			B[tag,obs]=B[tag,obs]+1
       	  else:
       			B[tag,obs] = 1
       		##print(prev,tag)
       	  if A.has_key((prev,tag)):
       			A[prev,tag]=A[prev,tag]+1
       	  else:
       			A[prev,tag] = 1
       	  prev=tag
       	if last.has_key(prev):
       		last[prev]=last[prev]+1
       	else:
       		last[prev] = 1		
#print(Q)
Qcount=len(Q)-1
#print(Qcount)
#print(B)
#print(A)
#print(last)
#print(V)
#print(Qlist)

hmmmodel=open("hmmmodel.txt", "w+")

#transmission matrix
#A_size=len(A)
##print(str(A_size))
#print("Qcount")
#print(Qcount)
for tag in Q: 
  total=Q[tag]
  ##print(tag)
  if(last.has_key(tag)): 
		total=total-last[tag]
  for next in Qlist[tag]:
		##print(tag+" "+next+" "+str(A[tag,next]))
		prob=(1+A[tag,next])/(Qcount+total)
		hmmmodel.write(tag+" "+next+" "+str(prob)+"\n")
  probx=1/(Qcount+total)  
  hmmmodel.write(tag+" "+"qX"+" "+str(probx)+"\n")  	
hmmmodel.write("*****\n")    
#emission matrix
#B_size=len(B)
##print(str(B_size))
for tag in Q:
	total=Q[tag] 
	for obs in V[tag]:
		#print(tag+" "+obs+" "+str(B[tag,obs]))
		prob=B[tag,obs]/total
		#hmmmodel.write(tag+" "+obs+" "+str(prob)+"\n")
		hmmmodel.write(obs+" "+tag+" "+str(prob)+"\n")

hmmmodel.close()