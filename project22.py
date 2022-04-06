def edit_file(filename):
    total = 0
    with open(filename, "r") as filestream:
        with open('answers.txt', "w") as filestream2:
            for line in filestream:
                current_line = line.split(',')
                sorted_line = sorted(current_line)
                for i, name in enumerate(sorted_line):
                    i = i+1
                    score = 0
                    for character in name[1:-1]:
                        val = ord(character.lower()) - 96
                        score += val
                    result = score * i
                    print(f'The result for {name} in the dict is {result}')
                    total += result
                    filestream2.write(str(score))
    print(total)

print(edit_file('p022_names.txt'))
