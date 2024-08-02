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

### Cloud Computing

- cloud storage
    - advantages
        - paying a low monthly fee
        - has no physical precense, so, takes no space
        - can backup data automatically
        - syncing ensure files are automatically updates across all devices connected
    - disadvantages
        - data is in hands of third party
            - so, less secure
        - providers can be transient
            - resulting in possible data loss
        - only as reliable as the user's internet connection
        - some may charge a cheap initial fee, but may increase prices later
        - users are at risk of not having data stored in compliance with government regulations if the physical storage location resides in a different country

## Software

- Software are programs used to direct the operation of a computer and related hardware

FULL DIRAGRAM IMAGE HERE


## System Software

- directly operates the computer hardware
- both compiler and interpreter converts high level programming language to a lower level instructions
- designed to run a computers hardware and application programs
- managed computer hardware

- Question

![alt text](image-2.png)

![alt text](image-3.png)


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
    - difficult for hackers to modify compiled code

### Interpreters

- features
    - translates each line of source code inito an intermediate stage and then executes that line / statment
    - reports on errors as lines of source code are enetered
    - only a few lines of source code needs to be in memory at any one time
    - some interpreters execute code within a virtual machine
    - these have been designed to disallow code from directly accessing the data computer
    - converts high level instructions to an intermediate form (called "object code")
    - translates one statment at a time
    - stops translating after the first error
    - interpreter has to be in memmory for the program to run
    - can be modified at runtime (changing functions)

### Linkers

- a linker takes one more more object files and combines them into a single executable file

### All

- why we need all of these?
    - many programming languages allow the wiritng of different peices of modules seperately
    - programming tasks are simplified as large programs can be broken into smaller manageable pieces
    - the linker is used to put all the modules together
    - without the comiler, the linker would have no object files to combine

### Operating systems

- tasks carried out
    - allocates memmory to software
    - sends instructions to printers
    - responds to input devices
    - opens and closes files on devices
    - multi-programming systems allocate equitable processing time to each task
    - sends error messages if an error
    - hanldes user logins
    - handles file permissions
    - provides the interface between a user and the computer

### Device drivers

- purpose
    - it controls a device attatched to the computer
    - without required device driver, corresponding hardware device fails to work
    - it is the interface between OS and hardware device
    - tells the OS how to communicate with hardware device
    - upon installation, it detects and identifies peripheral devices
    - handles translation of requests between device and computer
    - ?? defines where outgoing data must be stored before it can be sent ??


## Utility Software

- programs that help maintain the computer
- performs a very specific task, usually, managing system resources

### Anti Virus Software

- note: viruses are also a type of software
- to remove viruses
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

- to reduce storage file size of a file
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

- removes non-contiguous spaces on disk
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

### Backup Software

- to make copies for future use 

### File Copying

- creation of new files, which has the same contents as an existing file

### Deleting Files

- removing a file from the computer's file system
- most OS keeps track of where files are on hard disk using pointers
    - each file and folder on a hard disk has a pointer that tells the OS
    - where the file's data ends and begins with
- when a file is deleted, 
    - OS deletes pointers
    - marks secotrs containing that file as available
- its considered that files are no longer present in hard disk (considered as free space)
- uses a file allocation table (FAT) to store the location of files on the disk
- the delete utility just deletes the reference of the index in the FAT
- until OS writes new data, deleted files are still recoverable
- recovery programs can scan for deleted files and restore them
- if file is partially overwritten, can only recovery half of that file
- file recovery pointers work by reinstating pointers
    - reinstating the index in FAT

## Application Software

- group of software designed for the end user
- uses computer to perform specific tasks

## Software

### Off the Shelf

- description
    - software that is ready-made and already exists
    - it is available to all bussiness and companies
    - it is owned by a company that created it
    - has to adapted to fit the bussiness that has purchased it

- advantages
    - cheaper, as mass produced
    - available straight away
    - testing can be righteously carried out by developers, so, less bugs
    - many sources of support
    - includes helplines with operators who have already dealth with many problems, so, experienced

- disadvnatages
    - difficult to adapt to particular use required by the school
    - has bloated, distracting, unwanted extra features
    - may not be compatible with current systems and infrastructure
    - some very specific functions may not be available
    

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


- advantages
    - designed specifically for client's requirements
    - there will be no unncessecary features
    - it does not have to be adapter for use
    - programmers are available to make any changes required
    - programmers will ensure the software is compatible with company devices and infrastructure

- disadvantages
    - costs more to pay programmers to write more
    - testing is limited to only what programmers think is required
        - based on how they think the software will be used
        - not thoroughly tested
        - so, can have a lot of bugs
    - support is limited to team of programmers only
    - can take a long time to develop the software


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
- used by advanced computer users
- less likely to change over time
- uses less memmory
- requires user to learn many commands
- processing is faster than others

