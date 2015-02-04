# Caesar cipher

Caesar cipher is one of the simplest and most widely known encryption techniques. The method is named after Julius Caesar, who used it in his private correspondence.

You have the implement a function with the following signature: caesar_encrypt(str, n).
- The argument str is of type string
- The argument n is of type integer.
- The function should return an encrypted string

The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,..., Z = 25. Encryption of a letter x by a shift n can be described mathematically as,

![](http://upload.wikimedia.org/math/b/b/b/bbb819c72cda43180d98e6ade5cadb04.png)

`Do not` encrypt any non-alphabetical characters!

Example:

```
>>> caesar_encrypt("abc", 1)
"bcd"
>>> caesar_encrypt("ABC", 1)
"BCD"
>>> caesar_encrypt("abc", 2)
"cde"
>>> caesar_encrypt("aaa", 7)
"hhh"
>>> caesar_encrypt("xyz", 1)
"yza"
```
