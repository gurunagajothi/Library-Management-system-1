class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"'{value}' pushed to stack.")
    def pop(self):
        if self.top is None:
            print("Stack is Empty!!!")
        else:
            temp = self.top
            print(f"Popped element: {temp.data}")
            self.top = self.top.next
            del temp
def display(self):
        if self.top is None:
            print("Stack is Empty!!!")
        else:
            temp = self.top
            print("Stack elements are:")
            while temp:
               	print(f"{temp.data} --> ", end="")
                temp = temp.next
            print("NULL")
# Main program with user input
def main():
    stack = Stack()
    while True:
        print("\nStack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            value = input("Enter the value to push onto the stack: ")
            stack.push(value)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()