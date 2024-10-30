import random

# guess_count = 0  # int
# guessed_letters = []  # list
# current_word = [] ""  # 'str', list
# word_list = ["Apple", "Banana"]

# strings are immutable -> build a new string
current_word = "_____"
s = ""
for i in range(len(current_word)):
    if i == 0:
        s += "A"
    else:
        s += current_word[i]
print(s)

# list is mutable
current_word = ["_", "_", "_", "_", "_"]
current_word[0] = "A"  # update element in the list
print(" ".join(current_word))

# how to choose a word randomly from the list?
word_list = ["Apple", "Banana", "Pineapple", "Durian", "Watermelon", "Kiwi", "Strawberry"]
# index -> int -> random int
i = random.randint(0, len(word_list) - 1)
print(word_list[i])

# to choose a random item directly from the list (without index)
random_word = random.choice(word_list)
print(random_word)

# loop
while True:
    # condition_to_end: guess_count, get the answer
    if condition_to_end:
        break



