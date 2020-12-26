distancematrix=[[0,5,9,9],[5,0,14,4],[9,14,0,11],[9,4,11,0]]
arum=[[1,1,3,"RF",1,0,0,1,1,2,0,0,1],
      [1,1,3,"UF",2,0,1,1,0,0,2,2,0],
      [1,2,5,"RF",3,1,0,2,3,1,1,2,0],
      [1,2,5,"RF",0,1,1,2,2,0,1,2,0],
      [2,2,2,"RF",3,1,0,2,3,1,1,2,0],
      [2,2,2,"UF",0,1,1,2,2,0,1,2,0],
      [2,3,4,"RF",0,2,1,2,5,0,1,3,1],
      [2,3,4,"UF",1,0,0,2,1,0,2,0,1],
      [3,1,6,"RF",1,0,0,1,1,2,0,0,1],
      [3,1,6,"UF",2,0,1,1,0,0,2,2,0],
      [3,4,8,"RF",2,0,2,0,1,1,1,1,0],
      [3,4,8,"UF",0,2,1,1,2,0,1,3,0],
      [4,4,9,"RF",2,0,2,0,1,1,1,1,0],
      [4,4,9,"UF",0,2,1,1,2,0,1,3,0],
      [4,5,3,"RF",1,0,1,2,0,1,2,2,1],
      [4,5,3,"UF",1,0,2,3,1,0,0,0,3]]

distancecostmatrix=[[0,5,9,9],
                    [5,0,14,9],
                    [9,14,0,11],
                    [9,4,11,0]]
SAFT=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

i=0
sum=0
x=0
while(i<16):
	sum=sum+arum[i][2]*(arum[i][4]+arum[i][5]+arum[i][6])	
	if(i==3 or i==7 or i==11 or i==15):		
		SAFT[x][0]=sum		
		x=x+1
		sum=0
	i=i+1


i=0
sum=0
x=0
while(i<16):
	sum=sum+arum[i][2]*(arum[i][7]+arum[i][8]+arum[i][9])
	#print("dff"+str(sum))	
	if(i==3 or i==7 or i==11 or i==15):		
		SAFT[x][1]=sum	
		#print(sum)	
		x=x+1
		sum=0
	i=i+1


i=0
sum=0
x=0
while(i<16):
	sum=sum+arum[i][2]*(arum[i][10]+arum[i][11]+arum[i][12])	
	if(i==3 or i==7 or i==11 or i==15):		
		SAFT[x][2]=sum		
		x=x+1
		sum=0
	i=i+1




ARUF=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
sum2=0
sum=0
xx=0


sum=0
j=0
while(j<3):
	for i in range(4):
		sum=sum+SAFT[i][0]*distancecostmatrix[j][i]
		
	ARUF[j][0]=sum
	sum=0
	j+=1
sum=0
for i in range(4):
	sum=sum+SAFT[i][0]*distancecostmatrix[3][i]
ARUF[3][0]=sum



sum=0
j=0
while(j<3):
	for i in range(4):
		sum=sum+SAFT[i][1]*distancecostmatrix[j][i]
		
	ARUF[j][1]=sum
	sum=0
	j+=1
sum=0
for i in range(4):
	sum=sum+SAFT[i][1]*distancecostmatrix[3][i]
ARUF[3][1]=sum


sum=0
j=0
while(j<3):
	for i in range(4):
		sum=sum+SAFT[i][2]*distancecostmatrix[j][i]
		
	ARUF[j][2]=sum
	sum=0
	j+=1
sum=0
for i in range(4):
	sum=sum+SAFT[i][2]*distancecostmatrix[3][i]
ARUF[3][2]=sum



print(ARUF)

list=[]
for i in range (3):
	max=0
	for k in range(4):
		if max<=ARUF[k][i]:
			max=ARUF[k][i]
	list.append(max)
print(list)


i=0
x=0
max=0
while(i<3):
	if max<list[i]:
		max=list[i]
		x=i
	i+=1

print(x)

if x==0:
	print("primary candidate attribute is Birth-date")
if x==1:
	print("primary candidate attribute is salary")
if x==2:
	print("primary candidate attribute is location ")

