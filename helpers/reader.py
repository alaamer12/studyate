
def block_reader(file_path):
    blocks = {}
    with open(file_path, 'r') as file:
        current_note = None
        current_block = ""
        for line in file:
            line = line.rstrip('\n')
            if not line.strip() or line.strip().startswith('//'):  # Skip empty lines or comments
                continue
            indent_level = len(line) - len(line.lstrip())
            note_name = line.strip()
            if indent_level == 0:
                if current_note is not None:
                    blocks[current_note] = current_block
                current_note = note_name
                current_block = ""
            else:
                current_block += line + "\n"
        if current_note is not None:
            blocks[current_note] = current_block
    return blocks


if __name__ == '__main__':
    # Example usage
    file_path = 'x.txt'  # Path to your file
    tasks_dict = block_reader(file_path)
    print(tasks_dict)
