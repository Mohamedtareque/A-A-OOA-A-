## CAN (Controller Area Network)
 > is a message based serial communication protocol used especially for reliable data exchange 

### CAN network structure
- A CAN network consists of a number of CAN nodes which are linked via a physical transmission link (can bus)  In practice,           the CAN network is usually based on a line topology with a linear bus to which a number of electronic control units are each connected via a CAN interface. The passive star topology may be used as an alternative.


- ISO 11898-1 describes the CAN protocol In relation to the reference model of data communication, the CAN protocol just covers the Data Link Layer (MAC Medium Access Control, LLC Logical Link Control) and the Physical Layer (PLS Physical Signaling).
### CAN based on two layers 
* Physical 
  - Physical Signaling
    - Bit encoding de-coding
    - Bit timing/synchronization
  - Physical Medium Attachment
     - Driver/receiver characteristics
  - Medium Dependent Interface
    - Connectors/wires
* Data
  - The Logical Link Control (LLC) manages the over- load control and notification, message filtering and recovery management          functions. 
  - The Medium Access Control (MAC) performs the data encapsulation/decap- sulation,
  - error detection and control, 
  - bit stuffing/de- stuffing 
  - the serialization and deserialization functions.
  
![image](x.png)

### Physical layer
- A twisted two-wire line is the physical transmission medium depends on Electrical Difference formation that can be used to eliminate noises and the useful signal remains unaffected. Symmetrical signal transmission results in a physical transmission medium (can bus) consisting of two lines: the CAN-High line (CANH) and CAN-Low line (CANL)
The CAN protocol uses Non-Return-to-Zero or NRZ bit coding. 

- This means that the signal is constant for one whole bit time and only one time segment is needed to represent one bit. The two bus conductors are called "CAN_H" and "CAN_L"
The maximum CAN bus speed is 1 MBaud, which can be achieved with a bus length of up to 40 meters when using a twisted wire pair. 

- The bus must be terminated at each end, typically using a resistor of 120 Ohms. For bus lengths longer than 40 meters the bus speed must be reduced. A 1000 meter bus can still be realised with a 50 KBaud bus speed. For a bus length above 1000 meters special drivers should be used.

### The CAN standard has the following main features: 
* Serial communication protocol. 
* Supports real time control. 
* High level of error handling 
* Multi master multi slave communication. 
* Message based protocol. 
* Maximum rate of 1 Mbps with a bus length of 40 m with a maximum of 30 nodes.

### A CAN transceiver always has two bus pins: 
* one for the CAN high line (CANH) and one for the CAN low line (CANL).
>This is because physical signal transmission in a CAN network is symmetrical to achieve electromagnetic compatibility, and the physical transmission medium in a CAN network consists of two lines. Signaling is diﬀerential which is where CAN derives its robust noise immunity and fault tolerance. Balanced diﬀerential signaling reduces noise coupling and allows for high signaling rates over twisted-pair cable. Balanced means that the current ﬂowing in each signal line is equal but opposite in direction, resulting in a ﬁeld-canceling eﬀect that is a key to low noise emissions. The use of balanced diﬀerential receivers and twistedpair cabling enhance the common-mode rejection and high noise immunity of a CAN bus.

- The maximum number of CAN nodes is speciﬁed as **32** in ISO 11898. In practice
- the maximum number of CAN nodes largely depends on the performance of the CAN transceivers used and whether it is a high-speed or low-speed CAN network.

### CAN bus levels
* CAN specifies two logical states: recessive and domi- nant. ISO-11898 defines a differential voltage to repre- sent recessive and dominant states (or bits)

* High-speed CAN transceivers interpret a differential voltage of more than 0.9 Volt as a dominant level within the common mode operating range, typically between 12 Volt and -12 Volt. Below 0.5 Volt, however, the diﬀerential voltage is interpreted as a recessive level. 
* Regarding the bus logic, the __dominant__ bus level corresponds to logical __0__. 
* The recessive bus level corresponds to logical 1. 
* The dominant bus level overwrites the recessive bus level. When diﬀerent CAN nodes send dominant and recessive bus levels simultaneously, the CAN bus assumes the dominant bus level. The recessive bus level only occurs if all CAN nodes send recessive levels. In terms of logic, such behavior is AND-logic. Physically, AND-logic is implemented by a so-called open collector circuit.

