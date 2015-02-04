#usage: python rap2cog.py infile(.m8 from rapsearch) outfile
from sys import argv

rap=open(argv[1]) #rapsearch result
specie=open("species") #org.txt  specie annotation
function=open("fun.txt") #function category
totalinf=open("kog")#whog  contains information on each COG, including the COG name,functional classification (using a one-letter code), function description, and the the list of proteins (or domains) from all  66 complete genomes included in the COG database.
equal=open("pa")
out=open(argv[2],"w")

dicrap={}
org={}
func={}
total={}
diceq={}
#
for i in rap:
	q=i.split("\t")
	if i.startswith("#")==False:
		if q[0] not in dicrap:
			dicrap[q[0]]=q[1] #dicionario com o scaffold e o hit, no tipo YGR109w-b_2

for u in specie:
	p=u.split("  ")
	org[p[1].strip()]=(p[-1].strip()).strip("\n")
print (org)

#	
for e in function:
	if e.startswith(" ["):
		v=e.split("]")
		func[v[0].strip()+"]"]=cat+v[1].strip("\n") #dicionario tipo [J] - INFORMATION  - Translation
	else:
		cat=(e.strip("\n"))+"\t"
#		
for a in totalinf:
	if a.startswith("["):
		cat2=a.split(" ",2)
	elif a.startswith(" "):
		li=[]
		z=a.split(":")
		if len(z)!=1:
			line=z[0].strip()
		li.append(cat2[0])
		li.append((cat2[-1].strip()).strip("\n"))
		li.append(line)
		acess=((z[-1].strip()).strip("\n")).split()
		for r in acess:
			total[r]=li #dic do tipo: hit= [[H],glutamate,Afu]
#
for o in equal:
	if o.startswith("  ")==False:
		la=o.split(" ")
		num=la[4].strip(")")
		if float(num)<= 0.00001:
			if la[0] not in diceq and la[0]!=la[2]:
				ttt=[]
				ttt.append(la[2])
				diceq[la[0]]=ttt
			elif la[0]!=la[2]:
				diceq[la[0]].append(la[2])


out.write("Scaffold\tHit\tCategory\tSubcategory\tDescription\tOrganism\n")

for key, value in dicrap.items():
	if value in total:
		out.write(key+"\t"+value+"\t")
		if total[value][0] in func:
			out.write(func[total[value][0]]+"\t")
		else:
			out.write(total[value][0]+"\t"+"na"+"\t")
		out.write(total[value][1]+"\t")
		out.write(org[total[value][2]]+"\n")
	elif value in diceq:
		for t in diceq[value]:
			if t in total:
				out.write(key+"\t"+value+"\t")
				if total[t][0] in func:
					out.write(func[total[t][0]]+"\t")
				else:
					out.write(total[t][0]+"\t"+"na"+"\t")
				out.write(total[t][1]+"\t")
				out.write(org[total[t][2]]+"\n")
				break


rap.close()
specie.close()
function.close()
totalinf.close()
out.close()
equal.close()

