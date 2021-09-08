import stack
# The stacks are particularly good at reversing things!
# first stacks is the module and second is the class
s = stack.Stack()

string = "This is the first question to solve using stakc. The objective is to reverse this string."
reversed_string = ""

for i in string:
    s.push(i)

while not(s.is_empty()):
    reversed_string = reversed_string + s.pop()

# Here is the reversed string
print("the reversed string is: ")
print(reversed_string)




