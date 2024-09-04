---
title: 4. Security
---

Questions left out:

p3-ch3-pg15
p3-ch3-pg88

## Encryption

- how to combat cyber crime
    - protects information by scrambling it
    - data cannot be understood without decrypting
    - asymmetric encryption 
        - has two keys
            - public key: available publicly
                - so, no need to send keys
            - private key: not shared
                - no risk of interception
        - used for communications + web
        - secure emails + text messages
    - symmetric encryption
        - to store data on disks
        - cannot be understood if data is stolen
        - protects cloud storage
        - protects data in USB devices
        - prevents use of stolen passwords
            - to protect personal data
            - eg: use in identity theft  


### Symmetric

- to protect data
    - advantages
        - stolen/intercepted data cannot be understood
            - without decryption key
        - data can be sent via insecure networks (eg: public wifi)
            - no issue, since data is scrambled
        - data remains confidential
            - can only be read by person with decryption key
            - eg: not by system admins
        - independent data security (from device) 
    - disadvantages
        - hard to administer encryption keys
        - if key is lost, data is lost
        - need more processing power
            - expensive
        - cross application incompatibility
        - it staff needs specialized training
        - symmetric keys have to be distributed everytime data is sent
            - increases preparation time


### Asymmetric

## AAA

### Authentication

- biometric
    - how it works? (good)
        - biometric parameter scanned into system
        - image converted into a binary system
        - binary pattern stored in system
        - pattern compared with existsing patterns (in database)
        - if match, accessed allowed
        - if not, show error
    - how it works?
        - scanner scans biometric factor
        - software converts it to standardized digital format
        - comparing match points of observed data with stored data
        - securely stored biometric data (for comparison)
        - to store student account data
        - to tranfer funds
    - paying with biometric authentication system 
        - ?? register for biometric program by presenting valid info ??
        - student scans biometric parameter (finger / face / iris)
        - scanner encrypts multiple point-to-point measurements
        - is biometric data is stored in centralized database
        - at the event
        - scans biometric parameter
        - compares data from new scan to encrypted data
        - system finds match in database
        - check if have access / authorization
            - check if have balance / money
            - if yes, pay and issue reciept
    - advantages
        - unique to invidual
            - so, extremely hard to forge
        - more than one characteristic can be used 
            - increased accuracy
        - no forgetting passwords, etc...
            - always readily can authenticate easily
        - password reset & administration (service desk) costs reduced
    - disadvantages
        - more time taken to enroll staff
        - high false match rate
        - can have high error rate 
            - wastes time / inconvenient
        - cannot share access (with others)
        - biometric parameters may change over time
        - staff may not like having their biometric data stored
        - staff maybe identified in places they dont need to
            - eg: in public crowds
            - violating user privacy



### Authorization


## Threats

- how to detect?
    - use anti-malware to
        - scan incoming data
        - scan existing data
    - examine signature and compare with database
        - (signature based detection)
    - do behaviour based detection
    - use firewall to filter 
        - packets, ports
        - incoming connections
        - outgoing connections
        - detect abnormal (network) activity
            - abnormal patterns
    - proxy servers to hold and analyze packets
    - use honeypots 
        - to track intruders 
        - and notify admins
    - check network logs to discover threats

## Malware

