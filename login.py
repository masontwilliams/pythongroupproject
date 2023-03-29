def login(id, s_list):

    userPin = input("Please enter your student PIN number: ")
    for i in s_list:
        if (id, userPin) == i:
            return True
        else:
            print("This PIN is not registered with a student ID in our student list")
            return False
