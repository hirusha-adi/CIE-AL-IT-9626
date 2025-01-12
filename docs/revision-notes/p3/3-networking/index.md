---
title: 3. Networking
---

All Past Paper Questions: https://docs.google.com/document/d/1vNZHDwmVpjr_FtfKK6hSrniGD02bbcCwLTdDMDe65Q4/edit?usp=sharing

Questions left out:

- p3-ch2-pg71
- p3-ch2-pg85
- p3-ch2-pg89
- p3-ch7-pg15

## Data Terms

- bit rate
    - description
        - number of bits transmitted per unit of time
        - units: Kbps (kilobits per second)
        - measure of how fast data can be sent from one device to another
    - how its measured physically?
        - Start video streaming a file of known size
        - Use software to capture video traffic
        - Select video stream from captured traffic and calculate bits per second.
    - factors affecting it
        - bandwidth available (on communication channel)
        - level of SNR ratio (signal to noise ratio)
        - number of signal levels used to represent data

## Network Classification

### LAN

### WAN

### Comparisons

- LAN vs WAN
    - LAN
        - small geographical area
        - high data transfer speeds
        - uses Ethernet / Token Ring technologies
        - connect together into bigger LANs using fiber optic cabling
        - owned by one organization (usually)
        - fewer errors raised (when transmitting data)
        - fewer congestion problems
        - use Layer 1 or Layer 2 devices
            - eg: switches, 
            - bridges,
            - hubs,
            - repeaters, etc...
    - WAN
        - uses ATM / Frame Relay
        - connect together using public telecommunication systems
        - has collective ownership
        - use Layer 3 devices
            - eg: routers
            - multi layer switches

## Network Models

### TCP/IP Model

### OSI Model

### Packet Switching

