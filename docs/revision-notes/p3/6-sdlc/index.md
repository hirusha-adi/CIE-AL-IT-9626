---
title: 6. Software Development
---

More in

p3-ch3-pg80

## SDLC

- stages
    - list
        - analysis
        - design
        - development
        - testing
        - implementation
        - documentation
        - evaluvation
        - maintainance
    - how they are related
        - each stage has to be completed
            - before starting the next stage
        - deliverables 
            - from this stage is used in next stage
            - of one stage scan be used to revisit previous stage for alteration
        - process can be iterative with repeated movement
            - between adjescent stages
        - documentation from each stage  
            - used to produce system documentation
            - outcomes compared with initial requirements
        -  maintainance stage can result in revisiting the design stage to restart cycle

## Analysis

- data collection
    - online forms
        - explain
            - done by clerk
            - provides feedbkac + shows progress
            - ensures instructions understoof by clerk
            - ensures language is consistent
            - can prevent errors
                - validation techniques
            - can correct mistakes
                - suggest correction
            - shortcuts to maximise performance
            - reduce unnessesary information 
                - to not confuse the clerk
            - provides documentation when additional explanation is required


## Design

- design specification (document)
    - why
        - specify criteria for development
        - give guidance for developers
        - specify how system will meet user requirement
        - form part of patent application (for the desing)
        - form basis of accurate costing
        - be a part of legal contract between client and developers
    - contents (for a DBMS)
        - document stating
            - purpose for design
        - description (for intended audience)
            - for purpose of calculations
            - of formulas and calculations
            - error handling requirements
            - backup/recovery procedures
            - system startup/shutdown procedures
            - validation performed
                - and error messages shown
            - layout of report
            - securitu design
                - access control mechanisms
                - audit log provision
                - user authentication
                - encryption process 
        - identify intended products
            - using names and references
        - summary (of contents)
        - overview of design
        - relationship between data elements
        - file requirement description
            - eg: file access methods 

## Development

- agile software development
    - for
        - customer satisfaction is highest priority
            - (from early to late stages of development)
        - can easily manage changes in requirement
        - produces working software for client in short period of time
        - devs must work together
        - face-to-face conversation (more efficient)
        - promotes constant pace of development
        - iterative testing, so
            - errors corrected quickly (constant testing)
        - teams are allowed to self-organize
            - leading in better wokring practices
    - against
        - face-to-face daily meetings means must be in same workplace
            - travel costs
        - cost estimates change over time
        - milstones difficult to set
            - uncertain about what they will address in the near future 

## Testing

## Implementation

- pilot running
    - advantages
        - if system fails
            - only one part fails
        - easy to manage implentation at once
            - than a full direct change over
        - staff can be trained in small groups
        - staff can learn from mistakes (made by grouping)
        - trained staff can support training staff
        - only part of company is changed
            - implentation costs can be phased over a longer time period
            - saving company money (large costs at once)
    - disadvantages
        - full implementation takes time
            - eg: direct change over
        - can cause more disruption (to company)
        - IT staff has to support two teams at the same time
            - (unlike direct changeover) 
        - old and new systems have to interact data
            - so, data is at risk of loss
        - data lost if system fails

## Documentation

- types
    - technical documentation
        - purpose
            - for use 
                - after delivery of software
                - by technicians 
                    - when maintaining the software
                    - when re-developing the app
            - allows completion of program 
                - (when the original programmer is no longer available)
        - information to include
            - comments explaining how code works
            - comments on use of variables
            - data structures used 
            - file naming conventions used
            - detailed of used validation routines
            - navigation layout
            - database details
                - tables & their purpose
                - relationships
            - explaining stages of macro script
            - records of test logs and test results
            - security method details
            - details on how software can be installed
            - details on how to backup + restore app
    - user documentation
        - describe
            - explains end-users the functions of software
            - and how to carry out tasks
    - requirements specification
        - describe
            - details user requirements
    - system specification
        - describe
            - details software and hardware needed
    - design specification
        - describe
            - details of what software will be able to do







