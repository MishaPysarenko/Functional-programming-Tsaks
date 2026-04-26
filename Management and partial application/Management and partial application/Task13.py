def format_message(prefix):
    def middle(suffix):
        def inner(text):
            return f"{prefix}{text}{suffix}"
        return inner
    return middle


html = format_message("<b>")("</b>")
md = format_message("**")("**")
brackets = format_message("(")(")")

print(html("Python"))
print(md("FP"))
print(brackets("Currying"))