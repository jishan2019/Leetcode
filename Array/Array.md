# Arrays

After completing this post, you will be able to:
* Create arrays
* Perform various operations on arrays
* Determine the time and space complexities of array operations
* Describe how costs and benefits of array operations depend on how arrays are 
represented in computer memory
-----------------------------

An array contains items that can be replaced or accessed using the index. 
A Python list is an array. 

__Alert__: the length ir capacity of an array is fixed when it is created, 
which means that we cannot add new or remove old items of the array or make 
the array larger or smaller.

```python
class Array(object):
    """Represents an array."""
    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array. fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)
    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)
    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
```
## A Basic Array Operations
* Insert 
* Delete
* Search

### Array Insertions
* Inserting a new element at the end of the array
* Inserting a new element at the beginning of the array
* Inserting a new element at any given index inside the array

#### Inserting at the Start of an Array
To insert an element at the beginning of an array, we'll need to shift all other 
elements in the array to the right by one index to create space for the new element.
This is very costly operation, since each of the existing elements has to be shifted
one step to the right. The need to shift everything implies that this is not a 
constant time operation. In fact, the time taken for insertion at the beginning of
an array will be proportional to the length of the array. The time complexity is 
O(N), where N is the length of the array.


#### Deleting items from an array

Deletion at the end of an array is similar to people standing in a line,
also known as a queue. The person who most recently joined the queue can 
leave at any time without disturbing the rest of the queue. Deleting from
the end of an array is the least time consuming of the three cases.


### Search Items From an Array

The edge cases for searching in an array:
1. the item may not exist in the array
2. the input array is null, which means it doesn't contain any elements

Check for edge cases. Is the array null or empty?
If it is, then we return false because the element we're
searching for couldn't possibly be in it.



