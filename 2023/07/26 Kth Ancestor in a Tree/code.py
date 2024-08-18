def kthAncestor(root, k, node, ancestors = None):
    if not ancestors:
        ancestors = []
        
    if not root:
        return -1
    
    ancestors.append(root.data)
    if root.data == node:
        if k > len(ancestors):
            return -1
        return ancestors[-k]
    
    left = kthAncestor(root.left, k, node, ancestors)
    right = kthAncestor(root.right, k, node, ancestors)
    ancestors.pop()
    return max(left, right)
    