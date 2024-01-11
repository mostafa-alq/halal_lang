With this new language and built in interpreter (also on my profile), you are able to utilise a stack-based language to execute code. Here is a list of the syntax:

PUSH - Push a number into the top of stack (e.g PUSH 3)

POP - Take out a number from the stack and return it

ADD - Pops 2 numbers from the top of the stack and pushes the sum

SUB - Pops 2 numbers from the top of the stack and subtracts the second from the first

SUBO - Pops 2 numbers from the stack and subtracts the first from the second (this is here because i can)

PRINT - Prints out a string literal to the terminal (e.g PRINT "Salam 3laykum sheikh". This should also work with apostrophes if you may like)

READ - Get a number as an input and pushes it into the stack (e.g READ 3. It is important to mention that it does not prompt you to enter a number, which may be fixed in the future)

JUMP.E0 - Jump to a function if the top of the stack is 0 (If I have a function "LOOP:", then "JUMP.E0 LOOP" will jump to the function LOOP if the value of the top of the stack is 0)

JUMP.G0 - Jump to a function if the top of the stack is greater than 0 (If I have a function "LOOP:", then "JUMP.E0 LOOP" will jump to the function LOOP if the value of the top of the stack is greater than 0)

JUMP.GE0 - Jump to a function if the top of the stack is greater or equal to 0 (If I have a function "LOOP:", then "JUMP.E0 LOOP" will jump to the function LOOP if the value of the top of the stack is greater or equal to 0)

JUMP.L0 - Jump to a function if the top of the stack is less than 0 (If I have a function "LOOP:", then "JUMP.E0 LOOP" will jump to the function LOOP if the value of the top of the stack is less than 0)

JUMP.LE0 - Jump to a function if the top of the stack is less or equal to 0 (If I have a function "LOOP:", then "JUMP.E0 LOOP" will jump to the function LOOP if the value of the top of the stack is less than 0)

HALT - just stop lol (You always need this at the end of your thing or else it will run infinitely and cause many tears)

TOP - Return the value at the top of the stack
