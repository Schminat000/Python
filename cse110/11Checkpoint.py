with open("books.txt") as bom_file:
    for line in bom_file:
        clean_line = line.strip()
        print(clean_line)