### The CAN singalling represents a 1 and 0 in the following way:
* Logic 1 __(recessive)__: No signal sent (logic 0 wins) Transceiver output at CAN_L floats to 2.5V Transceiver output at CAN_H floats to 2.5V (i.e. there is a no voltage difference)
* Logic 0 __(dominant)__: Forces bus to a zero level Transceiver output at CAN_L driven to 1.5V Transceiver output at CAN_H driven to 3.5V (i.e. there is a 2V voltage difference)
![levels]()
```
//note
recessive is weak guy which means no difference voltage
dominant is strong one which means there is difference in voltage
```
To enable arbitration, CAN uses 3 levels, in which one symbol lets both conductors float to zero. The other symbol drives both conductors - one to the opposite polarity of the other. This also has constant power envelope. The higher rate of CAN utilises synchronous transmission.

 CAN Modules Types
The CAN modules can be classiﬁed as the following: 
• 2.0A type: consider 29-bit ﬁeld for the ID as an error 
• 2.0B passive: just ignores the 29-bit IDs. 
• 2.0B Active: handles both the 11-bit and 29-bit IDs. The TM4C123GH6PM microcontroller includes two CAN controllers with support of CAN protocol version 2.0 part A/B.


Bit Stuffing
Synchronous transmission is used, with bit stuffing to ensure transparent synchronisation of all bus nodes. When transmitting the sender observes the sequence of bit values being sent. A maximum of five consecutive bits are allowed to have the same polarity, this removes contiguous series of identical values on the bus. Whenever five consecutive bits of the same polarity have been transmitted, the transmitter will insert one additional bit of the opposite polarity into the bit stream before transmitting further bits.
Examples of Bit Stuffiing:
1010101001 sent on cable, received as 1010101001 
1010000001 sent on cable, received as 1010000001
1010000111 sent on cable, received as 1010000111
1010111111 sent on cable, received as 1010111111
The receiver also checks the number of bits with the same polarity and removes the stuff bits again from the bit stream. This is called "destuffing". Hence, the sequence 0111111 becomes 01111101 on the wire, but the receiver correctly receives 0111111. The rule dictates also that the 0111110 becomes 01111100 on the wire, but the receiver then receives 0111110, since the receiver will automatically remove any bit after 5 consecutive bits. The removed stuffing bit must be the opposite polarity (or noted as an error). This happens automatically and ensures receivers always see transitions. - It can add up to one bit in five, maximum 20% additional overhead.
Effect of a corrupted stuffing bit
Using "stuffing", a sequence 0111111 becomes 01111101 on the wire, but the receiver correctly receives 0111111 after removing the extra "stuffed" bit. Several problem can arise when such a stuffed stream is corrupted (i.e. a bit is inverted). Consider the following
* Corruption of the wire transmission of 01111101 to 01101101 (inverting the 4th bit). This results in the receiver output sending 01101101 - one bit has been inverted, but also the stuffing bit has not been removed, and there is therefore a bit-slip, all later data will be shifted by one bit.
* Corruption of the wire transmission of 01111101 to 01111111 (inverting the 7th bit). ). This results in the receiver experiencing an illegal sequence. It expected a stuffing bit, but did not find one. The receiver is aware of the error and needs to take appropriate action.
* Corruption of the wire transmission of 0111100 to 0111110 (inverting the 6th bit). In this case there was no stuffing inserted by the transmitter, but the receiver sees a sequence that causes it to remove (de-stuff) the final 0. The output is 011111 One bit has been inverted, and one bit has been removed, and there is therefore a bit-slip, all later data will be shifted by one bit.
The advantage of being able to send any binary data, while preserving clock transitions is that any errors can result in insertion or deletion of bits. While this is likely to be uncommon in practice (there are not usually many stuffing bits - so it is unlikely that they will be corrupted), the receiver must use an integrity that provides a strong guarantee of detecting destuffing mistakes. A CRC is usually used.



 











DATA LINK LAYER,
The CAN data link layer provides the functional and procedural means to transfer data between nodes including size of transmitted data buffer alocation  and ensures correct reception of data, it comprises two protocols: Classical CAN  and CAN FD ( ISO 11898-1),  

The structure of CAN data frames are the same for Classical CAN and CAN FD, just the field details are different



CAN framing
There are ﬁve types of the CAN bus frame. Those can be classiﬁed as the following: 
• Data frame. 
• Remote frame. 
• Error frame. 
• Overload frame.

