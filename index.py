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


    elif option == "5":
        print("DISMISSED!")
        break
