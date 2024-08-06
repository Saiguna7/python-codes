# Read the number of elements in the set and the set itself
n = int(input())
s = set(map(int, input().split()))

# Read the number of commands
num_commands = int(input())

# Process the commands
for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        element = int(command[1])
        s.remove(element)
    elif command[0] == 'discard':
        element = int(command[1])
        s.discard(element)

# Calculate and print the sum of the elements in the set
print(sum(s))
