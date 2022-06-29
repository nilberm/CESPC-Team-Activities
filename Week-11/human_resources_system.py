name = []
id_number = []
job_title = []
salary = []



with open("hr_system.txt") as information:
  for line in information:
    line = line.strip()
    line_info = line.split(" ")
    name.append(line_info[0])
    id_number.append(line_info[1])
    job_title.append(line_info[2])
    salary.append(float(line_info[3]))


print()
for i in range(len(name)):
  salary_paycheck = salary[i]/24
  if job_title[i] == "Engineer":
    salary_paycheck += 1000

  print(f"{name[i]} (ID: {id_number[i]}), {job_title[i]} - {salary_paycheck:.2f}")