"In-order Traversal adalah jenis Penelusuran Mendalam Pertama, di mana setiap simpul dikunjungi dalam urutan tertentu"

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)