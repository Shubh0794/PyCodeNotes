### Objective : Introduction to List Comprehension and Generators and Generator Expressions ###


###############################################################
############  CREATING A FUNCTION TO GENERATE LIST OF NUMS ####
###############################################################

def GetListOfNums(max):
    nums_list = []
    for i in range(max):
        nums_list.append(i)
    return nums_list


nums_list_ = GetListOfNums(5)
print(" Printing List of nums ")
print(nums_list_)
###############################################################


###############################################################
############  CREATING A LIST COMPREHENSION ###################
###############################################################

## Using a List comprehension technique to generate a list of numbers.
## A single line format to populate a list.
## Use of square brackets is important []. If () are used, it becomes generator expresion.
##  Remember it like list is defined in [], so is list comprehension.

## Syntax for a list comprehension :
## <op_list> = [ <expression> for i in <iterable> < conditional_statements > < nested_looping> ]
## The expression is evaluated an appended to the list.
## < conditional statement : is evaluated and if its op is true, then only expr is evaluated.
## <nested looping> a chain of for loops can be added.

nums_list = [i for i in range(5)]
print(" Using List Comprehension ")
print(nums_list)

# The statement is a list comprehension and is equivalent to :
nums_list = []
for i in range(5):
    nums_list.append(i)
###############################################################


###############################################################
# Iterating over a list using a  for -loop vs list comprehension.
###############################################################

# 1.) using for -loop
for i in nums_list:
    print(i)
###  print (i) < Still prints 4

# 2.) using list comprehension
[print(i) for i in nums_list]


###  print (i) < error

# both work fine.
# list comprehension is used to write a 1-liner for loops as above.
# Bit the variable 'i' taken to iterate on both the cases has different lifetime
#	IN 1. 'i' is still valid after for-loop ends and is equal to its last value in loop. (here 4)
#	In 2. 'i' goes out of scope as soon as iteration in list comprehension ends.
###############################################################


###############################################################
############  CREATING A GENERATOR FUNCTION ###################
###############################################################

### Define a Generator Function which will generate numbers from 0 to max.
# Generators are functions with a 'yield' statement ( Return statement if encountered marks the end of the function)
def NumberGenerator(max):
    start = 0
    while (start <= max):
        yield start
        start += 1
    return


### Create a number generator object.
nums = NumberGenerator(5)
### Function execution will not start right now.
### It will start when a 'next()' function is called on generator_object. ( 'next' is automaticcally called by the for loop )
### Function execution pauses as it reaches yield statement and value after that is returned. When the 'next' is again called on generator object, execution continues from the line following yield statement. ( State of the  function like local vars etc. is preserved )
### This helps us avoid saving numbers in memory.

print(' Printing using Generator Function ')
for num in nums:
    print(num)
###############################################################

###############################################################
############  CREATING A GENERATOR EXPRESSION  ################
###############################################################

# A generator expression is a short way of creating a generator function ( as shown previosuly )

## Create a generator expression object.
## Now we can iterate on this object
nums_generator = (i for i in range(5))

print(" Printing using Generator expression object ")
for num in nums_generator:
    print(num)
###############################################################


########################################
############  CONCLUSION ###############
########################################

# List Comprehension is a short way to create a list.
# since a list is created, use this when you need to store elements in the memory.
# Iterating over an iterable  in a normal for loop : the iterating variable (generally 'i') still exists after the loop ends and value = last value in for loop.
# Iterating over an iterable  in a list comprehension : the varible 'i' has lifetime only of that line.
# Generator Expression is a short way to create generator function.
# An iterable object is created on which we can iterate. 
# Elements are not stored in memory.
########################################
########################################
