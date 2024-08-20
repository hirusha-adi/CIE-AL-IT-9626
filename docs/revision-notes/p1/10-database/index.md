---
title: 10. Database
---

All Past Paper Questions: ...

## Managmehnt Information Systems

- how efficiently?
    - provides past, present and prediction information
    - helps in decision making
    - MIS manager 
        - analyses bussiness problems
        - designs and maintains computer applications
            - to solve organizations problems
        - helps with project management
    - used to create reports and charts
        - sales
        - inventory
        - production
    - reports provided at regular intervals
    - to help evaluvate companies performance
    - to spot trends in revenue growth

- description
    - helps with decision making
    - help with project managment
    - gather and information about various aspects, like
        - personnel
        - sales
        - inventory
        - production
    - to create reports
    - to evaluvate company's performance
    - to compare reports (daily, weekly, monthly, anually)
    - to spot trends in revenue / growth / profit
    - to assist them in making predictions about company

## Queries

### Static Parameter Query

- a query that is fixed
- examples
    - search for John (static parameter query)
        - everytime, the query will search for first_name John
        - if want to search another name
            - open query in design view
            - change first_name to that name

### Dynamic Parameter Query

- examples
    - search for John (dyanmic parameter query)
        - she can type different names
        - everytime the query is run
            - dialog box asks for first_name
            - or any other parameters
        - saves time of designing

## Normalization

Questions

- pg. 4

### 0NF (Zero Normal Form)

#### Description

Also called "unnormlized" data

This is an unnormalized form where the table may contain duplicate rows and non-atomic (multi-valued) attributes.

#### Features

- **No Structure:** Data may be stored without any specific structure or constraints.
    - no Primary Key 
- **Repeating Groups:** Columns can contain sets or lists of values.
- **Redundancy:** High potential for data redundancy and anomalies.

### 1NF

#### Description

A table is in 1NF if it has a primary key and all attributes are atomic (cannot divide).

#### Features

- **Atomicity:** Each column contains single, indivisible values (no lists or sets).
- **Primary Key:** A unique identifier for each row, ensuring that all rows are distinct.
- **Fixed Number of Columns:** The number of columns is fixed, and each column contains values of a single type.
- **No Repeating Groups:** Data is organized into rows and columns, with no repeating groups or arrays.

### 2NF

#### Description

A table is in 2NF if it is in 1NF and all non-key attributes are fully functionally dependent on the entire primary key.

#### Features

- **No Partial Dependency:** Every non-key attribute is fully dependent on the whole primary key, not just part of it (important for tables with composite keys).
- **Elimination of Redundancy:** Reduces redundancy by eliminating partial dependencies.
- **Improved Data Integrity:** Ensures that updates, deletions, and insertions maintain consistency in the database.

### 3NF

#### Description

A table is in 3NF if it is in 2NF and all attributes are only dependent on the primary key, not on other non-key attributes.

#### Features

- **No Transitive Dependency:** Non-key attributes are independent of other non-key attributes, only depending on the primary key.
- **Minimal Redundancy:** Further reduces redundancy by removing transitive dependencies.
- **Better Data Integrity:** Simplifies the data structure and reduces the potential for anomalies during data manipulation.

## Datatypes

- Date
    - description
        - can be in the form: mm/dd/yyyy
    - size
        - 3 bytes
- Boolean
    - description   
        - stores only 2 entries
            - 1 or 0
            - True or False
    - size  
        - 1 byte
- Text
    - description   
        - when data consists of letters
    - size  
- Lookup Table
    - description   
        - when only a limited number of options
    - size  
- Integers
