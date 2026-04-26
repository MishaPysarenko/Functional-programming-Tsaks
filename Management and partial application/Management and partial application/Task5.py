def volume_curried(length):
    def second(width):
        def third(height):
            return length * width * height
        return third
    return second


print(volume_curried(2)(3)(4))

box_base = volume_curried(2)(5)
print(box_base(10))
print(box_base(20))