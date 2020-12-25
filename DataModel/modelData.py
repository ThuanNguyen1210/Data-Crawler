import json
import pymysql

json_data = open("job_detail.json", encoding="utf8").read()
json_obj = json.loads(json_data)

con = pymysql.connect(host="localhost", user="root", password="", db="job")
cursor = con.cursor()

i = 0
for item in json_obj:
    i += 1
    ID = "ID" + "{:06d}".format(i)
    EID = "EID" + "{:06d}".format(i)

    # NAME = item.get("company")
    if item.get("company") is not None:
        check = item.get("company").find("Công ty")
        if check != -1:
            NAME = item.get("company")
        else:
            NAME = -1
    else:
        NAME = -1

    LOCAL = item.get("location")
    POSITION = item.get("position")
    DESCRIPTION = item.get("job_description")
    BENEFIT = item.get("benefit")
    SALARY = item.get("salary")
    REQUIREMENT = item.get("job_requirement")
    QUANTITY = item.get("quantity")

    IID = ID
    INAME = item.get("job_title")
    ILOCAL = item.get("location")

    CID = ID

    if item.get("company") is not None:
        check = item.get("company").find("Công ty")
        if check != -1:
            CNAME = item.get("company")
        else:
            CNAME = -1
    else:
        CNAME = -1

    CLOCAL = item.get("location")

    cursor.execute(
        "insert into Employment_Information(ID, EID, NAME, LOCAL, POSTION, DESCRIPTION, BENEFIT, SALARY, REQUIREMENT, QUANTITY) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (ID, EID, NAME, LOCAL, POSITION, DESCRIPTION, BENEFIT, SALARY, REQUIREMENT, QUANTITY))

    cursor.execute(
        "insert into Individual(IID, INAME, ILOCAL) values(%s, %s, %s)",
        (IID, INAME, ILOCAL))

    cursor.execute(
        "insert into Organization(CID, CNAME, CLOCAL) values(%s, %s, %s)",
        (CID, CNAME, CLOCAL))


con.commit()
con.close()
