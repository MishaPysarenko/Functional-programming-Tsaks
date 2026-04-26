def validate_user(user):
    errors = []

    if not user.get("name"):
        errors.append("name is empty")

    if user.get("age", 0) < 18:
        errors.append("age < 18")

    if errors:
        return Error(errors)

    return Ok(user)