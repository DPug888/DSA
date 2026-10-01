# cook your dish here
def attendance_marker():
    attendance = list(map(int, input().split()))
    absentees = 0
    for num in attendance:
        if num == 0:
            absentees += 1

    if absentees >= 1:
        print(absentees, "student absent")
    else:
        print("No absentees")

attendance_marker()