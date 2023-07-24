class Solution:
    def rightView(self, root, view = None, level = 0):
        if not view:
            view = []
        if not root:
            return view
        if level >= len(view):
            view.append(root.data)
        self.rightView(root.right, view, level + 1)
        self.rightView(root.left, view, level + 1)
        return view