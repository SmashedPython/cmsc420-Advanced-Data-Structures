import bst

root = bst.insert(None, 2,1)
bst.insert(root, 3,1)
bst.insert(root, 1,1)
bst.insert(root, 4,1)
print(root.key)
print(root.leftchild.key)
print(root.rightchild.key)
print(root.rightchild.rightchild.key)
print("-----------------")
root = bst.restructure(root)
print(root.key)
print(root.leftchild.key)
print(root.rightchild.key)
print(root.rightchild.rightchild.key)

