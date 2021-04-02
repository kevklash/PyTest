from random import choice

questions = ["Where are all the dinosaurs?: ", "What are we eating today?: ", "What do I want?: ",
             "What fairy tail will we read?: "]

question = choice(questions)
answer = input(question)

while answer != "just because".strip().lower():
    answer = input("Why?: ")

print("Alrighty!")