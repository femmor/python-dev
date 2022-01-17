# Draw a pine tree, after asking users for the row of the pine tree. How tall is the tree?

tree_height = int(input("How tall is your tree: "))
spaces = tree_height - 1
hashes = 1
stub_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stub_spaces):
    print(' ', end="")
print("#")




























