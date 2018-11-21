def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<i>" + wynik + "<\\i>"
    return wrapper

@bold
@italic
def nasza_funkcja():
    return "jakiś napis"



print(nasza_funkcja())