- how a video is streamed
    - computer requests stream
    - NIC on server determines dst address for file
    - Video file is converted into packets (by NIC on server)
    - NIC on server uses packet switching
    - packets contain details of dst address
    - Packets are sent from network (server's LAN) to router
    - Router compares packet dst IP with routing table
    - Router chooses next hop to send packets 
        - (based on routing table)
    - Applies QOS (quality of service) rules to prioritise the packets 
        - (of the streamed video)
    - Sends packets to next router
    - Next router does the same thing
        - and passes on the packet
    - user's Router receives packets from the internet routers
    - and transfers to laptop viewing video
    - Dynamic routing tables of routers may be updated to ensure QOS for streaming

### Circuit Switching

### Frame Relay

- why
    - supports high speed data transmission
    - connectionless service
        - each packet through network
        - contains address information
    - can use virtual circuits
        - they appear permanent to users
    - multiplexing of virtual circuits to share network bandwidth
    - can only detect errors at Data Link layer
        - so, no flow control
    - faulty frames dropped
        - no request for re-transmission
    - supports variable frame sizes
    - operated at Physical layer and Data Link Layer
        - so, can be used for internet
    - no error control
        - so it requires less reliable method 
        - for transmission    
- advantages
- disadvantages
    - frames delivered unreliably
        - have to be retransmitted if sender is aware (to resend)
        - frames may go missing
            - no acknowledgement from recieving packets
        - packets may not be delivered in same order as sent
        - no flow control
            - cannot stop data transmission 
            - if network is congested
            - so, data is lost
        - data is lost if frame doesnt get re-transmitted

### Comparisons

- TCP/IP vs OSI model
    - similarities
        - 
    - differences
        - 

## Hardware

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
- routing
    - static 
        - stuff (compared to dynamic)
            - created by network admins
            - does not (automatically) consider network conditions
            - routes are fixed
            - routing tables are not updated
            - routing table does not time out
        - how?
            - Routes entered into database
                - by network admin
            - Entries are fixed
                - (not reconfigured automatically)
                - Defines fixed routes 
                    - for packets 
                    - to take from the router
            - forwarding table created 
                - by the routing algorithm
                - when choosing the next hop
            - Defines route of exit point from router
            - As fail-safe if dynamic routing does not provide a route
            - Can transfer routing information from one router to another
    - dynamic 
        - stuff (compared to static)
            - generated by algorithms
            - creates routing table
                - by considering real-time logical network layouts
            - can adjust to changing network conditions
            - routing changes shared between routers
            - can  limit number of hops
            - have limited time-to-live data
                - cuz table will be updated
        - how?
            - Routing protocols create a table of routing information from real-time logical network layouts
            - Created automatically
                - Using many protocols to determine 'best' route
            - Routing information shared with other routers (automatically)
                - to discover changes in networks
            - to limit the number of 'hops' that a packet can take
            - after TTL (time-to-live), table will be updated
            - Packets forwarded via different routes
            - Packets can be routed around network issues
            - Allow as many routes as possible to be kept open.
    - static vs dynamic routing
        - similarities
            - used in routers
            - to determine next hop to send packet
            - algorithms create a 'forwarding table' 
                - (routing table)
                - when choosing the next route
                - its stored in non-volatile memmory 
                    - (of router hardware)
            - provides default route for packet
                - if no route can be determined
- QOS
    - quality of service
    - for video streaming
        - set router's QOS configuration to prioritise video stream
        - use traffic shaping configuration to prioritise video stream
        - configure specific ports for video service
        - intelligent QOS with prioritise in a pre-determined order
            - (only in new routers)
            - order:
                - voice
                - video
                - application traffic
                - print services
                - file downloads


### Hubs

- stuff 1 (compared to Routers)
    - broadcast all received data 
    - to all devices on the network
    - do not store information about devices
    - can reduce network performance
        - will use all available bandwidth

### Switches

- stuff 1 (compared to Routers)
    - used in LANs
    - all ports in switch has same broadcast domain
    - store data in a CAM (content addressable memmory) table with MAC addresses
    - usually wired only
    - can configure to do
        - circuit switching
        - message switching
        - packet switching
- stuff 2 (compared to Hubs)
    - examine data packets 
    - to determine where to send them
    - store information about MAC addresses of devices
    - more efficient (bandwidth usage)
        - as they do not self data to all devices
    - lower latency
        - eg: can ehance gaming
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
- role and 
    - Connects devices together
        - more than devices to a single cable connection
    - process packets from 
        - end-user devices (eg: laptop)
        - and intermediary devices (eg: switches)
    - Forward packets to destination device.
- operation
    - Operates at data link layer (Layer 2)
    - Creates table in memory
        - Content Addressable Memory
        - has MAC addresses and ports
            - (of recieved network frames)
    - uses MAC address 
        - (not IP address) 
        - in Ethemet frame
    - Compares with stored table of MAC addresses
    - Sends frame to known port
    - Unknown frames are sent to all ports


### NIC

- network interface card
- how it works
    - circuitry between computing device and transmission medium
    - Each NIC has a MAC address
        - unique
        - 48 bits
        - in Headecimal 
    - for high speed data transmission (cabled)
    - Uses the OSI model 
        - to send signals at the physical layer, 
        - transmit data packets at the network layer 
        - and operate as an interface at the TCP/IP layer.
    - Data
        - from CPU and sends to destination
    - Translates data 
        - to form so can send in cable
        - from cable into form useable by 
        - Converted to/from parallel structure from/to linear structure
    - Uses interrupts 
        - tell CPU
        - ready to receive data for sending
    - Polled by CPU 
        - to determine if NIC has data 
        - for it to deal with
    - CPU moves data to/from NIC to memory
    - Uses DMA 
        - to transfer data to/from main memory 
            - (via system bus)
        - independent of CPU
    - Prepares data for transmission 
        - in form of frames
    - Process bits from the physical layer and pass to next layer.

### WAP

- wireless access point
- description (short)
    - connects portable devices to a cabled network (over WiFi) 
- roles
    Allow Wi-Fi connections from devices
    Connected to the wired network (LAN by ethernet)
    devices can be mobile
    secure access using password
- limitations
    - limited connection distance
    - signal affected by
        - Obstacles 
            - can reduce connectivity (inbetween WAP and device )
        - type of antenna in use
        - presence of other wireless devices
            - (transmitting on the same frequencies)
        - Weather conditions
        - Power output
    - less bandwidth (vs wired)
        - 350 Mbits/s vs 1000 Mbits/s (Gigabit)
    - multiple devices -> increases congestion
    - Security is based on encryption 
        - adds overhead to packets processing
    - devices that can connect to a WAP is limited
    - Unsecured WAP allows access to anyone within range
    - less secure
        - can easily intercept traffic
    - can slow down workflow is password is forgotten
    - faraday cages in building structures
        - will not allow users inside it to connect
- how to improve security?
    - Hide SSID (service set identifier) 
        - "Hidden Network"
            - SSID doesnt appear
            - asks for SSID before connecting
        - provides limited protection
    - Filter MAC addresses to only allow known devices
        - Ensure WAP is not issuing IP addresses to unknown devices
    - Use encryption
        - (between WAP and client device)
        - use up-to-date encryption protocol
            - eg: WPA3
        - dont use old protocols
            - WEP (Wired Equivalent Privacy)
            - TKIP (Temporal Key Integrity Protocol)
        - requires user to enter a 'network key'
            - (password)
            - atleast use 14 characters
- how data transferred from LAN to WAP
    - Uses radio waves 
        - frequency ranges: 2.4GHz / 5GHz 
        - frequency bands: 900 MHz and 3.6 GHz
    - frames are modulated onto carrier wave
    - Spread spectrum used for higher power levels
    - Two channels used for full duplex exchange of data
        - (most WiFi is half-duplex)
    - WiFi network uses SSID to identify itself
    - Access point and device must be connected to same WiFi network
    - Data is encrypted during transmission
    - Devices must use IEEE 802.11 standards
        - IEEE 802.11 has variants 
        - a/b/g/n/ac(/ad/ah/aj/ax/ay/az)
    - 14 channels on 2.4 GHz
        - which are 5 MHz spaced


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

- hub vs switch
    - similarities
        - allows multiple devices to connect to a network
        - devices can form a LAN
        - send the packets to other devices
        - can transfer data to all devices (on a network)


## Wired

- data transferring
    - unencrypted
    - less subjected to interference
    - cannot easily intercept
    - no need credentials to connect
    - requires device to be physically connected
        - so, less portable

### Copper Cables

- why
    - Can use long runs of cable
        - less signal loss
    - Greater tensile strength
    - no harm from electrical interference
    - no harm from environmental changes
    - Can provide very high bandwidth
- advantages
- disadvantages
    - Difficult to setup
    - Loss of signal at joins.
    - cannot bend too much
        - not very flexible 
        - (if bent beyond their limited physical arc, they will break) 
    - Special test equipment required
    - susceptible to physical damage
        - eg: being cut / broken
    - Data transmission losses occur 
        - when wrapped around curves 
        - with small radius.
    - expensive than wireless
    - cannot provide high bandwidth like fibre optics

### Fiber Optic Cables

## Wireless

- why less secure (in LAN)
    - might be unencrypted
    - easier to intercept (than wired connections)
    - Access points can be 'spoofed'
    - access points broadcast SSID (network ID) to public.
- data transferring
    - slow speeds
    - high latency
    - need recognition of connection between devices
    - requires connection to be encrypted
    - requires user to input credentials
    - encrypted data is easier to intercept (even if no meaning)
    - easier & cheaper to install
    - signal interference from other devices
    - more portability to client devices 

- advantages
    - internet (radio signals) around home
    - can control devices remotely / portably
    - multiple wireless handsets to use one wired landline
    - can use wireless doorbells
    - communication without disruption
    - can be used in historic buildings (without network wires)
    - multiple devices connect to centralaccess points so
    - easy sharing of printers, files, etc...
    - mobility / portability of devices
    - can use of (discrete) hearing aids 
        - so, high volumes doesnt disturb others
    - remote control of household appliances
        - eg: smart home devices (IoT)
        - eg: like CCTVs
- disadvantages
    - subjected to interference 
        - from electronic devices
        - microwave ovens
        - fridges
        - so, unreliable
    - security issues if not set up properly


### Microwave Transmissions

- how
    - Uses beam of electromagnetic waves
    - Uses line-of sight between antennae
    - Uses frequencies: 300 MHz to 300 GHz 
        - (wavelength 10cm to 1mm)
    - Uses parabolic dishes 
        - with (horn) antennae 
        - to provide 'spot' beams
    - Uses multiple antennae 
        - to send/receive signals 
        - (if sending/receiving simultaneously)
    - Data is modulated 
        - onto carrier wave 
        - using OFDM (orthogonal frequency-division multiplexing) / OFDMA (orthogonal frequency-division multiple access)
    - Pulsed transmission of waves 

- advantages
    - directional antennae
        - increased performance
        - low power usage
        - point directly at each other
            - can use same frequencies 
            - (as neighbouring transmissions) 
            - without interference
    - Narrow microwave beams do not interfere (with other equipment)
    - Small antennae means more portable 
        - e.g. portable radio systems
    - large bandwidth
        - carry more data

- disadvantages
    - tall antennae 
        - difficult to install
    - Line of sight required
        - antenna cannot be 'over horizon' (earth curvature)
        - (limited to 50-80 km)
        - else,
            - obstacles will interfere
            - Unable to penetrate obstacles
            - causes interference
        - so position antennas intrusively
    - atmospheric conditions can degrade signal
        - (weather)
        - 'Rain fade' absorbs microwaves by weather
        - dust / smoke / high-pollen-counts because signal scatters (by particles)
        - Solar events
    - ?? can be intercepted behind official antenna (eg: by space satellite) ??

- uses
    - phone systems (3G, 4G, 5G)
    - WiFi systems (in LAN)
    - communication between base station and satellites
        - \+ uplink and downlink satellites
    - used for TV / radio
        - to transmit programs from outside the studio
        - (broadcasts)
        - instead of using expensive satellite links
    - used to carry cellular data between stations
        - to provide backbone to carrier system
    - for short-range indoor communications
    - to link remote telephone exchanges to main exchanges without using cobber/fibre-optic cabling 


### WiFi

- stuff
    - asymmetrical
        - one central point to many remote devices
    - uses a central access point (usually)
    - covers wider area
    - complex to establish a connection
        - requires a lot of authentication and encryption stuff
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
- using public wifi
    - advantages
        - low cost / free
        - attracts more customers
        - allows mobile connections, so, more productive
        - convenient when travelling
        - avoids use of data allowance in mobile phone networks
    - disadvantages
        - unreliable connections
        - some services might be restricted
            - eg: torrenting
        - might insert advertisements
        - may require authentication/verification with personal details
        - can be intercepted by others
            - subjected to MITM attacks
            - might inject malware code 
            - personal data can be stolen
                - and used for fraudulent activities
        - might limit bandwidth unless extra fees paid


### Bluetooth

- stuff 1 (vs WiFi)
    - to be used upto 8 devices
    - doesnt use a central access point (usually)
    - symmetrical
        - two devices
    - covers short range connections
    - more affected by obstacles
    - simple to establish a connection
    - has low bandwidth
    - less harm from electromagnetic interference than WiFi
    - less secure than WiFi
    - uses less power
    - shorter range
    - restricted by solid barriers (eg: walls)
- stuff 2 (vs NFC)
    - working distance: 100m
        - (devices must be kept very close)
    - sets up in 6 seconds
    - bitrate: 2.1Mbits
    - requires PIN
    - one-to-one connection (peer-to-peer)
    - new technology (doesnt support older devices)
- stuff 3 (compared to infra red)
    - uses radio frequency: 2.4GHz
    - can use multiple channels
        - (spread spectrum technology)
    - can travel through walls (but signal will deteriorate)
    - free standard
    - high bandwidth (compared to IR)
- how Bluetooth connection is established
    - turn on both devices
    - ensure within range (both should find eachother)
    - set one device to search for other
    - device is discovered/found
    - device required password/user-response
        - eg: pressing a button
        - or confirming a one-time code
    - password confirmed by both devices
    - devices are paired
    - frequencies+channels to be used are decided
- advantages
    - free to use
    - many devices support it
    - uses less power (than e.g. WiFi) 
        - saved phone battery life
    - Easy to pair devices
        - no need passwords
    - Connections are 'remembered' 
        - so simple to repeat
    - It is wireless (so, convenient)
    - Can connect through obstacles (usually)
    - Has greater range than infra-red connections
    - It is short range
        - signals hard to intercept
        - so, more secure

- disadvantages
    - can hack Connection of idle devices
    - short range only
    - slow when sending large files
    - low bandwidth
        - compared to e.g. WiFi/cable connections
    - only 8 devices at max
        - (can connect to 7 devices at once ONLY)
    - Can lose connection due to interference / obstacles
    - Can receive viruses

### Infra-red

- for data transmission
- stuff (compared to bluetooth)
    - uses wavelength: 20 to 400THz
    - less susceptible to interference
    - requires line of sight
    - limited to 10m
        -  depends on power of IR source
    - can only use with 1 other device
    - usually need proprietary equipment
    - IR bandwidth is limited
        - depends on on/off pulses of data
    - can setup personal area network (PAN) 

### NFC

- near field communication
- uses
    - to make contactless payments
    - identify user in ticketing systems
    - in social networking for sharing images
        - (between close devices)
    - exchange personal details 
        - eg: bussiness card
    - unlock doors with smart locks 

- stuff (vs Bluetooth)
    - working distance: \<20cm
    - sets up in \<0.1 seconds
        - (quicker than bluetooth)
    - bitrate: 400kbps (lower)
    - uses less power
    - can be used to activate passive tags
    - automatic connection

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

### 5G, 4G, 3G

- 5G
    - feaures (suitable for large networks)
        - large connection capacity
            - upto a million devices per km<sup>2</sup>
        - very high bandwidth (data transfer)
            - even allows use UHD video on demand
        - very low latencies (fast responses)
        - seamless handover between base stations
        - use 'beam-forming' techniques
            - by base stations
            - to improve connections to specific devices
    - advantages
        - (most stuff in `features` section above)
        - may gradually replace land-line connections (for internet connections)
    - disadvantages
        - reduced coverage
            - need more cell towers
            - more expensive
        - shortage of radio frequencies
        - can interfere with existing radio spectrum
        - new devices required to acecss 5G
        - new technology required to implement 5G
        - potential for cyber attacks
        - low latency
            - can control devices remotely, in real time
        - high infrastructure costs
- 4G
    - stuff
        - use only packet switching

- 3G

### Comparisons

- 4G vs 3G
    - higher bandwidth
        - due to higher range of frequencies
        - due to use of MIMO 
            - (multiple input and multiple output)
            - using multiple transmit/recieve antenna 
            - to increase use of transmission channels
        - connections use frequency multiplex division to share
        - due to use of spread spectrum technology
            - to allow multiple connections
            - on same set of frequencies
        - gives
            - faster download speeds
            - more buffering capacity
            - content loads faster
    - handovers between base stations are smoother
        - less interruptions
    - use only packet switching
        - allows packets to be multiplexed
        - so, increased rate of data flow

- bluetooth vs infra-red
    - bluetooth

    - infra-red

## Satellite Communication

- how it works?
    - Satellite remains in orbit 
        - follows rotation over Earth 
        - appears stationary over target area
    - Multiple satellites 
        - can be arranged in constellation 
        - each covering of small area of surface
        - can cover areas farthest from equator
        - target specific areas of Earth
    - Satellite can use spot beams 
        - to target specific areas
        - provides high bandwidth 
    - Ground stations 
        - maintain permanent (microwave) links 
        - with satellites
        - Both uplink and downlink connections
        - via dish antenna
    - User 
        - has dish with transceiver 
        - via LNB pointed at satellite
        - dish needs to be line of sight
        - eg: dish in Southern hemisphere northerly direction.
    - MORE STUFF -> (for full marks)
    - Ground (gateway) stations 
        - have internet connection 
        - relay user internet data to from satellite
        - convert data carried by satellite signals to/from IP packets
    - Satellite 
        - serves to receive, amplify and re-transmit signal 
        - (without processing of data)
    - User 
        - has satellite modem 
        - to modulate/demodulate data 
        - between local IP packets 
            - and satellite link signals.

- advantages
    - Satellites are in geostationary orbit 
        - so ground stations for uplink 
        - can point directly at them 
        - so less power needed
    - Receiving dishes 
        - can point directly at satellite 
        - for less fluctuation (in signal)    
    - Low/medium orbit satellites
        - provide low latency connections 
        - with high speeds
    - Physical connections not required 
        - so access can be from anywhere
    - No need ground-based infrastructure
    - aircraft/ships can use to access internet
    - Coverage can be optimised for high bandwidth
- disadvantages
    - Satellites in geostationary orbit are 
        - c. 18 000 km high 
        - so signal has to travel c. 36 000 km 
        - resulting in delay
            - high latency (worse than dial-up)
            - SSL may not succeed
            - TCP protocols may break
    - Interference by weather conditions 
        - can reduce signal quality
    - Must be line of sight to satellite
    - Reflections reduce signal quality 
        - by phase cancellation effects.

- broadcast from satellite to TV
    - Satellite is in geostationary orbit 
        - appears to be at fixed point above
    - be at correct height
        - 37 000 km above equator
    - Satellite has 
        - ransmitting dish pointed at Earth.
        - has transponder(s) 
            - which receives and transmits 
            - signals (to/from) Earth.
            - use different frequencies.
                - set range: 4—8 and 12—18 GHz range
    - Horizontal & vertical signal polarisation
        - to increase capacity.
    - TV signal may be encrypted 
        - to prevent viewing without paying
    - High definition signals with multi-channel sound requires more bandwidth.
    - Receiving dish on Earth 
        - pointed at the satellite in line of sight.
        - has LNB (Low Noise Block) at antenna 
            - to amplify signal 
            - allows use of cheaper cable to receiver.
    - Receiver 
        - decodes signal into pictures and sounds 
        - decrypts the encrypted TV signal (paid).


## Networking Models

### Client-Server

- explanation
    - all files in a centralized server
    - only one copy has to be maintained
    - files can be mirrored to other servers
        - for increased performance
        - without the need to copy to each device in use
    - disaster recovery is easy + quick
        - can quickly recovery backups
    - servers can be updated (easily scalable)
        - without upgrading user devices
    -  data shared across different devices
    - data can be accessed from different locations
        - (as long as the device is in the same network)
        - (or by using a VPN tunnel)
    - data can be queried from DBMS (SQL or No-SQL database)
        - regardless of interface
    - better data security
    - server can perform authentication before returning data  

### Peer to Peer

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

### BitTorrent

- description
    - peer-to-peer file sharing
    - web seeding to allow use of HTTP sources
    - provide RSS feeds 
        - via 'broadcatching' 
        - (for content distribution)
    - Used to
        - stream videos
        - transfer large files using minimum bandwidth
        - ?? social media to distribute updates to servers ??

- how it works
    - Peers share processing power without a central server
    - Nodes work as both client and server for other nodes
    - Nodes can connect undstructured or in structured topology
    - Unstructured mode 
        - robust when nodes join/drop frequently 
        - but finding a file is more difficult
    - Structured mode is organised 
        - (using hash tables) 
        - and files can be found easily
    - Peer-to-peer software run on /node
        - Software queries other nodes to find file 
            - Search request 
                - has 'time to live' (TTL) 
                - after which it ceases to search
                - propagates from queried nodes to others
            - When found, 
                - software downloads from node to node
            - Other nodes can copy downloaded file from each node
    - fragments of file can be copied from different nodes at once,
        - increasing speed.

- how it works? (old)
    - source computers are used without a central server
    - BitTorrent client required on internet-connected computer 
        - to implement BitTorrent protocol
            - works well over low-bandwidth connections
    - BitTorrent descriptor file is used to describe file being distributed
    - BitTorrent node set up with use of descriptor file and file to be distributed
    - Node becomes seed for download
    - Files made available to others for download by connection to other peers
    - File is divided into small segments
    - Segment becomes available to other peers as it is downloaded
    - original (source) seed is relieved of load
    - Every segment protected by a cryptographic hash 
        - used to detect changes
        - to ensure file integrity
    - Segments downloaded in random order
        - and re-ordered by BitTorrent client.

- why its insecure
    - Nodes more susceptible to remote attack
    - IP address is clearly visible to others so
        - (so, easy for hackers to target)
    - can use IP to steal user data
    - resulting in fraud / blackmail
    - Malicious code can edit routing tables of nodes
    - responses to requests can contain malicious code
    - so, we download malware instead of original resource 
    - Authors are unknown
        - so, may contain trojans/malware/stealers
    - Sections of files can be replaced with malware
    - Downloaded Bit Torrent files 
        - stored by default in folder along with other user data 
        - risking exposing the data to others
    - session can be left open unintentionally
    - Bit Torrent traffic is not encrypted by default
        - UDP and TCP ports used
            - might be subjected to monitoring by ISP
        - so, use VPN 
    - piracy (of copyrighted materials) give rise to legal issues

## Tunnelling

- why
    - set up VPN  
        - (allows data to be private)
    - data can be be kept secure when working remotely
        - (eg: working from home)
    - can circumvent firewall rules 
        - to allow access to internal network 
        - by data carried in packets
    - can use foreign' protocols on networks
        - (when its not supported)
        - e.g. use of IPv6 on IPv4 networks.
- how? (to tunnel over the internet)
    - data broken into small packets
        - (for transmission over IP network)
    - IP packets encapsulated by tunnelling protocol (L2TP)
    - IP packet sent over internet (public communication channels)
    - data is encrypted using SSH / IPSec
    - packets are decapsulated and unencrypted at destination 

### VPN

- evaluvate
    - Encrypts all data (secure)
        - protects privacy of user
    - changing the user IP address 
        - allows users to browse internet anonymously
        - prevents tracking of activity by ISP, trakcets, etc...
    - can configure to block advertisements
    - can bypass geo-restrictions
        -  access material from other countries
        - eg: journalists looking for news
        - movies, music, etc...
    - to bypass censorship (imposed by ISPs or countries)
    - can bypass ISP bandwidth
    - may be illegal in some countries (might lead to prosecution)
    - reduce performance and increase letency/ping
    - may collect data and sell to third party (data brokers)
    - can be difficult to set up
    - ?? need latest OS to use VPN ??
    - Some sites may block VPN
    - can be configured to allow an extranet to be set allowing remote access to a private network


## Cloud Computing

- meaning
    - ...

- Storing data on remote servers
- Servers maintained by third-party (companies)
- Accessed via web browser
- Can use VPN for secure connection.
- servers can be accessed from anywhere (with internet access).
- Resources shared between clients and provider (seamlessly).
- dynamically changed by provider
- many service models exist eg,
    - providing infrastructure/
    - providing software 
    - providing the 'computing platform'
    - providing development environment
- impact 
    - cheap maintenance costs
        - no need servers, IT staff
    - large storage for cheap
    - performance is monitored by provider
    - Productivity is increased
    - invest in reliable internet.
    - dynamic Scalability 
        - requirements met quickly
    - Resources expanded and contracted as required
    - unexpected costs when resources exceed
    - no full control of their data.
    - Data may not be stored in the same jurisdiction
        - laws difficult to comply with
    - expensive service provision

- storing data in cloud
    - meaning
        - store in network of servers
        - accessed over internet
        - Access available from any (remote) device
        - data may be managed by third parties
        - managed by a cloud storage provider.
    - security issues
        - Data not under our direct control
        - depends on third party for security
            - cannot trust third party companies with our data
        - Data is susceptible to cyber-attack 
            - as only accessible over intemet
            - as multiple copies of data (buckups)
            - attack to servers 
                - e.g. DOS attacks
                - uses all server resources
        - Data accessible to government check / subpoenas
        - data loss, may result in legal issues
            - could storage provider is responsible
        - Data is difficult permanently
            - already in cloud
            - already had multiple copies (backup)
        - not standardised across all companies
            - if a company using cloud storage
            - they might not be able to change supplier 
        - cannot access data without internet (while offline)

## Bit Streaming

- describe
    - contiguous sequence of bits
    - sent/recieved serially
    - over a communications network

### Real Time

- stuff
    - from a live source
    - cannot be accessed later

### On Demand

- stuff
    - from a pre-recorded video
    - can be streamed at any time

## Protocols

- Also at: 
    - [File Servers (FTP)](#ftp-server)
    - [BitTorrent Protocol](#bittorrent)
    - [TCP/IP Network Model / Protocol Stack](#tcpip-model)

### DHCP

- describe
    - a network manaqement protocol
    - Automatically assigns 
        - a network configuration to a device
        - an IP address
        - a gateway address
        - a subnet mask
    - Creates a database 
        - to avoid addressing conflicts

### UDP

- describe
    - Sends data (in datagrams) using lP
    - Provides 
        - checksums
        - port numbers for source/destination 
        - (of datagram)
    - Connectionless communication
    - No reporting of lost packets (to sender)
    - Used when delivery of datagrams is not important
    - Avoids processing overheads 
        - (of error checking)
    - No handshaking
    - No guarantee of delivery/
    - No order of datagrams
    - No error checking.
- packet header
    - four fields of 2 bytes
    - source port field used to reply if needed
    - dst port used to specify reciever port number
    - dst port is always required
    - header + data field 
        - (in bytes)
        - used for error checking
    - length of header (8 bytes minimum)
    - checksum field 
        - results of calculations
        - to be used to check errors
        - optional in IPv4
            - set to `0` if not calculated
        - required in IPv6  
- advantages
- disadvantages
    - no acknowledgement after recieving packet
    - not sure if packet lost or recieved
    - provides for ordering of packets so there is no tracking of messages
    - no congestion control 
        - so these have to be separately
        - carried at application level
    - Reciever must handle lack of handshake 
        - of data
        - increasing complexy/overheads.

### TCP

- describe
    - Sends data (in datagrams) using lP
    - Provides 
        - checksums
        - port numbers for src/dst 
        - (of datagram)
    - Connection-oriented communication
        - (point to point)
    - Reporting to sender of lost packets
    - Establishes how data is transferred over network
    - Handshaking is carried out to establish connection.
    - Manages flow control
    - Used when delivery of datagrams is important
    - Error checking.

### FTP

- file transfer protocol
- for sharing files to/from server

### HTTP

- hyper text transfer protocol
- for accessing web pages

### HTTPS

- hyper text transfer protocol secure
- learn more at: [Chapter 4 - Security](../4-security/index.md)
- for secure data transfer

### SMTP

- simple mail transfer protocol
- to send emails

### IMAP

- Internet Message Access Protocol
- to recieve emails

### POP3

- post office protocol 3
- to recieve emails

### SSH

- secure shell
- for secure access to a server

### SFTP

- secure file transfer protocol
- for secure method of uploading data to a server

### SMB

- Server Message Block (used by Samba)
- for transferring files to a file server

### TELNET

- teletype network
- to connect computers to a switch/router

## Applications

### Forums

- advantages
Accessible from anywhere
Interaction between experts from different areas is possible
Can develop a group opinion
moderated comments can increase reliability

- disadvantages
- difficult to maintain (when discussing medical issues)
- unable to verify accuracy of comments.
- Comments added at any time.
- No non-verbal clues about participants.
- Can become little more than a group chat about symptoms with no focus.
- ?? Posting of the same comment multiple times can cause reliability of data issues ??

### Blogs

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

- how to social engineer
    - pg73

### Micro Blogs

- advantages
    - specific Topics
    - reflects real time activities
    - Use short sentences
        - for users who don't have the patience to go through longer blog posts
    - Can be impromptu
    - no need to construct passages
    - Takes less time for blogger
    - Use video links (no embeds)
        - can only open if like
        - or if device is powerful
- disadvantages
    - may not be long lived
    - small Word count 
    - overloads reader with information 
        - information unfolds quickly
    - leads to crucial information being overlooked
    - difficult to customised pages.


### Proxy Server

- evaluvate
    - intermediate gateway between client and websites
        - so, websies cannot log activity of user
        - cannot log IP
            - so, cannot determine geolocation
            - keeps clients identity secure + private
        - can do access control
        - can filter out unwanted stuff
        - can cache frequenly used websites
            - reduced internet usage
            - but user may recieve outdated info
            - user will not know and will use old data
        - can encrypt web requests from client (enforce HTTPS)
        - can provide VPN services (for remote access)
            - eg: students remotely accessing school network
        - high latency (as all traffic goes through the body)

### Printer Server

- explanation
    - Accept print jobs from client devices
    - Manage print job to printer
    - Queue print jobs (if printer is busy)
    - management of print queues
    - quota of print jobs
    - can enforce admin policies
    - Allow authentication
        - water-marking of print jobs.

### Web Server

- explanation
    - store html documents (on secondary storage devices)
    - store media/scripts/stylesheets associated with HTML documents
    - process incoming network requests
    - use HTTP(S) to receive/deliver communications
    - provides server-side script services (for dynamic web pages)

### FTP Server

- how it works
    - uses file transfer protocol
    - between server and client
    - FTP addresses being with `ftp://`
        - (to indicate the protocol required to transfer)
    - server listens for USER and PASS commands
        - (username and password)
    - FTP uses port 21 (by default)
    - active mode 
        - uses port 21 
        - for connection with client
    - passive mode is used 
        - if client is behind a firewall
        - (if unable to recieve incoming TCP connections)
        - sets up different port (for c-s data connections) 
    - USER and PASS are not encrypted (by default)
        - encrypted in 
            - SFTP (Secure FTP - over SSH)
            - uses port 22 (ssh)
    - server sends acknowledgement 
        - to client 
        - if valid credentials
        - and session is opened
    - anonymous access can download, but not upload
    - server allows checkpoints
        - so, downloads can be resumed (if interrupted) 
            
### E-Mail

- explanation
    - Manage email accounts
    - Host domains for provision of email accounts
    - Send email using Simple Mail Transfer Protocol/SMTP
    - Receive email using Intemet Message Access Protocol (IMAP) / POP3
    - uses store and forward model.

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

- how emails are sent and recieved (basic)
    - Mail server provides email services to email client
    - Email client sends request to server
    - Server sends a response to email client
    - Email client logs-in to mail server
    - Rules for requests are determined by protocols
        - eg: SMTP, IMAP, POP3
    - Messages are transferred between client and server
        - (from emails stored on server).

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

## Other

- types of transmission media (for UHD TV)
    - 25 megabits/sec bandwidth needed
        - might not be available to everyone
    - Satellite signals might provide it.
        - less channels 
        - (unless more satellites brought to service)
    - Wireless/mobile networks have restricted bandwidth
        - not enough for UHD
    - 5G will make UHD available 
        - but new phones needed
    - Copper cable networks 
        - bandwidth 100 Mbit/s (Cat 5) to 1 Gbit/s (Cat 6)
        - can provide ultra HD.
        - limited distance
            - bandwidth reduces over distance
    - Fibre optic cables  
        - can provide high bandwidth (10 Gbit/s).
        - expensive
        - FTC (Fibre to cabinet) may provide UHD to more homes.
        - allows much longer cable 
            - (low installation costs)
        - long distances from exchange to home.


---

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
