names = input('Enter names spreated by commas: ').split(',')
assignments =  input('Enter number of missing assignments spreated by commas: ').split(',')
grades =  input('Enter current grades spreated by commas: ').split(',')
print(names,assignments,grades)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for num,val in enumerate(names):
    print(message.format(val.title(),int(assignments[num]),int(grades[num]),int(grades[num])+int(assignments[num])*2))
