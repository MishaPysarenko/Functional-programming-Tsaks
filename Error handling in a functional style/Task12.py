user = {"age": "25"}

def parse_age(user):
    try:
        return Ok(int(user["age"]))
    except:
        return Error("invalid age")


def check_age(age):
    return Ok(age) if age > 18 else Error("too young")


result = parse_age(user).flat_map(check_age)