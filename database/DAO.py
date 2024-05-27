from database.DB_connect import DBConnect
from model.Team import Team


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.`year` 
                    from teams t
                    where `year` >= 1980
                    order by `year` desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    def getTeamsOfYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct * 
                    from teams t
                    where t.`year` = %s"""

        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

