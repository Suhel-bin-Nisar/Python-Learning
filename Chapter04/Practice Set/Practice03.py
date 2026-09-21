# Check that a tuple type cannot be changed in python.

a = (1, 2, 3 , 5, )

a[2] = 10  #This will give an error as tuple type is immutable and we cannot change any value in it.
