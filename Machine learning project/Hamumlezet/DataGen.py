import os
from Main import main
from DataSet import DataSet

REMAINING_POINTS = []

DataSet()

students = os.listdir('C:/Users/avivs/Desktop/Studies/Machine Learning Project/Students Gen 1 + 2/new students')
for stu in students:
    #run the program with the student file
    #if name is not 'new_student.txt' then continue
    if stu != 'new_student.txt':
        continue
    print(f'Running {stu}')
    main(f'C:/Users/avivs/Desktop/Studies/Machine Learning Project/Students Gen 1 + 2/new students/{stu}')
    print(f'Done {stu}')

print('Done!')


#studnts will be a list of all the students.txt files
# semesters = os.listdir('Students')
# #remove all the str with sufix 'xlsx'
# for sem in semesters:
#     #remove all the str with sufix 'xlsx'
#     if sem.endswith('xlsx'):
#         semesters.remove(sem)
#         continue
    # students = os.listdir(f'Students/{sem}')
    #remove all the str with sufix 'xlsx'
    # for stu in students:
    #     if stu.endswith('xlsx'):
    #         students.remove(stu)
    # for stu in students:
    #     #run the program with the student file
    #     print(f'Running {stu}')
    #     main(f'C:/Users/avivs/Desktop/Studies/AI Project/Students/{sem}/{stu}')
    #     print(f'Done {stu}')
# print('Done!')



