# A simple script to analyze student test scores

# 1. This is our raw data (a list of exam scores out of 100)
scores = [85, 92, 78, 90, 64, 88, 95, 71, 83]

print("Class Performance Report")

# Calculate the total number of students
total_students = len(scores)
print(f"Total Students: {total_students}")

# Find the highest and lowest scores automatically
highest_score = max(scores)
lowest_score = min(scores)
print(f"Highest Score: {highest_score}%")
print(f"Lowest Score: {lowest_score}%")

# Calculate the class average
class_average = sum(scores) / total_students
print(f"Class Average: {class_average:.1f}%")

# Sort the grades
sorted_scores = sorted(scores, reverse=True)
print(f"Leaderboard (Highest to Lowest): {sorted_scores}")

# Check if the class overall performed well
if class_average >= 80:
    print("Overall Performance: Excellent work, class!")
else:
    print("Overall Performance: Room for improvement.")
