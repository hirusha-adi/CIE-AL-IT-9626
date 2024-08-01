---
title: 2. Hardware and Software
---

## Computers

### Mainframe Computers

- why used to produce census?
    - mainframes has a,
        - high speed of processing data
        - scalable
        - reliable 
    - amount of data to be processed is very large
    - as countries have a lot of people
        - it also keeps on increasing
        - census processes & produces more data
    - more poweful machines are needed as more data is added


### Super Computers

### Characteristics

- fault tolerance
    - both
        - whether computer will repair itself if an error occurs
        - a computer can operate even if components fail
        - without system downtime
        - computers operating quality can be reduce
            - but it does not fail completely
        - whether when a hardware component fails, is it hot swappable
    - super computer only
        - will run two copies of software
        - if one fails, the second copy will start

- heat maintainance
    - computers generate a lot of heat
        - due to quality and quantity of processors
    - it can be a problem when it overheats
    - to address this issue
        - good cooling systems are needed
            - can air cool with an AC - expensive
            - can water cool - cheap, efficient
            - build datacenter in a cold part of the world, eg: greenland.

## System Software

- directly operates the computer hardware
- both compiler and interpreter converts high level programming language to a lower level instructions

### Compilers

- features
    - translates the whole porgram as one complete unit
    - creates an executable file
    - is able to report on a number of errors in the code after compilation
    - does not need to be present in order to run the program (compiled executable)
    - can optimize source code to run as fast or as efficiently as possible
    - often produces a seperate object code program
    - converts high level instructions to machine language
    - entire file is compiled before execution
    - list of errors is created after the compiltation process
    - compiled program is directly executed using the machine code
    - has to be recompiled even if the smallest change is made

### Interpreters

- features
    - translates each line of source code inito an intermediate stage and then executes that line / statment
    - reports on errors as lines of source code are enetered
    - only a few lines of source code needs to be in memory at any one time
    - some interpreters execute code within a virtual machine
    - these have been designed to disallow code from directly accessing the data computer
    - converts high level instructions to an intermediate form
    - translates one statment at a time
    - stops translating after the first error
    - interpreter has to be in memmory for the program to run
    - can be modified at runtime (changing functions)

### Linkers

- a linker takes one more more object files and combines them into a single executable file

### Operating systems

### Device drivers

## Utility Software

### Anti Virus Software

- note: viruses are also a type of software
- scans computer for viruses
- software used to prevent, detect and remove malicious software (called 'malware' for short)
- can protect from: 
    - malicious browser helper objects, 
    - browser hijackers, 
    - ransomware, 
    - keyloggers,
    - backdoors,
    - rootkits,
    - trojan horses,
    - worms,
    - adware,
    - spyware, 
    - etc...
- signature based detection
    - compares the contents of  file
    - to its database of known signatures
- heuristic-based detection
    - detects malware vased on characteristics typically used in known malware code
- behavourial based detection
    - based on behavourial fingerprint of the malware at runtime
    - is only able to detect malware after they have start malicous actions
- sandbox detection
    - based on behavourial detection
    - but it doesnt detect behavourial at runtime
    - it executes the programs in a virtual environment
        - logging the actions performed by the file
- gives the user options to delete or qurantine the files

### Data Compression

- encoding information using fewer bits than the original representation
- two types
    - lossless compression
        - reduces the number of bits
            - by identifying repeated patterns
            - and encoding them in special ways
                - eg: Run Length Encoding (RLE), Huffman Encoding
        - same quality
        - information is not lost
    - lossy compression
        - reduces the number of bits 
            - by identifying unncecessary information
            - and removing them
        - reduced quality 
        - information is lost
    

### Disk Defragmentation

- organizes contents of the disk into smallest number of contiguous blocks
- attempts to create larger regions of free space using compaction
- some defragmentation utilities try to keep smaller files within a single directory together
- the movement of the hard drive's read/write heads over different areas of the disk when accessing fragmented files is slower
    - compared to accessing the entire contents of a non-fragmented file sequentially


### Disk Formatting

- prepares a data storage device for initial use
- organizes the tracks on a disk into sectors
- a new disk medium is fully prepared in order to store files
- the first stage is low-level formatting followed by
    - partitioning which makes the data storage device visible to an OS
    - followed by high-level formatting which generated a new file system

