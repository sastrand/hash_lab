## Part I: Build a hash function with comprehensions

In this part:
   * read a file of UUIDs into a new program
   * implement the following simple hash function:
       * for each character in the string representation of a given UUID, find its Unicode integer representation (Python provides a built-in function for char to int conversion.)
       * sum the integer values of each character in the UUID
   * apply this function to every UUID in `uuid.txt` and determine its collision rate.

Improve this hash function, aiming for a collision rate below 1%. In particular, consider how values that are anagrams of one another will hash.

Then compare the results with those of Python's built-in `hash()` function.

**For practice in this lab, use comprehensions instead of for loops.**

<hr>

## Part II: Build a dictionary (hash map) class that uses your hash function

In this part:
   * Create a class named something like `Hash_Map` that will support a 1024-element associative array, called `assoc_array` and has a constructor that fills all 1024 spaces with independent empty lists.
   * Include your hash function from part I as a method or instead use the Python's built-in `hash()` function when you need to hash.
   * Write an `add` method that:
        * will take a key and a value (aka "kv"), hash the key, and mod the hash by 1024. This value is the index in `assoc_array` where the kv pair will be stored.
        * store the kv pair as a tuple in the list at this position in `assoc_array`. If there's already a kv pair in the list, this is a collision. In the event of a collision, add the new kv pair to the list just the same.
   * Write an `in` function that takes a key and checks if the corresponding kv pair is in the dictionary.

<hr>

In this directory there are two files of UUIDs:
   * `uuid.txt` contains 65,536 UUIDs
   * `uuid_test.txt` contains 16 UUIDs

`gen_uuid.py` will create more UUIDs. Its command line parameters are described in the comments at the top of the file.
