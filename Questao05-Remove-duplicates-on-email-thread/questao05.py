# Question 05
# Remove duplicates on email thread

class Node:
	def __init__(self, mensagem):
		self.mensagem = mensagem
		self.next = None


node1 = Node("B")
node2 = Node("B")
node3 = Node("B")
node4 = Node("B")

node1.next = node2
node2.next = node3
node3.next = node4

# test priting linked list

node = node1
while (node):
	print(node.mensagem)
	node = node.next


# test removing duplicated node
'''

while (node):
	print(node.mensagem)
	if node.next:
		if node.mensagem==node.next.mensagem:
			if node.next.next:
				node.next=node.next.next
			else:
				node.next=None
	node = node.next

# test priting linked list after the change
'''
node_reference = node1
node_checking = node1

while node_reference:
	while node_checking:
		if node_checking.next:
			if node_reference.mensagem == node_checking.next.mensagem:
				if node_checking.next.next:
					node_previous = node_checking
					node_checking.next = node_checking.next.next
					#print("a")
				else:
					node_checking.next = None
					#print("b")
			else:
				node_previous = node_checking
				node_checking = node_checking.next
				#print("c")
		elif node_reference.mensagem==node_checking.mensagem:
			node_previous.next = None		
			node_checking = node_checking.next
			#print("d")
	node_checking = node_reference.next
	node_reference = node_reference.next
	#print("e")

print("XXXXXXXXXXXXXXXXXXXXXX  linked list after the change")


node = node1
while (node):
	print(node.mensagem)
	node = node.next