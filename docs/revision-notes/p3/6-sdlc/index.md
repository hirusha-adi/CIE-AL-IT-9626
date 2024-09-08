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

### RAD

- stages
    - determine user reqiurements
    - create early prototypes (function, quickly)
    - gather feedback
    - use it to create high quality feedback
    - reapeat his until software is finished
    - test prototypes throughout development
    - crease user documentation
    - produce final product for rollout to users
- why (instead of waterfall)
    - project divided to small subtasks
        - (teams can work concurrently)
    - subtasks can make use of specialised teams
    - prototypes created quickly
    - development time is not wasted, 
        - prototype does not work as intended
    - (waterfall method) if project fails, start again 
    - can adapt changes in user requirement
    - can work well when developers telework
    - changes made before final product is created
    - client not surprised by unexpected end product


### Waterfall Model

- phases
    - create requirements
    - analyse to create models / schemes
    - design to create technical designs
    - implementing the code
        - integrating units of code
    - create techinical/user documentation
    - testing (using a test plan)
    - deploy software by 
        - installation
        - migration
        - support
        - maintainance


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

- examining documents
    - preparing
        - identify documents to explore
        - consider how they will be accessed
            - language & cultural barriers
        - acknowledge and address biases in humans
        - consider relevance of document
        - be clear about what to searching
        - consider ethical documents
            - eg: confidential documents
        - consider alternative sources (if requested)
    - examining
        - gather relevant documents
        - develop organization and management
        - produce data flow diagram
        - determine src/dst of documents
        - make copies of originals for annotations
        - assess authenticity
        - examine
            - purposes
            - background information
            - the content
        - keep records of observations


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


- good designs
    - on screen input (form)
        - should be straight forward
            - to reduce misunderstanding
        - consistent
        - simple to use & obvious
        - clear design with enough space
        - keep necessary keystrokes to a minimum to reduce time
        - form should include validation routines
        - use input controls
        - provide immediate feedback
        - appropriate use of white space

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

- types
    - alpha testing
        - leads to beta testing
        - stuff
            - usues white box & black box testing
            - by employees
            - uses lab/testing environment
            - takes place under control of developers
            - does reliability testing 
            - does security testing
            - crtical issues fixed immediately
        - features
            - type of acceptance testing
            - to identify erros before releasing to end users
            - uses both black & white box testing
            - usually work for the software developer
    - beta testing
        - stuff
            - involves black box testing (usually)
            - by third-parties
            - takes place under control of users
        - features
            - done by real end users
            - in real environment
            - final testing phase before release of product
    - other
        - comparisons
            - alpha vs beta
                - similarities
                    - last tests before release
                    - done by other (other than programmers)
                    - impacts final quality of product
- tester reporting error (report)
    - should have
        - purpose of test
        - how it was carried out
    - special test environment that was created for the test
    - expected reults
    - actual results
    - whether or not the software passes
    - recommendations for testing the software
- test data
    - why
        - to find errors in logic / formulae
        - to show errors in logic formulae
        - confirm validation routines work as expected
        - confirm given input
            - gives expected output 
        - check error handling
            - eg: abnormal inputs 
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
- phased implentation
    - effectiveness
        - done part by part
        - implementation done in stages
        - time is available for adjustments
        - users have time to adjust
        - technical staff concentrates on one part
        - problems (that arise) at start are less critical
        - training confusin for users
            - used to old system
            - less productive
        - system delivery unclear
            - long duration of change over
            - users workflow disrupted
            - more disruption to bussiness
        - check integrity of data before adding new module
        - 'fall back' to each stage becomes more difficult
        - implementation unclear
            - increases complexity
            - lack of motivation
        - need several adjustments
        - at later stages
            - fall back to old system
            - becomes impossible
            - so, should use half-completed new system


- parallel running (during migration)
    - advantages
        - can compare results (to ensure there's no error)
        - can use existing system
            - while deploying new system
            - so, production is not stopped
        - can use existing system to rectify errors
        - staff can be trained on new system
            - so, staff is confident
    - disadvantages
        - expensive
            - need to pay for two sets of hardware
        - production slows down
            - staff needs to update both systems at once
            - need to input data twice
            - increases data entry
            - to ensure accurate input to both systems
        - high maintainance time
            - slow production
            - more expensive


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
        - why
            - so installer knows what hardware is required
            - data structures can be amended by analyst
            - programmer understands how data flows
            - to provide basis for technical writers
            - provide reference for programmers
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

- how
    - determine if now system is better (time saving)
    - if easy to use
        - (+ requires less training)
    - go through requirements one by one
        - compare with requirements specification to check that all requirements have been met
    - get user suggestions
    - identify issues/problems
    - SDLC to started again to correct the issues
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
- why
    - pg53

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
        - incremental
            - advantages
                - whole system clearly defined and understoof
                - early user feedback
                - minor details allowed with time
                - allows additional features to be added
                - builds on a basic foundation
                - divides final product into parts
                - parts developed seperately
                - easy to identify errors
                    - testing and debugging can be done
                - product must sell early
                - new technology being used
                - required skills not available yet
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
