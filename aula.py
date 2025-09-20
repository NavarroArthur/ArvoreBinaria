from arvore import ArvoreBinaria, Node

def postorder_exemplo():

    tree = ArvoreBinaria()

    n0=Node("R")
    n1=Node("A")
    n2=Node("R")
    n3=Node("T")
    n4=Node("H")
    n5=Node("U")

    n0.left=n2
    n0.right=n5
    n2.left=n1
    n5.left=n3
    n5.right=n4
    n1.left=None
    n3.left=None
    n4.left=None
    




    tree.root = n0

    return tree

if __name__ == "__main__":
    tree= postorder_exemplo()
    print("percurso em pós ordem:")
    tree.postorder()




