# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        data = []
        queue_ref = deque([])
        queue_ref.append(root)
        while queue_ref:
            node_ref = queue_ref.popleft()
            if node_ref:	
                data.append(str(node_ref.val))
            else:
                data.append('None')
                continue
            if node_ref:
                queue_ref.append(node_ref.left)
                queue_ref.append(node_ref.right)
  
        return ','.join(data)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        q_data = deque(data.split(","))

        q_ref = deque([])
        data_val = q_data.popleft()
        node_ref = TreeNode(data_val)
        q_ref.append(node_ref) 
        while q_data:
            parent_node = q_ref.popleft()
            node_left_val = q_data.popleft()
            node_right_val = q_data.popleft()
            if node_left_val != 'None':
                node_left = TreeNode(node_left_val)
                parent_node.left = node_left
                q_ref.append(parent_node.left)
            else:	
                parent_node.left = None
            if node_right_val != 'None':
                node_right = TreeNode(node_right_val)
                parent_node.right = node_right
                q_ref.append(parent_node.right)
            else:	
                parent_node.right = None

	return node_ref






#['1','2','3','None','None','4','5']



	
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))