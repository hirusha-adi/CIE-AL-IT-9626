---
title: 3. Networking
---

## Networks

### Computer Networks

- Advantages
    - easier to share files in group projects
    - easier for teachers to monitor students when working
    - easier for network manager to roll out new software
    - can access internet more easily
    - school intranet would become available to all students more frequently
    - can share peripherals
- Disadvantages
    - easier for students to share work
        - which could lead to copying
    - bigger server maybe required when more clients added to network
    - extra network points needed, so, expensive
    - if server breaks, it might be unaccessible
    - viruses can transmit easily (worms)

### Mobile Networks

- Advantages
    - more coverage than WiFi
    - forces users to depend upon hotspots in each area visited
    - 4G offers a coverage of 30 miles 
        - and more and with overlapping networks
        - high ranges means connectivity all the time
    - mobile devices can be used out in the field
    - portability
    - big problemts with wifi networks in online security
- Disadvantages
    - more expensive
    - quality can be poor if you are not close
        - could go 2G, 3G, etc..
    - power consumption issues on devices powered by batteries
    - mobile VPNs are unsafe to connect to
    
### Topologies

- LAN
    - covers smaller geographical area
    - does not always need a router to connect computers togethers

### Connection Types

#### Client-Server Networks

- more secure than P2P networks
- servers will handle authentication and authorization to accessing resources
- if a client crashes/disconnects, it doesnt affect other clients or the server

#### Peer to Peer Networks

- can communicate and share files with every other computer on the network
- Advantages
    - cheaper (no need to buy servers)
        - does not servers
        - as files accessed from inidividual's workstations
        - no need to pay IT staff (System Administrator, Network Technicians)
        - overall cost of setting up is cheaper
    - very redundant
        - if one computer fails, it will not disrupt anything
        - everything else will continue    
- Disadvantages
    - files and folders are difficult to recover as they cannot be centrally backed up
    - more difficult to share
        - with magnets and torrent descriptor files
    - less security than permissions
    - system is not cntralised, hard to administrate
    - more expensive security, all devices should have its own anti-virus
    - diificult to have more than a few users
    - peers should have good storage too
    - when peer being accessed by other peers, it might slow the computer down

## Internet

- meanining
    - global system of interconnected computer systems
    - uses TCP/IP to link devices
    - network of networks linked by an array of electronic, wireless and optical networking technologies
- there is a danger of accessing inapproprate / insure websites
- for communication
    - advantages
    - disadvantages


## Intranet

- private networked used within one organization
- can only be accessed by workers within organization
- based on TCP/IP protocls
- used to share information within the organization
- tends to be a LAN

## Extranet

- website that allows controlled access to authorized users to an organizations network
- usually only allows access to a subset of information on the organizations intranet
- provides access to specific services without granting access to organizations entire network
- operates within VPN framework
- operated over public telecommunications protocls

## Connection Types

- ADSL
    - asynchronous digital subscriber line
    - bandwdith and bit rate is greater toward the subscriber
    - ISPs usually provide ASDL as a service 
        - to recieve internet acces
        - in a relatively passive mode
    - video conferencing would stutter due to low speeds
- SDSL
    - synchronous digital subscriber line
    - bandwdith and bitrate in the downstream direction
    - aimed at bussiness customers
    - more expensive
    - high bandwdith
        - can use for video conferencing
- ISDN
    - integrated services digital network
    - allows simultaneous digital transmission of voice, video, data
        - over PSTN (Public Switched Telephone Network)
    - Circuit swicthed telephone network system
        - also provides access to packet switched networks
        - results in better quality
            - than an analgue phone can  
    - extremely expensive
    - HD videos conferencing achievable
        - with PRI (Primary Rate Interface)
        - alsmost similar qualities like when using SDSL
        
### Services

- e-mail
    - electronic mail
    - email is a message that may contain text, files, images or other attatchments
    - sent through a network to an individual or a group of individuals

- WWW
    - world wide web
    - description
        - system of internet servers
        - that support formatted HTML documents
        - tends to be upto date
        - has vast amounts of information
    - how it works?
        - invented by Tim Berners Liee in 1989
        - can be accessed via the internet
        - accessed using web browsing software
        - HTML is a markup (formatting) lanuage for WWW
            - web pages are text documents formatted and annotated using HTML
        - uses URL (Uniform Resource Locator) 
            - an address thats unique to identify the web page
        - HTTP allows retireval of linked resources across the web
        - HTTPS provides secure websites
        - web pages may contain images. video, etc...
        - hyperlinks allow users to navigate between web pages
        - comporises websites made up of a number of web pages
        - is basically a system of web servers (serving HTML documents)

- video conferencing services
    - to conduct conferences between two or more participants
    - at different sites
    - by using computer networks to transmit audio and video
    - video codecs used to transfer data
        - requires digital compression of audio and video streams (in real time)
        - hardware/software that performs compression is called a codec
        - compression ratios of 50:1 are achieved
        - digital stream is subdivided into data packets
            - which are transmitted through digital network
        - each packet has a 'header' that identifies its contents
        - protocol used is usually determined by the need to have reliable or unreliable communications
        - TCP is a protocl designed for error free transmission of data 
            - when delivery needs to be assured
            - will retransmit missing packets when data is lost
            - can cause delays and reduced throughput
        - UPD is a less reliable protocol
            - if data is lost, its not retransmitted
        - video conferencing should use UDP over TCP
            - because packets arrived late would ruin the conference 

- VoIP
    - Voice over Internet Protocol
    - delivery of voice communications 
    - and multimedia sessions over IP networks

- instant messaging
    - to communicate vis messages in real time over the inertnet

- video streaming
    - video is sent to viewer in real time

- file transfer
    - transmitting files over a computer network like the internet

## VPNS

- Virtual Private Networks

- Meaning
    - is not physically a private network
    - uses internet other than WAN to transmit data
    - data remains encrypted throughout transmission
    - data is only decrypted at destination computer
    - this process is called tunneling
        - as it uses secure means to tunnel
        - through a publicly accessible network
    - uses public telecommunications system
    - normally consist of LAN that maybe remote to each other
        - like different branches of an organization
    - enables organizations to communicate over a large area
    - cheapter than creating conventional WAN
    - the security used consists of firewalls, encryption, the use of IPSec - IP Security 

- Advantages
    - offer a much higher level of secure communication when compared to other methods
    - every file coming into a computer or going out from a computer is encrypted
    - so, no unwanted user will be able to open the files and understand it
    - can be used to work automatically as part of logging on
- Disadvantages
    - company may not permit him to use other third party software on his computer
        - in order to safegaurd the integrity of their VPN connection
    - use of mobile device to iniate access to VPN can cause security issues
    - if local wireless network is insecure, or using public wifi
    - packet loss will be higher with the VPN and cause data to be lost and need to be retransmitted
    - increasing time taken to recieve documents
    - connection depends on ISP, so, performance can be variable
    - will need to install extra anti-malware tools to ensure his PC is clean
        - to meet the company's security standards

## Search Engines

- lack of experience of developer might lead to bad search engine optimization

## Security

- encryption protocols can be used

- SSL
    - secure sockets layer
- TLS
    - client-server applications use TLS to prevent eavesdropping

## Safety (for Digital Divide)

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
