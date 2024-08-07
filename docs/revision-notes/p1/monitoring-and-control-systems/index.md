---
title: Monitoring and Control Systems
---

All Past Paper Questions: https://docs.google.com/document/d/1Ms7cSAQ7I4NGc3m3egiCirOHodjetUsTdt2eyuenYjI/edit?usp=sharing

## Analongue-Digital

- Microporcessors/computers cannot directly process analogue data

### ADC


### Processor


### DAC

## Monitoring

- Computers
    - never forget to take reading at regular interval
    - more accurate
    - several variables can be measures simultaneously
    - results processed automatically
    - can take readings from dangerous areas (using sensors)

- Humans
    - needed to place sensors
    - needed to interpret results
    - maintain broken senors
    - have to program the computers
    - have to plan where to place the sensors

### Uses

- Weather Stations
    - sensors are used to feed data back to computer
        - sesnors gather: humidity, temperature, rainfall, etc...
    - analgue data is converted to digital form for processing using ADC
    - compurter stores readings in a table
        - ready to be processed
        - plots graphs automatically
    - calculates minimum and maximum temperature
    - outputs graphs on screen

- CCTV monitoring
    - advantages
        - will monitor constantly
        - so, will keep criminals away
        - makes employees less likely to steal
        - if a crime occurs, CCTV fotage can be used as evidence
        - if conflict among employees, boss can decide what actions to take by watching footage
        - disputes with customer and employee, can share blame with this footage
    - disadvantages
        - not able to display every bit of an area
        - invasion of privacy
        - employees may feel uncomfortable
        - hackers can get into the system
            - and see everything
            - and delete footage of crimes commited

- Monitor Workplace
    - advantages (emloyer) 
        - software expensive to purcahse
        - system expensive to set up
        - can lend to lawsuits for piracy infringement
        - mistrusting employees creates trust issues
    - advantages (employee) 
        - video monitoring gaurantees their security
        - provides detailed view of what employees are doing
            - weather they are following orders, etc...
    - disadvantages (employee) 
        - allows employers to monitor without employees knowing
        - but, some employers do not notify employees
            - they secretly monitor (so, bad)

- Monitoring Pollution
    - place sensors at upstream and downstream in factory
    - temperature/light sensor connected to computer
    - ADC converts analogue data to digital data
    - so the computer can understand readings
    - readings are compared with pre-set limits
    - different results are printed out
    - graphs automatically produces
    - computer stores in a table, ready for further processing

- How to monitor data?
    - sensors are used to gather the particular physical variables
    - sensors feedback data computer
    - analgue data is converted to digital data by ADC
    - computer stores readings
    - computer compares to pre-set values
    - computer performes calculations and processing
    - calculates this at set intervals
    - computer produces graphs automatically

## Control Systems

- output affects the input

- Monitoring vs Control Systems
    - similarities
        - both involve the use of sensors
        - both do not require human output
        - both require ADC
    - differences
        - in control systems, output affects the inputs
        - acts in real-time
        - uses output devices like acturators

### Uses

- car park barrier
    - answer 1
        - (with micro-controllers)
        - pressure sensor / induction loop in driveway
        - sends signal to processor
        - ADC converts analogue signal to digital signal for microprocessor to process
        - microprocessor compares input with pre-set value
        - if its greater,
            - send signal to actuator
            - which raises the barrier
        - light sensor detects break in laser
        - when beam of light resumeds,
            - actuators activated again
            - lowring the barrier
    - answer 2 (detailed)
        - when car arrives
            - precence detected by induction loop
                - because electromagnetic loop is disturbed by metallic object
            - message sent to computer
            - computer sends signal to motor
            - motor raises the barrier
            - a light beam from one post passes across
            - to a light sensor in the other post
            - if microprocessor recieves signal
                - signal sent to motor to lower the barrier
            - else, barrier remains vertical 
        - when car leaves
            - gues recieved ticket from reception
            - exit barrier asks for the ticket
            - computer compares ticket with acceptable tickets to check validity
            - if it matches
                - computer sends signal to motor
                - motor causes barrier to raise
                - a light beam from one post passes across
                - to a light sensor in the other post
                - if light sensor sends a signal
                    - signal sent to motor
                    - to lower the barrier
                - else
                    - barrier remains vertical


- in bussinesses
    - computer controlled production lines
        - increase unemployment
    - computer controlled printing presses 
        - replace printing workers
    - IT technicians needed to maintain these infrastructure
    - number of new jobs are less than jobs lost

-  in homes
    - microcontrolled devices can be used to do small tasks, saving time
    - burglar alarms can be used
    - can lead to people becoming lazy
    - loss of household skills (due to use of microcontrolled devices)

- traffic lights
    - fewer traffic jam than manually controlled
    - input devices
        - induction loop
            - when a vehicle goes over it
            - the computer will get a signal
        - sound sensor
            - kerb stones constantly feeding back to computer sound level
            - if noise above set value limit, 
                - it means a vehicle has passed it
        - video camera
            - fixed above traffic lights
            - registers approaching vehicles
            - and sends to computer
        - push buttons
            - when predestrian presses a button
            - signal goes to computer
            - to register a pedestrian is waiting to cross
    
- street light
    - more economical
    - turns on/off automatically

- Air Conditioning in stores
    - increases costs of store
    - so, prices to the customer

## Input

- MICR
    - magnetic ink character recognition
    - advantages
        - characters are readable even if document is overprinted
        - high security
            - since they are difficult to forge
        - error rate reading them is small
    - disadvnatages
        - more demanging printing process
        - has difficult-to-achieve standards
        - causes a slower print
        - readers are expensive to purchase
        - recognizes fronts written in specific format only
        - MICR printer catridges are much more expensive
- OCR
    - optical character recognition
    - advantages
        - faster than entering large amount of text
        - cheapter than paying someone to enter text
        - allows documents to be made editable
        - will have a sofcopy, incase of a conflict
        - can read all data
        - in banks:
            - cheques can be processed after being deposited at ATMs
            - cheques can be processed after being sent by phone
    - disadvnatages
        - all documents should be checked manually and carefully
        - as its not 100% accurate
            - has errors:
                - 'm' instead of 'rn'
                - '0' instead of 'O'
        - less secure,
            - eg: in banks, checks are easier to forge
        - need expensive OCR equipment and software

- OMR
    - optical mark recognition
    - advantages
        - used in exams
        - easier for students to complete
        - essential candidate details can be pre-printed
        - faster to mark scripts
        - more accurate marking of scripts
        - statistics are more easily produced
    - disadvnatages
        - cannot express themselves easily
        - answers are not easily human readable
        - questions cannot be open ended
        - equipment is more expensive to purchase


## Other

### Expert Systems

- Knowledge Base
    - consists of a database of facts
    - inference engine 
        - uses rules base to reason through symptoms
        - uses facts in knowledge base for reasoning
        - compares to symptoms to those in knowledge base
        - uses rules base of IF...THEN...
    - knowledge base editor enables knowledge engineer to edit rules 

