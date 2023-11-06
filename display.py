from build_tree import buildTree
from build_tree import buildTree2

def display(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % self.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _display_aux(self.left)
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _display_aux(self.right)
        s = '%s' % self.val
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(self.left)
    right, m, q, y = _display_aux(self.right)
    s = '%s' % self.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2
#display(root)
#from binarytree import Node
#root = Node(1)
#root.left = Node(256)
#root.right = Node(3555555555)
#root.left.right = Node(42)
#root.right.left = Node(888)
#print(root)

#display(root)


def find_first_and_last_non_empty_space_indices(input_string):
    first_index = input_string.find('|')
    last_index = input_string.rfind('|')
    return first_index, last_index


def find_first_and_last_non_empty_space_indices2(input_string):
    first_non_empty_space = -1
    last_non_empty_space = -1

    for i, char in enumerate(input_string):
        if char != ' ':
            if first_non_empty_space == -1:
                first_non_empty_space = i
            last_non_empty_space = i

    return first_non_empty_space, last_non_empty_space

max_right_loc = []

def _display_aux_multip(root, start_loc):
    """Returns list of strings, width, height, and horizontal coordinate of the root. the """
    # No child.
    if root.kids == []:
        line = '%s' % root.value
        width = len(line)
        height = 1
        #middle = width // 2
        left = start_loc
        right = width + start_loc
        mid = int((left+right)/2)
        #left = right
 
        return [line], height, left, right,  mid
    else:
        lines_3 = []
        root_height = 0
        line_2 = ""
        # this is for record the leftest word length
        word_l = 0
        word_r = 0
        for index, kid in enumerate(root.kids):
            lines, height, left, right, mid = _display_aux_multip(kid, start_loc)
            #mid = int((left+right)/2)
            #This is to give an empty space between two nodes
            start_loc = right + 1 
            if index == 0:
                root_l = left
                word_l = right - left
            if index == len(root.kids)-1:
                root_r = right
                word_r = right - left
            # This is to find the highest path
            if root_height < height:
                root_height = height
            if index != 0:
                lines_3 = [item + ' ' for item in lines_3]
                
                #for lines2 in line_2:
                line_2 = line_2 + " "
            
            max_length = max(len(lines_3), len(lines))
            if len(lines_3) < len(lines):
                # Pad the shorter list with empty strings
                lines_3 += [''] * (max_length - len(lines_3))
                lines_3 = [s.ljust(len(lines_3[0])) for s in lines_3]
            elif len(lines_3) > len(lines):
                lines += [''] * (max_length - len(lines))
                lines = [s.ljust(len(lines[0])) for s in lines]
            
            c = []
            for row_a, row_b in zip(lines_3, lines):

                # Append the combined row to the list c
                c.append(row_a+row_b)
            if c == []:
                lines_3=lines
            else:
                lines_3 = c
            
            line_2 = line_2 + " " * (mid-left) + "|" + " " *(right-mid-1)

        line = '%s' % root.value
        width = len(line) 
        # This is the case that the node is longer than the root 
        if root.value == "CCOPT_INST__cdb_inv_03181/I":
            adebug = 1
        
        if width < root_r - root_l:
            
            number_left = int((root_r-root_l + 1 - width)/2)
            number_right = root_r - root_l + 1 - number_left - width

            #number_empty_left = int(word_l/2)    
            #number_empty_right = word_r - int(word_r/2)

            loc_line_left, loc_line_right = find_first_and_last_non_empty_space_indices(line_2)
            number_empty_left = loc_line_left + 1
            number_empty_right = len(line_2) - loc_line_right

            # of its root or itself 
            if len(root.kids) > 1:
                # Method1: this is one way to generate the line_1: based on the rightest and leftest location

                # Method2: Another way of generating the line_1 is based on the location of "|" in line_2
                # loc_l is the start point of the bar in a node form. including
                # loc_r is the end point of the bar in a node form, excluding 
                loc_l = number_empty_left
                loc_r = root_r - root_l - number_empty_right 
                loc_r = root_r - root_l - number_empty_right 
                number_horizontal_bar_left = int((loc_r-loc_l - width)/2)
                number_horizontal_bar_right = loc_r - loc_l - width - number_horizontal_bar_left
                line_1 = number_empty_left*" " + "-"*number_horizontal_bar_left + line + "-"*number_horizontal_bar_right + " "*number_empty_right


               
            else:
                number_empty_left =  loc_line_left - int(width/2)
                number_empty_right = root_r - root_l - number_empty_left - width
                
                line_1 = " "*number_empty_left + line + " "*number_empty_right
                #line_1 = " "*number_left + line + " "*number_right
            
            # Method2: Another way of generating the line_1 is based on the location of "|" in line_2
            
        # This is the case that the root is longer than the node
        else:
            number_left = int((width - (root_r-root_l))/2)
            number_right = width - (root_r - root_l) - number_left
            if number_left != 0 or number_right != 0:
                lines_3 = [' '*number_left + item + ' '*number_right for item in lines_3]
            
            line_1 = line
            line_2 = ' '*number_left + line_2 + ' '*number_right
            root_r = root_l + width
        

        if root.value == 1010101010:
            adebug = 1
        
        l, r = find_first_and_last_non_empty_space_indices2(line_1)
        mid = int((l+r)/2)
        mid_intree = root_l + mid
        #mid = int( (root_l + int(word_l/2) + root_r -int(word_r/2))/2)  
        return [line_1, line_2]+ lines_3, root_height+1, root_l, root_r, mid_intree



#lines = []
#queue = []
def build_tree_bfs(root):
        q = []
        q.append(root)
        i = 0
        j = 1
        while i<j:
            root = q[i]
            for kid in root.kids:
                q.append(kid)
                j = j+1
            i = i+1
            
        return q

            


##################### main function starts here #############################

import argparse
parser = argparse.ArgumentParser(description='Horizontaly-Print-Multi-tree', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--TreeForm',  default='function',  type=str,   help='[function,json]')
args = parser.parse_args()

if args.TreeForm == 'function':
    root_node = buildTree()
elif args.TreeForm == 'json':
    root_node = buildTree2("tree.json")

print('End of building tree successful')
queue = build_tree_bfs(root_node)
build_tree_bfs(root_node)
lines, height, left, right, mid = _display_aux_multip(root_node, 0)
#print("lines", lines)
for line in lines:
    # Step 2: Write content to the file
   print(line)
print('End of printing tree successful')

with open('output2.txt', 'w') as file:
    # Step 2: Write content to the file
    file.write('This is the first line.\n')
    for line in lines:
        file.write(line+"\n")
        #file.write("\n")
    file.write('End of printing tree successful')