# Part-A: Total Combinations
die_faces = [1, 2, 3, 4, 5, 6]
total_combinations = len(die_faces) ** 2
print("Total Combinations:", total_combinations)

# Part-A: Distribution of Possible Combinations
combinations_distribution = [(i, j) for i in die_faces for j in die_faces]
print("\nCombinations Distribution:")
for i in range(0, total_combinations, len(die_faces)):
    print(combinations_distribution[i:i + len(die_faces)])

# Part-A: Probability of Sums
print("\nProbability of Sums:")
for i in range(2, 13):
    count = sum(1 for face in combinations_distribution if sum(face) == i)
    probability = count / total_combinations
    print(f"P(Sum = {i}): {count}/{total_combinations} = {probability:.2f}")
