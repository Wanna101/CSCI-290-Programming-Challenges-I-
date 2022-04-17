import math
import pprint

# P = percentage
# V = volume
# SP = superpower
# PN = parent node
# N = node

tree = {}
tree[1] = [0, 0, 0, 0]
# pp = pprint.PrettyPrinter(indent=4)

def calculateNodeVolume(node):
	V = tree[node][1]
	while True:
		if node == 1:
			break		
		P, IGNORE_V, SP, PN = tree[node]
		if SP == 1:
			V = math.sqrt(V)
		V = V / (P / 100.0)
		node = PN
	return V

def main():
	# reading in tree
	number = int(input()) - 1
	for i in range(number):
		line = input()
		PN, N, P, SP = line.split(" ")
		tree[int(N)] = [int(P), 0, int(SP), int(PN)]
	volumes = input()
	for i, V in enumerate(volumes.split(" "), 1):
		tree[i][1] = int(V)
	maxV = -1
	for i, V in enumerate(volumes.split(" "), 1):
		V = int(V)
		if V > 0:
			# print(i, V)
			maxV = max(calculateNodeVolume(i), maxV)
			print()
	print(maxV)
main()