import json
import ast
import datetime
import re

class Human:
    def __init__(self, id, first, last):
        self.first_name = first
        self.last_name = last
        self.id = id

    def make_jason(self):
        return json.dumps(self.__dict__)


if __name__ == '__main__':

    d1 = datetime.date(2020, 1, 1)

    string = "{'א': {'Day': 'ג', 'Date': datetime.date(2023, 7, 25), 'Season': 'א', 'Examination time': None}, 'ב': {'Day': 'ב', 'Date': datetime.date(2023, 10, 23), 'Season': 'ב', 'Examination time': None}, 'ג': {'Day': None, 'Date': None, 'Season': None, 'Examination time': None}}"
    # Define the regular expression pattern to match date strings
    date_pattern = r"datetime.date\((\d{4}), (\d{1,2}), (\d{1,2})\)"

    # Replace all date strings with datetime.date objects
    string = re.sub(date_pattern, lambda match: "datetime.date({}, {}, {})".format(*match.groups()), string)

    # Evaluate the modified string as a Python expression
    data = eval(string)

    # Convert the date strings to datetime.date objects
    for key, value in data.items():
        if isinstance(value["Date"], str):
            value["Date"] = datetime.date.fromisoformat(value["Date"])

    print(data)

    Aviv = Human('1', 'Aviv', 'Sasson')
    Rotem = Human('2', 'Rotem', 'Silfin')
    Efrat = Human('3', 'Efrat', 'Cohen')
    lst = [Aviv, Rotem, Efrat]
    json_data = '{"People":['
    for i in lst:
        json_data += i.make_jason() + ','
    json_data = json_data[:-1] + ']}'
    json_file = open("people.json", "w")
    json_file.write(json_data)
    json_file.close()

