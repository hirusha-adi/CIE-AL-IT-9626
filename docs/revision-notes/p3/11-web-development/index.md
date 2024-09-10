---
title: 11. Web Development
---

All Past Paper Questions: https://docs.google.com/document/d/1huzD3ywePF8riWc9sYnAZJBI1650B5WlNi45cHm9f9o/edit?usp=sharing


## Terms

- terms (general)
    - operand
        - numbers used in arithmetic operations
    - operator precedence
        - order of performing arithmetic operations
    - assignment operator
        - to give a value to a variable
    - literals
        - fixed values (/numbers/strings) assigned to a variable

- terms (javascript)
    - how object given a new property
        - new property added
        - by declaring a value
    - display properties using loop
        - JS code enclosed in HTML for use
        - use of `for...in` loop (JS)
        - define a variable (var/const) for storing (iterated) process
        - specify objects to be examined
        - enclose code within brackets - `{}`
        - include code to count iterations of loop
        - use code to pass results to HTML to display
            - eg: `document.getElementById("id").innerHTML = xxx`
        - use `console.log(...)` for debugging

- data types
    - string
        - purpose
            - to store and manipulate characters


- keywords
    - names of HTML 
        - objects / properties
        - event handlers
        - window handler objects
        - reserved terms  (used in other programming languages)


- iterations
    - `for` loop
        - how
            - loops through a block of code, given number of times
                - until condition is broken
            - requires 3 expressions
                - a declared variable
                - expression to evaluvated 
                    - at start maybe omitted
                    - at end, increment value ( of declared variable)
            - incrementing variable at end is optional
            - loop continues 
                - until condition is met
                - forever
            - if evaluvate statement omitted
                - `break` must be included
                - to exit the loop 
    - `while`
        - test condition at beginning
        - executes block if condition is true
        - may never be executed
    - `do ... while`
        - test condition at end
        - executes block even if condition is false
        - always executed, atleast once (first time, before checking condition)


- conditionals
    - types
        - `if...else`
            - explain
                - If ... else allows different actions to occur as a condition
                - condition produces a Boolean result
                - If TRUE an action is taken
                - If FALSE another (different) action is taken
                - Number is stored in variable
                - Comparison operators to test valuewith variable
        - ternary operator
            - Reduces code to a single statement to make code small
            - take up less storage space
            - Code is less complex to understand
            - easier to wite
            - less repetitive coding
            - Code is easier to debug
            - Can run multiple operations with code that is easier to follow
        - `switch...case`
            - Variable declared to store a specified condition
            - `switch(...)` used to gather data to be tested against the variable
            - Use of case to create blocks of code that may be executed
            - Variable with the condition listed for testing (against case)
            - Use of break to end out of `switch(...)` when variable matches case
            - Use of default at end of code block to specify code to be executed if no match found
    - logical operators
        - Used in if-else/switch statements 
        - to test if conditions are true
        - Compare the logic between variables
        - Can be used 
            - with any data type
            - in a more complex manner 
            - \- complex conditions \-
        - ![alt text](image.png)

- debugging / finding errors


