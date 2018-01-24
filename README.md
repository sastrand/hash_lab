## NB Algorithms: Data Structures
### Lab II of II

For this lab
    * read a file of UUIDs into a new program
    * implement the following simple hash function:
        * for each character in the string representation of the UUID, find its Unicode integer representation. 
            * you may find the Python ord() function helpful for this
        * sum the integer values of each character in the UUID
        * return that sum modulo a constant of your choice
    * use a list to track the hashes you create and record the number of collisions
    * adjust the modulo value and find the lowest possible collision rate with this algorithm over this dataset

No matter what, this set of UUIDs will have a high collision rate with this algorithm. Expand the algorithm in some way to reduce the collision rate

Then compare the results with Python's built-in hash() function.

In this directory are two files of UUIDs:
    * `uuid.txt` contains 65,536 UUIDs
    * `uuid_test.txt` contains 16 UUIDs

These files should be sufficient for this lab, but you can use the `gen_uuid.py` script to generate more or different files. Its command line parameters are described in the comments at the top of the file.

