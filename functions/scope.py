scope = 3


def callMe():
    scope = 2
    print("Local scope value is " + str(scope))


callMe()
print("Global scope value is " + str(scope))
