def findSpiral(root):
    traversal = []
    cur_level = [root]
    direction = -1
    
    while cur_level:
        traversal += [node.data for node in cur_level[::direction]]
        direction *= -1
        
        next_level = []
        for node in cur_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        cur_level = next_level
        
    return traversal
    