# Readings

## Chapter 1

### Introduction

A computer fundamentally performs two functions: it calculates and stores the results of those calculations, executing billions of instructions per second and possessing significant storage capabilities. Historically, human computation was limited by manual calculation speeds and record-keeping abilities. Modern computers, however, have vastly expanded the scope of solvable problems, although some remain beyond current computational capabilities.

### Computational Thinking

Computational thinking differentiates between declarative knowledge (statements of fact) and imperative knowledge (procedures for deducing information). Algorithms, which are formalized sequences of instructions, embody imperative knowledge. An example is the algorithm for approximating square roots using Heron's method, which iteratively refines guesses.

### Flow of Control and Programming

Computational processes involve a flow of control, determining the order of operations through sequences and conditional jumps. Flowcharts visually represent this control flow using standardized symbols for processes and decisions.

### Programming Languages and Turing Completeness

The design of modern computers evolved from fixed-program machines to stored-program computers, capable of executing a wide variety of instructions. This versatility hinges on the concept of the Universal Turing Machine, which underpins Turing completeness. A programming language is Turing complete if it can simulate a Turing Machine, making all such languages equivalent in computational power.

### Programming Language Structure

Programming languages consist of primitive constructs, syntax, static semantics, and semantics. These components dictate the formation and meaning of instructions. Syntax errors are easily detectable and correctable, while semantic errors can lead to unintended program behavior, necessitating careful debugging.

### Error Handling

Programs can fail in several ways: crashing, running indefinitely, or producing incorrect results. The latter is particularly dangerous, emphasizing the importance of writing programs that clearly indicate when they malfunction.

### Practical Consideration

Writing effective algorithms requires precision, as computers execute instructions literally. This precision is crucial for developing reliable software that performs as intended.

## Chapter 2.1

Programming languages, though varied, can be compared along several dimensions:

Low-Level vs. High-Level: Low-level languages involve machine-level instructions (e.g., moving data bits), while high-level languages use more abstract operations (e.g., displaying a menu).

General vs. Domain-Specific: General-purpose languages apply to a broad range of tasks, whereas domain-specific languages, like SQL, are tailored to specific applications, such as database queries.

Interpreted vs. Compiled: Interpreted languages execute code directly, offering easier debugging, while compiled languages convert code to machine-level instructions, resulting in faster execution and less memory usage.

Python, a general-purpose, interpreted language, to teach programming concepts. Python is user-friendly, provides helpful runtime feedback, and has a wealth of libraries that extend its functionality. Despite its benefits, Python's weak static semantic checking makes it less suitable for high-reliability or long-term, large-scale projects.

Python's simplicity and extensive libraries make it an excellent language for beginners and for solving a wide array of problems

## Chapter 2.2

### Objects, Expressions, and Numerical Types

Objects are the core elements manipulated by Python programs. Each object has a type that defines its behavior. Types can be scalar (indivisible) or non-scalar (having internal structure). Scalar types include:

int: Represents integers (e.g., -3, 5).

float: Represents real numbers with a decimal point (e.g., 3.0, -28.72). They can also be expressed in scientific notation (e.g., 1.6E3 for 1600.0).

bool: Represents Boolean values True and False.

None: Represents a single value None.

Expressions combine objects and operators to produce new objects. For instance, 3 + 2 evaluates to 5 (an int), and 3.0 + 2.0 evaluates to 5.0 (a float). The == operator tests equality, and != tests inequality.

The type function can determine an object's type.

### Variables and Assignment

Variables associate names with objects.

In Python, a variable is just a name bound to an object. An assignment statement associates the name on the left with the object denoted by the expression on the right.
