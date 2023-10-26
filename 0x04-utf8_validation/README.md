# alx-interview

This repository contains the solutions to the technical interview questions for the ALX Software Engineering program.

## 0x04. UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: `def validUTF8(data)`
* Return: `True` if data is a valid UTF-8 encoding, else return `False`
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Environment

* Language: Python 3.4.3
* OS: Ubuntu 20.04 LTS
* Compiler: python3
* Style guidelines: [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/)
* Module name: `utf8_validation`

## Learning Objectives

* What is UTF-8?
* What is the represenation of UTF-8 in characters?
* What is the ASCII character set?
* What is the UTF-8 character set?
* What is byte order?
* How does UTF-8 encode characters?
* How to validate a UTF-8 byte sequence

## Resources

* [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
* [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
* [UTF-8 Validator](https://www.fileformat.info/info/unicode/utf8validator.htm)
* [Datatracker - RFC 3629: UTF-8](https://datatracker.ietf.org/doc/html/rfc3629#page-4)
