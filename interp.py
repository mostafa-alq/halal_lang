# Stack based language (just a stack of elements)
# PUSH - push a number into the stack
# POP - Tkae out a number from the stack and return it
# ADD - Pops 2 numbers from the stack and pushes the sum
# SUB - Pops 2 numbers from the stack and subtracts the first from the second
# SUBO - Pops 2 numbers from the stack and subtracts the second from the first (this is here because i can)
# PRINT - Prints out a string literal to the terminal
# READ - Get a number as an input/output and pushes it into the stack
# JUMP.E0 - Jump to function if the top of the stack is 0
# JUMP.G0 - Jump to function if the top of the stack is greater than 0
# JUMP.GE0 - Jump to function if the top of the stack is greater or equal to 0
# JUMP.L0 - Jump to function if the top of the stack is less than 0
# JUMP.LE0 - Jump to function if the top of the stack is less or equal to 0
# HALT - just stop lol
# TOP - Return the value at the top of the stack

import sys

#read arguments
program_filepath = sys.argv[1]

#Make the tokens
program_lines = []
with open(program_filepath, 'r') as program_file:
  program_lines = [line.strip() for line in program_file.readlines()]
  
  
#Parse yo shit
program = []
token_counter = 0
function_tracker = {}
for line in program_lines:
  parts = line.split(" ")
  opcode = parts[0]
  
  #whitespace
  if opcode == "":
    continue
  
  elif opcode.endswith(":"):
    function_tracker[opcode[:-1]] = token_counter
    continue
  
  #store the opcode
  program.append(opcode)
  token_counter += 1
  
  #handle each opcode
  if opcode == 'PUSH':
    #Validate they are passing an integer
    number = int(parts[1])
    program.append(number)
    token_counter += 1
  
  elif opcode == 'PRINT':
    #parse the string literal
    string_literal = ' '.join(parts[1:])[1:-1]
    program.append(string_literal)
    token_counter += 1
  
  elif opcode == "JUMP.E0":
    function = parts[1]
    program.append(function)
    token_counter += 1
    
  elif opcode == "JUMP.G0":
    function = parts[1]
    program.append(function)
    token_counter += 1
  
  elif opcode == "JUMP.GE0":
    function = parts[1]
    program.append(function)
    token_counter += 1
  
  elif opcode == "JUMP.L0":
    function = parts[1]
    program.append(function)
    token_counter += 1
  
  elif opcode == "JUMP.LE0":
    function = parts[1]
    program.append(function)
    token_counter += 1

#Now interpret yo shit
#buf - buffer, just the stack bro
#sp - stack pointer (point at the location in the stack)

class Stack:
  def __init__(self,size):
    self.buf = [0 for _ in range(size)]
    self.sp = -1
    
  def push(self, number):
    self.sp += 1
    self.buf[self.sp] = number
  
  def pop(self):
    number = self.buf[self.sp]
    self.sp -= 1
    return number
  
  def top(self):
    return self.buf[self.sp]


#program counter
pc = 0
#make yo stack
stack = Stack(256)


while program[pc] != 'HALT':
  opcode = program[pc]
  pc += 1
  
  if opcode == 'PUSH':
    number = program[pc]
    pc += 1
    stack.push(number)
    
  elif opcode == 'POP':
    stack.pop()
    
  elif opcode == 'ADD':
    a = stack.pop()
    b = stack.pop()
    stack.push(a+b)
  
  elif opcode == 'SUB':
    a = stack.pop()
    b = stack.pop()
    stack.push(b-a)

  #thats the letter o not zero
  #also this subtracts the other way around because why not lol
  elif opcode == 'SUBO':
    a = stack.pop()
    b = stack.pop()
    stack.push(a-b)
    
  elif opcode == 'PRINT':
    string_literal = program[pc]
    pc += 1
    print(string_literal)
    
  elif opcode == 'READ':
    number = int(input())
    stack.push(number)
  
  #thats a zero not the letter o  
  elif opcode == 'JUMP.E0':
    number = stack.top()
    if number == 0:
      pc = function_tracker[program[pc]]
    else:
      pc += 1
      
  #thats a zero not the letter o  
  elif opcode == 'JUMP.G0':
    number = stack.top()
    if number > 0:
      pc = function_tracker[program[pc]]
    else:
      pc += 1
  
  #thats a zero not the letter o  
  elif opcode == 'JUMP.GE0':
    number = stack.top()
    if number >= 0:
      pc = function_tracker[program[pc]]
    else:
      pc += 1
  
  #thats a zero not the letter o  
  elif opcode == 'JUMP.L0':
    number = stack.top()
    if number < 0:
      pc = function_tracker[program[pc]]
    else:
      pc += 1
  
  #thats a zero not the letter o  
  elif opcode == 'JUMP.LE0':
    number = stack.top()
    if number <= 0:
      pc = function_tracker[program[pc]]
    else:
      pc += 1
      
      