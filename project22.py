def edit_file(filename):
    with open(filename, "r") as filestream:
        with open('answers.txt', "w") as filestream2:
            for line in filestream:
                current_line = line.split(',')
                sorted_line = sorted(current_line)
                for name in sorted_line:
                    filestream2.write(name)

print(edit_file('p022_names.txt'))
