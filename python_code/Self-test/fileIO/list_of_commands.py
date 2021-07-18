arr = []
f = open('list_commands').read()
commands = f.split("\n")
# commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']
#
#
for i in commands:
    command = i.split(" ")
    print(f"----------------\n{command}")
    if len(command) == 3:
        cmd = command[0]
        index = command[1]
        integer = command[2]
        if cmd == "insert":
            arr.insert(int(index), int(integer))
    elif len(command) == 2:
        cmd = command[0]
        integer = command[1]
        if cmd == "append":
            arr.append(int(integer))
        elif cmd == "remove":
            arr.remove(int(integer))
    elif len(command) == 1:
        cmd = command[0]
        if cmd == "print":
            print(arr)
        elif cmd == "sort":
            arr = sorted(arr)
        elif cmd == "reverse":
            arr = sorted(arr, reverse=True)
        elif cmd == "pop":
            arr.pop()
    print(f"arr: {arr}\n---------------------")