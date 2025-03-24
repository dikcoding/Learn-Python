"Pre-order Traversal adalah jenis Depth First Search, di mana setiap node dikunjungi dalam urutan tertentu"

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)