### OTHER

- new UI for doctors to access patient records
    - meaning
        - implementating the change in one center
        - before implementing the change in remaining centres
    - for
        - issues in one facility can be fixed 
            - (before addressing the other)
            - reducing the overall problems
        - users have access to new system + docs
            - they can assist others in its use
        - workload can be spread out over time
        - technicians required to fully implement new system
        - disruption caused in less
            - so, less danger to patients
        - user feedbacks to assist training
        - improving user experience at centers 
            - less impact to patient care
    - against
        - more time taken
            - to be available at all centers
        - more expensive
            - ?? IT staff will have to be relocated multiple times ??  
        - other staff moving between centers
            - should be familiar with both new and old UI
        - motivation of staff may decrease over time
            - slow work 

## Evaluvation

- ease of use
    - could be examined
        - (to check if its easy to do stuff) 
        - installation procedures 
        - start-up procedures
        - end-users can access and use as required
        - user navigation
        - system producing required results
            - with less errors
        - are features easy to find
        - assesment of user acceptance (of new system)
        - well structured user documentation
        - trouble-shooting advice to help users 
    - purpose
        - to check whether or not the new system
            - meets specifications set by analyst/designer
            - meets the designs
            - has expected behaviour
            - has problems
                - and how they might affect the funcationality
        - determine opportunies for adding new feature 

## Maintainance

- meaning
    - correcting a problem in the system
    - after system is broken
    - restoring functionality
- steps
    - diagnose the problem
        - (by testing system modules and components)
    - gather information (logs and users)
    - identify the problem
    - isolate faulty code/component
    - replace it with a new component
    - test it
    - check and remove viruses
    - re-format storage devices
    - perform a system restore
    - refer to technical documentation
    - make a report for reference
    - re-test system at the end

### Corrective

- description
    - modifies software to correct problems 
    - that have been identified in error reports from users

### Adaptive

- description
    - updates software after delivery to the users
    - In response to
        -  new environment
        - changes in industry
        - business requirements
        - changes to regulations & legislation.

### Preventative

- description
    - updates software after delivery to the users
    - To avoid possible errors 
        - that might occur in the future
    - To fix errors that do not affect function
        - (eg: CSS issues) 
        - (but may become significant in the future)

### Perfective

- description
    - Enhances 
        - performance after delivery
            - (during the lifetime of the software)
        - user experience
        - reliability + security  
            - (to increase its life span)
        - the ease of maintenance of software


## Unknown / Uncategorized

- prototyping
    - advnatages
        - customers need changes
            - so, high costs
        - quality can be improved by testing prototypes
        - prevents disasters at end
            - discovered in early prototypes
            - saves money
        - need more client involvement
            - show working model first
            - means clients are more aware
        - customers provides immediate feedback
        - meeting expected results
        - reduces miscommunications
            - end product more closely meets requirements
        - avoids later changes (saving time)
    - disadvnatages
        - insufficient analysis (deviated focus)
            - may overlook problems
            - overlooking better solutions, so, poor specification
            - so, bad engineering
                - hard to maintain
        - users might confuse prototype with actual product
            - (might assume the final product is incomplete)
        - user might need all features in prototype
            - slowed development
        - prototypes take time to develop (so, more expensive)
    - use
        - issues detected during development
        - users involved at all stages of development
        - users can interact with app
            - and give feedback
            - incooperated during development
        - users get a better understand of the product
        - to investigate potential market for the app 
    - types
        - throw away
            - stuff
                - discarded at any stage
                - produced quickly and cheaply
                - maybe non functional
                - more user involvement
                - easy to measure progress
                - easy to set time-scale
        - evolutionary
            - stuff
                - becomes a part of the final product
                - developed over time
                - functional from the inception (from start)
        - comparisons
            - throw away vs evolutionary
                - similarities
                    - develop early prototypes
                    - no full requirement
                    - devs and users interact frequently
                    - end users can add/request features
                    - use interactive reviews
                - differences
