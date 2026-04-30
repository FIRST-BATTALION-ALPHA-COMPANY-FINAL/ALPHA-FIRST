try:
    f = open("diary.txt", "x")
    f.write("Military Diary")
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
    print("[5] EXIT")

    option = input("ENTER OPTION: ")

    if option == "1":
        try:
            with open("diary.txt", "a") as file:
                file.write(input("ENTER YOUR DIARY: "))
                print("MISSION COMPLETE!")

        except FileNotFoundError:
            print("FILE NOT FOUND!")
            
    elif option == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.readlines()
                print("\n--- DIARY CONTENT ---")
                for line in content:
                    print(line.strip())
                
                print("--------------------")
                print(f"TOTAL LINES: {len(content)}")
        except FileNotFoundError:
            print("FILE NOT FOUND!")

    elif option == "3":
    wordSearch = input("ENTER WORD TO SEARCH: ")

        try:
            with open("diary.txt", "r") as file:
                lines = file.readlines()
    
            found = 0
    
            for line in lines:
                if word in line:
                    print("FOUND:", line.strip())
                    found = found + 1
    
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
            number = number + 1

        choice = int(input("ENTER NUMBER TO DELETE: "))

        if choice >= 1 and choice <= len(lines):
            del lines[choice - 1]

            with open("diary.txt", "w") as file:
                for line in lines:
                    file.write(line)

            print("ENTRY ELIMINATED!")
        else:
            print("INVALID NUMBER!")

    except FileNotFoundError:
        print("FILE NOT FOUND!")

    except ValueError:
        print("ENTER NUMBERS ONLY!")

    elif option == "5":
        print("DISMISSED!")
        break
