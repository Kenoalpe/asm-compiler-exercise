# custom-assembler
This repository provides an assembler written in Python for a simulated CPU in Logisim, enabling the conversion of custom assembly code into machine code.

## Getting started
### Clone:
`git clone https://github.com/Kenoalpe/custom-assembler.git`

### Change directory:
`cd asm-compiler-excercise`

### Get required packages (Linux):
1. Create a virtual environment:
   1. [venv in pycharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
2. Move into **venv**:
   1. `source venv/bin/activate`
3. Install requirements:
    1. `python3 -m pip install -r requirements.txt`

### Run:
`python3 -m app`

# How to use
It is important to notice that the output of this Assembler only works for a specific CPU made for this projekt.

## Writing an Assembler File
To use the Assembler you'd have to write an Assembler file named `asm.txt` containing your instructions for your CPU programm.

This particular Assembler supports the following instructions:
| Instruction     | Definition      |
| ------------- | ------------- |
| NOP           | No Operation; does nothing and moves on to the next instruction after one CPU cycle|
| INPUT    | Reads data from the external input field and writes it into register A|
| OUTPUT | Copies the content from register A to the output bus, where it's displayed in hex format |
| JMP `<adress>` | Jumps to `<address>` address in  RAM  |
| LOAD A,#`<value>` | Loads a constant `<value>` value in register A |
| LOAD A,`<address>` | Loads a value from `<address>` address of the RAM in register A |
| INC A | Increments register A by 1 |
| INC B | Incrementes register B by 1 |
| MOV B,A | Copies contents of register A into register B |
| ADD A,B | Calculates the **sum** of contens of register A and register B and writes the result in register A | 
| SUB A,B | Calculates the **difference** of register A and register B and writes the result in register A |
| AND A,B | Does a bitwise **and** of contents of register A and register B and writes the result in register A |
| OR A,B | Doas a bitwise **or** of contents of register A and register B and writes the result in register A |
| EQUAL | Checks if content of register A and register B is the equal and writes the result in register A (0h if equal, else not equal) |
| BEQ `<address>` | Jumps to `<address>` adress in RAM if contents of regsiter A and register B are the same |
| STORE `<address>` | Stores the content of register A at `<address>` adress in the RAM
| DB `<value>` | Definies a byte in the RAM |
| EQU `<value>` | Defines a constant for a label |
| RESB `<number>` | Reserves number of `<number>` bytes in RAM |

You can also place comments. They beginn with a `;` and end at the end of the line:
```asm
; This is a comment
INPUT ; this is a comment too 
; MOV B,A this whole line is a comment 
```

Additionally you can use `labels:` to acess your values and constants and define jump markers, like this:
```asm
my-byte-adress: DB 4A  ; Places a 0x4A at the position of this labeln in the RAM, can be used for instruction with a address parameter.
my-constant:    EQU 34 ; Definies a constant 0x34 at the position of this labeln in the RAM, can be used for instructions with a value paramter.
reverved-bytes: RESB 5 ; Definies 5 bytes, can be used for instruction with a address parameter, points to the first byte. Get placed where the instruction sits in the asm code.

my-jump-label:  MOV A,B
                INC A
                INC A

my-label:       SUB A,B
                AND A,B
                JMP my-jump-label
```

Now you can generate the machine code via `python3 -m app`
This generates an output `machine-code.txt` file.
You can now copy the contents of this file and paste them into your RAM of your Logisim CPU.

Well DONE!!!
