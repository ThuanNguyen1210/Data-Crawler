import json
import pymysql

json_data = open("job_detail.json", encoding="utf8").read()
json_obj = json.loads(json_data)

con = pymysql.connect(host="localhost", user="root", password="", db="job")
cursor = con.cursor()

i = 0
for item in json_obj:

    i += 1
    EID = "EID" + "{:06d}".format(i)

    IEID = EID
    # if item.get("job_title") is not None:
    #     check = item.get("job_title").find("hot")
    #     if check != -1:
    #         INAME = item.get("job_title")
    #     else:
    #         INAME = -1
    INAME = item.get("job_title")
    ILOCATION = item.get("location")

    OEID = EID
    if item.get("company") is not None:
        check = item.get("company").find("Công ty")
        if check != -1:
            ONAME = item.get("company")
        else:
            ONAME = -1
    else:
        ONAME = -1
    OLOCATION = item.get("location")


    ID = "ID" + "{:06d}".format(i)
    IEID = EID
    if item.get("company") is not None:
        check = item.get("company").find("Công ty")
        if check != -1:
            NAME = item.get("company")
        else:
            NAME = -1
    else:
        NAME = -1
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
