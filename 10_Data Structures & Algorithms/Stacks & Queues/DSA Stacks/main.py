"Stack adalah struktur data yang dapat menampung banyak elemen"

stack = []

# Push
stack.append('A')
stack.append('b')
stack.append('C')

# Pop
element = stack.pop()
print("Pop:", element)

# Peek
topElement = stack[-1]
print("Peek:", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpety:", isEmpty)

# Size
print("Size", len(stack))