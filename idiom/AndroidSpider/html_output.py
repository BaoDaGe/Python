import time
import sqlite3
from pathlib import Path
from urllib.request import pathname2url
import os


class HtmlOutput(object):
    def __init__(self):
        self.datas = []
        self.var = "12";
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):


            my_db = r"idiomdb"
            my_tb="idiom"+ self.var

            conn = sqlite3.connect(my_db, uri=True)
            c = conn.cursor()

            #if os.path.isfile(my_file):
                #os.remove(my_file)

            #c.execute('''drop table if exists idioms4''')
            c.execute('''SELECT count(*) FROM sqlite_master WHERE type = '{tn}' AND name = '{cn}' '''.format(tn='table',cn=my_tb))
            if c.__next__()[0]==1:
                c.execute('''drop table '{cn}' '''.format(cn=my_tb))
            if self.var=='4':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT)'''.format(cn=my_tb))
            elif self.var=='5':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT)'''.format(cn=my_tb))
            elif self.var=='6':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT )'''.format(cn=my_tb))
            elif self.var=='7':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT )'''.format(cn=my_tb))
            elif self.var=='8':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT ,data8 TEXT )'''.format(cn=my_tb))
            elif self.var=='9':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT ,data8 TEXT ,data9 TEXT )'''.format(cn=my_tb))
            elif self.var == '10':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT ,data8 TEXT ,data9 TEXT,data10 TEXT )'''.format(cn=my_tb))
            elif self.var == '11':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT ,data8 TEXT ,data9 TEXT,data10 TEXT ,data11 TEXT )'''.format(cn=my_tb))
            elif self.var == '12':
                c.execute('''CREATE TABLE '{cn}' (IndexItem  integer, date1 TEXT,date2 TEXT,date3 TEXT,date4 TEXT,date5 TEXT,data6 TEXT,data7 TEXT ,data8 TEXT ,data9 TEXT,data10 TEXT ,data11 TEXT ,data12 TEXT )'''.format(cn=my_tb))

            k=0
            for i in self.datas:
                for j in i:
                    k=k+1
                    if self.var == '4':
                        z = [k, j[0], j[1], j[2], j[3]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '5':
                        z = [k, j[0], j[1], j[2], j[3],j[4]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '6':
                        z = [k, j[0], j[1], j[2], j[3], j[4],j[5]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '7':
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5],j[6]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '8':
                        j=j.replace('，', '')#delete ","
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5], j[6],j[7]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '9':
                        j = j.replace('，', '')  # delete ","
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7],j[8]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '10':
                        j = j.replace('，', '')  # delete ","
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8],j[9]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '11':
                        j = j.replace('，', '')  # delete ","
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9],j[10]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?,?,?,?,?)".format(cn=my_tb), z)
                    if self.var == '12':
                        j = j.replace('，', '')  # delete ","
                        z = [k, j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10],j[11]]
                        c.execute("INSERT INTO {cn} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)".format(cn=my_tb), z)


            conn.commit()
            conn.close()

            conn = sqlite3.connect(my_db)
            c = conn.cursor()
            all_rows = c.execute("SELECT * FROM {cn} ".format(cn=my_tb))
            print (c.fetchall())

        #c.execute('''SELECT NAME FROM SQLITE_MASTER  WHERE type='table' ''')#get you a list of all the tables names.
        #c.execute("PRAGMA table_info(idioms4)")#get you a list of all the column names.

        # 1) Contents of all columns for row that match a certain value in 1 column
        #c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'.format(tn='idioms', cn='date1'))



