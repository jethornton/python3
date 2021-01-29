Built In Functions
==================

abs()
-----

Return the absolute value of a number.

all()
-----

Return True if all elements of the iterable are true (or if the iterable is empty).

any()
-----

Return True if any element of the iterable is true. If the iterable is empty, return False. 

ascii()
-------

As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes. This generates a string similar to that returned by repr() in Python 2.

bin()
-----

Convert an integer number to a binary string prefixed with “0b”.

bool([x])
---------

Return a Boolean value, i.e. one of True or False.

Here are most of the built-in objects considered false:

* constants defined to be false: None and False.

* zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

* empty sequences and collections: '', (), [], {}, set(), range(0)

breakpoint()
------------

This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice.

bytearray()
-----------

Return a new array of bytes.

bytes()
-------

Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.

callable()
----------

Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.

chr(i)
------

Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.


@classmethod()
--------------

Transform a method into a class method.

A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:
::

	class C:
		@classmethod
		def f(cls, arg1, arg2, ...): ...

compile()
---------

Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.

complex([real[, imag]])
-----------------------

Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

delattr(object, name)
---------------------

This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.

dict()
------

::

	class dict(**kwarg)
	class dict(mapping, **kwarg)
	class dict(iterable, **kwarg)

Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.

For other containers see the built-in list, set, and tuple classes, as well as the collections module.


dir([object])
-------------

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

If the object has a method named __dir__(), this method will be called and must return the list of attributes. This allows objects that implement a custom __getattr__() or __getattribute__() function to customize the way dir() reports their attributes.

If the object does not provide __dir__(), the function tries its best to gather information from the object’s __dict__ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom __getattr__().

The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

* If the object is a module object, the list contains the names of the
  module’s attributes.

* If the object is a type or class object, the list contains the names
  of its attributes, and recursively of the attributes of its bases.

* Otherwise, the list contains the object’s attributes’ names, the names
  of its class’s attributes, and recursively of the attributes of its
  class’s base classes.


divmod(a, b)
------------

Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply.

enumerate(iterable, start=0)
----------------------------

Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
::

	seasons = ['Spring', 'Summer', 'Fall', 'Winter']

	list(enumerate(seasons))
	[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

	list(enumerate(seasons, start=1))
	[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

eval(expression[, globals[, locals]])
-------------------------------------

The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key before expression is parsed. This means that expression normally has full access to the standard builtins module and restricted environments are propagated. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed with the globals and locals in the environment where eval() is called. Note, eval() does not have access to the nested scopes (non-locals) in the enclosing environment.

The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:
:::

	x = 1
	eval('x+1')
	2

This function can also be used to execute arbitrary code objects (such as those created by compile()). In this case pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, eval()’s return value will be None.

exec(object[, globals[, locals]])
---------------------------------

This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). 1 If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section “File input” in the Reference Manual). Be aware that the return and yield statements may not be used outside of function definitions even within the context of code passed to the exec() function. The return value is None.

filter(function, iterable)
--------------------------

Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.

float([x])
----------

Return a floating point number constructed from a number or string x.

If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More precisely, the input must conform to the following grammar after leading and trailing whitespace characters are removed:
::

	sign           ::=  "+" | "-"
	infinity       ::=  "Infinity" | "inf"
	nan            ::=  "nan"
	numeric_value  ::=  floatnumber | infinity | nan
	numeric_string ::=  [sign] numeric_value

Here floatnumber is the form of a Python floating-point literal, described in Floating point literals. Case is not significant, so, for example, “inf”, “Inf”, “INFINITY” and “iNfINity” are all acceptable spellings for positive infinity.

Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (within Python’s floating point precision) is returned. If the argument is outside the range of a Python float, an OverflowError will be raised.

For a general Python object x, float(x) delegates to x.__float__(). If __float__() is not defined then it falls back to __index__().

If no argument is given, 0.0 is returned.

Examples:
::

	>>> float('+1.23')
	1.23
	>>> float('   -12345\n')
	-12345.0
	>>> float('1e-003')
	0.001
	>>> float('+1E6')
	1000000.0
	>>> float('-Infinity')
	-inf

format(value[, format_spec])
----------------------------

Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: 
`Format Specification Mini-Language <https://docs.python.org/3/library/string.html#formatspec>`_

The default format_spec is an empty string which usually gives the same effect as calling str(value).

