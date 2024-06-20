grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
solution= []
students_sorted=sorted(students)
for num in grades:
    solution_1= sum(num)/len(num)
    solution.append(solution_1)
result=dict(zip(students_sorted, solution))
print(result)

