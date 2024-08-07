---
title: 4. Security and Encryption
---

All Past Paper Questions: https://docs.google.com/document/d/1ivd2MdIj0b15Y9NipaAJUMKutLsAbF6eisv1y07ACmg/edit?usp=sharing

## Safety


### Issues

- *in the form of:*
    - Issue
        - Prevention
    - overloading sockets causing overheating
        - CO<sub>2</sub> file extinguider in room
        - seperate sockets for each plug
    - water split into live wires & cause electrocution
        - do not allow food and drinks into the computer room
        - ensure all wires are properly insulated
    - trailing cables can cause users to trip up and injure themselves
        - ensure proper trunking is in place
    - heavy objects can all off tables can cause injury
        - use strudy stable desks
        - dont place heavy objects in the corner of desk   

### Accidents

- arise from suddent accident
    - can result in serious injury
    - issues
        - fire hazards
        - electrocution
        - personal injury
    - can be caused by
        - overloading sockets (causing overheating)
        - overheating of computers
        - water split into live wires
        - handling bare wires
        - trailing cables can cause users to trip up
        - heavy objects falling off tables

### Health

- health issues
    - arise from **long term use** of computers
    - issues
        - RSI
        - carpal tunnel syndrome
        - lower back pain
        - eye strain
        - headaches
        - upper back pain
        - neck pain
        - shoulder pain
        - etc...
    - can be caused by
        - typing at a keyboard continuously
        - gripping a mouse and repetitive clicking
        - sitting in the same position (with a bad posture) the whole day
        - staring at a computer screen all day
        - glare from screen

## e-Safety

- personal data, kept confidential
    - can commit identity theft
    - can trick banks into performing unauthorized transfers
    - if publicly shared as not home, burglars may come
    - sharing personal views about politics & religion can affect job opportunities
    - subjected to credit card scams
    - insurace could be denied depending on whats shared
    - can sell data like medical info to others

- when students use the inernet
    - social media
        - unauthorized access to perosnal information
        - grooming
        - sharing personal images without consent
        - inappriate communication
        - cyber-bullying
    - other
        - exposed to unsuitable videos
        - innacurate information
        - plagiarism and copyright infringment
        - illegal media download
        - innappropriate content

- schools's e-safety policy
    - discourages access to illegal content
    - discourages piracy
    - teaches that unauthorized access to personal information might occur
    - reduces risk of grooming
    - reduces inappropriate communication
    - discourages sharing personal information without consent
    - teaches students to evaluvate accuracy of information
    - discourages plagirism and copyright infringement


## Web

### HTTPS

- advantages
    - message cannot be read by third party
    - certificate gaurantees that information is from expected domain
    - gaurantees data is sent to the right place
    - makes MITM attacks difficult
    - search engines shows HTTPS sites first
    - green-padlock in browser tells the site uses HTTPS 
- disadvantages
    - uses server resources for encryption
    - introduces latencies
    - SSL takes longer to setup more round trips
    - browser caching doesnt work properly
        - modern browsers run slowly without caching
    - need to buy SSL certificates from certificate authorities
        - we can also make our own
        - but others dont trust it
        - so, warnings can arise
    - there are proxy caching problems
    - everything is encrypted, including packet headers and contents
    - any caching that might have happened between two points at which data is encrypted and decrypted is blocked   


## Encryption

- disk encryption
    - advantages
        - other users cannot open (without permission)
        - file remains encrypted even if moved
        - can be used on any files
        - users with permissions should first decrypt and then use
        - other users get an error message
    - disadvantages
        - files lost if (irreversibly)
            - password is lost
            - OS fails
            - OS is re-installed

- email encryption  
    - advantages
        - protects contents from hackers
        - just passwords on email accounts are not enough
        - email providers never encrypts email (+attacthments)
        - recipients mail server may not be secure
        - without encryption, email sent as plain text
        - with encryption, email is scrambled and sent, so, unreadable
            - must unscramble and read contents  
    - disadvantages
        - hackers can intercept and delete emails
        - encrypting with private keys requires key to sent, which can be intercepted by hacker (symmetric)
        - managing digital certificates can become complex and time consuming

### Symmetric Encryption

- only private key
    - used to both encrypt and decrypt the messages
- 

### Asymmetric Encryption

- often reffered to as public key encryption
- public key to encrypt data
    - public key is visible to everyone
    - is shared publicly
- matching private key to decrypt the data
    - is kept secret
- anyone with a public key can encrypt information, and can be ready by 

## Malware

### Trojan Horse

- ditinctive features
    - disguises authentic software
    - do not affect to infect other files
    - do not self replicate themselves

### Worm

