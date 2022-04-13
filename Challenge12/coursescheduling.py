#!/usr/bin/python3
import sys

data = sys.stdin.readlines()

course_dict = {}
num_lines = int(data[0])
for i in range(1,num_lines+1):
    first_name, last_name, course_name = data[i].strip().split(" ")
    full_name = last_name + first_name
    if course_name in course_dict:
        if full_name not in course_dict[course_name]:
            course_dict[course_name]["count"] += 1
            course_dict[course_name][full_name] = True
    else:
        course_dict[course_name] = {}
        course_dict[course_name][full_name] = True
        course_dict[course_name]["count"] = 1

for course_name in sorted(course_dict):
    print(course_name, course_dict[course_name]["count"])
