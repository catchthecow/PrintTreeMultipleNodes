

#_display_aux_multip(tree)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.kids = []

    def add_child(self, child):
        self.kids.append(child)


#class Tree:
#    def __init__(self):
#        self.root = None

#    def set_root(self, node):
#        self.root = node

#    def get_root(self):
#        return self.root

# Example usage:
def buildTree():
# Create nodes
    node1 = TreeNode(111)
    node2 = TreeNode(2222222222)
    node3 = TreeNode(33333)
    node4 = TreeNode(444444)
    node5 = TreeNode(5555555)
    node6 = TreeNode(66)
    node7 = TreeNode(7777777777)
    node8 = TreeNode(88888)
    node9 = TreeNode(999999999999999)
    node10 = TreeNode(1010101010)
    node11 = TreeNode(11)
    node12 = TreeNode(12121212121212)
    node13 = TreeNode(131313131313)
    node14 = TreeNode(141414)
    node15 = TreeNode(15151515)
    node16 = TreeNode(161616)
    node17 = TreeNode(171717)
    node18 = TreeNode(181818)
    node19 = TreeNode(19)
    node20 = TreeNode(20)
    node21 = TreeNode(2121212121212121212121)
    node22 = TreeNode(22222222)
    # Link nodes
    node1.add_child(node2)
    node1.add_child(node3)
    node1.add_child(node4)
    node1.add_child(node10)
    node1.add_child(node15)
    node2.add_child(node5)
    node3.add_child(node6)
    node3.add_child(node7)
    node5.add_child(node8)
    node4.add_child(node9)
    node10.add_child(node11)
    node10.add_child(node20)
    node11.add_child(node12)
    node11.add_child(node13)
    node11.add_child(node14)
    node17.add_child(node16)
    node6.add_child(node17)
    node6.add_child(node18)
    node6.add_child(node19)
    node17.add_child(node21)
    node7.add_child(node22)
    return node1


def restore_tree_from_json(json_data):
    if not json_data:
        return None
    
    node = TreeNode(json_data["name"])
    for child_data in json_data.get("children", []):
        child_node = restore_tree_from_json(child_data)
        node.add_child(child_node)
    
    return node


import json

def buildTree2(file):

    # Step 1: Open the JSON file
    with open(file, 'r') as file:
        # Step 2: Load JSON data
        json_data = json.load(file)

    # Step 3: Close the file (file is closed automatically due to the 'with' statement)

    # Now 'data' contains the parsed JSON content
    print(json_data)
    #tree_data = json.loads(json_data)
    # Restore the tree
    root = restore_tree_from_json(json_data)

    return root






if __name__ == "__main__":
    tree = buildTree2("tree.json")
    print(tree)