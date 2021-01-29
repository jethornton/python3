Python 3
========

Builtin Types
-------------

In this section I have included information on the more basic builtin types. For information on more specialized builtin types, check out the [Python documentation](https://docs.python.org/3/library/stdtypes.html)

Boolean Types
.............

::

	class 'bool'


By default, an object is considered True unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero. Here are most of the builtin objects considered False:
 constants defined to be false: None and False
 zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
 empty sequences and collections: '', (), [], {}, set(), range(0)

Numeric Types
.............

::
	
	class 'int'
	class 'float'
	class 'complex'


Integers have unlimited precision. Floating point numbers are usually implemented using double in C, and are therefore systemdependent. Complex numbers have a real and imaginary part, which can be accessed using z.real and z.imag, respectively. Complex numbers must include j appended to a numeric literal (0j is acceptable for when you want a complex value with no imaginary part).

The standard libarary includes additional numeric types, [Fraction](https://docs.python.org/3/library/fractions.html#modulefractions)s which hold rationals, and [Decimal](https://docs.python.org/3/library/decimal.html#moduledecimal)s which hold floatingpoint numbers with userdefinable precision.

Sequence Types
..............

Immutable sequences have support for the hash() builtin, while mutable sequences do not. This means that immutable sequences can be used as dict keys or stored in set and frozenset instances, while mutable sequences cannot.

Mutable Sequences
"""""""""""""""""

::

	class 'list'
	class 'bytearray


bytearray objects are a mutable counterpart to bytes objects.

Immutable Sequences
""""""""""""""""""""

::

	class 'tuple'
	class 'range'
	class 'str'
	class 'bytes'


bytes objects are sequences of single bytes. The syntax for bytes literals is largely the same as that for string literals, except that a b prefix is added:	
 Single quotes: b'still allows embedded "double" quotes'
 Double quotes: b"still allows embedded 'single' quotes"
 Triple quotes: b'''3 single quotes''', b"""3 double quotes"""

Only ASCII chars are permitted in bytes literals.	
bytes objects actually behave like immutable sequences of integers, with each value restricted to 0 <= x < 256.

bytes objects can be created in several ways:
 A zerofilled bytes object of a specific length: bytes(10)
 From an iterable of integers: bytes(range(20))
 Copying existing binary data via the buffer protocol: bytes(obj)

Set Types
.........

::

	class 'set'
	class 'frozenset'


set is mutable, while frozenset is immutable.	
Note that since frozenset is immutable, it must be entirely populated at the moment of construction. It cannot use the literal curly brace syntax that ordinary set uses, as that syntax is reserved for set.

Instead, use frozenset([iterable]).

Mapping Types
.............

::

	class 'dict'

Statements
----------

assert
......

Assert statements are a convenient way to insert debugging assertions into a program:
::

	assert expression ["," expression]

Example:
::

	import sys
	try:
		assert sys.version_info >= (3, 6)
	except AssertionError:
		print('Python Verions must be 3.6 or newer')

pass
....

pass is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed, for example:
::

	def f(arg): pass    # a function that does nothing (yet)

	class C: pass       # a class with no methods (yet)

return
......

return may only occur syntactically nested in a function definition, not within a nested class definition.

If an expression list is present, it is evaluated, else None is substituted.

return leaves the current function call with the expression list (or None) as return value.

When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function.

In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the StopIteration.value attribute.

In an asynchronous generator function, an empty return statement indicates that the asynchronous generator is done and will cause StopAsyncIteration to be raised. A non-empty return statement is a syntax error in an asynchronous generator function.

break
.....

break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.

It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.

If a for loop is terminated by break, the loop control target keeps its current value.

When break passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the loop.

continue
........

continue may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop. It continues with the next cycle of the nearest enclosing loop.

When continue passes control out of a try statement with a finally clause, that finally clause is executed before really starting the next loop cycle.

import
......

The basic import statement (no from clause) is executed in two steps:

#. find a module, loading and initializing it if necessary

#. define a name or names in the local namespace for the scope where the import statement occurs.

When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for each clause, just as though the clauses had been separated out into individual import statements.

The details of the first step, finding and loading modules are described in greater detail in the section on the import system, which also describes the various types of packages and modules that can be imported, as well as all the hooks that can be used to customize the import system. Note that failures in this step may indicate either that the module could not be located, or that an error occurred while initializing the module, which includes execution of the module’s code.

If the requested module is retrieved successfully, it will be made available in the local namespace in one of three ways:

* If the module name is followed by as, then the name following as is
  bound directly to the imported module.

* If no other name is specified, and the module being imported is a top
  level module, the module’s name is bound in the local namespace as a
  reference to the imported module

* If the module being imported is not a top level module, then the name
  of the top level package that contains the module is bound in the
  local namespace as a reference to the top level package. The imported
  module must be accessed using its full qualified name rather than directly

The from form uses a slightly more complex process:

#. find the module specified in the from clause, loading and initializing it if necessary;

#. for each of the identifiers specified in the import clauses:

   #. check if the imported module has an attribute by that name

   #. if not, attempt to import a submodule with that name and then check
      the imported module again for that attribute

   #. if the attribute is not found, ImportError is raised.

   #. otherwise, a reference to that value is stored in the local
      namespace, using the name in the as clause if it is present,
      otherwise using the attribute name

Examples:
::

	import foo                 # foo imported and bound locally
	import foo.bar.baz         # foo.bar.baz imported, foo bound locally
	import foo.bar.baz as fbb  # foo.bar.baz imported and bound as fbb
	from foo.bar import baz    # foo.bar.baz imported and bound as baz
	from foo import attr       # foo imported and foo.attr bound as attr

If the list of identifiers is replaced by a star ('*'), all public names defined in the module are bound in the local namespace for the scope where the import statement occurs.

The public names defined by a module are determined by checking the module’s namespace for a variable named __all__; if defined, it must be a sequence of strings which are names defined or imported by that module. The names given in __all__ are all considered public and are required to exist. If __all__ is not defined, the set of public names includes all names found in the module’s namespace which do not begin with an underscore character ('_'). __all__ should contain the entire public API. It is intended to avoid accidentally exporting items that are not part of the API (such as library modules which were imported and used within the module).

The wild card form of import — from module import * — is only allowed at the module level. Attempting to use it in class or function definitions will raise a SyntaxError.

When specifying what module to import you do not have to specify the absolute name of the module. When a module or package is contained within another package it is possible to make a relative import within the same top package without having to mention the package name. By using leading dots in the specified module or package after from you can specify how high to traverse up the current package hierarchy without specifying exact names. One leading dot means the current package where the module making the import exists. Two dots means up one package level. Three dots is up two levels, etc. So if you execute from . import mod from a module in the pkg package then you will end up importing pkg.mod. If you execute from ..subpkg2 import mod from within pkg.subpkg1 you will import pkg.subpkg2.mod. The specification for relative imports is contained in the Package Relative Imports section.

importlib.import_module() is provided to support applications that determine dynamically the modules to be loaded.

Raises an auditing event import with arguments module, filename, sys.path, sys.meta_path, sys.path_hooks.

global
......

The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global.

Names listed in a global statement must not be used in the same code block textually preceding that global statement.

Names listed in a global statement must not be defined as formal parameters or in a for loop control target, class definition, function definition, import statement, or variable annotation.

Programmer’s note: global is a directive to the parser. It applies only to code parsed at the same time as the global statement. In particular, a global statement contained in a string or code object supplied to the built-in exec() function does not affect the code block containing the function call, and code contained in such a string is unaffected by global statements in the code containing the function call. The same applies to the eval() and compile() functions.



Sequence Operations
-------------------

The operations in the following table are supported by most sequence
types, both mutable and immutable.
::

	x in s # True if an item of s is equal to x, else False

	x not in s # False if an item of s is equal to x, else True

While the in and not in operations are used only for simple containment
testing in the general case, some specialised sequences (such as str,
bytes and bytearray) also use them for subsequence testing:
::

	"gg" in "eggs"
	True

Concatenating immutable sequences always results in a new object.
::

	s + t # concatenation of s and t


Slicing
.......

If i or j is negative, the index is relative to the end of sequence s:
len(s) + i or len(s) + j is substituted. But note that -0 is still 0.
::

	s[i] # ith item of s, origin 0

The slice of s from i to j is defined as the sequence of items with
index k such that i <= k < j. If i or j is greater than len(s), use
len(s). If i is omitted or None, use 0. If j is omitted or None, use
len(s). If i is greater than or equal to j, the slice is empty.
::

	s[i:j] # slice of s from i to j

The slice of s from i to j with step k is defined as the sequence of
items with index x = i + n*k such that 0 <= n < (j-i)/k. In other words,
the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is
reached (but never including j). When k is positive, i and j are reduced
to len(s) if they are greater. When k is negative, i and j are reduced
to len(s) - 1 if they are greater. If i or j are omitted or None, they
become “end” values (which end depends on the sign of k). Note, k cannot
be zero. If k is None, it is treated like 1.
::

	s[i:j:k] # slice of s from i to j with step k

Dictionaries
------------

Iteration
.........

Get w/ default value if key not in dict:
::

	my_dict[k] = my_dict.get(k, 0) + 1; # get retrieves value for k, or 0 if k not in dict


Iterating a dict iterates only the keys:
::

	for k in my_dict:	# k will be each key, not each keyvalue pair



Testing membership: if k in dict: ...

To get actual keyvalue pairs at the same time:
::

	for k,v in my_dict.items():


applies to comprehensions as well: new_d = {k: v+1 for k,v in d.items()}

Sorting
.......

It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted. Dictionaries are inherently orderless, but other types, such as lists and tuples, are not. So you need an ordered data type to represent sorted values, which will be a list—probably a list of tuples.	
 sorted(d.items())
	 sorted list of keyvalue pairs by key
	 by value: sorted(d.items(), key=lambda x: x[1]
 sorted(d)
	 sorted list of keys only
	 sorted list of keys by value: sorted(d, key=lambda x: d[x])


Lists
-----

Comprehensions
..............

General Syntax:
::

	[<expression> for item in list if conditional]

is equivalent to:
::

	for item in list:
			if conditional:
					<expression>


Note how the order of the for and if statements remains the same.
For example, 
::

	for row in grid:
			for x in row:
					<expression>

is the same as
::

	[<expression> for row in grid for x in row]


Initialization
..............

Can use comprehensions:
::
	
	my_list = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

2D list (list of lists):
::

	my_list = [[] for i in range(3)] # [[], [], []]

This is useful for a "visited" grid of some kind (common in Dynamic Programming problems):
::

	visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

*BE CAREFUL* when initializing a matrix.
Do this:
::

	my_list = [[None] * n for i in range(n)]

**NOT** this:
::

	my_list = [[None] * n] * n

The latter method makes copies of the **reference** to the original list, thus any modification to one row will change the other rows in the same way. The first method does not do this.

A list can be created from a string using list(my_str)
We can apply a filter as well:
::

	my_list = list(c for c in my_str if c not in ('a', 'c', 'e'))


Reversal
........

	my_list[::1]
		returns copy of list in reverse
	reversed(my_list)
		returns an iterator on the list in reverse
		can turn into a list via list(reversed(my_list))
	my_list.reverse()
		actually modifies the list
 
List Sorting
............

	sorted(my_list)
		returns copy of sorted list
	my_list.sort()
		actually modifies the list
	 
By default, these methods will sort the list in ascending order.
For descending order, we can supply the arg reverse=True to either of the aforementioned methods.

We can also override the key for sorting by supplying the key arg.
For example, if we have a list of tuples and we want to use the second item as the key:
::

	list1 = [(1, 2), (3, 3), (4, 1)] 
	list1.sort(key=lambda x: x[1]) # list1 is now [(4, 1), (1, 2), (3, 3)]

Additionally, if we want to sort in descending order:
::

	list1.sort(key=lambda x: x[1], reverse=True) # list1 is now [(3, 3), (1, 2), (4, 1)]


When using sorted() it works the same, except we supply the list as the first arg:
::

	list2 = sorted(list1, key=lambda x: x[1], reverse=True)



Strings
-------

F Strings
.........

`Python <http://www.python.org/>`_

`PEP 498 <https://www.python.org/dev/peps/pep-0498/>`_ 
Literal String Interpolation introduced in version 3.6

f-strings are evaluated at runtime, any valid Python expression can be in them.

* Either `f` or `F` can denote a F String.
* Functions or Methods can be called inside a F String

Multi line example
::

	name = 'John Doe'
	age = 50
	sex = 'Yes'

	message = (f"Name = {name} "
						f"Age = {age} "
						f"Sex = {sex}")

	message
	'Name = John Doe Age = 50 Sex = Yes'

From List
.........

::

	my_list = ['te', 's', 't', '1', '2', '3', '_']
	s = ''.join(my_list) # "test123_"
	s2 = ''.join(c for c in my_list if c.isalnum()) # "test123"


String Methods
..............

Python has a lot of useful string methods. A few of them are shown below.
For a complete list, see the [documentation](https://docs.python.org/3.7/library/string.html)
::

	str.capitalize()
	str.center(width[, fillchar])
	str.count(sub[, start[, end]])
	str.endswith(suffix[, start[, end]])
	str.find(sub[, start[, end]])
	str.isalnum()
	str.isalpha()
	str.isdecimal()
	str.isdigit()
	str.isnumeric()
	str.join(iterable)
	str.ljust(width[, fillchar])
	str.lower()
	str.lstrip([chars])
 
 e.g. if d in string.digits: ...
 
isalnum
.......

Returns True if a string consists only of alphanumeric characters.
::

	s = "test123"
	s.isalnum() # True


split
.....

Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit + 1 elements). If maxsplit is not specified or 1, then there is no limit on the number of splits (all possible splits are made).	
Usage:
::

	str.split(sep=None, maxsplit=1)


::

	'1,2,3'.split(',') # ['1', '2', '3']
	'1,2,3'.split(',', maxsplit=1) # ['1', '2,3']
	'1,2,,3,'.split(',') # ['1', '2', '', '3', '']


strip
.....

Returns copy of string without surrounding whitespace, if any.
::

	s = "	 test "
	s.strip() # "test"

join
....

Return a string which is the concatenation of the strings in iterable.
::

	str.join(iterable)

	list = ['aaa', 'bbb', 'ccc']

	# join all the strings in the list with nothing in str
	string = ''.join(list)
	print(string)
	>>> aaabbbccc

	# join all the strings in the list with comma in str
	string = ','.join(list)
	print(string)
	>>> aaa,bbb,ccc

	# join all the strings in the list with dash in str
	string = '-'.join(list)
	print(string)
	>>> aaa-bbb-ccc

	# join all the strings in the list with new line in str
	string = '\n'.join(list)
	print(string)
	>>> aaa
	>>> bbb
	>>> ccc

str vs repr
...........

See [this GeeksForGeeks article](https://www.geeksforgeeks.org/strvsreprinpython/) for more info.


Iterators
---------

In Python, an iterator is an object with a countable number of values that can be iterated upon.
An iterator is an object which implements the iterator protocol, consisting of __iter__() and __next__().	
The __iter__() method returns an iterator on the object, and the __next__() method gets the next item using the iterator, or raises a StopIteration exception if the end of the iterable is reached.

Iterator vs Iterable
....................

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable *containers* which you can get an iterator from.
All these objects have a __iter__() method which is used to get an iterator:
::

	mytuple = ("apple", "banana", "cherry")
	myit = iter(mytuple)

	print(next(myit)) # apple
	print(next(myit)) # banana
	print(next(myit)) # cherry
	print(next(myit)) # raises StopIteration exception

Note	next(obj) is the same as obj.__next__().


How for loop works
..................

The for loop can iterate any iterable.	
The for loop in Python is actually implemented like so:
::

	iter_obj = iter(iterable) # create iterator object from iterable

	# infinite loop
	while True:
			try:
					element = next(iter_obj) # get the next item
					# do something with element
			except StopIteration:
					break

So, internally, the for loop creates an iterator object by calling iter() on the iterable, and then repeatedly calling next() until a StopIteration exception is raised.

Creating an Iterator
....................

Here is an example of an iterator that will give us the next power of two in each iteration.
::

	class PowTwo:
			"""Class to implement an iterator of powers of two"""

			def __init__(self, max = 0):
					self.max = max

			def __iter__(self):
					self.n = 0
					return self

			def __next__(self):
					if self.n <= self.max:
							result = 2 ** self.n
							self.n += 1
							return result
					else:
							raise StopIteration


Now we can use it as follows:
::

	>>> a = PowTwo(4)
	>>> i = iter(a)
	>>> next(i)
	1
	>>> next(i)
	2
	>>> next(i)
	4
	>>> next(i)
	8
	>>> next(i)
	16
	>>> next(i)
	Traceback (most recent call last):
	...
	StopIteration

Or, alternatively, using a for loop:
::

	>>> for i in PowTwo(5):
	...		 print(i)
	...		 
	1
	2
	4
	8
	16
	32



Functional Iteration
--------------------

For some good explanations and examples for the following functions, see [here](http://book.pythontips.com/en/latest/map_filter.html).

Note that map() and filter() both return iterators, so if you want a list, you need to use list() on the output. However, this is typically better accomplished with list comprehensions or for loops for the sake of readability.
	
map
...

map() applies a function to all the items in a list.
::

	map(function_to_apply, list_of_inputs)

	
For example, the following code:
::

	items = [1, 2, 3, 4, 5]
	squared = []
	for i in items:
			squared.append(i**2)

can be accomplished more easily with map():
::

	items = [1, 2, 3, 4, 5]
	squared = list(map(lambda x: x**2, items))


filter
......

filter() creates a list of elements for which a function returns True.
	
Here's an example:
::

	number_list = range(5, 5)
	less_than_zero = list(filter(lambda x: x < 0, number_list))
	print(less_than_zero) # [5, 4, 3, 2, 1]


reduce
......

reduce() is used to perform a rolling computation on a list.

Here's an example:
::

	from functools import reduce
	number_list = [1, 2, 3, 4]
	product = reduce((lambda x, y: x * y), number_list) # output: 24


Often times, an explicit for loop is more readable than using reduce().
But if you're trying to flex in an interview, and the problem calls for it, it could be a nice way to subtly show your understanding of functional programming.


Decorators
----------

A decorator is a function returning another function, usually applied as a function transformation using the @wrapper syntax. This syntax is merely syntactic sugar.

The following two function definitions are semantically equivalent:
::

	def f(...):

	f = staticmethod(f)

	@staticmethod
	def f(...):



@classmethod
............

Transform a method into a class method. A class method receives the class as implicit first argument, just like how an instance method receives the instance. To declare a class method:
::

	class C:
			@classmethod
			def f(cls, arg1, arg2, ...):
		


A class method can be called either on the class (like C.f()) or on an instance (like C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

Note that class methods are not the same as C++ or Java static methods. If you want those, see [@staticmethod](#staticmethod).

@staticmethod
.............

Transform a method into a static method. A static method does not receive an implicit first argument. To declare a static method:
::

	class C:
			@staticmethod
			def f(arg1, arg2, ...):
		


A static method can be called either on the class (like C.f()) or on an instance (like C().f()). Static methods in Python are similar to those found in Java or C++.

@property
.........

Return a property attribute.
Usage:
::

	property(fget=None, fset=None, fdel=None, doc=None)

fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. doc creates a docstring for the attribute.

The following is a typical use case for defining a managed attribute x:
::

	class C:
			def __init__(self):
					self._x = None

			def getx(self):
					return self._x

			def setx(self, value):
					self._x = value

			def delx(self):
					del self._x

			x = property(getx, setx, delx, "I'm the 'x' property.")

Or, equivalently:
::

	class C:
			def __init__(self):
					self._x = None

			@property
			def x(self):
					"""I'm the 'x' property."""
					return self._x

			@x.setter
			def x(self, value):
					self._x = value

			@x.deleter
			def x(self):
					del self._x


If c is an instance of C, then c.x will invoke the getter; c.x = value will invoke the setter; and del c.x the deleter.

If doc is not provided, the property will copy fget's docstring, if it exists. Thus, it is straightforward to create readonly properties with the @property decorator:
::

	class Parrot:
			def __init__(self):
					self._voltage = 100000

			@property
			def voltage(self):
					"""Get the current voltage."""
					return self._voltage

The @property decorator turns the voltage() method into a “getter” for a readonly attribute with the same name, and it sets the docstring for voltage to “Get the current voltage.”

For more information, check out [the documentation](https://docs.python.org/3/library/functions.html#property) and [this Programiz article](https://www.programiz.com/pythonprogramming/property).


Generators
----------

Generators are simpler ways of creating [iterators](#iterators). The overhead of creating __iter__(), __next__(), raising StopIteration, and keeping track of state can all be handled internally by a generator.

A generator is a function that returns an object (iterator) which we can iterate over, one value at a time. 

Using yield
...........

To create a generator, simply define a function using a yield statement.

A function containing at least one yield statement (it may contain other yield and return statements) becomes a generator.

Both yield and return return some value from a function. The difference is that, while a return statement terminates a function entirely, yield pauses the function, saving its state and continuing from where it left off in successive calls.

Once a function yields, it is paused and control is transferred back to the caller. Local variables and their states are remembered between successive calls. When the function terminates, StopIteration is raised automatically on further calls.

Below is a simple generator example, for the sake of demonstrating how generators work.
::

	def my_gen():
			n = 1
			print('This is printed first')
			yield n

			n += 1
			print('This is printed second')
			yield n
			
	# Without for loop:
	a = my_gen()
	next(a) # 'This is printed first'
	next(a) # 'This is printed second'
	next(a) # Traceback ... StopIteration

	# With for loop:
	for item in my_gen():
			print(item)


Below is a more typical example. Generators often use loops with a suitable terminating condition.
::

	def reverse(my_str):
			for i in range(len(my_str)	1, 1, 1):
					yield my_str[i]
				
for char in reverse("hello"):
		print(char) # prints each char reverse on a new line

Note that the above example works not just with strings, but also other kinds of iterables.

Generator Expressions
.....................

Generator expressions can be used to create an anonymous generator function. The syntax is similar to that of [list comprehensions](#listcomprehensions), but uses parentheses instead of square brackets. However, while a list comprehension produces the entire list, generator expressions produce one item at a time.

Generator expressions are kind of lazy, producing items only when asked for. For this reason, using a generator expression is much more memory efficient than an equivalent list comprehension.

::

	items = [1, 3, 6]
	item_squared = (item**2 for item in items)
	print(next(item_squared)) # 1
	print(next(item_squared)) # 9
	print(next(item_squared)) # 36
	next(item_squared) # StopIteration


Generator expressions can be used inside function calls. When used in such a way, the round parentheses can be dropped.
::

	sum(x**2 for x in items) # 46
	max(x**2 for x in items) # 36



Other Builtin Functions
-----------------------

For a complete list of builtins in Python 3, see [the documentation](https://docs.python.org/3/library/functions.html).
abs()
Returns the absolute value of a number, either an integer or floating point number.
If the argument is a complex number, its magnitude is returned.

any
...

Usage:
::

	any(iterable)

any() takes any iterable as an argument and returns True if at least one element of the iterable is True.

::

	any([1, 3, 4, 0])	 # True
	any([0, False])		 # False
	any([0, False, 5])	# True
	any([])						 # False

	any("This is good") # True
	any("0")						# True
	any("")						 # False


See [here](https://www.programiz.com/pythonprogramming/methods/builtin/any) for more info.

Check if any tuples contain a negative value:
::

	if any(x < 0 or y < 0 for (x, y) in list_ranges): ...


all
...

::

	all(iterable)

all() takes any iterable as an argument and returns True if all the elements of the iterable are True.

::

	all([1, 3, 4, 5])	# True
	all([0, False])		# False
	all([1, 3, 4, 0])	# False
	all([0, False, 5]) # False
	all([])						# True

	all("This is good") # True
	all("0")						# True
	all("")						 # True


See [here](https://www.programiz.com/pythonprogramming/methods/builtin/all) for more info.

Check if all elements of a list are x: 
::

	if all(c == x for c in alst): ...


chr
...

Returns the string representing a character whose Unicode code point is the integer passed.

For example, chr(97) returns the string a, while chr(8364) returns the string €.

This is the inverse of [ord()](#ord).

enumerate()
Usage:
::

	enumerate(iterable, start=0)

Returns an enumerate object. iterable must be a sequence, iterator, or some object which suports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to zero) and the values obtained from iterating over the iterable.	

Example:
::

	seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	list(enumerate(seasons))							# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
	list(enumerate(seasons, start=1))		 # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

This is equivalent to:
::

	def enumerate(sequence, start=0):
			n = start
			for elem in sequence:
					yield n, elem
					n += 1


input
.....

Gets input from the user.
Usage:
::

	input([prompt])


Example: 
::

	>>> s = input('> ')	
	> Monty Python's Flying Circus
	>>> s	
	"Monty Python's Flying Circus"

If the prompt arg is present, it is written to stdout without a trailing newline.

isinstance
..........

Usage:
::

	isinstance(object, type)

Built in Types
::

	int
	float
	complex
	str
	list
	dict
	tuple
	set

Returns true if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. Returns false otherwise.

If classinfo is a tuple of type objects, return true if object is an instance of any of *any* of these types.

len
...

Return the length of an object. The argument may be a sequence (e.g. string, bytes, tuple, list, or range) or a collection (e.g. dictionary, set, frozen set).

max
...

Returns the max item in an iterable, or the max of multiple arguments passed.

min
...

Returns the min item in an iterable, or the min of multiple arguments passed.

ord
...

Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.

For example, ord('a') returns the integer 97. ord('€') (Euro sign) return 8364. 

This is the inverse of [chr()](#chr).

pow
...

Usage:
::

	pow(x, y[, z])

Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z).	
pow(x, y) is equivalent to x**y.

type
...

Usage:
::

	type(object)
	type(name, bases, dict)


With one argument, return the type of object. The return value is a type object and generally the same object as returned by object.__class__.

E.g.
::

	x = 5
	type(x)	# class 'int'


The [isinstance()](#isinstance) function is recommended for testing the type of an object, since it accounts for subclasses.


Common Gotchas
--------------

Nested List Initialization
..........................

When creating a list of lists, be sure to use the following structure:
::

	my_list = [[None] * n for i in range(n)]

Read the section on [list initialization](#listinitialization) to see why.

Mutable Default Arguments
.........................

If we try to do something like def f(x, arr=[]) this will most likely create undesirable behavior.
Default arguments are resolved *only once*, when the function is first defined. The same arg will be used in successive function calls. In the case of a mutable type like a list, this means that changes made to the list in one call will be carried over in successive calls.
Instead, consider doing:
::

	def f(x, arr=None):
			if not arr: arr = []


