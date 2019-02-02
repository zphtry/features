**boolean**

* **char**: holds a single character
* **char (#)**: holds # number of characters. Spaces will be inserted to fill any extra room.
* **varchar (#)**: holds a maximum of # number of character. Can contain less.

### integer values
* **smallint**: whole number between -32768 and 32767.
* **int**: whole number between -214783648 and 214783647.
* **serial**: Auto-populated integer number.

### floating-point values
* **float (#)**: floating point number with at least # points of precision.
* **real**: 8-byte floating point number
* **numeric (#,after_dec)**: real number with # number of digits, and after_dec digits after decimal

### date and time values
* **date**: stores a date value
* **time**: stores a time value
* **timestamp**: stores a date and time value
* **timestamptz**: stores a timestamp that includes timezone data
* **interval**: stores the difference between two timestamp values
