def is_valid(username, password):
    # Write code here
    if (username == "user" and password == "qweasd"):
        return True
    elif(username == "admin"):
        return True
    else:
        return False
