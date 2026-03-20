from Packages import username, password


def usname(un):
    if '_' in un:
        return un
    else:
        return "Invalid username"
print(usname(username.un))


def passd(passw):
    if len(passw) != 8:
        return "Password must be 8 characters"
    u = l = d = s = 0
    for ch in passw:
        if 'A' <= ch <= 'Z':
            u += 1
        elif 'a' <= ch <= 'z':
            l += 1
        elif '0' <= ch <= '9':
            d += 1
        else:
            s += 1

    if u == 2 and l == 2 and d == 2 and s == 2:
        return "Valid password"
    else:
        return "Invalid password"
print(passd(password.pwd))















            
