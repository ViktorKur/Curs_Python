from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base!\n")


def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
       match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                work = False
            case _:
                print("Try again!\n")


main_menu()