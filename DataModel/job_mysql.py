import json
import pymysql

empInfo = open("Employment_Information.json", encoding="utf8").read()
list_empInfo = json.loads(empInfo)

individual = open("Individual.json", encoding="utf8").read()
list_individual = json.loads(individual)

company = open("Company.json", encoding="utf8").read()
list_company = json.loads(company)

comInfo = open("Company_Information.json", encoding="utf8").read()
list_comInfo = json.loads(comInfo)

con = pymysql.connect(host = "localhost", user = "root", password="", db="job")
cursor = con.cursor()

for item in list_empInfo:
    EID = item.get("EID")
    ENAME = item.get("ENAME")
    ID_JOB = item.get("ID_JOB")

    cursor.execute(
        "insert into Employment_Information(EID, ENAME, ID_JOB) values(%s, %s, %s)",
        (EID, ENAME, ID_JOB))

for item in list_individual:
    IID = item.get("IID")
    INAME = item.get("INAME")
    ILOCAL = item.get("ILOCAL")
    IPOSTION = item.get("IPOSTION")
    IDESCRIPTION = item.get("IDESCRIPTION")
    IBENEFIT = item.get("IBENEFIT")
    ISALARY = item.get("ISALARY")
    IREQUIREMENT = item.get("IREQUIREMENT")
    QUANTITY = item.get("QUANTITY")

    cursor.execute(
        "insert into Individual(IID, INAME, ILOCAL, IPOSTION, IDESCRIPTION, IBENEFIT, ISALARY, IREQUIREMENT, QUANTITY) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (IID, INAME, ILOCAL, IPOSTION, IDESCRIPTION, IBENEFIT, ISALARY, IREQUIREMENT, QUANTITY))

for item in list_company:
    CID = item.get("CID")
    CNAME = item.get("CNAME")
    CLOCAL = item.get("CLOCAL")
    CPOSITION = item.get("CPOSITION")
    CDESCRIPTION = item.get("CDESCRIPTION")
    CBENEFIT = item.get("CBENEFIT")
    CSALARY = item.get("CSALARY")
    CREQUIREMENT = item.get("CREQUIREMENT")
    CLOCAL = item.get("CLOCAL")

    cursor.execute(
        "insert into Company(CID, CNAME, CLOCAL, CPOSITION, CDESCRIPTION, CBENEFIT, CSALARY, CREQUIREMENT) values(%s, %s, %s, %s, %s, %s, %s, %s)",
        (CID, CNAME, CLOCAL, CPOSITION, CDESCRIPTION, CBENEFIT, CSALARY, CREQUIREMENT))

for item in list_comInfo:
    CIID = item.get("CIID")
    CINAME = item.get("CINAME")
    ADDRESS = item.get("ADDRESS")

    cursor.execute(
        "insert into Company_Information(CIID, CINAME, ADDRESS) values(%s, %s, %s)",
        (CIID, CINAME, ADDRESS))

con.commit()
con.close()
