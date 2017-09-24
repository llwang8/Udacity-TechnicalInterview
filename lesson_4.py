# Udacity Data Analyst Nanodegree

# Technical Interview

# Lesson 4. Maps and Hashing

# Quiz: python Dictionaries
"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] =  ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}
print 1
for c in sorted(locations['North America']['USA']):
    #print 'American {}'.format(c)
    print c
print 2
countries_cities = []
for country, cities in locations['Asia'].iteritems():
    for e in cities:
        countries_cities.append((country, e))

countries_cities.sort( key=lambda x: x[1])
#print countries_cities
for e in countries_cities:
    print '{} - {}'.format(e[1], e[0])


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""



# Quiz: String Keys Practice
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        self.table.append(string)

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        if string in self.table:
            return self.calculate_hash_value(string)
        else:
            return -1




# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')


# Quiz: Binary Tree Practice
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        #if self.root:
            #print self.root.value
            #print_tree(self.root.left)
            #print_tree(self.root.right)
        print self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False


    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal += str(start.value ) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()



