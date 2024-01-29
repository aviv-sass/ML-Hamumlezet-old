###
#  General settings
#   Add jason
###
# -*- coding: utf-8 -*-

DAYS = ['א', 'ב', 'ג', 'ד', 'ה', 'ו']
SEASON = ['א', 'ב', 'ג']
# !!!!IMPORTANT: DO NOT CHANGE THE TYPES ORDER IN COURSES_TYPES, YOU CAN ADD NEW TYPES ONLY IN THE END OF THE LIST!!

# UNIVERSAL ID -
# '4' - סמינר קורס (איחוד של סמינרים)
COURSES_TYPES = ["חובה",  # 0
                 "בחירה חופשית",  # 1
                 "העשרה",  # 2
                 "מתמטי נוסף",  # 3
                 "שרשרת מדעית",  # 4
                 "ספורט",  # 5
                 "רשימה א",  # 6
                 "רשימה ב",  # 7
                 "פרויקט",  # 8
                 "תת שרשרת מדעית"  # 9
                 ]

COURSES_SUBTYPES = [
    "פיזיקה 1",  # 0
    "פיזיקה 2",  # 1
    "ביולוגיה",  # 2
    "כימיה 1",  # 3
    "כימיה 2",  # 4
    "פיזיקה-כימיה"  # 5
]
COURSES_NUM_PER_SUBTYPES = {
    "פיזיקה 1": 1,  # 0
    "פיזיקה 2": 2,  # 1
    "ביולוגיה": 2,  # 2
    "כימיה 1": 2,  # 3
    "כימיה 2": 2,  # 4
    "פיזיקה-כימיה": 2  # 5

}
DAYS_BETWEEN_TESTS = 2
TOTAL_POINTS_A_B_LIST = 24.5
MIN_POINTS_PER_SEMESTER = 18
MAX_POINTS_PER_SEMESTER = 23
MAX_AVAILABLE_COURSES = 7

STUDY_PLAN = ["3 years - Computer Science",  # 0
              "4 years - Computer Science",  # 1
              "Software Engineering",  # 2
              "Computer Engineering"]  # 3

CATALOG_TYPES = ["2019-2020",  # 0
                 "2020-2021",  # 1
                 "2021-2022",  # 2
                 "2022-2023"]  # 3

GENERIC_COURSES = ["000011", "000012", "000021", "000022", "000023", "000031"]

SPECIAL_PREREQUISITES_COURSES = ['113014', '113013', '123015']

LENGTH_OPTIMIZATION = True

MANDATORY_COURSES_POINTS = 42
# more settings..
