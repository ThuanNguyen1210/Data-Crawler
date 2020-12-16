import json
import pymysql
json_data = open("job_detail.json", encoding="utf8").read()

json_obj = json.loads(json_data)

con = pymysql.connect(host = "localhost", user = "root", password="", db="job")


cursor = con.cursor()
i=0
for item in json_obj:
    job_title = item.get("job_title")
    company = item.get("company")
    salary = item.get("salary")
    location = item.get("location")
    position = item.get("position")
    job_description = item.get("job_description")
    job_requirement = item.get("job_requirement")
    benefit = item.get("benefit")
    quantity = item.get("quantity")
    i+=1

    ID= "C"+str(i)
    cursor.execute(
        "insert into job(job_title, company, salary, location, position, job_description, job_requirement, benefit, quantity) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (job_title, company, salary, location, position, job_description, job_requirement, benefit, quantity))
con.commit()
con.close()
