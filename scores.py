student_ids = [101, 102, 103, 104, 105]
student_names = ["Alice","Bob","Charlie","David","Eve"]
student_scores = [78, 85, 92, 88, 95]
average_score = 0
for score in student_scores:
    average_score += score

average_score = average_score/len(student_scores)

print(average_score)

search_id = int(input("Search by Student ID: "))

for i in range(len(student_ids)):
    if student_ids[i] == search_id:
        print(student_scores[i])
        break

high_score = 0
high_score_id = 0
for x in range(len(student_scores)):
    if student_scores[x] > high_score:
        high_score += student_scores[x]
        high_score_id = x

print(f"{student_names[high_score_id]} had the highest score of {high_score}")