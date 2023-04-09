# CTI-110

# P2HW2 - List

# Tory Horton

# 4-6-23

#



# user enters grades

Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

print()

# puts grades into a list

module_grades = [Module1, Module2, Module3, Module4, Module5, Module6]

# finds the lowest and highest grade



# results are shown lowest, highest, average, and sum

print('------------Results------------')
print(f'{"Lowest Grade:":<20}{min(module_grades):<10}') # min
print(f'{"Highest Grade:":<20}{max(module_grades):<10}') # max
print(f'{"Sum of Grades:":<20}{sum(module_grades):<10}') # sum

average_grade = (Module1 + Module2 + Module3 + Module4 + Module5 + Module6) / 6 # calculates average

print(f'{"Average:":<20}{average_grade:<10.2f}')

print('----------------------------------------')
