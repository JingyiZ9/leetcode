class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if root == None:
            return []
        
        queue = [root]
        list_val =[]
        result = []
        
        #use the queue to search every depth
        #pop the node and push node.left and node.right in the queue
        while queue:
            for node in queue:
                list_val.append(node.val)
            result.append(list_val)
            list_val = []
                
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    pass
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result[::-1]
                        
