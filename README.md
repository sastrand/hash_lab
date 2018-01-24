## NB Algorithms: Data Structures
### Lab II of II

In this lab:
   * read a file of UUIDs into a new program
   * implement the following simple hash function:
       * for each character in the string representation of a given UUID, find its Unicode integer representation (Python provides a built-in function for char to int conversion.)
       * sum the integer values of each character in the UUID
       * return that sum modulo a constant of your choice
   * track the unique hashes you create and record the number of collisions
   * adjust the modulo value and see if you can change the collision rate

The sets of UUIDs in this repo are not entirely random. There will be hash value collisions with the algorithm implemented exactly as above. Modify and expand on the algorithm to reduce this collision rate. In particular, consider how values that are anagrams of one another would hash.

Then compare the results with those of Python's built-in `hash()` function.

In this directory there are two files of UUIDs:
   * `uuid.txt` contains 65,536 UUIDs
   * `uuid_test.txt` contains 16 UUIDs

These files should be sufficient for this lab, but you can use the `gen_uuid.py` script to generate more or different files. Its command line parameters are described in the comments at the top of the file.
