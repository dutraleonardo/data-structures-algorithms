import sys
from datetime import datetime

class Logger:
    def __init__(self, filename=None):
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"splay_tree_log_{timestamp}.txt"
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def close(self):
        self.log.close()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None
        self.logger = Logger()
        sys.stdout = self.logger

    def _build_tree_string(self, root, curr_index, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        node_repr = str(root.key)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root positions
        l_box, l_box_width, l_root_start, l_root_end = self._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = self._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root to the left sub-box
        # Pad with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root to the right sub-box
        # Pad with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches and root
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and root positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def print_tree(self):
        print("\nTree Structure:")
        print("-" * 50)
        if not self.root:
            print("Empty tree")
        else:
            tree_str, _, _, _ = self._build_tree_string(self.root, 0, False, '-')
            print('\n'.join([''] + tree_str + ['']))
        print("-" * 50)

    def right_rotate(self, y, search_key):
        print(f"zig({search_key})")
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        self.print_tree()
    
    def left_rotate(self, x, search_key):
        print(f"zag({search_key})")
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.print_tree()
    
    def splay(self, node, search_key):
        while node.parent:
            if not node.parent.parent:  # Zig or Zag
                if node == node.parent.left:
                    self.right_rotate(node.parent, search_key)
                else:
                    self.left_rotate(node.parent, search_key)
            else:
                parent = node.parent
                grand = parent.parent
                
                if parent.left == node and grand.left == parent:  # Zig-Zig
                    print(f"zig-zig({search_key})")
                    self.right_rotate(grand, search_key)
                    self.right_rotate(parent, search_key)
                elif parent.right == node and grand.right == parent:  # Zag-Zag
                    print(f"zag-zag({search_key})")
                    self.left_rotate(grand, search_key)
                    self.left_rotate(parent, search_key)
                elif parent.left == node and grand.right == parent:  # Zig-Zag
                    print(f"zig-zag({search_key})")
                    self.right_rotate(parent, search_key)
                    self.left_rotate(grand, search_key)
                else:  # Zag-Zig
                    print(f"zag-zig({search_key})")
                    self.left_rotate(parent, search_key)
                    self.right_rotate(grand, search_key)
    
    def insert(self, key):
        print(f"\nInserting {key}")
        new_node = Node(key)
        
        if not self.root:
            self.root = new_node
            self.print_tree()
            return
        
        current = self.root
        while True:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
            else:
                return
        
        self.print_tree()
    
    def search(self, key):
        print(f"\nSearching for {key}")
        if not self.root:
            print(f"Key {key} not found")
            return None
        
        node = self._find_node(self.root, key)
        if node:
            print(f"Key {key} found")
            self.splay(node, key)
        else:
            print(f"Key {key} not found")
        
        self.print_tree()
        return node
    
    def _find_node(self, root, key):
        current = root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    
    def _find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def delete(self, key):
        print(f"\nDeleting {key}")
        if not self.root:
            print(f"Key {key} not found")
            return
        
        self.root = self._delete_node(self.root, key)
        self.print_tree()
    
    def _delete_node(self, root, key):
        if not root:
            print(f"Key {key} not found")
            return None
        
        if key < root.key:
            root.left = self._delete_node(root.left, key)
            if root.left:
                root.left.parent = root
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
            if root.right:
                root.right.parent = root
        else:
            print(f"Key {key} deleted")
            if not root.left:
                temp = root.right
                if temp:
                    temp.parent = root.parent
                return temp
            elif not root.right:
                temp = root.left
                if temp:
                    temp.parent = root.parent
                return temp
            
            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_node(root.right, temp.key)
            if root.right:
                root.right.parent = root
        
        return root

    def close_log(self):
        """Close the log file properly"""
        self.logger.close()
        sys.stdout = sys.stdout.terminal  # Restore original stdout

from itertools import zip_longest

def main():
    tree = SplayTree()
    
    # Insert some values
    insertion_list = [81, 1, 7, 3, 58, 32, 21, 4, 94, 1, 81, 16]
    for value in insertion_list:
        tree.insert(value)
    
    # Search for some values
    search_list = [81, 1, 11, 14, 4, 9, 4, 1]
    for v in search_list:
      tree.search(v)

    # Delete some values
    deletion_list = [1, 32, 16, 3]
    for v in deletion_list:
      tree.delete(v)
    
    # Close the log file
    tree.close_log()

if __name__ == "__main__":
    main()
