import sqlite3
conn = sqlite3.connect('patient.db')

cur = conn.cursor()
cur.execute("CREATE TABLE PATIENT_DETAILS(PATIENT_NAME VARCHAR(30),PATIENT_AGE INT,GENDER VARCHAR(10),RESULT VARCHAR(20))")
cur.execute("INSERT INTO PATIENT_DETAILS VALUES('Radhika Prakash',23,'Female','Non-diabetic ')")


conn.commit()