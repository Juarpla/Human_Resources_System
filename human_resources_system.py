"""
Author: Juan Plasencia

Team Activity - Human Resources System
"""

with open("hr_system.txt") as file:
    for line in file:
        row = line.strip().split(" ")
        name = row[0]
        id_number = row[1]
        job_title = row[2]
        salary = float(row[3])
        paycheck = salary/24

        if job_title.lower() == "engineer":
            paycheck += 1000
       
        print(f"{name.capitalize()} (ID: {id_number}), {job_title} - ${paycheck:,.2f}")