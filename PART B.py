#PART B-UndoomedDiceTransformer
def undoom_dice(die_a, die_b):
    scaling_factor = sum(die_a) / sum(die_b)
    new_die_a = [min(4, spots) for spots in die_a]
    new_die_b = [min(6, round(spots * scaling_factor)) for spots in die_b]
    return new_die_a, new_die_b
die_a = [1, 2, 3, 4, 5, 6]
die_b = die_a
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("\nNew Die A:", new_die_a)
print("New Die B:", new_die_b)
