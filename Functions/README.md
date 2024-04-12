## Python Lambda Functions

Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the
def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous
function in Python. 

**Python Lambda Function** 

**Syntax:**

`lambda arguments: expression`

- This function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
- It has various uses in particular fields of programming besides other types of expressions in functions.

# **Map()**

The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.

`map(function, iterable, ...)`

**map() Parameter**

The map() function takes two parameters:

- **function** - a function that perform some action to each element of an iterable
- **iterable** - an iterable like sets, lists, tuples, etc

You can pass more than one _iterable_ to the _map()_ function.

**map() Return Value**

The map() function returns an object of map class. The returned value can be passed to functions like

- list() - to convert to list
- set() - to convert to a set, and so on.

# **Filter()**

Python’s filter() is a built-in function that allows you to process an iterable and extract those items that satisfy a
given condition. This process is commonly known as a **filtering operation**. With filter(), you can apply a **filtering 
function** to an iterable and produce a new iterable with the items that satisfy the condition at hand. In Python, 
filter() is one of the tools you can use for functional programming.

In this tutorial, you’ll learn how to:

Use Python’s **_filter()_** in your code
- Extract **needed values** from your iterables
- Combine filter() with other **functional tools**
- **Replace** filter() with more **Pythonic** tools

**filter(function, iterable)**

# **Reduce()**

Python’s reduce() implements a mathematical technique commonly known as **folding** or **reduction**. You’re doing a fold or
reduction when you reduce a list of items to a single cumulative value. Python’s reduce() operates on any iterable—not
just lists—and performs the following steps:

- **Apply** a function (or callable) to the first two items in an iterable and generate a partial result.
- **Use** that partial result, together with the third item in the iterable, to generate another partial result.
- **Repeat** the process until the iterable is exhausted and then return a single cumulative value.

The idea behind Python’s reduce() is to take an existing function, apply it cumulatively to all the items in an iterable,
and generate a single final value. In general, Python’s reduce() is handy for processing iterables without writing
explicit for loops. Since reduce() is written in C, its internal loop can be faster than an explicit Python for loop.

`functools.reduce(function, iterable[, initializer])`

# **Zip()**

zip() is available in the built-in namespace. If you use dir() to inspect __builtins__, then you’ll see zip() at the end
of the list:

```dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', ..., 'zip']
```
According to the official documentation, Python’s zip() function behaves as follows:

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or 
iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns
an iterator of 1-tuples. With no arguments, it returns an empty iterator. (Source)

You’ll unpack this definition throughout the rest of the tutorial. As you work through the code examples, you’ll see 
that Python zip operations work just like the physical zipper on a bag or pair of jeans. Interlocking pairs of teeth on 
both sides of the zipper are pulled together to close an opening. In fact, this visual analogy is perfect for
understanding zip(), since the function was named after physical zippers!
