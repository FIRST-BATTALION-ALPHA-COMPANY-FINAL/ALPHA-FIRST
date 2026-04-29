try:
    f = open("diary.txt", "x")
    f.write("Military Diary")
    print("FILE CREATED!")
    f.close()
except FileExistsError:
    print("FILE ALREADY EXISTS!")