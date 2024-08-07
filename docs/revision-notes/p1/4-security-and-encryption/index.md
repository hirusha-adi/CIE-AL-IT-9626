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

- can result in serious injury
- issues
    - fire hazards
    - electrocution
    - personal injury
- can be caused by
    - overloading sockets (causing overheating)
        - use a multi-pin adaptor, 
        - use a circuit breaker
    - overheating of computers
    - water split into live wires
    - handling bare wires
    - trailing cables can cause users to trip up
        - ensure cables are tied up
    - heavy objects falling off tables
        - use sturdy tables
        - ensure equipment is not at edge of the table

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

- other methods of keeping data secure
    - use minimum amount of confidential information
    - use anonimized information whenever possible
    - secure dispose personal information
    - have access control systems
        - eg: RBAC
    - secure the network with firewalls

- when sharing images
    - remove geo-tags from images
    - or any other juicy EXIF data
 

- parents should tell children to
    - dont give out personal info
        - home address
        - parents name
        - school name
    - use a nickname online
    - dont sent images of themselves(+family) to unknown people
    - make sure your privacy settings are secure
    - inform parents if being cyber-bullied
    - dont meet up with random strangers

- parents should
    - talk to child about what they are doing
    - keep computer visible
    - teach child to block people
    - let the child know its never too late to let the parents know


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

### SSL/TLS

- encryption protocols can be used
- all major web browsers currently in use support TLS
- client-server applications use SSL/TLS to prevent eavesdropping
    - by using encryption protocols
    - so, technically, can secure carry out bank transactions
- are used in web browsing, email, internet faxing, messaging, VoIP, etc...

- SSL
    - secure sockets layer
    - is old technology
- TLS
    - transport layer security
    - successor to SSL

- how TLS/SSL is used in client-server networks?
    - TLS is used for applications that require data to be securely exchanged
        - eg: browser sessions, file transfers, etc..
    - server sends digital certiciate to client
        - to open a TLS connection
        - client needs to obtain the public key
        - public key is found in digital certiciate
        - digital certificate authenticates the server to the client
            - client checks if certiciate was issued from a trusted CA
            - check whether the server is legitamate owner of public & private keys
    - client does TLS handshake
        - client tells server what version of SSL/TLS it uses
        - and lsit of encryption protocols its able to use
        - client tells the server it wants to setup a communication channel
        - handhsaking occurs before the transfer of data can take place
        - server tells the client the type of encryption it has chosen from the client's list

## Encryption

- when encrypted
    - its useless even if the message is intercepted
    - the message is meaningless
    - data is scrambled
    - cannot unscramble without key

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
- shorter amount of time
- less processing power to encrypt
    - and also decrypt the message
- less complex & fast & less secure
   

### Asymmetric Encryption

- often reffered to as public key encryption
- two keys are used
    - no need to transfer one key
    - so, more secure
- public key to encrypt data
    - public key is visible to everyone
    - is shared publicly
- matching private key to decrypt the data
    - is kept secret
- anyone with a public key can encrypt information, and can be ready by 
- it is not possible to deduce/re-calculate private key from the public key
- more complex & fast & more secure

## Malware

- industrial espionage
    - downloading without realizing
        - when clicked on adware
    - trojan / spyware can be used
    - malware gains access to environment variables & database contents
    - data collected is sent back to hacker
    - used to exploit weaknesse in software to gain access,
        - eg: priviliage escalation
    - targetted social engineering attacks (eg: phishihg, etc...)
        - and installs spyware 

- how to stay safe?
    - follow anti-malware policies
    - use anti-virus / anti-malware
        - detects and quarantees malware
        - asks user to delete or keep
    - keep anti virus upto date
    - use firewall to filter incoming traffic
        - and outgoing traffic
            - unknown ports
            - used by backdoors / reverse shells
    - use anti-spyware softwrae
    - use spam filter tools in email 
    - only download software from trusted source
    - report unknown behaviour to IT helpdesk engineers
    - disconnect from network soon

### Rotkits

- gives admin access to computer
- hiding to the user
- 'root' refers to admin account in linux
- 'kit' refers to software components used to impletent that tool
- can be installed in many ways
- allows attacker to maintain command and control
- controller can remotely execute files
- controller can change system configurations
- can access log files and spy on computer's usage
- hard to detect, runs at system level

### Malicious Bots

- to automate tasks
- used to gather information (web crawlers)
- also used to interact dynamicllay with websites
- self-propagating malware to infect a host and connect back to central server
- attackers can launch remote-control type flodding attacks
- can launch DDOS attacks
- can infect immediately 

### Ransomware

- encrypts data and thratens to share unless ransom is paid
- user files become decipherable
- enceryption key is given only if ransom is given
- iniltrates as a trojan or a worm
- from websites or infected email attatchments
- some allows the use of computer, but prevents opening files by encrypting them

### Trojan Horse

- ditinctive features
    - disguises authentic software
    - do not affect to infect other files
    - do not self replicate themselves

### Worm

- ditinctive features
    - standawlone malware
    - replicates itself
    - find vulnerabilities in networks (eg: samba)
        - copies sent to other computers
    - slows downt the network 

### Spyware

- ditinctive features
    - collects user activity
        - web browser activity
        - messaging activity
        - browser session cookies
        - saved bank card information
    - passwords sent to hacker (without user's knowledge)
    - keylogger logs keystrokes and sends to attacker
    - does not usually replicate like a worm
- how hackers can abuse these data?
    - can sell information to criminals
    - can impersonate
    - can trick banks into asking new card PIN or transferring (withdraw) large amounts of money
    - can buy extra credit cards
    

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
- how to be safe?
    - dont trust emails sent from unrecognized senders
    - only contact the bank physically
    - dont open links from unknown senders
    - dont send personal information over email
    - protect computer using firewall
    - keep anti-malware tools upto-date
    - look for grammartical errors

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
- how to be safe?
    - avoid links in text messages
    - dont send texts with personal info
    - if a message is from bank, visit the bank physically and confirm
    - neglect everything thats like: 
        - "call this number or we will cancel your credit card, etc..."

### Vishing

- meaning
    - victim recieves phone call
        - claims to be from a bank
        - and tells we detected fradulent activities
        - robocall, will ask customer to call the fake bank
    - scammer answers fake bank
    - scammer tricks the victim to send money to scammer's bank account
- how to be safe?
    - dont give sensitive information from phone
    - dont answer calls from unknown callers
    - log into your back and check for suspicous activity
    - register your phone number with "national do not call list"
    - dont call numbers sent in voicemail
    - check background information on phone numbers

### Pharming

- involves creating a fake website that looks like the actual website
- meaning
    - installs malware to computer
    - when user tries to access bank's website
    - will redirect to fake website that looks real
        - (redirects genuine website's traffic to own website)
        - victim enters personal information to fake site
        - it will notify the attacker 
- meaning (complex)
    - create and host fake website that looks like legit bank's site
    - fools the user into thinking they are in the correct site
    - malware spreaded by hacker
        - adds entries to host file
    - OR, in public wifi's
        - DNS settings are changed to point to fake IP for domain
    - so, when user accessed original site (domain), traffic is forwarded to fake site
    - site asks to enter fake information
    - hacker uses stolen information to log into user's bank account 
    - and withdraw money
- how to stay safe?
    - use upto-date anti-virus to prevent downloading malware
    - firewalls to prevent malware
    - use trusated DNS servers
    - use an upto-date trusted browser, eg: Google Chrome, Firefox
    - use trusted ISP
    - check digital certificate to ensure its an original website
    - be suspicous if the site has grammar mistakes
    - dont use public wifi systems

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


