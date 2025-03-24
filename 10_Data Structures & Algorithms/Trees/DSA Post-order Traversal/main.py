"Post-order Traversal adalah jenis Depth First Search, di mana setiap node dikunjungi dalam urutan tertentu"

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")