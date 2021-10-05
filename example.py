students = {2020123:'Lee', 2019521:'Kim', 2016974:'Park', 2021273:'Jung'}

for key in students.keys():
    key_ = key//1000
    if key_ <= 2019:
        print(students[key])