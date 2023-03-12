import psycopg2
import time

# Connecting to server
def get_connection():
    conn = psycopg2.connect(user = "doadmin",
                            password = "AVNS_vTq8woZ41dehfRBnKRt",
                            host = "db-postgresql-nyc1-07777-do-user-10755856-0.b.db.ondigitalocean.com",
                            port = "25060",
                            database = "matcher",
                            sslmode = "require")
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed")

def find_students():
    try:
        conn = get_connection()
        cur = conn.cursor()
        select_query = """SELECT * FROM request WHERE status=FALSE"""
        cur.execute(select_query)
        list = cur.fetchall()

        # Finds tutors for each subject where a tutor is needed
        for request in list:
            query = "SELECT * FROM availability WHERE subject LIKE %s"
            # query = [x for x in query if [2] = ]
            print(request[3])
            cur.execute(query, (request[3],))
            print(cur.fetchall())


        close_connection(conn)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)


def pairing():
    try:
        conn = get_connection()
        cur = conn.cursor()

        TutorQuery = """SELECT * FROM tutor"""
        cur.execute(TutorQuery)
        TutorList = cur.fetchall()
        print(TutorList)

        StudentQuery = """SELECT * FROM request"""
        cur.execute(StudentQuery)
        StudentList = cur.fetchall()
        print(StudentList[0])

        for i in range(len((TutorList))):
            if TutorList[i][2] <= TutorList[i][3]:
                cur.execute("DELETE FROM avaialability WHERE tutor_id = ",(TutorList[i][1]))
        
        TutorQuery = """SELECT * FROM availability WHERE subject=%s AND university=%s"""
        
        for request in StudentList:
            cur.execute(TutorQuery,(request[3],request[4],))
            tutors = cur.fetchall()
            if(len(tutors) > 0):
                matchQuery = """INSERT INTO matches (student_id,tutor_id,subject,university)
                    VALUES (%s,%s,%s,%s)"""
                tutor = tutors.pop()
                print(tutor)
                print(request)
                cur.execute(matchQuery,(request[1],tutor[0],tutor[1],tutor[2]))
                alterQuery = """UPDATE tutor SET 
                                current_students = current_students + 1
                                WHERE id=%s"""
                cur.execute(alterQuery,(tutor[0],))
            
        
        conn.commit()
        close_connection(conn)

    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)
    
while True:
    pairing()
    time.sleep(100)