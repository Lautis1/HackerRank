"""Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N, the number of students. 
The 2N subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line."""

def nested_list():

	students = list()
	n = int(input())
	for i in range(n):
		name = input()
		score = float(input())
		students.append([name, score])

	scores = [students[x][1] for x in range(n)]
	scores.sort()
	lowest = min(scores)
	scores = [x for x in scores if x != lowest]


	students = [st[0] for st in students if st[1]==scores[0]]
	students.sort()
	print(students)
	for name in students:
		print(name)