Where the data frame can transport a maximum payload of eight bytes.
  Data Frame is generated by a CAN node when a node wishes to transmit data. Each frame carry up to 8 data bytes, Each individual component carries out an important task during transmission

 Remote frame is a frame type with which user data, i.e. data frames, can be requested from any other CAN node. Except for its missing data ﬁeld, a remote frame has the same structure as a data frame. 

The error frame is available to indicate errors detected during communication. 

Overload frame is generated due to internal conditions of receiver which require a delay of the next data or remote frame.

 Regarding the data frame, Transmission of a data frame begins with the start bit (Start of Frame SOF). It is transmitted by the sender as a dominant level which produces a signal edge from the previous recessive (bus idle) level which is used to synchronize the entire network. In order for the receivers not to lose synchronism to the sender during transmission of the frame, they compare all recessive-to-dominant signal edges with their preset bit timing
In case of deviation, receivers re-synchronize by the amount of the relevant phase error (re-synchronization). 








CAN Medium Access
Access to the bus is using a half-duplex with a distributed architecture. Bus nodes do not have a specific address. Instead, the address information is contained in the identifiers of the messages that are transmitted. Hence each message ID indicates the type of content and the priority. The lack of addresses allows the number of nodes to be changed dynamically without disturbing the communication of existing nodes - useful when nodes need to be replaced or new nodes added to an existing bus.
When a node has no data to send (or between frames), a node sends at least 3 recessive bits (1-value), called the Intermission. This time allows nodes to perform internal processing before the start of the next message.

A Data Frame is generated by a CAN node when a node wishes to transmit data. Each frame carry up to 8 data bytes. The small size results in a low latency between transmission request and start of transmission.
Access to the bus access is handled via the Carrier Sense Multiple Access/Collision Detection with Non-Destructive Arbitration, which allows any node to start transmission of a message after an Intermission. It requires any sending node to monitor the bus to see if the transmission is successful. Each message starts with the message ID. The use of the CAN_H and CAN_L signals result in two bus states, called "dominant" (the two lines driven in opposite directions) and "recessive" (both lines floating to the same level). Note the first bit where a 0 (driven bus) is forced onto a 1 (floating bus) signal. This indicates the place where arbitration takes place. A bit with a 0 level always wins. This means that during the transmission of the message ID the lowest numbered message always wins, other nodes stop sending and retransmit later. A Cyclic Redundancy Field (CRC-15) field follows the frame data. CAN provides sophisticated error-detection and error handling mechanisms such as CRC check, and high immunity against electromagnetic interference. Erroneous messages are automatically retransmitted

CAN error detection
In the CAN standard. The error types is being classiﬁed as the following:
1. cyclic redundancy check:
 During the CAN traﬃc, the calculated CRC should be matched with the received CRC. Otherwise the frame was not received correctly (CRC error).

2. Frame check 
NO dominant bits are allowed in: 
• Ack and CRC delimiters. 
• End of frame bit ﬁeld. 
• Inter frame spaces. Otherwise, form error is generated.

3. Bit monitoring : 
Each Node transmits a bit must be able to read back it correctly. Dominant bits are allowed to overwrite recessive bits only in the arbitration phase and ACK slot. Otherwise, a bit error should be issued.

4. Bit stuﬃng : 
6 consecutive bits with same polarity are not allowed between Start of Frame and CRC Delimiter Otherwise Bit Stuﬃng Error.

5. Acknowledgment: 
A frame must be acknowledged by at least one other node. Otherwise ACK error is generated.

Detected errors are made public to all other nodes via Error Frames. The transmission of the erroneous message is aborted and the frame is repeated as soon as possible. The error frame is a special message that violates the formatting rules of a CAN message. It is transmitted when a node detects an error in a message, and causes all other nodes in the network to send an error frame as well. The original transmitter then automatically retransmits the message. An elaborate system of error counters in the CAN controller ensures that a node cannot tie up a bus by repeatedly transmitting error frames.DATA LINK LAYER,
The CAN data link layer provides the functional and procedural means to transfer data between nodes including size of transmitted data buffer alocation  and ensures correct reception of data, it comprises two protocols: Classical CAN  and CAN FD ( ISO 11898-1),  

The structure of CAN data frames are the same for Classical CAN and CAN FD, just the field details are different



CAN framing
There are ﬁve types of the CAN bus frame. Those can be classiﬁed as the following: 
• Data frame. 
• Remote frame. 
• Error frame. 
• Overload frame.

