with open("module_4/names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)

new_name = "Luke"
with open("module_4/names.txt", 'a') as write_file:
    write_file.write(new_name)

with open("module_4/names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)

new_name = "Luke"
with open("module_4/new_names.txt", 'w') as write_file:
    write_file.write(new_name)

import logging
logging.basicConfig(level=logging.DEBUG)
logging.warning("warning!")
logging.debug("debug")