'''Lab Attendance Summarizer:
The function prints
 The total number of sessions 
 The number of sessions in which the student was present 
 The number of absences 
 The number of late arrivals 
 The attendance percentage, where both P and L count as attendance 
 Whether the student is eligible to appear for the laboratory examination
 The maximum number of continuous leave'''

attendance=input('Enter attendance string: ').upper()

#To count number of Present, Absent and Late
present=attendance.count('P')
absent=attendance.count('A')
late=attendance.count('L')

#To calculate Attendance Percentage
attendance_percentage=((present+late)/len(attendance))*100

#Printing count of Present, Absent, Late and Attendance percentage
print(f'Total sessions: {len(attendance)}')
print(f'Present: {present}')
print(f'Absent: {absent}')
print(f'Late: {late}')
print(f'Attendance percentage: {attendance_percentage}')

#To check continuous absences
i=1
max_absent=0
while i<=len(attendance):
    if i*'A' in attendance:
        max_absent=i
    i+=1
print(f'Maximum consecutive absences: {max_absent}')

#To check if student is eligible for lab examination
if attendance_percentage>=75:
    print('Eligible: Yes')
else:
    print('Eligible: No')