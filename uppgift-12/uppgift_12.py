# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students):
    student_dict = {name: age for name, age in students}
    return student_dict
students = [("Anna", 25), ("Gustav", 23), ("Sara", 24)]
print(create_student_register(students))