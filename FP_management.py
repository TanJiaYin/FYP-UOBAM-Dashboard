import sqlalchemy as db
engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()

FP = db.Table('financial_position1', metadata,
              db.Column('financial_position_id', db.Integer, primary_key=True),
              db.Column('Year', db.Integer),
              db.Column('Types', db.String(200)),
              db.Column('Amount', db.DECIMAL(20,4)),
              )

CI1 = db.Table('comprehensive_income', metadata,
              db.Column('comprehensive_income_id', db.Integer, primary_key=True),
              db.Column('Year', db.Integer),
              db.Column('Types', db.String(200)),
              db.Column('Amount', db.Integer),
              )

metadata.create_all(engine)

def show_FPinfo():
    results = connection.execute(db.select([FP])).fetchall()

    fp = []
    for result in results:
        str = ''
        if result[2] == "Total Assets":
            str = 'Total Assets'
        elif result[2] == "Total Liabilities":
            str = 'Total Liabilities'
        elif result[2] == "Total Unitholders' Equity":
            str = "Total Unitholders' Equity"
        elif result[2] == "Total Equity and Liabilities":
            str = 'Total Equity and Liabilities'
        elif result[2] == "Units In Circulation":
            str = 'Units In Circulation'
        elif result[2] == "Net Asset Value Per Unit":
            str = 'Net Asset Value Per Unit'
        fp.append({
            'financial_position_id' : result[0],
            'Year' : result[1],
            'Types' : str,
            'Amount' : result[3]
        })

    #connection.close()

    return fp

def show_CI1info():
    results = connection.execute(db.select([CI1])).fetchall()

    ci1 = []
    for result in results:
        ci1.append({
            'comprehensive_income_id' : result[0],
            'Year' : result[1],
            'Types' : result[2],
            'Amount' : result[3]
        })

    #connection.close()

    return ci1
