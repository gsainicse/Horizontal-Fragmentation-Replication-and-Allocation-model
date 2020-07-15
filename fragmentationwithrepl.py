import csv
import psycopg2

print("Connecting to all the servers")

samphat = psycopg2.connect(host="10.100.53.25",   port=2345, database="gurdeep", user="postgres", password="it701");
kushal = psycopg2.connect(host="10.100.54.83",port=2345, database="gurdeep", user="postgres", password="it701");
niranjan= psycopg2.connect(host="10.100.53.121",port=5432, database="gurdeep", user="postgres", password="it701");


print("All servers are connected")

cur_samphat = samphat.cursor()
cur_kushal = kushal.cursor()
cur_niranjan = niranjan.cursor()



cur_samphat.execute("DROP TABLE employeeone;");
cur_kushal.execute("DROP TABLE  employeetwo;");
cur_niranjan.execute("DROP TABLE employeethree;");



#create tables 
cur_samphat.execute("CREATE TABLE employeeone (birthdate varchar(50),deptid integer,jobid varchar(50),location varchar(50),name varchar(50) ,salary integer );");
cur_kushal.execute("CREATE TABLE employeetwo (birthdate varchar(50),deptid integer,jobid varchar(50),location varchar(50),name varchar(50) ,salary integer  );");
cur_niranjan.execute("CREATE TABLE employeethree (birthdate varchar(50),deptid integer,jobid varchar(50),location varchar(50),name varchar(50) ,salary integer  );");


#write to servers
length=1
with open('employee2.csv','r') as f:
    reader = csv.reader(f) 
   
    for row in reader:
        length=length+1





with open('employee2.csv','r') as f:
    reader = csv.reader(f) 
    count=1
    for row in reader:
        print(row)
        a=row[0]
        b=row[1]                
        c=row[2]
        d=row[3]
        e=row[4]
        f=row[5]
        

        if int(f) < 1500:
                       
                cur_samphat.execute("INSERT INTO employeeone VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))

        elif int(f)==1500:
                cur_kushal.execute("INSERT INTO employeetwo VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))
                cur_niranjan.execute("INSERT INTO employeethree VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))
                cur_samphat.execute("INSERT INTO employeeone VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))

                
        elif int(f)>1500:

            cur_kushal.execute("INSERT INTO employeetwo VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))
            #cur_niranjan.execute("INSERT INTO employeethree VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))
            cur_samphat.execute("INSERT INTO employeeone VALUES (%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))
        
        count = count + 1    

cur_samphat.close()
cur_kushal.close()
cur_niranjan.close()

samphat.commit()
kushal.commit()
niranjan.commit()


