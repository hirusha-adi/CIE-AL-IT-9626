---
title: 3. Networking
---

## Computer Networks

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

### Topologies

- LAN
    - covers smaller geographical area
    - does not always need a router to connect computers togethers

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

### Services

- e-mail
    - electronic mail
    - email is a message that may contain text, files, images or other attatchments
    - sent through a network to an individual or a group of individuals

- WWW
    - world wide web
    - system of internet servers
    - that support formatted HTML documents
    - tends to be upto date
    - has vast amounts of information

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
