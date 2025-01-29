# Return the Homework Average for Each Student
def homework_average(grades, student_id):
    if student_id not in grades:
        return 0
    else:
        student_info = grades[student_id]
        homework = student_info.get('homework', [])
        x = sum(homework) / len(homework)
    return x

# Return the Laboratory Average for Each Student
def laboratory_average(grades, student_id):
    if student_id not in grades:
        return 0
    else:
        student_info = grades[student_id]
        laboratory = student_info.get('laboratory', [])
        y = sum(laboratory) / len(laboratory)
    return y

# Return the Total Weighted Average for Each Student
def total_weighted_average(grades, student_id):
    if student_id not in grades:
        return 0
    else:
        return (homework_average(grades, student_id) * 0.25) + (laboratory_average(grades, student_id) * 0.75)