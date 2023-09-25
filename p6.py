import psycopg2

conn = psycopg2.connect(
   database="university",
   user='postgres', 
	 password='inspiron', 
	 host='localhost', 
	 port= '5432'
)
cursor = conn.cursor()
cursor.execute('''SELECT * from student''')

result = cursor.fetchall();
print(result)

conn.close()