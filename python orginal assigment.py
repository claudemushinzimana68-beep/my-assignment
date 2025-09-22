
# Project 75: Photography Contest Ratings
# -------------------------------

# === INTEGERS ===
ratings = [78, 85, 92, 67, 88, 95, 73]  # Example integer ratings (marks/scores)

# Perform integer operations
total = sum(ratings)          # Compute total of all ratings
average = total / len(ratings)  # Compute average rating
minimum = min(ratings)        # Find the lowest rating
maximum = max(ratings)        # Find the highest rating

print("=== INTEGERS ===")
print(f"Ratings: {ratings}")
print(f"Total: {total}, Average: {average:.2f}, Min: {minimum}, Max: {maximum}")
print()
# === STRINGS ===
print("=== STRINGS ===")
# Create formatted reports using f-strings
report = f"The Photography Contest had {len(ratings)} participants with an average rating of {average:.2f}."
report2 = f"The highest rating achieved was {maximum}, while the lowest was {minimum}."
print(report)
print(report2)
print()
# === BOOLEANS ===
print("=== BOOLEANS ===")
threshold = 80  # Define threshold to check quality
# Compound boolean condition: average > 80 AND maximum > 80
status = "Above Standard" if average > threshold and maximum > threshold else "Below Standard"
print(f"Average rating: {average:.2f} → Status: {status}")
print()

# === LISTS ===
print("=== LISTS ===")
print("Original Ratings:", ratings)

# Add a new rating
ratings.append(90)   # Adding a new score

# Remove ratings below 70 (simulate removing low performers)
ratings = [r for r in ratings if r >= 70]

# Sort the list
ratings.sort()

print("Modified & Sorted Ratings:", ratings)
print()
import array 
# === ARRAYS ===
print("=== ARRAYS ===")
# Convert the list into an array of integers
ratings_array = array.array('i', ratings)

# Compute sum of array
sum_array = sum(ratings_array)

print("Ratings Array:", ratings_array.tolist())  # Convert back to list for display
print("Sum using Array:", sum_array)
print("Comparison with List Sum:", sum_array == sum(ratings))  # Compare with list version
print()

# === DICTIONARIES ===
print("=== DICTIONARIES ===")
# List of dictionaries (id, name, value)
records = [
    {"id": 1, "name": "Alice", "value": 78},
    {"id": 2, "name": "Bob", "value": 85},
    {"id": 3, "name": "Charlie", "value": 92},
]

# Update Bob’s score
for rec in records:
    if rec["name"] == "Bob":
        rec["value"] = 90  # update value

# Delete Alice’s record
records = [rec for rec in records if rec["name"] != "Alice"]

# Compute total of 'value' fields
total_value = sum(rec["value"] for rec in records)

print("Records:", records)
print("Total of 'value' fields:", total_value)


    