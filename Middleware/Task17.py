def validate_name(func):
    def wrapper(data):
        if "name" not in data or not data["name"]:
            return "Invalid name"
        return func(data)
    return wrapper


@validate_name
def create_user(data):
    return f"User {data['name']} created"