- botnet
    - describe
        - collection of many devices
        - malware is running on each conencted computer
        - security has been taken over by a third party
        - node controlled by a third party
        - connection uses standard internet protocol
    - how they gain unauthorized access to data
        - setup
            - devices has malware installed (without user's knowledge)
            - can setup peer-to-peer connections with controller device
            - bots connect together using internet protocols
            - use of IRC to communicate with remote server
            - bots can automatically scan computer
        - uses
            - bot herder directs bots to log keystrokes
            - can run other malware (on behalf of attacker)
            - can carry DOS attacks to other services
            - can send disguised images
            - can distribute spyware to gather data
            - can use user's computer resources


## Data Security

### Threats

- data destruction
    - deleting data
    - eg: deleting record from database

- data modification
    - changing data to a different value
    - overwriting original value
    - eg: changing value in a cell from 100 to 101 (in spreadsheets)

### Data Protection

- advantages
    - use of passwords to restrict access
    - enter OTP when logging in
        - prevents others from logging in 
        - even if password is shared
    - tokens do not need network connections
    - physical barriers
        - eg: locks on doores
    - security cameras recording all the time
    - encrypt data
    - backup & restore data
        - but does not protect the data from being damaged 

- disadvantages
    - passwords can be forgotten
    - sharing of password -> unwanted access
    - tokens 
        - have limited number of uses for access
        - limited battery life
    - physical barriers can be broken
        - eg: door locks 
    - security cameras must be watched all the times
    - watchers maybe distracted

- how data is lost
    - accidental deletion
    - malware deleting files
    - mechanical failiure of storage systems
    - magnetic interference with hard disk surfaces leading to loss of sectors
    - power failiure
        - loss of data in memmory buffers
    - theft of storage media, physical loss of files
    - physical damage
        - eg: natural disasters 

- how to protect?
    - prevent unauthorized access
        - use authentication with credintials
        - use firewalls
    - make subnets to restrict access to users
    - use VPN for secure connections
        - eg: to cloud / remote network
    - do regular checks on data integrity
    - use encryption (256bit) to restrict understanding data

- software methods
    - keep software upto date
    - keep antivirus upto date
    - provides real-time monitoring
    - use encryption to make data meaningless (unless decrypted)
        - protects confidential information
    - encrypt hard disks
        - safe even if device is lost
    - use biometric authentication
        - access only to authorized users
    - use of access rights / access control lists
        - which have allow / deny entries
    - use passwords on individual files
        - to control user access
        - encrypt documents (encryption key)
        - control editing rights
            - to prevent unauthorized users from accessing
    - use steganography to hide data in other files, eg: images (JPEG)
        - users are unaware of available data
    - backup
        - use automatic schedules
        - backup elsewhere (another device, and maybe also elsewhere)
        - can restore data is damaged
    - use of regular software updates
    - address security issues

- access rights
    - different permissions given to different users
    - eg: RBAC
    - setup ACLs (access control lists)
    - works on files and directories
    - permissions on folder maybe cascaded
    - files within folder have different permissions (than the parent folder)
    - permissions
        - read
            - can view file
        - write
            - can modify files
        - execute 
            - allows files to be executed
    - permissions must be set

### Backups

- backup strategy
    - make copies regularly
    - automate it
    - store backups on different media
    - implement incremental backup systems
    - keep records of backups
    - test the restore process periodically
    - have off-site backups
        - (eg: incase of fire)

## Protect

- from data breach
    - enforce password policies
        - require to change password every 90 days
        - password strength restrictions and stuff
    - use access control
    - keep software upto-date
    - use standardized software
    - dont install sketchy software (from sketchy sources)
    - use firewalls
        - protect with inbound+outbout rules
    - give training in
        - data security
        - identifying threats
        - how to respond to data breaches
    - use anti-virus software 

- using public wifi
    - logout of account after using
    - disable file sharing (eg: to disable unauthorized copying)
    - turn off wifi/bluetooth when not in use
    - only use HTTPS websites
    - use a secure VPN (with encryption)
    - dont allow auto-connect to WiFi
    - dont log-in to accounts
        - (verify secure connection before doing it)
    - dont use sensitive sites, eg: banking sites
    - dont login into open wifi networks

- when using credit card online
    - loss of card data
    - merchant can use them fraudulently
        - keylog with javascript to log card info
        - use illegally
    - victim unaware of loss
    - cardholder not present when transaction is made
    - might be redirected to fake site (eg: pharming)
    - might get emails/calls asking for OTPs and verification info
        - impersonating a bank
    - BIN attacks (bank identification number)
        - could reduce money from real active accounts
    - dont use http sites or public wifi
    - physical theft of card
    - card details stored by merchant are stolen

## Uncategorized

- identity theft
    - meaning
        - Unauthorised use of personal information
        - hacker pretends to be another person
        - Using information for personal gain (unauthorized)
        - to cause harm to victim
        - to create a new identity
    - impact
        - can use when doing crime
        - difficult to prove innocence 
        - ID might be rejected by institutions
            due to already fraudulent use of ID by others
        - difficult to correct false information
        - victims left financially viable for transcations they didnt do
        - innocent individuals caught for no reason
        - mental health issues for victims
        - victims are liable for things they didnt do
        - child's ID stolen at young age, get loans, child will be in debt at adulthood


