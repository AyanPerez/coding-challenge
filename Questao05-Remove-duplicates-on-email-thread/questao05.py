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

	def removing_duplicated(self):
		node_reference = self
		node_checking = self

		while node_reference:
			while node_checking:
				if node_checking.next:
					if node_reference.mensagem == node_checking.next.mensagem:
						if node_checking.next.next:
							node_previous = node_checking
							node_checking.next = node_checking.next.next
						else:
							node_checking.next = None
					else:
						node_previous = node_checking
						node_checking = node_checking.next
				elif node_reference.mensagem==node_checking.mensagem:
					node_previous.next = None		
					node_checking = node_checking.next
				elif node_reference.mensagem!=node_checking.mensagem:
					node_previous = node_checking
					node_checking = node_checking.next
			node_checking = node_reference.next
			node_reference = node_reference.next


node_first = None
temp = None

# Input of messages - linked list
print('Please, include the messages (type "0" to quit):')

message = input("Message: ")
node_first = Node(message)
temp = node_first

while True:
	message = input("Message: ")
	if message=='0':
		break
	node = Node(message)
	temp.next = node
	temp = node
	x =+ 1

# Priting linked list informed
print('The linked list of messages informed:')
node = node_first
node.listing()

# Removing duplicated messages
node.removing_duplicated()

# Priting linked list changed by removing duplicated nodes
print("The linked list after removing duplicated messages: ")
node = node_first
node.listing()
