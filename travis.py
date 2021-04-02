known_users = ["Kevin", "Fatima", "Diny", "Mateo", "Invitado", "Tester"]

while True:
    print("Hi! My name is travis, and I'm your security bot")
    name = input("Please type your name: " + '\n').strip().capitalize()
    if name in known_users:
        print("Hello {}, welcome back!".format(name))
        remove = input("Would you like to be removed from the list?(y/n)").strip().lower()
        if remove == "y":
            print("Former list: {}".format(known_users))
            known_users.remove(name)
            print("New list after changes: {}".format(known_users))
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Hmmm I don't think I've met you yet {}".format(name))
        add_me = input("Would you like to be added to the system? (y/n):").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "no":
            print("No worries, see you around!")