class Node():

    def __init__(s,data):
        s.left=None
        s.right=None
        s.data=data

    def insert(s,data):

        if s.data:
            if s.data<data:
                if s.right is None:
                    s.right=Node(data)
                else:
                    s.right.insert(data)
            else:
                if s.left is None:
                    s.left=Node(data)
                else:
                    s.left.insert(data)
        else:
            s.data=data

    def print_Tree(s):
        if s.left:
            s.left.print_Tree()
        print(s.data,end=" ")

        if s.right:
            s.right.print_Tree()

    def search(s,data):
        if s.data==data:
            print("found")
        elif s.data>data and s.left:
            s.left.search(data)
        elif s.data<data and s.right:
            s.right.search(data)
        else:
            print("not found")
            
            
        
            









            
            
