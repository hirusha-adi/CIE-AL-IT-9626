---
title: 2. Networking
---

All Past Paper Questions: https://docs.google.com/document/d/1vNZHDwmVpjr_FtfKK6hSrniGD02bbcCwLTdDMDe65Q4/edit?usp=sharing

Questions left out:

- p3-ch2-pg71
- p3-ch2-pg85
- p3-ch2-pg89

## Hardware

### Hubs


### Routers

- stuff
    - in L3 (network layer) of OSI model
    - used in WANs
    - connect two (or more) networks together
    - connects devices to internet
    - do not use data frames 
        - (deals with data packets, not ethernet frames) 
    - work with IP addresses (packets)
    - can dynamically change route (for shortest path)
    - carries out NAT (network address translation)
    - does routing decisions between networks
    - have own broadcast domain
    - store routing data in 'routing tables'
    - contains WAP in same physical unit (AIO)
    - mostly does packet switching only

### Switches

- stuff
    - used in LANs
    - all ports in switch has same broadcast domain
    - store data in a CAM (content addressable memmory) table with MAC addresses
    - usually wired only
    - can configure to do
        - circuit switching
        - message switching
        - packet switching
- types
    - L2 switch
        - in L3 (data link layer) of OSI model
        - connects nodes in same network
    - L3 switch
        - in L3 (network layer) of OSI model
        - can connect two networks
        - deals with frames & also packets
        - work with MAC addresses (frames)
        - faster at connecting segments/routes


### Comparisons

- switch vs router
    - similarities
        - used in LAN
        - handles data packets
        - have multiple data ports
        - conenct to multiple devices
        - send data to specific devices
        - provide high transmission rates
        - can work in full duplex mode
        - can work in  broadcat, multicast and unicast 


## Wired

## Wireless

- why less secure (in LAN)
    - might be unencrypted
    - easier to intercept (than wired connections)
    - Access points can be 'spoofed'
    - access points broadcast SSID (network ID) to public.
- how WiFi connection is established
    - User selects Wi-Fi connection (SSID) 
        - (from list of available connections)
    - Connection to a WAP (in a router) (1st)
        - which is wired into the LAN
    - Uses radio waves
        - frequencies in the 2.4/5 GHz range
        - to carry data packets
    - Wi-Fi uses frames 
        - uses Wi-Fi protocols
        - working at data link layer of TCP/IP stacks 
        - (to carry data over radio waves)
    - WAP sends beacon frames at intervals to announce its SSID
    - Smartphone sends authentication frames (probe frames) 
        - to WAP 
        - requesting connection.
    - WAP responds with authentication credentials
    - User input of authentication credentials to establish security
        - encryption for data exchange, eg:
            - WPA2 (and variants)/
            - TKIP protocols/
        - using 128/256 bit keys for encryption
    - error control used between smartphone and WAP when maintain connection
    - User data 
        - encapsulated within data frames 
        - using Wi-Fi protocols

## Cellular Networks

- structure
    - base stations
        - in a cell
        - for wireless connection
        - to end user
    - central switched network
        - handles voice calls & text messages
    - packet switched network
        - handles mobile data
    - public switched telephone network (PSTN)
        - for connection
        - into global telephone networks
- why no interference
    - use frequency multiplex division (to share frequencies)
    - Spread spectrum technology allows multiple connections on same frequencies
    - Multiple input and multiple output (MIMO) 
        - using multiple transmit/receive antenna 
        - to increase data flow
    - Antennae from base stations directional to avoid
        - so, no interference to other towers
    - Adjacent cells use different frequencies from neighbouring cells
    - wireless frequencies 
        - are re-used by cells 
        - distant from each other 
        - to increase capacity 
        - (where ranges of frequencies are limited)

## Peer to Peer

- advantages
    - No centralised system
    - so failure of one device does not affect others
    - Access to files is local/faster 
    - more productive to users
    - No need network operating systems
    - as its stores own files
    - Less knowledge to setup
    - less technicians needed
    - No central records of access are stored
    - so can be used for piracy
    - easy scaling
        - without performance impact
- disadvantages
    - Files not centrally organised
    - difficult to locate specific files
    - high Risk of malware
        - each peer/node is responsible for their own security 
    - Security is lower as not centrally deployed
    - no central Backup systems
        - user's responsibility to backup
    - document templates may exist in different versions
    - hard to be consistent
    - Files cannot be checked before download
    - security issued
        - no central control over access
        - Remote access can be insecure
    - one device down = affect others
        - that portion of files is lost


- video streaming, viewing resolution affected, p3-ch2-pg71
    - The more available bandwidth on the connection the higher quality of video that can be streamed
    - Use of a 3G connection to the intemet limits video/streaming to low bit rate of 400 Kb/s
    - Buffers not filled completely so video pauses/stops/jerky if frames not received fast enough
    - Provides video of 320 x 240 pixels without apparent stuttering/buffering/stop-start issues
    - This will be a poor video/low definition video as seen on the 1024 x 576 screen
    - Use of a 4G connection with higher bandwidth of c. 15Mbit/s allows video with higher bitrates to be viewed properly
    - This is 1024 x 576 is possible and this is HD quality
    - Highest bit rates of 19/ 30 Mbit/s allowing resolutions of up to 1920 x 1080 pixels
    - Available/can be streamed over Wi-Fi (IEEE 802.1 g) wireless connections....
    - Which have a maximum of 54 Mbit/s
    - 1920 x 1080 pixels will have to be downscaled for viewing on the smartphone screen
    - Which may lead to artefacts and loss of quality.

## Applications

## Blogs

- to adversite bussiness
    - advantages
        - can increase bussiness
        - encourages feedback
        - repeat visitors
        - can analyze data from blog to learn more about customers
        - ensure to alert customers regularly
        - easy to setup
        - can be started by anyone
    - disadvantages
        - can be continually updated
        - hard to follow bad written content
            - often written alone
        - can be inconsistent in details
        - might not show up in search results
        - maybe misleading to customers
        - if blog not updated
            - income may fall
            - we get negative feedback



## E-Mail

- having own mail server
    - advantages
        - can provide custom email
        - only to be used for bussiness
        - can have more emails at no extra cost
        - company can control email policy
            - authorization
        - company has more control over email
        - more secure, as we own the data
        - can archive emails
            - eg: for later reference, for legal requirements
        - can be filtered/scanned for malware
            - before delivered to employee
        - can set a max size for sender   
    - disadvantages
        - complex to configure
        - need experts to setup
            - expensive
        - hard to maintain
        - SMTP services of email from own server are prihibited on ISP accounts
            - extra costs
        - hard to avoid blacklists
            - eg: for bad DNS listing

### Instant Messaging

- advantages
    - simple to setup
    - accessible any time
    - accessible with any device
        - no need specific hardware
    - gives real-time communication
        - (enables fast responses)
    - cheaper than using telephone-systems (for long distances)
    - can keep record of conversations
    - less disruptive to employee workflow
    - can increase productivity
        - can have simultaneous IM connections
        - to text with multiple people
        - in the same time
    - can use along-side video conferencing
    - group chats
    - custom-written apps more secure than emails
        - specially using: end-to-end encryption
- disadvantages