- ditinctive features
    - standawlone malware
    - replicates itself
    - copies sent to other computers
    - slows downt the network 

### Spyware

- ditinctive features
    - collects user activity
    - passwords sent to hacker (without user's knowledge)
    - keylogger logs keystrokes and sends to attacker

### Adware

- distinctive features
    - Automatically generates advertisements in order to gain revenue for its
    - author
    - Advertisements may appear in the user interface/screen shown to the user
    - by the software
    - Examines which intemet sites visited and presents advertising according to
    - the types of goods/services featured on these/usually the type of
    - goods/adverts the user is interested in.

## Social Engineering

### Phishing

- meaning
    - sending an email to lure personal information from victims
    - may include URL to website
        - looks like bank, but a fake website
        - asks customer to enter bank details
    - easily grabs attention
        - eg: We confirm that you have signed up to our service and will be charged 50$ per month.

### Smishing

- meaning
    - sending a text message to lure personal information from victims
    - text message may include 
        - a URL
            - looks like a bank's website (but its fake)
            - asks for personal information
        - a phone number
            - that connects to a scammer asking for bank details
        - message usually grabs immediate attention

### Vishing

- meaning
    - victim recieves phone call
        - claims to be from a bank
        - and tells we detected fradulent activities
        - robocall, will ask customer to call the fake bank
    - scammer answers fake bank
    - scammer tricks the victim to send money to scammer's bank account

### Pharming

- involves creating a fake website that looks like the actual website
- meaning
    - installs malware to computer
    - when user tries to access bank's website
    - will redirect to fake website that looks real
        - (redirects genuine website's traffic to own website)
        - victim enters personal information to fake site
        - it will notify the attacker 


## General Online Safety

- only use websites recommneded by teachers
- think twice before opening an email
- should not now how to block and report unwated users from social media styles
- dont use real name of games like sites


## Other (Move)

### Software (for software and hardware)

- blogging, which software can be used:
    - Using word processing it is easier to edit documents ready for inclusion in the
    - website compared to text editors, spreadsheets and databases
    - Using word processing it is easier to format documents ready for inclusion in
    - the website compared to text editors, spreadsheets and databases
    - Using word processing it is more difficult to enter statistics and manipulate
    - these compared to spreadsheets and databases
    - Easier to calculate statistics with a spreadsheet than using database software
    - Can produce charts to show sales growth with a spreadsheet easier than using
    - a database
    - Databases could be used to store and process sales figures easier than a
    - spreadsheet
    - Easier to query a database than using a spreadsheet
    - Easier to produce reports with a database than a spreadsheet
    - With a text editor formatting is not lost when convening to HTML
    - Using web authoring package is easier to produce a blog than using text
    - editor...
    - ...easier to use than text editor as functions are provided. 

- antivirus
    - Scans the computer to make sure it is not infected with a virus/to find
    - viruses
    - Compares with existing viruses/detects changes in behaviour of files
    - It may quarantine the infected programs
    - It will ask the user whether or not they want to delete the infected programs
    - (Does background scans of downloads and attachments for viruses) and
    - informs the user if anything found.

- backup software
    - Creates (additional exact) copies of files, databases hard disks or network
    - servers
    - Use these copies to restore the original contents in the event of data loss
    - Asks user to enter type of backup
    - Asks if you wish to restore the backup
    - Asks if you wish to verify the backup
    - Asks when backup is to take place/frequency of backups.

- disk defragmentation software
    - Rearranging files stored on a disk
    - Causes data to occupy contiguous storage locations
    - Physically organises the contents of the mass storage device used to store
    - files
    - Organises data into the smallest number of contiguous regions (fragments)
    - Attempts to create larger regions of free space.

### Digital Divide

- in schools
    - BYOD widens digital divide 
    - widens digital divide
        - Students whose families can afford the devices have an unfair advantage
        - Teachers find it difficult to manage learning activities when they have to
        - support multiple platforms and device types
        - Some activities and applications may only be compatible with certain devices
        - The gap widens as underprivileged students lack access to high performance
        - computers at home
        - Underprivileged students do not have intemet access at home so they do not
        - leam the same things putting them at a distinct disadvantage.
    - rectify digital divide
        - Teachers could be given time to train on and understand the platforms they are
        - using
        - Teachers could have to learn how to integrate them into a class of students
        - who may not have access to the internet or mobile devices at home
        - Schools need to have different versions of software that can be used on all
        - devices
        - Libraries and schools should offer technology training for parents
        - A fund for the purchase or subsidy to purchase machines for poor children
        - A stock of spare machines kept in school in case students do not have
        - machines
        - A list of software could be issued to staff which runs across all platforms.


