import mysql.connector as connection
class forest:
    def __init__(self):
        self.cup = connection.connect(host='localhost',use_pure=True,password = '!dsai21@mysqL',port='3306',
        database='institutions',user='root')
        query="create table if not exists table_A(college varchar(200) primary key,discipline varchar(200),name varchar(200), id int(32),location varchar(200))"
        cup1=self.cup.cursor()
        cup1.execute(query)
        print('table created')

    def insert_values(self,c_n,dis,st_name,roll,loc):
        query= "insert into table_a(college,discipline,name,id,location) values('{}','{}','{}',{},'{}')".format(c_n,dis,st_name,roll,loc)
        print(query)
        cu = self.cup.cursor()
        cu.execute(query)
        self.cup.commit()
        print('values inserted')

    def fetch_all(self):
        query = 'select * from table_a'
        ca = self.cup.cursor()
        ca.execute(query)
        for row in ca:
            print('college : ',row[0])
            print('discipline : ',row[1])
            print('name : ',row[2])
            print('id : ',row[3])
            print('loaction : ',row[4])
            print()
            print()

    def delete_user(self,college):
        query = "delete from table_a where college = '{}'".format(college)
        cd = self.cup.cursor()
        cd.execute(query)
        self.cup.commit()
        print('deleted')

    def update_users(self,college,new_name,new_id):
        query = "update table_a set name='{}',id={} where college='{}'".format(new_name,new_id,college)
        print(query)
        ch = self.cup.cursor()
        ch.execute(query)
        self.cup.commit()
        print('updated')