## Software

### Off the Shelf

- description
    - software that is ready-made and already exists
    - it is available to all bussiness and companies
    - it is owned by a company that created it
    - has to adapted to fit the bussiness that has purchased it

### Custom Written

- description
    - software that is specially developed for a specific company
    - it is made to accomodate that customer's particular preferences and needs
    - written by programmers to solve specific problems
    - owned by the bussiness that commisions it

- what
    - software created for defined purposes
    - does not need to be adapted for use
    - any built in settings can be changed
    - programmer will ensure device compatibility
    - if software doesnt meet companies requirements
        - programmers with have everything fixed
        - eg: ability to copy software to several devices
    - they will not have unncecessary bloated features
        - the usually takes less space than off the shelf software
            - so, less expensive storage costs
    - *company will own the custom written software, so, they can sell it to others*


## User Interfaces

- CLI & GUI
    - more accurate

- GBI & Dialog Interface
    - for handicapped users who cannot use keyboard and mouse
        - or control their limbs accurately
    - more expensive to develop
    - for reasons of hygene, not even a doctor is allowed to touch the device
        - then, use gestures or dialog to control device

### CLI

- Command Line Interface

### GUI

- Graphical User Interface

### Dialog Interface

- Dialog Interface
- stuff?
    - can speak into a microphone to control the device
    - requires training session with user
    - unreliable when there is a background noise
    - gives hands free control
        - can use when driving, can use voice instead of driving with one hand

### GBI

- Gesture-Based Interface
- stuff?
    - can perform a gesture to control the device
    - quicker way of initating a response from a device
    - less effective when several users or with background movement
    - gestures can be taught through manuals
    - unreliable when used in the dark
    - bad when driving, will have to drive with one hand while doing gestures with the other hand
    - unintentional gestures might be registered


## Hardware

- Another name for physical parts of the computer

### Input Devices

- Keyboard
    - type in values
    - advantages
        - experiences users can enter data more quickly
    - disadvantages
        - difficulty of entering amounts other than selecing numbers using a mouse
        - data is slow to enter (compared with DDE)
    - using the keyboard
        - can use CTRL + other keys to save, print, copy, paste, cut, etc... (keyboard shortcut)
        - can use arrow keys to navitage through text
        - can use tab key to indent, delete key to delete forwards, backspace to delete backwards
        - can use the alphbetic keys and number keys to type content

- Touch Screen
    - could be used to eneter amounts
    - quicker to enter data than using a mouse
    - may cause screen to be stained and make viewing difficult

- RFID reader
    - reader can be used to enter details from passport / bank card
    - quicker than manually entering data
    - readers are expensive to buy initially

- in Bank Cards (credit cards / debit cards)
    - uses a chip reader to read cards
    - reliable than reading a magnetic stripe
    - quicker than typing details from the card
    - contactless card readers speed up transactions as no PIN is required

### Output Devices

IMAGE HIERARCHIAL

- Printers
    - Dot Matrix Printer
        - not very clear comparatively
        - slow to print 
            - if busy, will cause queues of people waiting to print
        - less risk of this running out of paper
        - will have 'noise' in print (bad)
        - cheaper to run 
            - ink ribbon is cheaper than catridges or toners

    - Inkjet Printer
        - high quality tickets
        - slow to print 
            - (all copies, including the first copy)
            - if busy, will cause queues of people waiting to print
        - will need to change catridges more frequently
        
    - Laser Printer
        - quiality of print will be good
            - can see it clearly
        - takes time to produce the first copy
        - does not have tio change toner as often as inkject catridges

### Storage Devices

IMAGE HIERARCHIAL

- Optical Drive
    - Advantages
        - faster data access times (comapred to tape)
        - more viable when theres large variations of temperature
    - Disadvantages
        - not very portable (compared to tape)
        - more suspectible to damage when handling

- Magnetic Media
    - aka Tape 
    - Advantages
        - costs less per unit storage
            - so, more cost effective (for large companies)
        - stores more data
        - appropriate for server backups
        - less suspectible to damage when handling
            - because its completely encased
    - Disadvantages
        - costs more per tape
        - gets curropt if placed near a magnetic field

