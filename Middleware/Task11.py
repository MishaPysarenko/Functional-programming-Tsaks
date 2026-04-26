def require_auth(func):
    def wrapper(user):
        if not user.get("authenticated"):
            return "Access denied"
        return func(user)
    return wrapper


@require_auth
def dashboard(user):
    return f"Welcome, {user['name']}"