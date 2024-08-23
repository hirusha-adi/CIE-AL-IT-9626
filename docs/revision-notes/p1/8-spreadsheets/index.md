---
title: 8. Spreadsheets
---

All Past Paper Questions: https://docs.google.com/document/d/1ReuFmYn_-i8h5jH70eQGKaGyCpTkyM1Pej-U5FhyFAA/edit?usp=sharing

You can also learn more [here](../2-hardware-and-software/index.md#spreadsheet-software)

Questions remaining to do: `1, 3, 6, 10, 12, 17, 19, 22, 23, 26, 33, 40, 43, 46, 48, 52, 55, 57, 60, 67, 72, 81, 82, 87, 93, 95, 99, 106`

## Spreadsheet Software

### Key Terms

- Cells
    - specific location within a spreadsheet
    - defined by intersection of row and column
    - referenced by a letter and a number combination
    - give an example
- Rows
    - runs horizonatally in a spreadsheet
    - each row is identified by a number in the row header
    - give an example
- Columns
    - runs vertically in a spreadsheet
    - each column is identified by a letter in the column field
    - give an example
- Worksheets
    - a single page in a spreadsheet
    - each worksheet has a name
    - default worksheets are named Sheet1, Sheet2, Sheet3, etc...
    - give an example

### Uses

#### for Modelling

- why use spreadsheet?
    - can use relative & absolute cell referencing
        - to only increment parts of formula
        - that we need
    - cell protection 
        - makes sure the cell's data doesnt change by accident
    - user interface forms
        - makes it easier to input values to the model
    - macros
        - makes it easier to perform complex functions
    - automatic-recalculation   
        - so, dont need to evaluvate formula everytime
        - will update automatically
    - conditional formatting
        - allows to highlight values that match specific criteria
        - can see information at a glance
    - graphs & charts to detect trends
    - can also interact with databases
        - to provide data in the fields
        - reducing the need for manual input
    - goalseek can be used
            - to determine which variables need to be changed
            - to acheive a a target/goal 
    - pre-written functions allow users to create complex formulae
    - values can be changed to ask "what if" questions

- for financial models?
    - advantages
        - calculations performed more quickly
        - what-if statements can be asked/used
            - without re-building the model from scratch
        - provides quick answers to events
            - that may actually happen in a month, etc..
        - graphs produced to easily understand
            - are also updates automatically after re-calculation
        - graphs/charts updated automatically 
            - when new values
            - or any other update
        - they provide consisten results
        - can use templates for regularly used spreadsheet models (come pre-build & pre-installed)
        - data can be imported easily from a database
        - data can be entered more accurately due to computer based validation & verification 
        - quantities can be entered more accurately
            - from computer based validation
    - disadvantages
        - cannot account for every possible change
        - cannot model the exact values
            - eg: how much people think they will save
        - cannot predict what will happen incase of a financial crisis
        - need to consider many variables
            - to improve the model
            - try to account for many variables
            - as possible
            - to increase accuracy  
        - some situations will need purpose-built software
            - and expert knowledge
            - so, its expensive to buy
        - producing an effective model might get time consuming
        - complex sales predictions may need additional software
            - expensive to buy
            - expensive to train the staff

- to store sales data?
    - advantages
        - easy to use and store data
        - easy to
            - sort data
            - perform numeric calculations
            - functions: SUM, COUNT, AVERAGE
            - filter
        - can adjust layouts to generate output and reports
        - advanced features to do stuff easily
            - make subtotals
            - power pivot tables
            - pivot charts
            - analysis toolkit
        - easy to produce graphs
            - to show trends
        - can easily create models
            - financial models
            - to predict future growths  
        - automatically re-calculates data when data is edited
    - disadvantages
        - when amount of data increases
            - difficult to change and manage
        - difficult to produce well formatted reports
        - when new record added
            - need to modify formulas 
            - or named ranges
        - more difficult to create advanced filters

#### for Other Stuff

- spreadsheets vs database
    - spreadsheets  
        - advantages
            - easier to create complex formulae in spreadsheets
                - for calculating net wages
                    - after tax
                    - insurance
                    - pension numbers
            - easier to use functions like COUNTIF
                - to count the number meeting a specific condtion
            - charts are easier to produce
            - repeated data is easy to enter
            - easier to model scenarios
                - eg: future wage expenditure 
            - dont need to learn a lot
            - easier to get solution right away
            - easier to store data and use them
            - easier to enter repeated data 
            - good for creating one-time analysis
                - eg: exam scores once a year
        - disadvantages
            - when amount of data increases
                - spreadsheet becomes more complex to manage
                - difficult to manage
            - bugs out if data grows and evolves over time
            - as new data is added, might need to change formulea
    - database
        - advantages
            - data structure and normalization are available through multiple tables
            - data and referential integrity is inbuilt
            - queries and reports and easier to create
            - fields are easier to name and query
                - eg: name, address, rate of pay, wages
            - can use complex filters/queries
            - eg:
                - workers in specific department
                - earning a specific amount or more
            - queries can be saved and used/updated later
                - using database management software
            - can only create relational databases
                - to relate workers to payroll
        - disadvantages
            - hard to create calculated fields
            - need knowledge and skill to use this
            - hard to structure the information
            - more complicated to create
                - (than just entering data in spreadsheet)
            - not easy to copy and paste blocks of data
    - hybrid solution
        - is the BEST
        - where data is exported to a spreadsheet (from a database)

## Named Ranges

- why use?
    - saves time
    - no need to type an absolute cell reference everytime
    - not necessary to remeber (absolute/relative) cell references in the formula
    - easier to remeber names than cell ranges
    - easier to explain to other people
    - less prone to errors when typing a name, instead of cell ranges
    - easy to update formulas when data is added
        - only need to change cells belonging to the named range

## Cell Referencing

### Relative

- used by including a `$` within cell reference
- used when cell reference is kept constant
- cell references will not increment

### Absolute

- just letters and numbers are used
- cell references will increment

## Formula

- provide representations of mathematical operations
- user created
- can be simple or complex, as user wants
- may contain functions
    - can also write without using any functions
- eg: `=A3-C3` is a formula

- 

## Functions

- provided by spreadsheet software
- a function is also a formula,
    - but, parts have been pre-defined by the computer software
- most functions have a criteria
    - but not all
    - eg: RAND(...)
- eg: `=AVERAGE(A1:A9)` is a function

## Formula vs Functions

- representations of mathematic operations
- can involve use of cell references within them
- not visible in csv format

## Graphs & Charts

### Bar Chart

- has x-axis and y-axis
- viewers can see comparisons by comparing line height
- to represent company profits in a quarter
    - heigh of bar: how much money
    - x axis: category axis

- shows data with blocks of different heights
- this height represents the quantity
- used for comparisons in categories of data
- better for comparing the sales of different months
    - but not the trend (can be used, but not very clear)
- has the y-axis starting from 0
    - so, the trend is more difficult to determine

### Line Chart

- can emphasize trends over time
- allows viewer to trace it backwards
- to represent company profits for all four quarters
    - money value against year
    - joined together by (straight) lines

- show a series of points
- connected by straight lines
- with the horizontal axis typically representing time
- good at showing trends over time
- easier to see small changes
- y-axis does not have to start from 0

## Test Plans
