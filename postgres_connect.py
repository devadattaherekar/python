import psycopg2


#1. create database connection
#2. create cursor
#3. execute sql query using cursor
#4. commit connection
#5. close connection

def create_table():
    connection=psycopg2.connect(user="kiran",password="redhat",database="kiran_database",host="localhost",port=5432)
    cursor=connection.cursor()
    cursor.execute('create table if not exists employee (empid integer primary key,empname text, empsal real)')
    connection.commit()
    connection.close()

create_table()


def add_employee(emp_id,emp_name,emp_sal):
    connection = psycopg2.connect(user="kiran", password="redhat",
                                  database="kiran_database", host="localhost",
                                  port=5432)


    cursor=connection.cursor()
    cursor.execute('insert into employee values(%s,%s,%s)',(emp_id,emp_name,emp_sal))
    connection.commit()
    connection.close()

#add_employee(1000,"Rajesh",99999.99)
#add_employee(2000,"Sonali",88888.88)
#add_employee(3000,"Suraj",77777.77)

def list_employees():
    connection = psycopg2.connect(user="kiran", password="redhat",
                                  database="kiran_database", host="localhost",
                                  port=5432)

    cursor=connection.cursor()
    cursor.execute('select * from employee')

    #print(data.fetchone()) # will fetch only first record
    data=cursor.fetchall()
    data=list(data)
    print("First record is ",data[0])
    print("Last record is ", data[-1])
    print("Last record second column is ", data[-1][1])

    for each_record in data: # unpack tuple
        print(each_record[0],each_record[1],each_record[2])
    connection.commit()
    connection.close()

list_employees()

def delete_employee(emp_id):
    connection = psycopg2.connect(user="kiran", password="redhat",
                                  database="kiran_database", host="localhost",
                                  port=5432)


    cursor=connection.cursor()
    cursor.execute('delete from employee where empid=%s',(emp_id,))
    connection.commit()
    connection.close()

delete_employee(1000)
list_employees()

def update_employee(emp_id,emp_sal):
    connection = psycopg2.connect(user="kiran", password="redhat",
                                  database="kiran_database", host="localhost",
                                  port=5432)


    cursor=connection.cursor()
    cursor.execute('update employee set empsal=%s where empid=%s',(emp_sal,emp_id))
    connection.commit()
    connection.close()

update_employee(2000,1000000)
list_employees()
