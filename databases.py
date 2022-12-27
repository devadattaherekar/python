import sqlite3

#1. 5 datatypes 1. integer 2. real 3. text 4. null 5. blob

#1. create database connection
#2. create cursor
#3. execute sql query using cursor
#4. commit connection
#5. close connection

def create_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('create table if not exists employee (empid integer primary key,empname text, empsal real)')
    connection.commit()
    connection.close()

create_table()

def add_employee(emp_id,emp_name,emp_sal):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('insert into employee values(?,?,?)',(emp_id,emp_name,emp_sal))
    connection.commit()
    connection.close()

#add_employee(1000,"Rajesh",99999.99)
#add_employee(2000,"Sonali",88888.88)
#add_employee(3000,"Suraj",77777.77)

def list_employees():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    data=cursor.execute('select * from employee')
    #print(data.fetchone()) # will fetch only first record
    """
    data=list(data)
    print("First record is ",data[0])
    print("Last record is ", data[-1])
    print("Last record second column is ", data[-1][1])
    """
    data=data.fetchall() # will fetch all records
    for each_record in data: # unpack tuple
        print(each_record[0],each_record[1],each_record[2])
    connection.commit()
    connection.close()

list_employees()

def delete_employee(emp_id):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('delete from employee where empid=?',(emp_id,))
    connection.commit()
    connection.close()

delete_employee(1000)
list_employees()

def update_employee(emp_id,emp_sal):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('update employee set empsal=? where empid=?',(emp_sal,emp_id))
    connection.commit()
    connection.close()

update_employee(2000,1000000)
list_employees()