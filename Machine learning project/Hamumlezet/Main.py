# -*- coding: utf-8 -*-
import sys

import networkx as nx
import matplotlib.pyplot as plt
from JsonParser import JsonParser
import ast
from Course import Course
from Create_students import *
import Astar
from Data import Data
from State import State
from Student import Student
from CoursesGraph import CoursesGraph
from OptionsGraph import OptionsGraph
from GradeSheetParser import GradeSheetParser
from CatalogParser import CatalogParser
from GraduateParser import GraduateParser
import time
from HtmlDownloader import download_html
import time
from DataSet import DataSet
import json
import copy

def initialization(file_path: str):
    # open the file and read it
    """ file_name is the name of the file that contains the students """
    # print('------------------------------Student------------------------------')
    # file_path = "Students/3-Sem_54-69/3-Sem_54-69_Classic.txt"
    grade_sheet = GradeSheetParser(None, file_path)
    # print the name of file.
    # print('file name: ' + (file_path.split('/')[8]))
    catalog = CatalogParser()
    # courses_obj = GraduateParser(None, catalog, True, False) # arguments for extracting courses from CoursesTest
    # courses_obj = GraduateParser('courses.json', None, False, False) # arguments for extracting courses from json file
    # courses_obj = GraduateParser(None, CatalogParser, False, True)  # arguments for extracting courses from graduate with internet access
    # site with internet access
    courses_obj = GraduateParser(None, catalog, False,
                                 False)  # arguments for extracting courses from graduate site without internet access
    # without internet access
    Data()
    Data.get_instance().set_courses_dict(courses_obj.get_courses_dict())
    Data.get_instance().set_linked_dict(courses_obj.get_linked_dict())

    state = State(grade_sheet.get_completed_courses_id(),
                  catalog.get_three_year_degree_requirements_credit_points())
    student = Student(grade_sheet.get_name(), grade_sheet.get_id(),
                      grade_sheet.get_catalog_type(), grade_sheet.get_degree_type(), state)
    Data.get_instance().set_student(student)
    # print which courses the student has completed, id and name
    completed_courses = GradeSheetParser.get_instance().get_completed_courses_id()
    # print('completed courses:')
    # for course in completed_courses:
    #     print(Data.get_instance().courses_dict[course].get_name() + ' : ' + Data.get_instance().courses_dict[course].get_id())


# with open(f'{file_path}/Students - Completed 2/{new_name}.json', 'w') as outfile:
#     json.dump(new, outfile, indent=4)

# print("credits left for graduation: " + str(state.get_remaining_points()))
# print("credit points completed: " + str(state.get_completed_points()))
# print(state.get_remaining_points_per_req())


def heuristic_points_to_graduation(u, v):
    """ u and v are nodes in the graph. v is the goal node(end) """
    if u == "end":
        return 0
    return OptionsGraph.get_instance().get_heuristic(u)


def heuristic_importance(u, v):
    """ u and v are nodes in the graph. v is the goal node(end) """
    if u == "end":
        return 0
    importance_sum = 0
    # iterate over courses in the node tuple and sum their importance
    for course_id in u[0]:
        if course_id == "__DONE__":
            continue
        importance_sum += Data.get_instance().courses_dict[course_id].get_importance()
    importance_factor = 1 / importance_sum if importance_sum > 0 else 1
    return importance_factor


def main(file_path: str):
    #open json file
    json_file = open(f'{file_path}')
    student_data = json.load(json_file)
    initialization(file_path)
    # insert two keys to dict
    completed_courses = GradeSheetParser.get_instance().get_completed_courses_id()
    CoursesGraph()
    CoursesGraph.get_instance().create_graph()
    OptionsGraph()
    OptionsGraph.get_instance().create_graph()

    #####################################################################################################################

    ## importance Astar g is weight ##
    final_path_importance = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end",
                                             heuristic_importance)
    filtered_list = [item for item in final_path_importance if isinstance(item, tuple)]
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        # print(f"Semester {i}: {', '.join(course_names)}")
        sem = [Data.get_instance().courses_dict[course_id].get_id() for course_id in semester]
        temp = student_data['Suggested courses']
        temp[f'Semester {len(student_data["Completed courses"]) + i}'] = sem

    #####################################################################################################################

    # delete instances of classes
    Data.delete_instance(Data.get_instance())
    GradeSheetParser.delete_instance(GradeSheetParser.get_instance())
    CatalogParser.delete_instance(CatalogParser.get_instance())
    GraduateParser.delete_instance(GraduateParser.get_instance())
    CoursesGraph.delete_instance(CoursesGraph.get_instance())
    OptionsGraph.delete_instance(OptionsGraph.get_instance())
    Student.delete_instance(Student.get_instance())

    original_student_data = copy.deepcopy(student_data)

    # Find the first semester key in 'Suggested courses'
    first_semester_key = next(iter(student_data['Suggested courses']))
    # Move this semester to 'Completed courses'
    student_data['Completed courses'][first_semester_key] = student_data['Suggested courses'].pop(first_semester_key)
    #create new json file with the new data
    #remove from file_path until (not including) the last 'Semester'
    student_data['Suggested courses'] = {}
    return student_data, original_student_data
    pass



    #TODO עצרתי במחשבה איזה קבצים של גיסון אני צריך ליצור, אז סה"כ שניים. אחד לעדכן את הקובץ הנוכחי בתוצאות, שתיים זה ליצור קובץ חדר עם היסטוריה של סמסטר קדימה.


