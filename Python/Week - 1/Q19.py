##Create this list: grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
##Count how many students: got A (≥90), got B (80–89), got C (70–79), got below 70

grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
i = 0
grade_a = 0
grade_b = 0
grade_c = 0
below_70 = 0
while i < len(grades):
    if grades[i] >= 90:
        grade_a += 1
    elif grades[i] >= 80:
        grade_b += 1
    elif grades[i] >= 70:
        grade_c += 1
    else:
        below_70 += 1
    i += 1
print("Number of students who got A:", grade_a)
print("Number of students who got B:", grade_b)   
print("Number of students who got C:", grade_c)
print("Number of students who got below 70:", below_70)