### GUI

- Graphical User Interface
- involves the use of WIMP
    - Windows, Icons, Menus, Pointers

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
    - very reliable as most users have similar gestures for communicating
    - requires a line of sight (unlike dialog interface)


## Hardware

- Another name for physical parts of the computer
- collection of physical components

### CPU

- parts
    - Arithmetic Logical Unit (ALU)
    - Control Unit (CU)
    - Memmory
    - tends to be contains on an intergrated circuit chip called a microprocessor

- function
    - CU fetched instrctions from main memmory
    - decodes instructions
    - executes instructions
    - all input data are transferred via CPU's memmory
    - memmory stores instrctions as well as data
    - data is stored in the CPU memory, whilst a calculation or instruction is being carried out
    - input data are transferred to the ALU for processing
        - ALU makes use of 4 basic functions: +, -, *, /
        - ALU uses certian logic operations such as comparisons, selections and matching

### Mother Board

- description
    - the main printer circuit board of a computer
    - connects the main components of a computer
    - contains
        - mass storage interfaces
        - serial and parallel ports
        - usb ports
        - network ports
        - expansion slots (PCI, PCIe)
        - controllers required to control standard peripheral devices
        - southbridge
        - connections for attatching additional boards
        - bios
        - CPU socket
        - RAM slots

### Sound Card

- description
    - manipultate and output audio
    - manipulate sounds stored on disk
    - recieve sound from input from a microphone
    - output sound trhought speakers connected to the bord
    - nearly all sound cards upport MIDI, a standard for represeting audio electronically
    
### Input Devices

- Keyboard
    - or 'number pad' - whats used in supermarkets
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
    - in a shop, if product bar code is damaged, it cannot be input

- Touch Screen
    - both input and an output device
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
        - in many countries, there is a maximum amount of money allowed to be charged with this.
    - chip and pin-reader
        - reads details from bank cards
        - more secure
        - more reliable than rading magnetic stripe
        - quicker than typing details from the card

- Bar Code Scanner
    - used to read bar codes from products


### Output Devices

IMAGE HIERARCHIAL

- Monitor
    - results are produces instantly
    - graphs / diagrams / figures are represented more accurately
    - scroll through results easily (instead of turning pages)
    - need to be infront of monitor to view the output

- Printers
    - easier to annotate printouts taken
    - printouts can be transported and viewed anywhere
    - may skim on whats on-screen.
        - so, more likely for errors to occur

    - Dot Matrix Printer
        - not very clear comparatively
        - uses continous stationery
        - slow to print 
            - if busy, will cause queues of people waiting to print
        - less risk of this running out of paper
        - will have 'noise' in print (bad)
        - cheaper to run 
            - ink ribbon is cheaper than catridges or toners
        
        - advantages
            - can use carbon copy paper (requires less filling of the sheet feeder)
            - could use continuous stationary
                - which would require less human interction
                - doesnt run out of paper very quckly
            - ink ribbon lasts longer and is cheap
            - when ink runs out, print gets fainter, but is still legible

        - disadvnatages
            - striking of heads cause a lot of noise
                - distracting in office envrionments
            - quality of output is not very good
                - 240dpi, but inkjet does 1200dpi
            - slow output
            - to buy a dot matrix printer is very expensive
            - has a more limited character set
             
    - Inkjet Printer
        - high quality tickets
        - slow to print 
            - (all copies, including the first copy)
            - if busy, will cause queues of people waiting to print
        - will need to change catridges more frequently
        - when ink runs out, prinout is less legible
        
    - Laser Printer
        - quiality of print will be good
            - can see it clearly
        - takes time to produce the first copy
        - does not have tio change toner as often as inkject catridges

### Storage Devices

- Exam Question:

![alt text](image.png)

![alt text](image-1.png)



#### Primary

- quicker than secondary
- ROM content is sometimes copied to RAM and subsequently read from RAM
- very fast access times
- no moving parts
- stores data in use and stores data for later user

- RAM
    - Random Access Memmory
    - stored information for short term usage
    - volatile: data is deleted once power is lost
    - stores active program data
    - ?? faster than ROMs ??
    - used by computers for storing data during computing processes
    - stores active program data
    - can both read and write

- ROM
    - Read Only Memmory
    - cannot be changed, only read
    - non volatile: data is retained even when power is off
    - stores permanent computer instructions
    - (to store bootup instructions) contains instructions for the computer to start up when it is turned on again
        - stores bootup instrctions - that will activate the hard disk
    - to store software that is unlikely to need frequent updates


#### Secondary

