def message(prefix):
    def inner(name):
        return f"{prefix}: {name}"
    return inner


error_message = message("ERROR")
warning_message = message("WARNING")
info_message = message("INFO")

print(error_message("File not found"))
print(warning_message("Low memory"))
print(info_message("Process started"))