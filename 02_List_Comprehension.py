### List Comprehension ###

my_original_list = [20, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]

print(f"\nMy original list:\n{my_list}\n")
print(f"My list:\n{my_list}\n")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"My list:\n{my_list}\n")

my_range = range(10)

my_list = [i for i in my_range]
print(f"My list from my range:\n{my_list}\n")

my_list = [i + 1 for i in my_range]
print(f"My list from my range:\n{my_list}\n")

my_list = [i * 2 for i in my_range]
print(f"My list from my range:\n{my_list}\n")

my_list = [i * i for i in my_range]
print(f"My list from my range:\n{my_list}\n")

my_list = [2 ** i for i in my_range]
print(f"My list from my range:\n{my_list}\n")