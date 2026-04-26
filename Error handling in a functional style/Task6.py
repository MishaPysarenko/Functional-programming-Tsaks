result = (
    safe_divide(10, 2)
    .map(lambda x: x * 2)
    .map(lambda x: x + 5)
)

print(result.value if isinstance(result, Some) else "Nothing")