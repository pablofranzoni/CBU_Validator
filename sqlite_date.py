import sqlite3
import datetime
from decimal import Decimal

# adapt the Python type type into an SQLite type
sqlite3.register_adapter(Decimal, lambda d: str(d))
#convert SQLite objects into a Python object'
sqlite3.register_converter("DECTEXT", lambda d: Decimal(d.decode('ascii')))

class DecimalSum:
    def __init__(self):
        self.sum = None

    def step(self, value):
        if value is None:
            return
        v = Decimal(value)
        if self.sum is None:
            self.sum = v
        else:
            self.sum += v

    def finalize(self):
        return None if self.sum is None else str(self.sum)

con = sqlite3.connect("prueba.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
con.create_aggregate("decimal_sum", 1, DecimalSum)
cur = con.cursor()
#cur.execute("create table test(d date, ts timestamp)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

#cursor = con.cursor()
#cursor.execute("""
#    create table testnum (
#        amount DECTEXT not null
#    )
#""")

for _ in range(1000):
    cur.execute("insert into testnum(amount) values(?)", (Decimal("12.01"),))
con.commit()

# Uses floating point math:
cur.execute("select sum(amount) from testnum")
row = cur.fetchone()
print('Floating point sum:', row[0], type(row[0]))

# Uses decimal math but returns result as a string
# and so we do a final conversion from string to Decimal:
cur.execute("select decimal_sum(amount) as `amount [dectext]` from testnum")
row = cur.fetchone()
print('Decimal sum:', row[0], type(row[0]))


con.commit()
con.close()