frozenset([iterable])
---------------------

Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in set, list, tuple, and dict classes, as well as the collections module.


getattr()
---------

getattr(object, name[, default])

Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
::

	class Person:
			age = 23
			name = "Adam"

	person = Person()

	# when default value is provided
	print('The sex is:', getattr(person, 'sex', 'Male'))

	# when no default value is provided
	print('The sex is:', getattr(person, 'sex'))


globals()
---------

Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

hasattr(object, name)
---------------------

The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)

hash(object)
------------

Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

help([object])
--------------

Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

hex(x)
------

Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.

id(object)
----------

Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

input([prompt])
---------------

If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
::

	>>> s = input('--> ')  
	--> Monty Python's Flying Circus
	>>> s  
	"Monty Python's Flying Circus"

int([x]))
---------

Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('010') is, as well as int('010', 8).

isinstance(object, classinfo)
-----------------------------

Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples), return True if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.

issubclass(class, classinfo)
----------------------------

Return True if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

iter(object[, sentinel])
------------------------

Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

len(s)
------

Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

list([iterable])
----------------

Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.

locals()
--------

Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary.

map(function, iterable, ...)
----------------------------

Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

max()
-----

::

	max(iterable, *[, key, default])
	max(arg1, arg2, *args[, key])

Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, iterable, key=keyfunc).

New in version 3.4: The default keyword-only argument.

Changed in version 3.8: The key can be None.


memoryview(obj)
---------------

Return a “memory view” object created from the given argument. 

min()
-----

::

	min(iterable, *[, key, default])
	min(arg1, arg2, *args[, key])

Return the smallest item in an iterable or the smallest of two or more arguments.

If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.

There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

If multiple items are minimal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc)[0] and heapq.nsmallest(1, iterable, key=keyfunc).

New in version 3.4: The default keyword-only argument.

Changed in version 3.8: The key can be None.


next()
------

next(iterator[, default])

Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.


object()
--------

Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

oct()
-----

oct(x)

Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer. For example:
::

	oct(8)
	'0o10'

	oct(-56)
	'-0o70'

If you want to convert an integer number to octal string either with prefix “0o” or not, you can use either of the following ways.
::

	'%#o' % 10, '%o' % 10
	('0o12', '12')

	format(10, '#o'), format(10, 'o')
	('0o12', '12')

	f'{10:#o}', f'{10:o}'
	('0o12', '12')

open()
------

See :ref:`File I/O`

ord()
-----

::

	ord(c)

Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().


pow()
-----

::

	pow(base, exp[, mod])

Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, 10**2 returns 100, but 10**-2 returns 0.01.

For int operands base and exp, if mod is present, mod must also be of integer type and mod must be nonzero. If mod is present and exp is negative, base must be relatively prime to mod. In that case, pow(inv_base, -exp, mod) is returned, where inv_base is an inverse to base modulo mod.

Here’s an example of computing an inverse for 38 modulo 97:
>>>

>>> pow(38, -1, mod=97)
23
>>> 23 * 38 % 97 == 1
True

Changed in version 3.8: For int operands, the three-argument form of pow now allows the second argument to be negative, permitting computation of modular inverses.

Changed in version 3.8: Allow keyword arguments. Formerly, only positional arguments were supported.

print()
-------
::

	print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.

Changed in version 3.3: Added the flush keyword argument.


property()
----------

::

  class property(fget=None, fset=None, fdel=None, doc=None)

Return a property attribute.

fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.

A typical use is to define a managed attribute x:
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

If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.

If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fget’s docstring (if it exists). This makes it possible to create read-only properties easily using property() as a decorator:
::

	class Parrot:
	def __init__(self):
		self._voltage = 100000

	@property
	def voltage(self):
		"""Get the current voltage."""
		return self._voltage

The @property decorator turns the voltage() method into a “getter” for a read-only attribute with the same name, and it sets the docstring for voltage to “Get the current voltage.”

A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:
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

This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (x in this case.)

The returned property object also has the attributes fget, fset, and fdel corresponding to the constructor arguments.

Changed in version 3.5: The docstrings of property objects are now writeable.

range()
-------
::

	class range(stop)
	class range(start, stop[, step])

Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.

repr()
------
::

	repr(object)

Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.

reversed()
----------
::

	reversed(seq)

Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).


round()
-------
::

	round(number[, ndigits])

Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if ndigits is omitted or None. Otherwise the return value has the same type as number.

