marks = []
for i in range(5):
    subject_mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(subject_mark)

total_marks = sum(marks)
average_marks = total_marks / 5

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\nMarksheet")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Grade:", grade)
