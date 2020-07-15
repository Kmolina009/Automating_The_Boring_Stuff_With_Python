#Is it raining
    # if true
        # Do you have an umbrella
            # no -> wait a while
                # is it raining?(if yes, loop till not raining)
            # yet -> go outside
    # else "Go Outside"
#Needs user inputs of yes,no
# based on yes = true and  no = false

yes = True
no = False

while yes:
    input("Is it raining?yes or no")
    if yes:  
        input("Do you have an umbrella?")
        if no:
            print("Wait awhile")
        elif yes:
            print("Go outside")
            break
    elif no:
        print("Go outside")
    else:
        pass
