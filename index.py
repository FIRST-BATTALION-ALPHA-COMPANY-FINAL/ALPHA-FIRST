try:
    f = open("diary.txt", "x")
    f.write("Military Diary")
    f.close()
except FileExistsError:
    pass

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
        print("ENTER YOUR DIARY (type END to finish):")
        lines = []
        while True:
            text = input()
            if text.upper() == "END":
                break
            lines.append(text)

        with open("diary.txt", "a") as file:
            file.write("\n".join(lines) + "\n---\n")

        print("MISSION COMPLETE!")

    elif option == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.read()

            entries = content.split("---\n")

            print("\n--- DIARY CONTENT ---")
            for i, entry in enumerate(entries, 1):
                if entry.strip() != "":
                    print(f"\nENTRY {i}:")
                    print(entry.strip())

        except FileNotFoundError:
            print("FILE NOT FOUND!") 

    elif option == "3":
        word = input("ENTER WORD TO SEARCH: ").lower()

        try:
            with open("diary.txt", "r") as file:
                content = file.read()

            entries = content.split("---\n")

            found = 0
            for i, entry in enumerate(entries, 1):
                if word in entry.lower():
                    print(f"\nENTRY {i}:")
                    print(entry.strip())
                    found += 1

            if found == 0:
                print("NO MATCH FOUND!")

        except FileNotFoundError:
            print("FILE NOT FOUND!")


