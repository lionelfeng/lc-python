# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]
        result = []
        while len(stack) != 0:
            cur = stack[-1]
            
            if cur.left and not cur.left in set(result):
            	cur = cur.left
            	stack.append(cur)
            else:
            	result.append(stack.pop())
            	if cur.right:
            		stack.append(cur.right)

        return map(lambda x: x.val, result)

def test1():
	t0 = TreeNode(0)
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t4 = TreeNode(4)
	t5 = TreeNode(5)

	t0.left = t1
	t1.left = t2
	t1.right = t3
	t3.right = t4
	t4.right = t5

	expected = [2, 1, 3, 4, 5, 0]
	actual = Solution().inorderTraversal(t0)
	print "PASSED" if (expected == actual) else "FAILED"

def test2():
	t0 = TreeNode(0)
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t4 = TreeNode(4)
	t5 = TreeNode(5)

	t0.left = t1
	t0.right = t5
	t1.left = t2
	t1.right = t3
	t3.right = t4
	

	expected = [2, 1, 3, 4, 0, 5]
	actual = Solution().inorderTraversal(t0)
	print "PASSED" if (expected == actual) else "FAILED"

def test3():
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	
	t1.right = t2
	t2.left = t3

	expected = [1,3,2]
	actual = Solution().inorderTraversal(t1)
	print "PASSED" if (expected == actual) else "FAILED"
        
if __name__ == "__main__":	
	test1()
	test2()
	test3()
    
        