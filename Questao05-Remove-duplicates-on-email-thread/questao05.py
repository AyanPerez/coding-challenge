# Question 05
# Remove duplicates on email thread

class Node:
	def __init__(self, mensagem):
		self.mensagem = mensagem
		self.next = None

	def listing(self):
		node = self
		while (node):
			print(node.mensagem)
			node = node.next


node_first = None
temp = None

print('Please, include the messages (type exit to quit):')

message = input("Message: ")
node_first = Node(message)
temp = node_first

while True:
	message = input("Message: ")
	if message=='exit':
		break
	node = Node(message)
	temp.next = node
	temp = node
	x =+ 1

# test priting linked list
print('The linked list of messages informed:')
node = node_first
node.listing()

node_reference = node_first
node_checking = node_first

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
				#print("node_previous", node_previous.mensagem)
				#print("node_checking", node_checking.mensagem)
		elif node_reference.mensagem==node_checking.mensagem:
			node_previous.next = None		
			node_checking = node_checking.next
			#print("d")
		elif node_reference.mensagem!=node_checking.mensagem:
			node_previous = node_checking
			node_checking = node_checking.next
			#print("f")
	node_checking = node_reference.next
	node_reference = node_reference.next
	#print("e")

print("The linked list after removing duplicated messages: ")


node = node_first
node.listing()
