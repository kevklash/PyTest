# Python Basics
# Tips:
'''
Multiline comment
'''
# Print type: print(type(variable or value))


def basics():
    name = input("Enter your name:\n")
    print(f'Welcome {name}!')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def operar(valor):
    if float(valor)%2 == 0:
        print(f'El numero {valor} es par')
    else:
        print(f'El numero {valor} es impar')


def if_and_calling():
    valor = input("Proporcione un numero:\n")
    if valor.isnumeric():
        # Call a function
        operar(valor)
    else:
        print("El valor no es valido")


def arrays():
    my_array = ["A", "B", "C", "D"]  # List -- Array / Types {set} [list] (tuples)
    for i in range(0, my_array.__len__()):
        print(my_array[i])


# Creating a list in one line
def list_comprehension():
    even_numbers = [x for x in range(1, 101) if x % 2 == 0]
    print(even_numbers)


# Creating another list in one line
def list_comprehension2():
    words = ["que", "es", "lo", "que", "hay", "en", "el", "vaso"]
    new_list = [[w.upper(), w.lower(), len(w)] for w in words]
    print(new_list)


def listas():
    my_lista = ["Chanchito", "Oveja", "Cabra", "Vaca"]
    my_lista.insert(2, "Pollito") # Insertando "Pollito" en indice 2
    my_lista.append("Lorito Pepe") # Insertando al final de la lista
    my_lista = my_lista + ["Pato"] # Otra forma de agregar al final de la lista
    print(my_lista)


def print_table():
    number = input("Enter a number to print the table: \n")
    for i in range(1, 11):
        print(f'{number} * {i} = {i * int(number)}')


def rangos():
    # Creating a range from 1 to 10
    for number in range(1, 11):
        print(number)


def rangos2():
    # Creating a range from 1 to 10 but skipping a number
    for number in range(1, 11, 2):
        print(number)


def contar_letras():
    consonantes = 0
    vocales = 0
    for letter in "Supercalifragilisticoespiralidoso":
        if letter.lower() in "aeiou":
            vocales += 1
        elif letter == " ":
            pass
        else:
            consonantes += 1
    print(f'Total de vocales: {vocales}\n'
          f'total de consonantes: {consonantes}')


def estudiantes():
    students = {
        "male": ["Kevin", "Santiago", "Danery", "Juan", "Carlos", "Allan"],
        "female": ["Fatima", "Adriana", "Yanira", "Marcela", "Aida"]
    }
    # Printing names from male and female that contains letter a
    for key in students.keys():
        for name in students[key]:
            if "a" in name:
                print(name)


def rev(word):
    # This can also reverse other iterable objects like lists
    return word[::-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    list_comprehension2()
    word = input("Enter a word to reverse: ").strip().lower()
    print(f'The reversed version of the word: {rev(word)}')