- Hard Disk Drives (HDDs)
    - Advantages
        - higher storage capacitie
        - cost less per gigabyte
        - lasts longer
    - Disadvantages
        - more suspectible to damage and shock
            - consists of various moving parts
        - access speed is limited
            - depends on how close the data is to the read/write heads
        - loud, have whirring sounds due to moving parts

- Solid State Drives (SSDs)
    - Advantages
        - have faster transfer rate
        - have quicker boot ups
        - can have almost instantaneous data access ()
        - all parts of SSD can be accessed at once
        - use less power at peak load
        - energy efficiency can deliver longer battery life in laptops
        - no moving parts, so, SSDs run silently
    - Disadvantages
        - low storage capacities
        - costs more per gigabyte
        - doesn't last long
            - NAND flash used in SSDs can only be used for a finite number of writes
        - choices and availability is limited

- HDDs vs SSDs

| **Feature**               | **HDD**                                 | **SSD**                                        |
|---------------------------|-----------------------------------------|------------------------------------------------|
| **Storage Capacity**      | Higher storage capacities               | Lower storage capacities                       |
| **Cost per Gigabyte**     | Costs less per gigabyte                 | Costs more per gigabyte                        |
| **Durability**            | Lasts longer                            | Doesn't last as long                           |
| **Shock Resistance**      | More susceptible to damage and shock    | No moving parts, so more shock-resistant       |
| **Access Speed**          | Limited access speed                    | Faster transfer rate, quicker boot ups         |
| **Noise**                 | Loud, with whirring sounds              | Runs silently                                  |
| **Power Consumption**     | Higher power consumption                | Uses less power at peak load                   |
| **Energy Efficiency**     | Lower energy efficiency                 | Better energy efficiency, longer battery life  |
| **Availability**          | Widely available with more choices      | Limited choices and availability               |
| **Lifespan**              | Consists of various moving parts        | Finite number of writes due to NAND flash      |


## Software Stuff (to Database)

- **NOTE: THIS BELONGS TO THE 'DATABASE' PART OF P1**

- file types
    - why use text file (generic file format) instead of using word processed file? 
        - file size is smaller
            - takes less storage space
        - text format doesnt need to buy license / software
            - eg: of word processing software
        - can be opened by more applications
        - data can be exchanged among different OS / Computers
        - word processing software has many versions
            - one may not support documents made with another verison

- propietrary software
    - software that is owned by an individual or a company (usually the one that developed it)
    - there are almost always major restrictions on its use
    - a software vendor delineates the specific terms of use in an end-user license agreement
    - its source code is almost always kept secret
    - usually covered by copyright which provides a legal basis for its owner to establish exclusive rights

- open source file formats
    - can be used and implemented by anyone
    - an open source file format can be used by both propietrary and FOSS
    - also called free file formats if they are not covered by any copyrights
    - so that anyone may use them at no monetary cost for any desired purpose

## Web Conference (to Digital Divide)

- **NOTE: THIS BELONGS TO THE 'DIGITAL DIVIDE' PART OF P1**

- how to setup
    - send emails to every person being invited informing them of the conference
    - he sends log in details to users
    - uploads any necessary documents for the meeting
    - sends a link to the website
    - enter his username and password (obtained from the provider)
    - select a start time and end time
    - in the meeting area, type an agenda
    - using the software select participants
    - select appropriate meeting space/room
    - select those participants who can enter the room
    - choose those who can be presenters
        - and who can manage the meeting
        - limit participation of participants, 
        - disable messaging, 
        - disable camers

- how to setup
    - setup equipment and software 
    - agree a date and time
    - send reminder to participants before they start
    - send invitation link, with meeting password
    - adjust webcam so that can be seen
    - create and enter virtual rooms
    - share documents with appropriate software
    - upload any necessary documents for the meeting
    - sends a link to the website
    - enter his username and password
    - using the software, select participants to accept in to the meeting
    - select appropriate meeting space/room
    - select those who can enter the room
    - limit the participation of participants, mute, disable messaging / camera, etc...
    - communicate by speaking into a microphone and looking at the webcam

