File I/O
========

The open() fuction returns file object if sucessful. 

::

  with open(file_name, mode) as f:
    do something with f

Open a text file for reading
::

	with open('test.txt') as f:
		data = f.read()

Open a text file for appending [#]_
::

		with open('test.txt', 'a') as f:
			# using write to add text
			f.write('Some random text\n')
			# using print() to add text
			print('More random text', file=f)

Modes

* r	open for reading (default) [#]_
* w	open for writing, truncating [#]_ the file first
* x	open for exclusive creation, if the file already exists returns FileExistsError:
* a	open for writing, appending to the end of the file if it exists
* b	binary mode
* t	text mode (default)
* \+	open for updating (reading and writing)

.. [#] write does not add a new line, you need to add it yourself with \\n
.. [#] If the file is not found a FileNotFoundError: is returned
.. [#] truncating a file means removing the file contents without deleting the file

* class io.IOBase

    The abstract base class for all I/O classes, acting on streams of bytes. There is no public constructor.

    This class provides empty abstract implementations for many methods that derived classes can override selectively; the default implementations represent a file that cannot be read, written or seeked.

    Even though IOBase does not declare read() or write() because their signatures will vary, implementations and clients should consider those methods part of the interface. Also, implementations may raise a ValueError (or UnsupportedOperation) when operations they do not support are called.

    The basic type used for binary data read from or written to a file is bytes. Other bytes-like objects are accepted as method arguments too. Text I/O classes work with str data.

    Note that calling any method (even inquiries) on a closed stream is undefined. Implementations may raise ValueError in this case.

    IOBase (and its subclasses) supports the iterator protocol, meaning that an IOBase object can be iterated over yielding the lines in a stream. Lines are defined slightly differently depending on whether the stream is a binary stream (yielding bytes), or a text stream (yielding character strings). See readline() below.

    IOBase is also a context manager and therefore supports the with statement. In this example, file is closed after the with statement’s suite is finished—even if an exception occurs:

    with open('spam.txt', 'w') as file:
        file.write('Spam and eggs!')

    IOBase provides these data attributes and methods:

* close()

    Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.

    As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.

* closed

    True if the stream is closed.

* fileno()

    Return the underlying file descriptor (an integer) of the stream if it exists. An OSError is raised if the IO object does not use a file descriptor.

* flush()

    Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.

* isatty()

    Return True if the stream is interactive (i.e., connected to a terminal/tty device).

* readable()

    Return True if the stream can be read from. If False, read() will raise OSError.

* readline(size=-1)

    Read and return one line from the stream. If size is specified, at most size bytes will be read.

    The line terminator is always b'\n' for binary files; for text files, the newline argument to open() can be used to select the line terminator(s) recognized.

* readlines(hint=-1)

    Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.

    Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
    
    list(file_object) does the same thing as file_object.readlines()

* seek(offset, whence=SEEK_SET)

    Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence. The default value for whence is SEEK_SET. Values for whence are:

        SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive

        SEEK_CUR or 1 – current stream position; offset may be negative

        SEEK_END or 2 – end of the stream; offset is usually negative

    Return the new absolute position.

    New in version 3.1: The SEEK_* constants.

    New in version 3.3: Some operating systems could support additional values, like os.SEEK_HOLE or os.SEEK_DATA. The valid values for a file could depend on it being open in text or binary mode.

* seekable()

    Return True if the stream supports random access. If False, seek(), tell() and truncate() will raise OSError.

* tell()

    Return the current stream position.

* truncate(size=None)

    Resize the stream to the given size in bytes (or the current position if size is not specified). The current stream position isn’t changed. This resizing can extend or reduce the current file size. In case of extension, the contents of the new file area depend on the platform (on most systems, additional bytes are zero-filled). The new file size is returned.

    Changed in version 3.5: Windows will now zero-fill files when extending.

* writable()

    Return True if the stream supports writing. If False, write() and truncate() will raise OSError.

* ritelines(lines)

    Write a list of lines to the stream. Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end.

* __del__()

    Prepare for object destruction. IOBase provides a default implementation of this method that calls the instance’s close() method.