For a general Python object number, round delegates to number.__round__.

Note

The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information.

set()
-----
::

	class set([iterable])

Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.


setattr()
---------
::

	setattr(object, name, value)

This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.


slice()
-------
::

	class slice(stop)
	class slice(start, stop[, step])

Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.

sorted()
--------
::

	sorted(iterable, *, key=None, reverse=False)

Return a new sorted list from the items in iterable.

Has two optional arguments which must be specified as keyword arguments.

key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

Use functools.cmp_to_key() to convert an old-style cmp function to a key function.

The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

For sorting examples and a brief sorting tutorial, see Sorting HOW TO.


staticmethod()
--------------
::

	@staticmethod

Transform a method into a static method.

A static method does not receive an implicit first argument. To declare a static method, use this idiom:
::

	class C:
		@staticmethod
		def f(arg1, arg2, ...): ...

The @staticmethod form is a function decorator – see Function definitions for details.

A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).

Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors.

Like all decorators, it is also possible to call staticmethod as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:
::

	class C:
		builtin_open = staticmethod(open)

For more information on static methods, see The standard type hierarchy.

str()
-----
::

	class str(object='')
	class str(object=b'', encoding='utf-8', errors='strict')

Return a str version of object. See str() for details.

str is the built-in string class. For general information about strings, see Text Sequence Type — str.


sum()
-----
::

	sum(iterable, /, start=0)

Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().

super()
-------
::

	super([type[, object-or-type]])

Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

The object-or-type determines the method resolution order to be searched. The search starts from the class right after the type.

For example, if __mro__ of object-or-type is D -> B -> C -> A -> object and the value of type is B, then super() searches C -> A -> object.

The __mro__ attribute of the object-or-type lists the method resolution search order used by both getattr() and super(). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

If the second argument is omitted, the super object returned is unbound. If the second argument is an object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is useful for classmethods).

There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this:
::

	class C(B):
		def method(self, arg):
			super().method(arg)    # This does the same thing as:

	# super(C, self).method(arg)

In addition to method lookups, super() also works for attribute lookups. One possible use case for this is calling descriptors in a parent or sibling class.

Note that super() is implemented as part of the binding process for explicit dotted attribute lookups such as super().__getitem__(name). It does so by implementing its own __getattribute__() method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, super() is undefined for implicit lookups using statements or operators such as super()[name].

Also note that, aside from the zero argument form, super() is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references. The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessing the current instance for ordinary methods.

For practical suggestions on how to design cooperative classes using super(), see guide to using super().

tuple()
-------
::

	class tuple([iterable])

Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.

type()
------
::
	class type(object)
	class type(name, bases, dict)

With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.

The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.

With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the __name__ attribute. The bases tuple contains the base classes and becomes the __bases__ attribute; if empty, object, the ultimate base of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the __dict__ attribute. The following two statements create identical type objects:
::

	class X:
		a = 1

	X = type('X', (), dict(a=1))

See also Type Objects.

Changed in version 3.6: Subclasses of type which don’t override type.__new__ may no longer use the one-argument form to get the type of an object.


vars()
------
::

	vars([object])

Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).

Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.

A TypeError exception is raised if an object is specified but it doesn’t have a __dict__ attribute (for example, if its class defines the __slots__ attribute).


zip()
-----
::

	zip(*iterables)

Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:
::

	def zip(*iterables):
		# zip('ABCD', 'xy') --> Ax By
		sentinel = object()
		iterators = [iter(it) for it in iterables]
		while iterators:
			result = []
			for it in iterators:
				elem = next(it, sentinel)
				if elem is sentinel:
					return
				result.append(elem)
			yield tuple(result)

The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using `zip(*[iter(s)]*n)`. This repeats the same iterator n times so that each output tuple has the result of n calls to the iterator. This has the effect of dividing the input into n-length chunks.

zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables. If those values are important, use itertools.zip_longest() instead.

zip() in conjunction with the * operator can be used to unzip a list:
::

	>>> x = [1, 2, 3]
	>>> y = [4, 5, 6]
	>>> zipped = zip(x, y)
	>>> list(zipped)
	[(1, 4), (2, 5), (3, 6)]
	>>> x2, y2 = zip(*zip(x, y))
	>>> x == list(x2) and y == list(y2)
	True


