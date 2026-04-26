def read_file(name):
    if name == "missing.txt":
        return Error("file not found")
    return Ok("file content")