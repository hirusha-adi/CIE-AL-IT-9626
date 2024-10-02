---
title: 1. Data and Information
---

## Introduction

All Past Paper Questions: [Click here](https://drive.google.com/drive/folders/169hxE5eR4Hxhvmr3-AwoyhbqAcX-ahEW?usp=sharing)

## Data

### Introduction

- what
    - just a collection of text, numbers and symbols
    - with no meaning to it
    - cannot be interpreted until  it is organized
    - data must have context to become information

- context
    - NOTE: 
        - "A possible context is that the data is about ###" 
        - "and the information we have might be ###, ###, ###, ###" 
    - example:
        - ![alt text](image.png)

### Validation

- why?
    - cant gaurantee is data is accurate
    - checking is data is sensible
    - checks if data entered is reasonable
    - even if data is copied correctly
        - it might be in an invalid format
    - only "check digit" can check for transportation issues
    - eg: format -> DOB should be as `nn/nn/nnnn` (where `n` is a real positive integer) 

- approaches
    - length check
        - examples
            - X characters long

    - range check
        - we should know the upper and lower limit
        - examples
            - between X and Y
            - dates
                - day: 1 -> 31
                - month: 1 -> 12
                - year: 1950 -> 2024 **(assumptions)**
                - but will also allow dates like: `31/02/2001`

    - check digit
        - can only be done on long strings

    - lookup check
        - be one of given values, like `typing.Literal` in python.

    - format check
        - examples
            - where `n` is any real, positive integer
            - 8 numbers: `nnnnnnnn`
            - dates 
                - `nn/nn/nnnn`
                - but will also allow dates like: `69/96/3000`

    - consistency check
        - examples
            - date of birth
                - calculate age and check if it matches
    
    - type check
        - eg:
            - no alpha to a numeric field

### Verification

- why
    - checks if data entered is copied accurately
    - helps to stop users from making mistakes
    - will pick up transportation errors
    - will pick up transcription errors
    - cant gaurantee is data is accurate
- methods
    - visual verification
        - compare data being entered to another copy
        - and check visually
        - done by human against a source document
    - double data entry 
        - usually 2 people entering the same data
        - each input compared against each other
        - verification is done by the computer
        - it will alert if two inputs do not match and they can decide which version to keep

### Coding

- advantages
    - speed up data entry
    - more accurate
    - easy validation
    - reduce length of data
    - less space required
    - small DB size = faster search
- disadvantages
    - approximations is too general (for numerical values)
    - hard to use in calculations
    - coarserning of data
        - several data starting with same letter
        - eg: color `B` doesnt tell if its light or dark
        - uncertain (obscure) about the meaning of data
- questions
    - ![alt text](image-1.png)


## Data/Information Types

### Types

1. static information
    - description
        - sources are carefully checked for accuracy
        - because they are hard to change once stored
        - there is limited amount of information
        - after creating, it cannot be changed
2.  dynamic information
    - description
        - information updated quickly
        - so, usually upto date
        - there can be many contributors
            - eg: blog websites 
        - data that is read from and not written back to a file
        - difficult to add information to static information source after it has been created
        - can have many contributors, so, inaccurate
        - eg: web page that is updated from time to time
- both
    - need analysis techniques
    - provides a mixture of both relevant and irrelevant information             

### Quality

- accuracy of collected information affects quality
- extremely high detail affects the quality of information somtimes
- irrelevant information affects quality
- more complete it is, better the quality

## Knowledge

- points
    - remebering a set of facts
    - use of information to solve problems
    - understanding that `25 = 5 x 5` requires knowledge

## Data Collection

###  Direct Data Sources

- meaning
    - data collected for specific purpose / task
    - by many methods: questionairres, data logging, etc...
    - gives data thats called "original source data"
- advantages
- diadvantages
    - expensive 
        - need to hire people/company to gather data
        - purchase equipment, like data loggers, printers, etc...
    - comparatively expensive
    - more time to gather data
        - (by the time the project is completed, the data maybe outdated)
    - small sample size  
- inaccurate information
    - errors made when data entering
    - misconfigured/uncalibrated sensors
    - people used in study aren't very representative
    - if question is not clear, we get irrelevant answers
    - open ended questions will produce answers that aren't relevant
    - if MCQ, no enough choices for answers
- types
    - questionairres
        - distributed among people
    - interview
        - if question is not clear, we get irrelevant answers
    - observe
    - data logging
        - sensors used to gather data that could be processed & interpreted
- examples

### Indirect Data Sources

- meaning
    - data obtained from third party
    - not necessarily related to our need
    - data collected for a particular reason, other that what its being used for
    - eg: population data can be collected from local government agencies
    - could collect data from local environmental groups
- advantages
- diadvantages
- types

## Data Processing

### Batch Processing

- rocket scientists to moon
    - used by payroll department to pay wages
    - would be used if scientists had collected a very large amount of data offline & neeed to process all at once
    - transaction file of hours worked is kept
        - and used by master file to update the master file
    - jobs setup to run without human intervention
    - can use computer when its less busy

### Realtime Processing

- rocket scientists to moon
    - suitable for controlling rockets
    - causes a response within specified time constraints
        - (miliseconds latency - extremely fast)
    - inputs are processed and affects the output
        - which in turn affects the input
    - controlling rockets often involve the use of sensors & control systems
    - allows scientists to take immediate action
    - if rocket goes off track, computer would immediately fire engines to correct in 

## Files

### Transaction File

### Master File

### Questions

- before process happens
    - transaction file is validated
    - transaction file must be stored in the same order as master file
- how transaction file is used to update the master file?
    - first record from transaction file is read
    - first record from master file is read
    - these two records are compared
    - if they do not match
        - computer writes master file record to new master file
    - if it matches
        - transaction is carried out
        - computer does the calculation
            - (tell what happens here)
            - (examples)
                - calculates the rate of pay: pay * no. of hours worked.
                - (using rate from master file and hours worked from transaction file)
        - processed record is written to new master file
    - next record from transaction file is read
    - and compared to the next reocrd of the master file
    - and so on...
    - this is done until last record of transaction file
    - then, at last: all remaining old master file records are written to the new master file.


- examples
    - ![alt text](image-2.png)
    - ![alt text](image-3.png)

## Other

### Proof Reading

- define
    - slow and methodical search for errors
    - careful reading and re-reading of a yet to be finally printed document
    - to detect any errors & mark corrections for
        - spelling errors
        - typrographical errors
        - grammatical errors, etc...
    - checking different elements in the layout like
        - headings
        - illustrations
        - colors, etc...
    - also check for amitted words and endings
- how
    - read carefully to find grammar/spelling mistakes
    - print a hard copy and screen (instead of using a screen)
    - read the essay out loud
        - to hear problems
        - that we may miss when reading
    - check issues in similiar sounding words
        - eg: its vs it's, their vs they're
    - read backwards, sentence by sentence
    - read forwards, to make sure subjects & verbs agree.

### Charts

- Pie chart
    -  how to improve
        - put labels pointing to sectors
        - attach percentages to sectors
        - attach number of X for each sector
        - use different colors for each sector (to easily identify)
        - have a chart legend 
            - eg: dashed lines files, dotted fill, solid fill, etc...

## Other (other)

### Coding (Other Types)

- encryption
    - points
        - scrambling of text in a message
        - encoding so only authorized people can access them
        - understood only if decrypted
        - can only decrypt with key
- codecs
    - are hardware/software needed to convert data
    - so it can be transmitted down communication lines
