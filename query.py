import time
import csv
import psycopg2

print("Connecting to all the servers")

samphat = psycopg2.connect(host="10.100.53.25",   port=2345, database="gurdeep", user="postgres", password="it701");
kushal = psycopg2.connect(host="10.100.54.83",port=2345, database="gurdeep", user="postgres", password="it701");
niranjan= psycopg2.connect(host="10.100.53.121",port=5432, database="gurdeep", user="postgres", password="it701")#;


print("All servers are connected")

cur_samphat = samphat.cursor()
cur_kushal = kushal.cursor()
cur_niranjan = niranjan.cursor() 



start_time = time.time()
#here  we are execurting query  
cur_samphat.execute("SELECT * FROM employeeone WHERE deptid=2");
rows1 = cur_samphat.fetchall()
print("records in samphat  for query1 {}".format(len(rows1)))


cur_kushal.execute("SELECT * FROM employeetwo WHERE deptid=2");
rows2 = cur_kushal.fetchall()
print("Record in kushal for query1  {}".format(len(rows2)))



cur_niranjan.execute("SELECT * FROM employeethree WHERE deptid=2");
rows3 = cur_niranjan.fetchall()
print("Record in niranjan for query1  {}".format(len(rows3)))


end_time=time.time();
print((end_time-start_time)*1000);

query1="SELECT * FROM employeeone WHERE location='Riyadh' and jobid='MGR'" 

start_time = time.time()
#Execute  Query 
cur_samphat.execute("SELECT * FROM employeeone WHERE location='Riyadh' and jobid='MGR'");
rows1 = cur_samphat.fetchall()
print("records in samphat  for query12 {}".format(len(rows1)))



cur_kushal.execute("SELECT * FROM employeetwo WHERE location='Riyadh' and jobid='MGR'");

rows2 = cur_kushal.fetchall()
print("Records in kushal mondel for query2  {}".format(len(rows2)))

cur_niranjan.execute("SELECT * FROM employeethree WHERE location='Riyadh' and jobid='MGR'");

rows3 = cur_niranjan.fetchall()
print("Record in niranjan singh  for query2  {}".format(len(rows3)))



end_time=time.time();

print((end_time-start_time)*1000);




cur_samphat.close()
cur_kushal.close()
cur_niranjan.close()


samphat.commit()
kushal.commit()
niranjan.commit()


