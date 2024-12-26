import psycopg2
import psycopg2.extras

hostname='localhost'
database='people'
username='postgres'
pwd='123456'
portid =5432


try:

    conn = psycopg2.connect(host=hostname,
                        dbname=database,
                        user=username,
                        password=pwd, port=5432)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DROP TABLE IF EXISTS employee')

    data='''CREATE TABLE IF NOT EXISTS employee (
             id INT PRIMARY KEY,
             name VARCHAR(40),
             salary INT,
             department VARCHAR(100))'''


    insert ="INSERT INTO employee ( id,name,salary, department) VALUES (1,'sujesh',20000,'IT'),(2,'sudeesh',30000,'finance'),(3,'suresh',40000,'education'),(4,'sumesh',25000,'accounts'),(5,'sachin',12000,'security'),(6,'sreejith',18000,'cleaning')"
    cur.execute(data)
    cur.execute(insert)



    cur.execute('SELECT * FROM employee' )
    print(cur.fetchall())

    cur.execute('SELECT * FROM employee' )
    for records in cur.fetchall():
        print(records)

    cur.execute('SELECT * FROM employee' )
    for records in cur.fetchall():
        print(records[1],records[3])

    cur.execute('SELECT * FROM employee' )
    for records in cur.fetchall():
        print(records['name'],records['salary'])



    update = "UPDATE employee SET salary = 55000 WHERE name = 'sudeesh'"
    cur.execute(update)
    
    cur.execute('SELECT * FROM employee' )
    for records in cur.fetchall():
        print(records)



    update = "UPDATE employee SET name = 'failed' WHERE salary < 25000"
    cur.execute(update)

    delete = "DELETE FROM employee WHERE name = 'sudeesh'"
    cur.execute(delete)
    
 

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()    

cur.close()
conn.close()





