import mysql.connector

from mysql.connector.cursor import MySQLCursor
from mysql.connector import errorcode

from typing import NewType, TypeVar, Generator
from abc import ABC, abstractmethod



Options = NewType("Options", dict[str, str])

TConnection = TypeVar("TConnection")
TCursor = TypeVar("TCursor")


class DatabaseError(Exception):
    pass

class AccessDeniedError(DatabaseError):
    pass

class DatabaseNotFoundError(DatabaseError):
    pass


class DatabaseService(ABC):
    
    @property
    @abstractmethod
    def conn(self) -> TConnection:
        pass    
    
    @property
    @abstractmethod
    def cursor(self) -> TCursor:
        pass


class Sql(ABC):
    
    @abstractmethod
    def execute_query(self, query: str) -> None:
        pass

    @abstractmethod
    def get_query_results(self) -> Generator:
        pass


class MySQLService(DatabaseService):

    def __init__(self, options: Options) -> None:
        self.__options = options
        self.__conn = None

    @property
    def conn(self) -> mysql.connector.MySQLConnection:
        try:
            options = self.__options.copy()
            cnx = mysql.connector.connect(**options)

            self.__conn = cnx
            return cnx
        except mysql.connector.Error as err:
            cnx.close()

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise AccessDeniedError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise DatabaseNotFoundError("Database does not exist")
            else:
                raise DatabaseError(err)
    
    @property
    def cursor(self) -> MySQLCursor:
        return self.__conn.cursor()


class SqlService(Sql):

    def __init__(self, db: DatabaseService) -> None:
        self.__conn = db.conn
        self.__cursor = db.cursor

    def execute_query(self,  query: str) -> None:
        self.__cursor.execute(query)

    def get_query_results(self) -> Generator:
        try:
            return (challenge for challenge in self.__cursor.fetchall())
        finally:
            self.__cursor.close()
            self.__conn.close()
        

def main() -> None:
    options: Options = {
        "host": "mysql-5707.dinaserver.com",
        "user": "mouredev_read",
        "password": "mouredev_pass",
        "database": "moure_test"
    }
    try:
        db: DatabaseService = MySQLService(options)

        sql: Sql = SqlService(db)
        sql.execute_query("SELECT * FROM challenges")
        query_results = sql.get_query_results()

        for result in query_results:
            print(result)
    except (DatabaseNotFoundError, 
            DatabaseError, 
            AccessDeniedError) as err:
        print(err)
    
    

if __name__ == "__main__":
    main()