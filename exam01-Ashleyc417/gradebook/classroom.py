# Return the Class Average for a given hw assignment
def homework_average(grades, assignment_no):
    students = len(grades.keys())
    total_score = 0

    for student_id, info in grades.items():
        if assignment_no not in range(len(info.get('homework'))):
            return 0
        
        student_grades = info.get('homework')
        total_score += student_grades[assignment_no]

    return total_score / students

# Return the Class Average of All Homework Assignment
def homework_average_average(grades):
    if len(grades.keys()) == 0:
        return 0
    else:
        average_score = 0
        student_id = list(grades.keys())[0]
        student_info = grades[student_id]
        total_assignments = len(student_info.get('homework'))

        for index in range(total_assignments):
            average_score += homework_average(grades, index)
        
    return average_score / total_assignments


# Return Laboratory Average for a given lab assignment
def laboratory_average(grades, assignment_no):
    students = len(grades.keys())
    total_score = 0

    for student_id, info in grades.items():
        if assignment_no not in range(len(info.get('laboratory'))):
            return 0
        
        student_grades = info.get('laboratory')
        total_score += student_grades[assignment_no]

    return total_score / students


# Return the Class Average of All Lab Assignment
def laboratory_average_average(grades):
    if len(grades.keys()) == 0:
        return 0
    else:
        average_score = 0
        student_id = list(grades.keys())[0]
        student_info = grades[student_id]
        total_assignments = len(student_info.get('laboratory'))

        for index in range(total_assignments):
            average_score += laboratory_average(grades, index)
    
    return average_score / total_assignments


# Return the classroom total weighted avg of all student assignments
def total_weighted_average_average(grades):
    if len(grades.keys()) == 0:
        return 0
    else:
        return (homework_average_average(grades) * 0.25) + (laboratory_average_average(grades) * 0.75)
