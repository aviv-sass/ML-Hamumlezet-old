import os
from Main import main
from DataSet import DataSet
import json
import time

if __name__ == '__main__':
    #measure time begin
    start = time.time()
    file_path = 'C:/Users/avivs/Desktop/Intreviews/ML-Hamumlezet/Machine Learning Project/MLstudentsFromScratch'
    folders = os.listdir(file_path)

    #completed 1 semester:
    # for folder in folders:
    #     students = os.listdir(f'{file_path}/{folder}')
    #     if folder == 'Students - Completed 1':
    #         for stu in students:
    #             print(f'Running: {stu}')
    #             try:
    #                 new, original = main(f'{file_path}/{folder}/{stu}')
    #             except:
    #                 continue
    #             # update the json file and insert semesters to the suggested courses
    #             with open(f'{file_path}/{folder}/{stu}', 'w') as outfile:
    #                 json.dump(original, outfile, indent=4)
    #             # remove until '-'
    #             new_name = stu.split('-')[0]
    #             new_name += '-Semester2'
    #             # create json file from the student_data
    #             with open(f'{file_path}/Students - Completed 2/{new_name}.json', 'w') as f:
    #                 # convert to json with indent=4
    #                 json.dump(new, f, indent=4)
    #             print(f'Done: {new}')

    # #completed 2 semester:
    # for folder in folders:
    #     students = os.listdir(f'{file_path}/{folder}')
    #     if folder == 'Students - Completed 2':
    #         for stu in students:
    #             print(f'Running {stu}')
    #             try:
    #                 new, original = main(f'{file_path}/{folder}/{stu}')
    #             except:
    #                 continue
    #             # update the json file and insert semesters to the suggested courses
    #             with open(f'{file_path}/{folder}/{stu}', 'w') as outfile:
    #                 json.dump(original, outfile, indent=4)
    #             # remove until '-'
    #             new_name = stu.split('-')[0]
    #             new_name += '-Semester3'
    #             # create json file from the student_data
    #             with open(f'{file_path}/Students - Completed 3/{new_name}.json', 'w') as f:
    #                 # convert to json with indent=4
    #                 json.dump(new, f, indent=4)
    #
    #             print(f'Done {new_name}')
    # completed 3 semester:
    for folder in folders:
        students = os.listdir(f'{file_path}/{folder}')
        if folder == 'Students - Completed 3':
            for stu in students:
                print(f'Running {stu}')
                try:
                    new, original = main(f'{file_path}/{folder}/{stu}')
                except:
                    continue
                # update the json file and insert semesters to the suggested courses
                with open(f'{file_path}/{folder}/{stu}', 'w') as outfile:
                    json.dump(original, outfile, indent=4)
                # remove until '-'
                new_name = stu.split('-')[0]
                new_name += '-Semester3'
                # create json file from the student_data
                with open(f'{file_path}/Students - Completed 4/{new_name}.json', 'w') as f:
                    # convert to json with indent=4
                    json.dump(new, f, indent=4)

                print(f'Done {new_name}')
    #measure time end
    end = time.time()
    print(f'Time: {end - start}')
    print('Done All!')