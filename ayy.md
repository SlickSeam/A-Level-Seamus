AQA CS AS Notes

## 3.6 3.6	Fundamentals of computer systems 

### 3.6.1 	Hardware  and software
#### 3.6.1.1 Relationship  between hardware and software
+ Understand the relationship between hardware and software and be able to define the terms:
    + hardware is all the physical parts of a computer, such as the motherboard, CPU, input and output devices, storage devices. 
	+ software is all the written program that make a computer work as intended. 


#### 3.6.1.2 Classification of software
+ Explain what is meant by:
	+ system software is the software needed to run the computer’s hardware and application software. Examples: operating system, virus software, system monitor software, disk defragmenter etc. 
	+ application software is the software that performs one or a set tasks for users. Examples: word processor, spreadsheet, browser, graphic software etc. 
	
+ Understand the need for, and attributes of, different types of software.
	+ different types of software serve different purposes and priorities. Application software can't without an OS, and system software is more important as it is required to use the computer. Without system software applications would not be able to run.

#### 3.6.1.3 System software
+ Understand the need for, and functions of the following system software:
	+ operating systems (OSs)
	+ utility programs
	+ libraries
	+ translators (compiler, assembler, interpreter).

#### 3.6.1.4 Role of an operating system (OS)
+ Virtual machines are made to perform tasks and to hide the underlying system from the user. This makes it easier to display information to the user and underline hardware doesn't have to be managed at the same time.
	+ a scheduler is used to ensure all processes access the CPU and hardware without decreasing efficiency
		+ it has to ensure as many jobs/processes are completes as possible
		+ make use of the CPU time to the fullest
		+ be responsive so no delay is dealt to the user
		+ use all resources efficiently
		+ not ignore processes, and ensure all processes are treated fairly
		+ alter priorities according to the rules
		+ avoid 'deadlock'
	+ interrupt is a signal from hardware or software that needs to be dealt with by the OS. This halts the current process and forces the OS to handle the interrupt event. Software and hardware failure use interrupts. Interrupts can also be used when a task has been completed so the program can terminate or request services from the OS.

+ CPUs can only take one instruction at a time, and there will me many tasks with many instructions each. The OS manages these tasks by switching between them very fast, creating the illusion that they are all being processed at the same time to the user.
	+ the memory(backing store) is also managed by the OS, with a file system created to allow the management of the store. Files can be moved, read, and written in the store, and can be indexed to track the location of files. 
	+ I/O is managed by the OS by communicating with I/O devices (handshakes and drivers) and send/receiving data from the devices.
	+ A user interface is provided by the OS, through a command line(CLI) and a graphical user interface(GUI). 
		+CLI is a text based command prompt interface. An example would be the terminal in windows, OSX, and linux.
		+GUI includes windows, icons, menus, and the pointer(WIMP). This provides an interface that can be navigated, contain multiple applications through windows, and customisation. The GUI is easier to navigate than CLI as commands do not need to be memorised or used.

#### Role of utility programs
+ Utility programs are designed to configure, optimise, or maintain the computer. Tasks performed include:
	+ anti-virus software/ scanning for viruses
	+ disk defragmentation
	+ system monitoring
	+ file backup/restore
	+ firewall
	+ encryption
	+ compression/decompression

#### Role of library programs
+ Library programs are a collection of pre-written programs that can be used by other programs so they can run or be developed. They are normally made by experts and are bug-free/well tested


### 3.6.2 	Classification of programming languages
+ Programming languages are classes as high-level and low-level. 
+ Low-level programming languages are very similar to the underline hardware and are similar/based on the instruction set of the computer. Examples:
	+ machine-code
		+ Consists of binary digits and has an operation code(opcode) and an operand
		+ Opcode contains the instruction to be executed
		+ Operand contains the value or address of the value to be operated on
			```
			Advantages:		runs very quickly
			Disadvantages:	is hard for humans to read, takes a long time to do tasks
			```

	+ assembly language
		+ 2nd generation programming language. It was designed to be easier to read than machine code but still be similar to the underline hardware
		+ It uses words or strings instead of binary for the opcode
		+ Hexadecimal or decimal numbers replaced binary for the operand
		+ Assembly is specific to the computer architecture
			```
			Advantages:		runs very quickly, easier to read than machine code
			Disadvantages:	still takes a long time to write code and isn’t user friendly
			```


+ High-level languages allow the programmer to focus on the problem so they don't have to concern themselves with how the computer executes the instruction or how the data is fetched/stored. 
+ Imperative high-level languages is where each statement is a command to perform a single task such as assigning a variable or calling a function.


### 3.6.3 Types of program  translator
#### 3.6.3.1 Types of program translator
+ Understand the role of each of the following:
	+ assembler. translates assembly code into machine code instructions before being executed. 

	+ compiler. this translates code (such as JAVA, C, C#, C++) into machine code, also known as object code. bytecode can also be produced [very similar to machine code]. the object code is then executed. any changes made to the code will require the code to be re-compiled. it is common for the compiler to go through the code multiple times. the object code can also be executed at any time and saved. this code is often what is found on software installation disks.

	+ interpreter. goes through the code line by line to check for any syntax errors. once no errors are found it translates the code into machine code and it is executed. eg. python, ruby, perl, matlab 


+ Explain why an intermediate language such as bytecode is produced as the final output by some compilers and how it is subsequently used. bytecode is produced by virtual machines and is executed by the virtual machine or is converted into machine code.
	+ it is produced between source code and machine code. bytecode can be translated into any other programming language
	+ it needs to go through a bytecode interpreter, which adds another layer against malicious programs.
	+ jython is when python is compiled into java bytecode.

+ source code is the code that is **to be** translated. object code is the code that **has been** translated 



