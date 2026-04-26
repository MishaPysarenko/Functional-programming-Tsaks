def log(level):
    def inner(message):
        return f"[{level}] {message}"
    return inner


info = log("INFO")
error = log("ERROR")

print(info("App started"))
print(error("Crash detected"))

# ФІНАЛЬНИЙ ВИСНОВОК
# Currying:
# розбиває функцію на ланцюг функцій
# кожна приймає 1 аргумент
# Partial application:
# фіксує частину аргументів
# повертає нову функцію
# Різниця:
# currying → структура функції змінюється
# partial → функція залишається, але параметри “заморожуються”