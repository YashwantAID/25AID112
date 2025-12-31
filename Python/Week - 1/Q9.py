##Ask user for two exam scores (0–100).
##Print "You passed!" if both scores are ≥ 50, otherwise "You need to retake some exams".

score1 = float(input("Enter the first exam score (0-100): "))
score2 = float(input("Enter the second exam score (0-100): "))
if score1 >= 50 and score2 >= 50:
    print("You passed!")
else:
    print("You need to retake some exams.")
    