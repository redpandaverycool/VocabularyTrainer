import random
import pandas as pd

Vocabulary_dict = {"English":[], "Macedonian":[]}
word_english = None
word_macedonian = None

# Try to load existing .csv file and read the dictionary values
try:
    df = pd.read_csv("vocabulary.csv", index_col=0) # Try to read the CSV file back as a DataFrame
    Vocabulary_dict = df.to_dict("split") # Convert the DataFrame back to the original dictionary format
    Vocabulary_dict = dict(zip(Vocabulary_dict["index"], Vocabulary_dict["data"])) # Convert the DataFrame back to the original dictionary format
    print("Existing vocabulary dictionary successfully loaded!")
except IOError:
    print("ATTENTION: No existing vocabulary dictionary found! New dictionary will be created.")

print("Please add new words to your dictionary (always starting with the English word). You can enter as many as wanted. When finished type in 'exit' to continue to the training.")

counter1 = 1
while True:
    word_english = str(input(f"{counter1}. English: ")).casefold()
    if word_english == "exit":
        break
    word_macedonian = str(input(f"{counter1}.Macedonian: " )).casefold()
    if word_macedonian == "exit":
        break
    Vocabulary_dict["English"].append(word_english)
    Vocabulary_dict["Macedonian"].append(word_macedonian)
    counter1 += 1

# Safe vocabulary list to .csv file
df = pd.DataFrame.from_dict(Vocabulary_dict, orient="index")
df.to_csv("vocabulary.csv")
print("Successfully stored your new words into the dictionary.")

print("Now it´s time for training your vocabulary, translate the English words to Macedonian. If you are done training type in 'exit'")
counter2 = 1
while True:
    random_word = random.choice(list(Vocabulary_dict["English"]))
    random_word_index = Vocabulary_dict["English"].index(random_word)
    print(f"{counter2}. English: {random_word}")
    answer = str(input(f"{counter2}. Macedonian: ")).casefold()
    if answer == Vocabulary_dict["Macedonian"][random_word_index]:
        print("Correct!")
    elif answer == "exit":
        break
    else:
        print(f"Not correct, the answer is: {Vocabulary_dict['Macedonian'][random_word_index]}")
    counter2 += 1

print("Program successfully finished")

