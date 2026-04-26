def log(level, message):
    return f"[{level}] {message}"

log_info = partial(log, "INFO")
log_warning = partial(log, "WARNING")
log_error = partial(log, "ERROR")

print(log_info("Application started"))
print(log_warning("Disk space is low"))
print(log_error("Cannot connect"))