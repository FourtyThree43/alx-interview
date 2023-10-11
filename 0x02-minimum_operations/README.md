# alx-interview

## 0x02-minimum_operations

### Problem Description

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

### Function Prototype

```python
def minOperations(n: int) -> int:
    pass
```

The function `minOperations` takes an integer 'n' as input and returns an integer representing the minimum number of operations needed to get 'n' 'H' characters. If 'n' is impossible to achieve, the function returns 0.

### Example

For example, if 'n' is 9, you would need to perform 6 operations: start with 'H', Copy All, Paste (to get 'HH'), Paste (to get 'HHH'), Copy All, and then Paste twice (to get 'HHHHHHHHH'). So, the minimum number of operations here is 6.

```
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                          |F|o|u|r|t|y|T|h|r|e|e|4|3|
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                         
                         _|            _|  _|  _|_|_|    
                       _|_|  _|    _|  _|  _|        _|  
                         _|    _|_|    _|_|_|_|  _|_|    
                         _|  _|    _|      _|        _|  
                         _|  _|    _|      _|  _|_|_|    
                                                         
```
                                                         
## ❝ Quote ❞

```
Eternal nothingness is fine if you happen to be dressed for it.
		-- Woody Allen
```
