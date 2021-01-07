import json
import pymysql

json_data = open("data.json", encoding="utf8").read()
json_obj = json.loads(json_data)

con = pymysql.connect(host="localhost", user="root", password="", db="job")
cursor = con.cursor()

i = 0
for item in json_obj:

    i += 1
    EID = "EID" + "{:06d}".format(i)

    IEID = EID
    INAME = item.get("job_title")
    ILOCATION = item.get("location")

    OEID = EID

    if item.get("company") is None:
        ONAME = -1
    else:
        ONAME = item.get("company")
    OLOCATION = item.get("location")

    ID = "ID" + "{:06d}".format(i)
    IEID = EID
    if item.get("company") is None:
        NAME = -1
    else:
        NAME = item.get("company")
    LOCATION = item.get("location")
    POSITION = item.get("position")
    DESCRIPTION = item.get("job_description")
    BENEFIT = item.get("benefit")
    SALARY = item.get("salary")
    REQUIREMENT = item.get("job_requirement")
    QUANTITY = item.get("quantity")

    cursor.execute(
        "insert into EID(EID) values(%s)",
        (EID))

    cursor.execute(
        "insert into Individual(IEID, INAME, ILOCATION) values(%s, %s, %s)",
        (IEID, INAME, ILOCATION))

    cursor.execute(
        "insert into Organization(OEID, ONAME, OLOCATION) values(%s, %s, %s)",
        (OEID, ONAME, OLOCATION))

    cursor.execute(
        "insert into Employment_Information(ID, EID, NAME, SALARY, LOCATION, POSITION, DESCRIPTION, REQUIREMENT, BENEFIT, QUANTITY) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (ID, EID, NAME, SALARY, LOCATION, POSITION, DESCRIPTION, REQUIREMENT, BENEFIT, QUANTITY))

con.commit()
con.close()
