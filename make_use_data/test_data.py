import random
import json


def generate_stats_for_tests():
    all_tests_data = []

    for test_id in range(1, 15):
        test_data = {
            "test_id": f"Test_{test_id}",
            "total_time": random.randint(60, 180),
            "subjects": {
                "physics": generate_subject_data(),
                "chemistry": generate_subject_data(),
                "maths": generate_subject_data(),
                "biology": generate_subject_data(),
            },
        }
        all_tests_data.append(test_data)

    return all_tests_data


def generate_subject_data():
    total_questions = 800
    attempted = random.randint(400, 800)
    right = random.randint(0, attempted)
    wrong = attempted - right
    time_spent = random.randint(60, 120)

    questions = generate_question_data(attempted, time_spent)

    subject_data = {
        "attempted": attempted,
        "right": right,
        "wrong": wrong,
        "total": total_questions,
        "time_spent": time_spent,
        "questions": questions,
    }

    return subject_data


def generate_question_data(attempted, total_time_subject):
    questions = []

    for question_id in range(1, attempted + 1):
        # Ensure max_time is within remaining time
        max_time = min(30, total_time_subject)
        if max_time >= 10:
            time_taken = random.randint(10, max_time)
        else:
            time_taken = 0
        total_time_subject -= time_taken

        question_data = {
            "id": question_id,
            "time": time_taken,
            "attempted": random.choice([True, False]),
            "right": random.choice([True, False]),
        }
        questions.append(question_data)

    return questions


# Example usage
test_stats = generate_stats_for_tests()
with open("./questions_stats.json", "w") as file:
    json.dump(test_stats, file, indent=2)
# print(test_stat)
