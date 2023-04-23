scores = []

for i in range(5):
    score = int(input("Enter scores: "))
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average: {average}")
