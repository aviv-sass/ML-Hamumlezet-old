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


def initialization(file_path: str):
    """ file_name is the name of the file that contains the students """
    #print('------------------------------Student------------------------------')
    # file_path = "Students/3-Sem_54-69/3-Sem_54-69_Classic.txt"
    grade_sheet = GradeSheetParser(file_path)
    #print the name of file.
    #print('file name: ' + (file_path.split('/')[8]))
    catalog = CatalogParser()
    # courses_obj = GraduateParser(None, catalog, True, False) # arguments for extracting courses from CoursesTest
    # courses_obj = GraduateParser('courses.json', None, False, False) # arguments for extracting courses from json file
    # courses_obj = GraduateParser(None, CatalogParser, False, True)  # arguments for extracting courses from graduate with internet access
    # site with internet access
    courses_obj = GraduateParser(None, catalog, False, False)  # arguments for extracting courses from graduate site without internet access
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
    #print('completed courses:')
    # for course in completed_courses:
    #     print(Data.get_instance().courses_dict[course].get_name() + ' : ' + Data.get_instance().courses_dict[course].get_id())
   # print("credits left for graduation: " + str(state.get_remaining_points()))
    #print("credit points completed: " + str(state.get_completed_points()))
    #print(state.get_remaining_points_per_req())


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
    #iterate over courses in the node tuple and sum their importance
    for course_id in u[0]:
        if course_id == "__DONE__":
            continue
        importance_sum += Data.get_instance().courses_dict[course_id].get_importance()
    importance_factor = 1/importance_sum if importance_sum > 0 else 1
    return importance_factor