Where the data frame can transport a maximum payload of eight bytes.
  Data Frame is generated by a CAN node when a node wishes to transmit data. Each frame carry up to 8 data bytes, Each individual component carries out an important task during transmission

 Remote frame is a frame type with which user data, i.e. data frames, can be requested from any other CAN node. Except for its missing data ﬁeld, a remote frame has the same structure as a data frame. 

The error frame is available to indicate errors detected during communication. 

Overload frame is generated due to internal conditions of receiver which require a delay of the next data or remote frame.

 Regarding the data frame, Transmission of a data frame begins with the start bit (Start of Frame SOF). It is transmitted by the sender as a dominant level which produces a signal edge from the previous recessive (bus idle) level which is used to synchronize the entire network. In order for the receivers not to lose synchronism to the sender during transmission of the frame, they compare all recessive-to-dominant signal edges with their preset bit timing
In case of deviation, receivers re-synchronize by the amount of the relevant phase error (re-synchronization). 






 SOF 1BIT
DATA FRAME BEGINS WITH THE START BIT (START OF FRAME), IT IS RESPONSIBLE FOR CHECCKING THE BUS STATUS (IDLE) LEVEL WHICH IS USED TO SYNCHRONISM THE ENTIRE NETWORK, SO THE RECEIVER CAN NOT LOSE SYNCHRONISM  DURING THE TRANSMISSION, IT USE BIT TIMING TO
COMPARE ALL RECESSIVE TO DOMINATE SIGNAL EDGES, IF THERE IS DEVIATION RECEIVERS RE-SYNCHRONIZE.

ID 11BIT
identiﬁer, sets the priority of the data frame, and together with the acceptance ﬁltering it provides for sender-receiver relations in the CAN network that are deﬁned in the communication matrix
RTR 1BIT
 Remote Transmission Request, it is responsible for informing the receiver that the type of frame (which is data or remote frame ) for data frame the RTR will be dominate bit

IDE 
the identifier extension bit which distinguish between standard format and extended format. In standard format the identifier has 11 bits, and in extended format 29 bits

DLC
data length code contains The payload that transported in the data field. A maximum of 8 bytes can be transported in one data frame.

CRC 15bit
cyclic redundancy check which is ended by a delimiter bit, which is used to protect the data and be aware if the data sent correctly or not

ACK 1bit
also is followed by a delimiter bit, the receivers acknowledge positively or negatively depending on CRC

EOF 7bit
end of frame, after this the transmission of a data frame is terminated by seven recessive bits

CAN Medium Access
Access to the bus is using a half-duplex with a distributed architecture. Bus nodes do not have a specific address. Instead, the address information is contained in the identifiers of the messages that are transmitted. Hence each message ID indicates the type of content and the priority. The lack of addresses allows the number of nodes to be changed dynamically without disturbing the communication of existing nodes - useful when nodes need to be replaced or new nodes added to an existing bus.
When a node has no data to send (or between frames), a node sends at least 3 recessive bits (1-value), called the Intermission. This time allows nodes to perform internal processing before the start of the next message.

A Data Frame is generated by a CAN node when a node wishes to transmit data. Each frame carry up to 8 data bytes. The small size results in a low latency between transmission request and start of transmission.
Access to the bus access is handled via the Carrier Sense Multiple Access/Collision Detection with Non-Destructive Arbitration, which allows any node to start transmission of a message after an Intermission. It requires any sending node to monitor the bus to see if the transmission is successful. Each message starts with the message ID. The use of the CAN_H and CAN_L signals result in two bus states, called "dominant" (the two lines driven in opposite directions) and "recessive" (both lines floating to the same level). Note the first bit where a 0 (driven bus) is forced onto a 1 (floating bus) signal. This indicates the place where arbitration takes place. A bit with a 0 level always wins. This means that during the transmission of the message ID the lowest numbered message always wins, other nodes stop sending and retransmit later. A Cyclic Redundancy Field (CRC-15) field follows the frame data. CAN provides sophisticated error-detection and error handling mechanisms such as CRC check, and high immunity against electromagnetic interference. Erroneous messages are automatically retransmitted

CAN error detection
In the CAN standard. The error types is being classiﬁed as the following:
1. cyclic redundancy check:
 During the CAN traﬃc, the calculated CRC should be matched with the received CRC. Otherwise the frame was not received correctly (CRC error).

2. Frame check 
NO dominant bits are allowed in: 
• Ack and CRC delimiters. 
• End of frame bit ﬁeld. 
• Inter frame spaces. Otherwise, form error is generated.

