# FILEPATH = r'./files/todos.txt'
FILEPATH = r'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Write a to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

print('Hello from functions')
# print(x)

# """
print(__name__)
if __name__ == '__main__':
     print('Hello from functions - standalone')
     print(get_todos())
# """