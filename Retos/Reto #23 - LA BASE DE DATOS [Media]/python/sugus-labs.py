from sqlalchemy import create_engine, text

def query_database():
    
    host = "mysql-5707.dinaserver.com"
    port = 3306
    user = "mouredev_read"
    passw = "mouredev_pass"
    database = "moure_test"
    
    engine = create_engine(
        f"mysql+mysqlconnector://{user}:{passw}@{host}/{database}")
    conn = engine.connect()
    result = conn.execute(
        text("SELECT * FROM challenges"))
    for row in result:
        print(row)
     
if __name__ == "__main__":
    
    side_max = 3
    query_database()

