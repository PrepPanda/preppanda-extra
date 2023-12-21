import random
import json

user_test_data = {}
each_test_data = {}


def generate_stats_for_each_sub():
    subjects = ["physics", "chemistry", "maths", "biology"]

    for subject in subjects:
        attempted = random.randint(50, 800)
        right = random.randint(10, attempted)
        wrong = attempted - right
        total = 800

        user_test_data[subject] = {
            "attempted": attempted,
            "right": right,
            "wrong": wrong,
            "total": total,
        }

    with open("./student.json", "w") as json_file:
        json.dump(user_test_data, json_file, indent=2)


# generate_stats_for_each_sub()
