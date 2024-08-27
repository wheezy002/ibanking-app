import sqlite3
import random as r
class Bank:
    print("WELCOME TO THE BANK")
    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        print("sqlite3 connected")

    def CreateAccount(self):
        self.c.execute("""create table if not exists Bank (

            account_name text,
            acc_num integeer,
            balance integer     

        )""")
        #self.c.execute("drop table Bank")
        n1 = input("Enter Your First Name:- ").upper()
        n2 = input("Enter Your Second Name:- ").upper()
        
        if n1.isalpha() and not n1.isspace() and n2.isalpha() and not n2.isspace():
            name = n1+' '+n2
            num = r.randint(10000000,99999999)
            amount = 0
            self.c.execute("insert into Bank values(?,?,?)",(name,num,amount))
            self.c.execute("select * from Bank")
            print(self.c.fetchall())
        else:
            print("Enter Valid Name, Try again.....!")








bk = Bank()
bk.CreateAccount()