IMAGE HIERARCHIAL

- portable
- non volatile
- stores data for later use
- CPU can both read from and write to data 

- Optical Drive
    - uses laser to burn dark pits into medium
    - each dark pit is a binary digit
        - if there is a pit: 1, else: 0 
    - Advantages
        - faster data access times (comapred to tape)
        - more viable when theres large variations of temperature
    - Disadvantages
        - not very portable (compared to tape)
        - more suspectible to damage when handling
    - types:
        - CD
        - DVD
            - stored upto 8.7GB max (DVD - Double Side - Double Layer)
        - Blu Ray Disk
            - single blu-ray stores upto 128GB max
                - can store high quality videos
            - more expensive
            - costs less to buy per unit memmory
        - note:
            - BR drives can read DVDs
            - DVD drives cannot read BR dicsts 

- Magnetic Media
    - aka Tape 
    - small areas of tape are magnetized to represent 1/0
    - have surfaces coated with magnetically sensitive material such as iron oxide
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
    - have surfaces coated with magnetically sensitive material such as iron oxide
    - Advantages
        - higher storage capacitie
        - cost less per gigabyte
        - lasts longer
    - Disadvantages
        - consists of various moving parts
            - more suspectible to damage and shock / more prone to failiure
            - more pront to mechanical failiure
        - access speed is limited
            - depends on how close the data is to the read/write heads
        - loud, have whirring sounds due to moving parts
        - high power consumption

- Solid State Drives (SSDs)
    - uses electric circuits (NAND flash)
    - stores data with an electrical charge
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



---

## Other

---

- Pg 39 - 2019 March 12 - 1 (to Database)


## Software Stuff (to Database)

- **NOTE: THIS BELONGS TO THE 'DATABASE' PART OF P1**

- file types
    - why use text file (generic file format) instead of using word processed file? 
        - file size is smaller
            - takes less storage space
            - so, has small processing time
        - text format doesnt need to buy license / software
            - eg: of word processing software
        - can be opened by more applications
        - data can be exchanged among different OS / Computers
        - word processing software has many versions
            - one may not support documents made with another verison
        - its human readable and easy to edit manually
        - disadvantages
            - no distinction between text and numeric values
            - documents will have no formatting
            - cant embed images / graphics / videos
            - cannot have tables
            - resulting layout may make it difficult to read

- propietrary software
    - software that is owned by an individual or a company (usually the one that developed it)
    - there are almost always major restrictions on its use
    - a software vendor delineates the specific terms of use in an end-user license agreement
    - its source code is almost always kept secret
    - usually covered by copyright which provides a legal basis for its owner to establish exclusive rights
    - usually created by a company
        - with secret (proprietary) encoding scheme
        - so, it can be decoded only using software of company

- open source file formats
    - description
        - can be used and implemented by anyone
        - an open source file format can be used by both propietrary and FOSS
        - also called free file formats if they are not covered by any copyrights
        - so that anyone may use them at no monetary cost for any desired purpose
    - needed
        - not everyone can afford proprietary software
        - when transferring from one device to another, 
            - other devices may not have compatible software
        - archived proprietary files maybe difficult to read by new software


## Web Conference (to Digital Divide)

- **NOTE: THIS BELONGS TO THE 'DIGITAL DIVIDE' PART OF P1**

- how to setup 
    - answer 1
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
    - answer 2
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

- hardware required
    - server to handle video conferencing software
    - laptops/devices for each participant
    - microphone to speak to (sound - input)
    - speakers to hear (sound - output)
    - large monitor to see all participants
    - cameras/webcams to input pictures
    - router to connect to internet / network


## Web Authoring (no idea yet)

- using web authoring software instead of html?
    - advantages
        - do not have to spend time learning html
        - do not need to have web development knowledge/skills to make a functional website
        - can make websites with basic clicking and typing
        - writing html takes much longer
        - most are WYSIWYG editors
    - disadvantage
        - limits the users options as a designer
        - they only rely on templates with limited options
        - depening on what web authoring software package you use
            - they might not even different features
        - software may make user reliant to it
            - if software breaks, can no longer develop the site
        - learning html means sites can be built from any environment with basic text editing software
            - eg: notepad (most basic) to intelliJ webstorm ide (advanced) 

## Encryption (to Security)

- **NOTE: THIS BELONGS TO THE 'SECURITY' PART OF P1**

- how encryption stores data stores on a hard disk?
    - can use either symmetric or asymmetric encryption
    - can be through the use of public and private keys
    - causes data to be scrambled
    - requires an encryption key to encrypt
    - requires a descryption key to decrypt
    - resusls in data which is not understandable
        - even if read by someone else, it will have no meaning