3. Bit monitoring : 
Each Node transmits a bit must be able to read back it correctly. Dominant bits are allowed to overwrite recessive bits only in the arbitration phase and ACK slot. Otherwise, a bit error should be issued.

4. Bit stuﬃng : 
6 consecutive bits with same polarity are not allowed between Start of Frame and CRC Delimiter Otherwise Bit Stuﬃng Error.

5. Acknowledgment: 
A frame must be acknowledged by at least one other node. Otherwise ACK error is generated.

Detected errors are made public to all other nodes via Error Frames. The transmission of the erroneous message is aborted and the frame is repeated as soon as possible. The error frame is a special message that violates the formatting rules of a CAN message. It is transmitted when a node detects an error in a message, and causes all other nodes in the network to send an error frame as well. The original transmitter then automatically retransmits the message. An elaborate system of error counters in the CAN controller ensures that a node cannot tie up a bus by repeatedly transmitting error frames.



———————————————— ————————————————————— 

Tarek part 
 
——————————————————— 
Physical layer 
	A physical layer defines the electrical levels and signaling scheme on the bus, the cable impedance and similar things.

There are several different physical layers:
	The most common type is the one defined by the CAN standard, part ISO 11898-2, and it’s a two-wire balanced signaling scheme. 
		It is also sometimes known as “high-speed CAN”. 

A CAN network consists of a number of CAN nodes which are linked via a physical transmission medium (CAN bus) ,An unshielded twisted two-wire line is the physical transmission medium used most frequently in applications Typically, UTPs (unshelled twisted pair )have wire cross-sections between 0.34 mm2 and 0,6 mm2. Line resistance should be less than 60 mΩ.
The CAN bus uses Non-Return To Zero (NRZ) with bit-stuffing , There are two different signaling states: dominant (logically 0) and recessive (logically 1) ,if just one node is driving the bus to the dominant state, then the whole bus is in that state regardless of the number of nodes transmitting a recessive state. 

Maximum Bus Speed
The maximum speed of a CAN bus is 1 Mbit/second. 
Maximum Cable Length
At a speed of 1 Mbit/s, a maximum cable length of about 40 meters (130 ft.) can be used. 

An ISO 11898 CAN bus must be terminated. This is done using a resistor of 120 Ohms in each end of the bus. 
The termination serves two purposes:
1. Remove the signal reflections at the end of the bus.
2. Ensure the bus gets correct DC levels.
ISO 11898 specifies the maximum number of CAN nodes as 32.

CAN Bus Connectors
9-pin DSUB 
————————————— 
CAN Bit Timing 
Each bit on the CAN bus is, for timing purposes, divided into at least 4 quanta. The quanta are logically divided into four groups or segments –
* the Synchronization Segment
		The Synchronization Segment, which always is one quantum long, is used for synchronization of the clocks. 	
* the Propagation Segment
		The Propagation Segment is needed to compensate for the delay in the bus lines.
* the Phase Segment 1
* the Phase Segment 2
		The Phase Segments may be shortened (Phase Segment 1) or lengthened (Phase Segment 2) if necessary to keep the clocks in sync.
Here is a picture of a CAN data bit: 

———————————————————
CAN Bus Error Handling
- How CAN Handles Errors
	- The error handling aims at detecting errors in messages appearing on the CAN bus, so that the transmitter can retransmit an erroneous 		message.
	- Every CAN controller along a bus will try to detect errors within a message. If an error is found, the discovering node will transmit an Error 		Flag, thus destroying the bus traffic.
	- The other nodes will detect the error caused by the Error Flag and take appropriate action, i.e. discard the current message. 
	- Each node maintains two error counters: the Transmit Error Counter and the Receive Error Counter.
	- a transmitter detecting a fault increments its Transmit Error Counter faster than the listening nodes will increment their Receive Error 
	counter 
	-Using the error counters, a CAN node can not only detect faults but also perform error confinement. 
Error Detection Mechanisms
Two of these mechanisms works at the bit level, and the other three at the message level.
1. Bit Monitoring.
		Each transmitter on the CAN bus monitors (i.e. reads back) the transmitted signal level. If the bit level actually read differs from the one             		transmitted, a Bit Error is signaled.
1. Bit Stuffing
	When five consecutive bits of the same level have been transmitted by a node, it will add a sixth bit of the opposite level to the outgoing bit 	stream. The receivers will remove this extra bit. 	
