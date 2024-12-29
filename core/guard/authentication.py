isAuthenticated = False


def authenticate(username, password):
    global isAuthenticated
    if username == "admin" and password == "pass":
        isAuthenticated = True
        print(isAuthenticated)
