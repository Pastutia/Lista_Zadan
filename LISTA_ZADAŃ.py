#Python 3.9 Lista Zadań

print("Witaj w programie zadaniowym")

tasks = []

user_chois = -1


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")


def delete_task():
    show_tasks()
    task_index = int(input("Podaj index zadania do usunięcia: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje")
        return

    tasks.pop(task_index)
    print("Usunięto zadanie!")
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    print("Zapisano zmiany")


def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    print("Zapisano zadanie")


def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return


load_tasks_from_file()

while user_chois != 5:

    if user_chois == 1:
        show_tasks()

    if user_chois == 2:
        add_task()

    if user_chois == 3:
        delete_task()

    if user_chois == 4:
        save_tasks_to_file()

    print()
    print("1.Pokaż zadania")
    print("2.Dodaj zadanie")
    print("3.Usuń zadanie")
    print("4.Zapisz zmiany do pliku")
    print("5.Wyjdź")

    user_chois = (int(input("Wybierz liczbę: ")))
