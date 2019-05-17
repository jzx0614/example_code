#/usr/bin/python

import json
import sys
from pprint import pprint

import psycopg2

class SummaryReport():
    def __init__(self, sql):
        self.sql = sql 

    def product_report(self):
       self.query_event()

    def query_event(self):
        try:
            #conn = psycopg2.connect("dbname=ATM user=nobody")
            conn = psycopg2.connect(
                database="ATM", user="nobody",
                password="nobody", host="192.168.10.146")
        except psycopg2.Error as e:
            print e.pgerror
            return

        cur = conn.cursor()

        try:
            #cur.execute("SELECT * FROM xfsys_anomaly_event")
            cur.execute(self.sql)
        except psycopg2.Error as e:
            print e.pgerror
            return
        except:
            print "I can't select our test database!"
            return

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print type(row[0]),
            print row[0].time(), row[4]

        x = [row[0] for row in rows]
        byte = [row[4]/300 for row in rows]
        packet = [-row[5]/300 for row in rows] 
       
        from datetime import timedelta
        min5 = timedelta(minutes=5)
        first_time = x[0]
        last_time = x[-1] 


        x.insert(0, first_time-min5)
        x.append(last_time+min5)
        byte.insert(0, 0)
        byte.append(0)
        packet.insert(0, 0)
        packet.append(0)

        import matplotlib.pyplot as plt
        plt.fill(x, byte, 'yo-', label="$bytes$")
        plt.plot(x, packet, 'r', label="$packets$")
        plt.ticklabel_format(style='plain', axis='y')
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()
        plt.savefig('foo.png')
   
def main():
    sql = "SELECT * FROM xf005_05_inst_summary_20160403 where obj_index = 6 and inst_index = 509 and counter_index = 1 order by 1;"
    report = SummaryReport(sql)
    report.product_report()

if __name__ == "__main__":
    main()
