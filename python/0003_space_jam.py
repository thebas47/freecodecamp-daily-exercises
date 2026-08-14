def space_jam(s):

    result = []

    for char in s.upper():
        if char != " ":
            result.append(char)


    return '  '.join(result)


print(space_jam("freeCodeCamp"))
print(space_jam("   free   Code   Camp   "))
print(space_jam("Hello World?!"))
print(space_jam("C@t$ & D0g$"))
print(space_jam("allyourbase"))
