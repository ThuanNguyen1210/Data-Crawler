import json
import pymysql

json_data = open("job_detail.json", encoding="utf8").read()
json_obj = json.loads(json_data)

con = pymysql.connect(host="localhost", user="root", password="", db="job")
cursor = con.cursor()

i = 0
for item in json_obj:
    i += 1
    EID = "ID" + "{:06d}".format(i)
    ENAME = item.get("job_title")

    IID = EID
    INAME = item.get("job_title")
    ILOCAL = item.get("location")
    IPOSTION = item.get("position")
    IDESCRIPTION = item.get("job_description")
    IBENEFIT = item.get("benefit")
    ISALARY = item.get("salary")        
    IREQUIREMENT = item.get("job_requirement")
    QUANTITY = item.get("quantity")

    CID = EID
    if item.get("company") is not None:
        check = item.get("company").find("Công ty")
        if check != -1:
            CNAME = item.get("company")
        else:
            CNAME = None
    else:
        CNAME = None

    CLOCAL = item.get("location")
    CPOSITION = item.get("position")
    CDESCRIPTION = item.get("job_description")
    CBENEFIT = item.get("benefit")
    CSALARY = item.get("salary")
    CREQUIREMENT = item.get("job_requirement")

    CIID = CID
    if item.get("company") != "hot":
        CINAME = item.get("company")
    else:
        CINAME = None
    ADDRESS = item.get("location")

    cursor.execute(
        "insert into Employment_Information(EID, ENAME) values(%s, %s)",
        (EID, ENAME))

    cursor.execute(
        "insert into Individual(IID, INAME, ILOCAL, IPOSTION, IDESCRIPTION, IBENEFIT, ISALARY, IREQUIREMENT, QUANTITY) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (IID, INAME, ILOCAL, IPOSTION, IDESCRIPTION, IBENEFIT, ISALARY, IREQUIREMENT, QUANTITY))

    cursor.execute(
        "insert into Company(CID, CNAME, CLOCAL, CPOSITION, CDESCRIPTION, CBENEFIT, CSALARY, CREQUIREMENT) values(%s, %s, %s, %s, %s, %s, %s, %s)",
        (CID, CNAME, CLOCAL, CPOSITION, CDESCRIPTION, CBENEFIT, CSALARY, CREQUIREMENT))

    cursor.execute(
        "insert into Company_Information(CIID, CINAME, ADDRESS) values(%s, %s, %s)",
        (CIID, CINAME, ADDRESS))

con.commit()
con.close()
