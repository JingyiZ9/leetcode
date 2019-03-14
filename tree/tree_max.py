def maxvalue(root):
    max = root.val
    if root.left.val > max:
        max = root.left.val
        maxvalue(root.left)
    if root.right.val > max:
        max = root.right.val
        maxvalue(root.right)


