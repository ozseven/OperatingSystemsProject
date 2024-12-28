isAuthenticated = False


def authenticate(username, password):
    global isAuthenticated  # Global değişkeni kullanacağınızı belirtin
    if username == "admin" and password == "pass":
        isAuthenticated = True  # Global değişkeni değiştir
        print(isAuthenticated)
