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

In this directory there are two files of UUIDs:
   * `uuid.txt` contains 65,536 UUIDs
   * `uuid_test.txt` contains 16 UUIDs

`gen_uuid.py` will create more UUIDs. Its command line parameters are described in the comments at the top of the file.
