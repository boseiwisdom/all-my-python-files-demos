with open("int.txt","r") as file:
    # q=file.readline()
    # print(q)
    # for i in file:
        # print(i)
    with open("information.txt","a") as k:
        for i in file:
            k.write(i)