def main(file_path: str):
    initialization_start_time = time.time()
    initialization(file_path)
    initialization_end_time = time.time()
    courses_graph_start_time = time.time()
    CoursesGraph()
    CoursesGraph.get_instance().create_graph()
    #create list that the type of the cours is "חובה" and sort it by importance
    # hova = [course for course in Data.get_instance().courses_dict.values() if course.get_type() == "חובה"]
    # importance_sorted_courses_list = sorted(hova, key=lambda x: x.get_importance(), reverse=True)
    courses_graph_end_time = time.time()
    options_graph_start_time = time.time()
    OptionsGraph()
    OptionsGraph.get_instance().create_graph()
    options_graph_end_time = time.time()
    a_star_start_time = time.time()
    ## vanilla Astar ##
    final_path = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end", heuristic_points_to_graduation)
    a_star_end_time = time.time()
    #print('------------------------------Astar------------------------------')
    #print("path:")
    #print(final_path)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    #print the name of the courses in the path (names come from data.courses_dict)
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        #print(f"Semester {i}: {', '.join(course_names)}")
    a_star_importance_start_time = time.time()
    ## importance Astar g is weight ##
    final_path_importance = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end", heuristic_importance)
    a_star_importance_end_time = time.time()
    #print("path with importance g is weight:")
    #print(final_path_importance)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path_importance if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    #print the name of the courses in the path (names come from data.courses_dict)
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        #print(f"Semester {i}: {', '.join(course_names)}")
    a_star_importance_zero_start_time = time.time()
    ## importance Astar g is zero ##
    final_path_importance_zero = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end",
                                             heuristic_importance, "zero")
    a_star_importance_zero_end_time = time.time()
    #print("path with importance g is zero:")
    #print(final_path_importance_zero)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path_importance_zero if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    # print the name of the courses in the path (names come from data.courses_dict)
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        #print(f"Semester {i}: {', '.join(course_names)}")
    a_star_credit_left_start_time = time.time()
    ## Astar credits for graduation g is zero ##
    final_path_credit_left = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end",
                                                  heuristic_points_to_graduation, "zero")
    a_star_credit_left_end_time = time.time()
    #print("path with credits for graduation g is zero:")
    #print(final_path_credit_left)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path_credit_left if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    # print the name of the courses in the path (names come from data.courses_dict)
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        #print(f"Semester {i}: {', '.join(course_names)}")
    a_star_credit_left_inverse_weight_start_time = time.time()
    ## Astar h is credits for graduation g is inverse_weight ##
    final_path_credit_left_inverse_weight = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end",
                                              heuristic_points_to_graduation, "inverse_weight")
    a_star_credit_left_inverse_weight_end_time = time.time()
    #print("path with credits for graduation g is inverse_weight:")
    #print(final_path_credit_left_inverse_weight)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path_credit_left_inverse_weight if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    # print the name of the courses in the path (names come from data.courses_dict)
    for i, semester in enumerate(cleaned_list, start=1):
        course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
        #print(f"Semester {i}: {', '.join(course_names)}")
    a_star_inverse_weight_start_time = time.time()
    ## Astar h is zero g is inverse_weight ##
    final_path_inverse_weight = Astar.astar_path(OptionsGraph.get_instance().options_graph, "start", "end", None,
                                                 "inverse_weight")
    a_star_inverse_weight_end_time = time.time()
    #print("path with h is zero g is inverse_weight:")
    #print(final_path_inverse_weight)
    # Filter out non-tuple elements
    filtered_list = [item for item in final_path_inverse_weight if isinstance(item, tuple)]
    # Create a nested list with only numbers
    cleaned_list = [[num for num in tup[0] if num.isdigit()] for tup in filtered_list]
    #print(cleaned_list)
    # print the name of the courses in the path (names come from data.courses_dict)
    # for i, semester in enumerate(cleaned_list, start=1):
    #     course_names = [Data.get_instance().courses_dict[course_id].get_name() for course_id in semester]
    #     print(f"Semester {i}: {', '.join(course_names)}")
    #print times of the program in seconds and minutes
    # print("------------------------------times------------------------------")
    # print("total time: " + str(a_star_end_time - initialization_start_time) + " seconds" + " = " + str((a_star_end_time - initialization_start_time)/60) + " minutes")
    # print("initialization time: " + str(initialization_end_time - initialization_start_time) + " seconds" + " = " + str((initialization_end_time - initialization_start_time)/60) + " minutes")
    # print("courses graph time: " + str(courses_graph_end_time - courses_graph_start_time) + " seconds" + " = " + str((courses_graph_end_time - courses_graph_start_time)/60) + " minutes")
    # print("options graph time: " + str(options_graph_end_time - options_graph_start_time) + " seconds" + " = " + str((options_graph_end_time - options_graph_start_time)/60) + " minutes")
    # print("Astar time: " + str(a_star_end_time - a_star_start_time) + " seconds" + " = " + str((a_star_end_time - a_star_start_time)/60) + " minutes")
    # print("Astar with importance g=weight time: " + str(a_star_importance_end_time - a_star_importance_start_time) + " seconds" + " = " + str(
    #     (a_star_importance_end_time - a_star_importance_start_time) / 60) + " minutes")
    # print("Astar with importance g=zero time: " + str(
    #     a_star_importance_zero_end_time - a_star_importance_zero_start_time) + " seconds" + " = " + str(
    #     (a_star_importance_zero_end_time - a_star_importance_zero_start_time) / 60) + " minutes")
    # print("Astar with credits for graduation g is zero time: " + str(
    #     a_star_credit_left_end_time - a_star_credit_left_start_time) + " seconds" + " = " + str(
    #     (a_star_credit_left_end_time - a_star_credit_left_start_time) / 60) + " minutes")
    # print("Astar with credits for graduation g is inverse_weight time: " + str(
    #     a_star_credit_left_inverse_weight_end_time - a_star_credit_left_inverse_weight_start_time) + " seconds" + " = " + str(
    #     ( a_star_credit_left_inverse_weight_end_time - a_star_credit_left_inverse_weight_start_time) / 60) + " minutes")
    # print("Astar with h is zero g is inverse_weight time: " + str(
    #     a_star_inverse_weight_end_time - a_star_inverse_weight_start_time) + " seconds" + " = " + str(
    #     ( a_star_inverse_weight_end_time - a_star_inverse_weight_start_time) / 60) + " minutes")
    # print("finish!")

    #delete instances of classes
    Data.delete_instance(Data.get_instance())
    GradeSheetParser.delete_instance(GradeSheetParser.get_instance())
    CatalogParser.delete_instance(CatalogParser.get_instance())
    GraduateParser.delete_instance(GraduateParser.get_instance())
    CoursesGraph.delete_instance(CoursesGraph.get_instance())
    OptionsGraph.delete_instance(OptionsGraph.get_instance())
    Student.delete_instance(Student.get_instance())