1. Frame Check
	Some parts of the CAN message have a fixed format, i.e. the standard defines exactly what levels must occur and when. (Those parts are 	the CRC Delimiter, ACK Delimiter, End of Frame, and also the Intermission, but there are some extra special error checking rules for that.) If 	a CAN controller detects an invalid value in one of these fixed fields, a Form Error is signaled.
1. Acknowledgement Check
	All nodes on the bus that correctly receives a message (regardless of their being “interested” of its contents or not) are expected to send a 	dominant level in the so-called Acknowledgement Slot in the message. The transmitter will transmit a recessive level here. If the transmitter 	can’t detect a dominant level in the ACK slot, an Acknowledgement Error is signaled.
1. Cyclic Redundancy Check

CAN Controller
* fulfills communication functions prescribed by the CAN protocol

 CAN transceiver 
* connects the CAN controller to the physical transmission medium.
* In a CAN network, the CAN nodes differ in the number of CAN messages they each send or receive.
* CAN transceiver always has two bus pins: one for the CAN high line (CANH) and one for the CAN low line (CANL)

Differential signals
* CAN network is based on transmission of differential voltages (differential signal transmission)
    * This effectively eliminates the negative effects of interference voltages induced by motors, ignition systems and switch contacts.
    * the transmission medium (CAN bus) consists of two lines :
        * CAN high line (CANH) 
        * CAN low line (CANL)
    * Twisting of the two lines reduces the magnetic field considerably.
Dominant / Recessive
* The dominant bus level corresponds to logical “0”.
* he recessive bus level corresponds to logical “1”.
* The dominant bus level overwrites the recessive bus level.
* The recessive bus level only occurs if all CAN nodes send recessive levels.
Event driven
* the transmission of CAN messages does not follow any predetermined time sequence, rather it is event-driven. ??????? (Osama) is that means bit timing 
Receiver-selective addressing
* Is used to prevent dependencies between bus nodes 
* Every CAN message is available for every CAN node to receive (broadcasting) but only node that know id it required and receive.
——————————————————————————— 
Frame Types
1. Data Frame
    * For transmitting user data
    * data frame can transport a maximum payload of eight bytes
2. Remote Frame
    * remote frame has the same structure as a data frame.
    * a frame type with which user data, i.e. data frames, can be requested from any other CAN node.
3. Error Frame
* available to indicate errors detected during communication.
* It consists of just two parts:
    * The error flag 
    *  the error delimiter.
——————————————————————————— 
Data Frame
* SOF (Start of Frame)
    * It is transmitted by the sender as a dominant level which produces a signal edge
    * used to synchronize the entire network.
* ID and RTR
    * This sets the priority of the data frame
    * Next comes the RTR bit (Remote Transmission Request). It is used by the sender to inform receivers of the frame type (data frame or remote frame). A dominant RTR bit indicates a data frame.
* IDE
    * The IDE bit (Identifier Extension bit) which follows serves to distinguish between standard format and extended format. In standard format the identifier has 11 bits, and in extended format 29 bits.

* DLC
    * The DLC (Data Length Code) communicates the number of payload bytes to the receivers
    * The payload bytes are transported in the data field. A maximum of eight bytes can be transported in one data frame 
* CRC and ACK (cyclic redundancy check)
    * the receivers acknowledge positively or negatively in the ACK slot (acknowledgement) which also is followed by a delimiter bit.
* EOF (End Of Frame — EOF)
    * After this the transmission of a data frame is terminated by seven recessive bits .

——————————————————————————— 
Remote Frame
* a frame type used to request data , data frames, from any CAN node. 
* Data and remote frames are differentiated by the RTR bit (Remote Transmission Request).
* In the case of a data frame, the RTR bit is sent as dominant. 
* A remote frame is identified by a recessive RTR bit.
——————————————————————————— 
Addressing 
* It is not the CAN nodes that have identifiers, but rather the data and remote frames are identified (identifier — ID). 
* all CAN messages can be received by every CAN node (broadcasting). 
——————————————————————————— 
CRC and Acknowledgement
* CRC method that is used (CRC: Cyclic Redundancy Check) represents one of the most powerful error detection methods. 
Acknowledgement
* A receiver acknowledges either positively or negatively. 
* A dominant level in the ACK slot represents a positive acknowledgement, while a recessive level represents a negative acknowledgement. 
ACK delimiter
* is always transmitted recessively for the purpose of error tracking. 
* sender transmits both the ACK slot and the ACK delimiter recessively, one positive acknowledgement is sufficient to confirm the correctness of the message transmission to the sender.







