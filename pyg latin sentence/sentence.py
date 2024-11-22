display = input("write any sentence: ")

if len(display) > 0 and all(char.isalpha() or char.isspace() for char in display):
    words = display.split()
    if len(words) > 1:

        new = words[0]
        output = ' '.join(words[1:]) + ' ' + new

    print(output)
else:
    print("wrong input")