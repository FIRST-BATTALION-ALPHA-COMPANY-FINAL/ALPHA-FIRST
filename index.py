try:
    f = open("diary.txt", "x")
    f.write("Military Diary\n")
    print("FILE CREATED!")
    f.close()
except FileExistsError:
    print("FILE ALREADY EXISTS!")

while True:
    print("--------------------")
    print("|  MILITARY DIARY  |")
    print("--------------------")
    print("[1] ADD DIARY")
    print("[2] VIEW DIARY")
    print("[3] SEARCH DIARY")
    print("[4] DELETE DIARY")
    print("[5] UPDATE DIARY")
    print("[6] EXIT")

    option = input("ENTER OPTION: ")

    if option == "1":
        with open("diary.txt", "a") as file:
            file.write(input("ENTER TITLE: ") + "\n")
            print("MISSION COMPLETE!")

    elif option == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.readlines()
                print("\n--- DIARY CONTENT ---")
                for line in content:
                    print(line.strip())
        except FileNotFoundError:
            print("FILE NOT FOUND!")

    elif option == "3":
        word = input("ENTER TITLE TO SEARCH: ")
        try:
            with open("diary.txt", "r") as file:
                lines = file.readlines()

            found = 0
            for line in lines:
                if word in line:
                    print("FOUND:", line.strip())
                    found += 1

            if found == 0:
                print("NO MATCH FOUND!")
        except FileNotFoundError:
            print("FILE NOT FOUND!")

    elif option == "4":
        try:
            with open("diary.txt", "r") as file:
                lines = file.readlines()

            print("\n--- DIARY CONTENT ---")
            number = 1
            for line in lines:
                print(number, "-", line.strip())
                number += 1

            choice = int(input("ENTER NUMBER TO DELETE: "))

            if 1 <= choice <= len(lines):
                del lines[choice - 1]

                with open("diary.txt", "w") as file:
                    file.writelines(lines)

                print("ENTRY ELIMINATED!")
            else:
                print("INVALID NUMBER!")
        except FileNotFoundError:
            print("FILE NOT FOUND!")
        except ValueError:
            print("ENTER NUMBERS ONLY!")

    elif option == "5":
        try:
            with open("diary.txt", "r") as file:
                lines = file.readlines()

            print("\n--- DIARY CONTENT ---")
            number = 1
            for line in lines:
                print(number, "-", line.strip())
                number += 1

            choice = int(input("ENTER NUMBER TO UPDATE: "))

            if 1 <= choice <= len(lines):
                new_diary = input("ENTER NEW DIARY: ")
                lines[choice - 1] = new_diary + "\n"

                with open("diary.txt", "w") as file:
                    file.writelines(lines)

                print("ENTRY UPDATED!")
            else:
                print("INVALID NUMBER!")
        except FileNotFoundError:
            print("FILE NOT FOUND!")
        except ValueError:
            print("ENTER NUMBERS ONLY!")

    elif option == "6":
        print("DISMISSED!")
        break

    else:
        print("INVALID CHOICE!")