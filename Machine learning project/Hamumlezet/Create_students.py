import pandas as pd
import os


def create_students():
    folders = ['1-Sem_18-23', '2-Sem_36-46', '3-Sem_54-69', '4-Sem_72-92', '5-Sem_90-115']
    for folder in folders:
        # reading data from the xls file
        df = pd.read_excel(f"C:/Users/avivs/Desktop/Studies/AI Project/Students/{folder}/{folder}.xlsx")
        cols = ['Strong', 'Classic', 'Un1', 'Un2', 'Ran1', 'Ran2', 'Ran3', 'Ran4', 'Ran5', 'Ran6']
        # Iterate over the specified columns
        for col_name in cols:
            # Prepare the text for this file
            # specify the common header for each file
            header = f"Name:\n{col_name}\nID:\n123456789\nCatalog Type:\n2020-2021\nDegree Type:\n3 years - Computer " \
                     "Science\nCourses ID List:\n"
            text = header
            for val in df[col_name].dropna().unique():  # dropna() removes missing values, unique() gets unique values
                # Format the course ID as a 6-digit number, padded with zeros if necessary
                course_id = "{:06d}".format(int(val))
                text += course_id + '\n'

            # Write the text to a file
            with open(f"C:/Users/avivs/Desktop/Studies/AI Project/Students/{folder}/{folder}_{col_name}.txt", 'w') as f:
                f.write(text)
