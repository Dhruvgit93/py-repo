#!/usr/bin/env python
student={
    "dh15ty":{
        "name":"dhruv",
        "roll":"15",
        "section":"tyitm"
    }
}
student_code=""
def new_student(name,roll,section):
    global student_code
    student_code=name[:2]+roll[:2]+section[:2]
    print(student_code)
    if student_code in student:
        print("student is already register")
    elif any(n['roll']==roll for n in student.values()):

        print("roll number is already there")
    else:
         new_registration={
            "name":name,
            "roll":roll,
            "section":section,
            "enrollment":"cvm."+student_code+"2023"
        }
         student[student_code]=new_registration

new_student("druv","16","tyitm")
print(student)
