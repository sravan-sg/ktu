# Knowledge Base Note: Data Communications and Networking Forouzan 4th Ed


Don't forget to check out the Online Learning Center, www.mhhe.com/forouzan for
additional resources!


Instructors and students using Data Communications and Networking, Fourth Edition
by Behrouz A. Forouzan will find a wide variety of resources available at the Online
Learning Center, www.mhhe.comlforouzan

Instructor Resources
Instructors can access the following resources by contacting their McGraw-Hill Repre-
sentative for a secure password.
a PowerPoint Slides. Contain figures, tables, highlighted points, and brief descriptions
  of each section.
o Complete Solutions Manual. Password-protected solutions to all end-of-chapter
  problems are provided.
a Pageout. A free tool that helps you create your own course website.
D Instructor Message Board. Allows you to share ideas with other instructors
  using the text.

Student Resources
The student resources are available to those students using the book. Once you have
accessed the Online Learning Center, click on "Student Resources," then select a chap-
ter from the drop down menu that appears. Each chapter has a wealth of materials to
help you review communications and networking concepts. Included are:
a Chapter Summaries. Bulleted summary points provide an essential review of
  major ideas and concepts covered in each chapter.
a Student Solutions Manual. Contains answers for odd-numbered problems.
o Glossary. Defines key terms presented in the book.
o Flashcards. Facilitate learning through practice and review.
a Animated Figures. Visual representations model key networking concepts, bringing
  them to life.
D Automated Quizzes. Easy-to-use quizzes strengthen learning and emphasize impor-
  tant ideas from the book.
a Web links. Connect students to additional resources available online.


     DATA
COMMUNICATIONS
     AND
  NETWORKING

McGraw-Hill Forouzan Networking Series


Titles by Behrouz A. Forouzan:

Data Communications and Networking
TCPflP Protocol Suite
Local Area Networks
Business Data Communications

          DATA
     COMMUNICATIONS
          AND
       NETWORKING
                             Fourth Edition


                   Behrouz A. Forouzan
                             DeAnza College


                                    with


                       Sophia Chung Fegan


                   •        Higher Education
Boston Burr Ridge, IL Dubuque, IA Madison, WI New York San Francisco S1. Louis
 Bangkok Bogota Caracas Kuala Lumpur Lisbon London Madrid Mexico City
 Milan Montreal New Delhi Santiago Seoul Singapore Sydney Taipei Toronto

   The McGraw·HiII Companies               .~I


II Higher Education
DATA COMMUNICATIONS AND NETWORKING, FOURTH EDITION

Published by McGraw-Hill, a business unit of The McGraw-Hill Companies. Inc., 1221 Avenue
of the Americas, New York, NY 10020. Copyright © 2007 by The McGraw-Hill Companies, Inc.
AlI rights reserved. No part of this publication may be reproduced or distributed in any form or
by any means, or stored in a database or retrieval system, without the prior written consent of
The McGraw-Hill Companies, Inc., including, but not limited to, in any network or other
electronic storage or transmission, or broadcast for distance learning.
Some ancillaries, including electronic and print components, may not be available to customers
outside the United States.
This book is printed on acid-free paper.
1234567890DOC/DOC09876
ISBN-13    978-0-07-296775-3
ISBN-to    0-07-296775-7
Publisher: Alan R. Apt
Developmental Editor: Rebecca Olson
Executive Marketing Manager: Michael Weitz
Senior Project Manager: Sheila M. Frank
Senior Production Supervisor: Kara Kudronowicz
Senior Media Project Manager: Jodi K. Banowetz
Associate Media Producer: Christina Nelson
Senior Designer: David W Hash
Cover Designer: Rokusek Design
(USE) Cover Image: Women ascending Mount McKinley, Alaska. Mount McKinley (Denali)
   12,000 feet, ©Allan Kearney/Getty Images
Compositor: Interactive Composition Corporation
Typeface: 10/12 Times Roman
Printer: R. R. Donnelley Crawfordsville, IN

           Library of Congress Cataloging-in~Publication Data
Forouzan, Behrouz A.
 Data communications and networking I Behrouz A Forouzan. - 4th ed.
    p. em. - (McGraw-HilI Forouzan networking series)
 Includes index.
 ISBN 978-0-07-296775-3 - ISBN 0-07-296775-7 (hard eopy : alk. paper)
 1. Data transmission systems. 2. Computer networks. I. Title. II. Series.
TK5105.F6617         2007
## 004.6--dc22                                                        2006000013
                                                                      CIP
www.mhhe.com

To lny wife, Faezeh, with love
            Behrouz Forouzan


Preface   XXlX


PART 1           Overview       1
## Chapter 1        Introduction       3
## Chapter 2        Network Models          27

PART 2           Physical Layer and Media              55
## Chapter 3        Data and Signals         57
## Chapter 4        Digital Transmission           101
## Chapter 5        Analog Transmission            141
## Chapter 6        Bandwidth Utilization: Multiplexing and Spreading     161
## Chapter 7        Transmission Media            191
## Chapter 8        Switching      213
## Chapter 9        Using Telephone and Cable Networksfor Data Transmission     241

PART 3           Data Link Layer          265
## Chapter 10       Error Detection and Correction             267
## Chapter 11       Data Link Control            307
## Chapter 12       Multiple Access         363
## Chapter 13       Wired LANs: Ethernet            395
## Chapter 14       Wireless LANs          421
## Chapter 15       Connecting LANs, Backbone Networks, and Virtual LANs        445
## Chapter 16       Wireless WANs: Cellular Telephone and Satellite Networks    467
## Chapter 17       SONETISDH          491
## Chapter 18       Virtual-Circuit Nenvorks: Frame Relay andATM        517
                                                                               vii

viii   BRIEF CONTENTS


               PART 4           Network Layer          547
## Chapter 19       Netvvork Layer: Logical Addressing             549
## Chapter 20       Netvvork Layer: Internet Protocol          579
## Chapter 21       Netl,vork La.ver: Address Mapping, Error Reporting,
                                and Multicasting 611
## Chapter 22       Network Layer: Delivery, Fonvarding, and Routing           647

               PARTS            Transport Layer             701
## Chapter 23       Process-to-Process Delivery: UDp, TCP, and SCTP            703
## Chapter 24       Congestion Control and Quality ql'Sen'ice            761

               PART 6           Application Layer           795
## Chapter 25       Domain Name System                797
## Chapter 26       Remote Logging, Electronic Mail, and File Transfer         817
## Chapter 27       WWW and HTTP               851
## Chapter 28       Network Management: SNMP                 873
## Chapter 29       Multimedia       901

               PART 7           Security       929
## Chapter 30       Cf}1J tography       931
## Chapter 31       Network Security           961
## Chapter 32       Securit}' in the Internet: IPSec, SSLlTLS, PCp, VPN,
                                and Firewalls 995
               Appendix A           Unicode     1029
               Appendix B           Numbering Systems            1037
               Appendix C           Mathematical Review           1043
               Appendix D           8B/6T Code       1055
               Appendix E        Telephone History          1059
               Appendix F        Co!1tact Addresses         1061
               Appendix G           RFCs      1063
               Appendix H           UDP and TCP Ports            1065
               Acron.Vl11s   1067
               ClOSSOlY      1071
               References      1107
               Index    IIII

Preface   xxix

      PART 1       Overview          1
## Chapter 1       Introduction            3
## 1.1   DATA COMMUNICATIONS                         3
      Components 4
      Data Representation   5
      DataFlow 6
## 1.2   NETWORKS         7
      Distributed Processing 7
      Network Criteria 7
      Physical Structures 8
      Network Models 13
      Categories of Networks 13
      Interconnection of Networks: Internetwork             IS
## 1.3   THE INTERNET          16
      A Brief History 17
      The Internet Today 17
## 1.4   PROTOCOLS AND STANDARDS                           19
      Protocols 19
      Standards 19
      Standards Organizations    20
      Internet Standards 21
## 1.5   RECOMMENDED READING                         21
      Books 21
      Sites 22
      RFCs 22
## 1.6   KEY TERMS 22
## 1.7   SUMMARY 23
## 1.8   PRACTICE SET 24
      Review Questions 24
      Exercises 24
      Research Activities 25

## Chapter 2       Network Models                   27
## 2.1   LAYERED TASKS             27
      Sender, Receiver, and Carrier      28
      Hierarchy 29
                                                                 ix

x   CONTENTS


## 2.2   THE OSI MODEL           29
                     Layered Architecture 30
                     Peer-to-Peer Processes 30
                     Encapsulation 33
## 2.3   LAYERS IN THE OSI MODEL                  33
                     Physical Layer 33
                     Data Link Layer 34
                     Network Layer 36
                     Transport Layer 37
                     Session Layer 39
                     Presentation Layer 39
                     Application Layer 41
                     Summary of Layers 42
## 2.4   TCP/IP PROTOCOL SUITE 42
                     Physical and Data Link Layers 43
                     Network Layer      43
                     Transport Layer 44
                     Application Layer 45
## 2.5   ADDRESSING         45
                     Physical Addresses 46
                     Logical Addresses 47
                     Port Addresses 49
                     Specific Addresses 50
## 2.6   RECOMMENDED READING                  50
                     Books 51
                     Sites 51
                     RFCs 51
## 2.7   KEY lERMS 51
## 2.8   SUMMARY 52
## 2.9   PRACTICE SET 52
                     Review Questions 52
                     Exercises 53
                     Research Activities 54


                     PART 2       Physical Layer and Media               55
## Chapter 3       Data and Signals          57
## 3.1   ANALOG AND DIGITAL             57
                     Analog and Digital Data 57
                     Analog and Digital Signals 58
                     Periodic and Nonperiodic Signals    58
## 3.2   PERIODIC ANALOG SIGNALS                  59
                     Sine Wave 59
                     Phase 63
                     Wavelength 64
                     Time and Frequency Domains     65
                     Composite Signals 66
                     Bandwidth 69
## 3.3   DIGITAL SIGNALS 71
                     Bit Rate 73
                     Bit Length 73
                     Digital Signal as a Composite Analog Signal    74
                     Transmission of Digital Signals 74

                                                                        CONTENTS   xi


## 3.4    TRANSMISSION IMPAIRMENT                        80
        Attenuation 81
        Distortion 83
        Noise 84
## 3.5    DATA RATE LIMITS              85
        Noiseless Channel: Nyquist Bit Rate 86
        Noisy Channel: Shannon Capacity 87
        Using Both Limits 88
## 3.6    PERFORMANCE             89
        Bandwidth 89
        Throughput 90
        Latency (Delay) 90
        Bandwidth-Delay Product       92
        Jitter 94
## 3.7    RECOMMENDED READING                      94
        Books   94
## 3.8    KEYTERMS 94
## 3.9    SUMMARY 95
## 3.10   PRACTICE SET 96
       Review Questions    96
       Exercises 96

## Chapter 4        Digital Transmission                101
## 4.1    DIGITAL-TO-DIGITAL CONVERSION                          101
       Line Coding 101
       Line Coding Schemes      106
       Block Coding 115
       Scrambling 118
## 4.2    ANALOG-TO-DIGITAL CONVERSION                               120
       Pulse Code Modulation (PCM)         121
       Delta Modulation (DM) 129
## 4.3    TRANSMISSION MODES                  131
       Parallel Transmission 131
       Serial Transmission 132
## 4.4    RECOMMENDED READING                       135
       Books    135
## 4.5    KEYTERMS 135
## 4.6    SUMMARY 136
## 4.7    PRACTICE SET 137
       Review Questions   137
       Exercises 137

## Chapter 5 Analog TranSl1'lission                     141
## 5.1    DIGITAL-TO-ANALOG CONVERSION                           141
       Aspects of Digital-to-Analog Conversion         142
       Amplitude Shift Keying 143
       Frequency Shift Keying 146
       Phase Shift Keying 148
       Quadrature Amplitude Modulation 152
## 5.2    ANALOG-TO-ANALOG CONVERSION                            152
       Amplitude Modulation 153
       Frequency Modulation 154
       Phase Modulation 155

xii   CONTENTS


## 5.3   RECOMMENDED READING                   156
                       Books   156
## 5.4   KEY lERMS 157
## 5.5   SUMMARY 157
## 5.6   PRACTICE SET 158
                       Review Questions      158
                       Exercises 158

## Chapter 6       Ba17chridth Utili::.ation: Multiplexing
                                       and Spreading 161
## 6.1   MULTIPLEXING            161
                       Frequency-Division Multiplexing 162
                       Wavelength-Division Multiplexing 167
                       Synchronous Time-Division Multiplexing 169
                       Statistical Time-Division Multiplexing 179
## 6.2   SPREAD SPECTRUM               180
                       Frequency Hopping Spread Spectrum (FHSS)          181
                       Direct Sequence Spread Spectrum 184
## 6.3   RECOMMENDED READING                   185
                       Books   185
## 6.4   KEY lERMS 185
## 6.5   SUMMARY 186
## 6.6   PRACTICE SET 187
                       Review Questions      187
                       Exercises 187

## Chapter 7       Transmission Media            191
## 7.1   GUIDED MEDIA            192
                       Twisted-Pair Cable 193
                       Coaxial Cable 195
                       Fiber-Optic Cable 198
## 7.2   UNGUIDED MEDIA: WIRELESS                    203
                       Radio Waves 205
                       Microwaves 206
                       Infrared 207
## 7.3   RECOMMENDED READING                   208
                       Books   208
## 7.4   KEY lERMS 208
## 7.5   SUMMARY 209
## 7.6   PRACTICE SET 209
                       Review Questions      209
                       Exercises 210

## Chapter 8       Svvitching      213
## 8.1   CIRCUIT-SWITCHED NETWORKS                     214
                       Three Phases 217
                       Efficiency 217
                       Delay 217
                       Circuit-Switched Technology in Telephone Networks       218
## 8.2   DATAGRAM NETWORKS                   218
                       Routing Table   220

                                                              CONTENTS   xiii


      Efficiency 220
      Delay 221
      Datagram Networks in the Internet     221
## 8.3   VIRTUAL-CIRCUIT NETWORKS                     221
      Addressing 222
      Three Phases 223
      Efficiency 226
      Delay in Virtual-Circuit Networks 226
      Circuit-Switched Technology in WANs 227
## 8.4   STRUCTURE OF A SWITCH                 227
      Structure of Circuit Switches 227
      Structure of Packet Switches 232
## 8.5   RECOMMENDED READING                   235
      Books   235
## 8.6   KEY TERMS 235
## 8.7   SUMMARY 236
## 8.8   PRACTICE SET 236
      Review Questions   236
      Exercises 237


## Chapter 9       Using Telephone and Cable Networks for Data
                      Transm,ission 241
## 9.1   1ELEPHONE NETWORK               241
      Major Components 241
      LATAs 242
      Signaling 244
      Services Provided by Telephone Networks           247
## 9.2   DIAL-UP MODEMS            248
      Modem Standards    249
## 9.3   DIGITAL SUBSCRIBER LINE 251
      ADSL 252
      ADSL Lite 254
      HDSL 255
      SDSL 255
      VDSL 255
      Summary 255
## 9.4   CABLE TV NETWORKS               256
      Traditional Cable Networks 256
      Hybrid Fiber-Coaxial (HFC) Network          256
## 9.5   CABLE TV FOR DATA TRANSFER                        257
      Bandwidth 257
      Sharing 259
      CM and CMTS 259
      Data Transmission Schemes: DOCSIS           260
## 9.6   RECOMMENDED READING                   261
      Books   261
## 9.7   KEY TERMS 261
## 9.8   SUMMARY 262
## 9.9   PRACTICE SET 263
      Review Questions    263
      Exercises 264

xiv   CONTENTS


                    PART 3      Data Link Layer                265
## Chapter 10         Error Detection and Correction               267
## 10.1   INTRODUCTION             267
                    Types of Errors 267
                    Redundancy 269
                    Detection Versus Correction 269
                    Forward Error Correction Versus Retransmission            269
                    Coding 269
                    Modular Arithmetic 270
## 10.2   BLOCK CODING             271
                    Error Detection 272
                    Error Correction 273
                    Hamming Distance 274
                    Minimum Hamming Distance             274
## 10.3   LINEAR BLOCK CODES                   277
                    Minimum Distance for Linear Block Codes             278
                    Some Linear Block Codes 278
## 10.4   CYCLIC CODES             284
                    Cyclic Redundancy Check 284
                    Hardware Implementation 287
                    Polynomials 291
                    Cyclic Code Analysis 293
                    Advantages of Cyclic Codes 297
                    Other Cyclic Codes 297
## 10.5   CHECKSUM           298
                    Idea 298
                    One's Complement 298
                    Internet Checksum 299
## 10.6   RECOMMENDED READING                        30 I
                    Books 301
                    RFCs 301
## 10.7   KEY lERMS 301
## 10.8   SUMMARY 302
## 10.9   PRACTICE SET 303
                    Review Questions     303
                    Exercises 303

## Chapter 11         Data Link Control              307
## 11.1   FRAMING        307
                    Fixed-Size Framing 308
                    Variable-Size Framing 308
## 11.2   FLOW AND ERROR CONTROL                        311
                    Flow Control 311
                    Error Control 311
## 11.3   PROTOCOLS 311
## 11.4   NOISELESS CHANNELS                   312
                    Simplest Protocol 312
                    Stop-and-Wait Protocol 315
## 11.5   NOISY CHANNELS                 318
                    Stop-and-Wait Automatic Repeat Request 318
                    Go-Back-N Automatic Repeat Request 324

                                                                    CONTENTS   xv


       Selective Repeat Automatic Repeat Request      332
       Piggybacking 339
## 11.6   HDLC     340
       Configurations and Transfer Modes      340
       Frames 341
       Control Field 343
## 11.7   POINT-TO-POINT PROTOCOL                 346
       Framing 348
       Transition Phases 349
       Multiplexing 350
       Multilink PPP 355
## 11.8   RECOMMENDED READING                    357
       Books   357
## 11.9 KEY TERMS 357
## 11.10 SUMMARY 358
## 11.11 PRACTICE SET 359
       Review Questions    359
       Exercises 359

## Chapter 12         Multiple Access       363
## 12.1   RANDOMACCESS              364
       ALOHA 365
       Carrier Sense Multiple Access (CSMA) 370
       Carrier Sense Multiple Access with Collision Detection (CSMAlCD) 373
       Carrier Sense Multiple Access with Collision Avoidance (CSMAlCA) 377
## 12.2   CONTROLLED ACCESS                379
       Reservation 379
       Polling 380
       Token Passing 381
## 12.3   CHANNELIZATION             383
       Frequency-Division Multiple Access (FDMA) 383
       Time-Division Multiple Access (TDMA) 384
       Code-Division Multiple Access (CDMA) 385
## 12.4   RECOMMENDED READING                    390
       Books   391
## 12.5   KEY TERMS 391
## 12.6   SUMMARY 391
## 12.7   PRACTICE SET 392
       Review Questions 392
       Exercises 393
       Research Activities 394

## Chapter 13         Wired LANs: Ethernet         395
## 13.1   IEEE STANDARDS            395
       Data Link Layer 396
       Physical Layer 397
## 13.2   STANDARD ETHERNET                397
       MAC Sublayer 398
       Physical Layer 402
## 13.3   CHANGES IN THE STANDARD                  406
       Bridged Ethernet 406
       Switched Ethernet 407
       Full-Duplex Ethernet 408

xvi   CONTENTS


## 13.4   FAST ETHERNET             409
                    MAC Sublayer 409
                    Physical Layer 410
## 13.5   GIGABIT ETHERNET                412
                    MAC Sublayer 412
                    Physical Layer 414
                    Ten-Gigabit Ethernet 416
## 13.6   RECOMMENDED READING                         417
                    Books   417
## 13.7   KEY TERMS 417
## 13.8   SUMMARY 417
## 13.9   PRACTICE SET 418
                    Review Questions    418
                    Exercises 419

## Chapter 14         Wireless LANs              421
## 14.1   IEEE 802.11    421
                    Architecture 421
                    MAC Sublayer 423
                    Addressing Mechanism       428
                    Physical Layer 432
## 14.2   BLUETOOTH          434
                    Architecture 435
                    Bluetooth Layers 436
                    Radio Layer 436
                    Baseband Layer 437
                    L2CAP 440
                    Other Upper Layers 441
## 14.3   RECOMMENDED READING                         44 I
                    Books   442
## 14.4   KEYTERMS 442
## 14.5   SUMMARY 442
## 14.6   PRACTICE SET 443
                    Review Questions    443
                    Exercises 443

## Chapter 15         Connecting LANs, Backbone Networks,
                                       and VirtuaL LANs 445
## 15.1   CONNECTING DEVICES                    445
                    Passive Hubs 446
                    Repeaters 446
                    Active Hubs 447
                    Bridges 447
                    Two-Layer Switches 454
                    Routers 455
                    Three-Layer Switches 455
                    Gateway 455
## 15.2   BACKBONE NETWORKS                     456
                    Bus Backbone 456
                    Star Backbone 457
                    Connecting Remote LANs          457

                                                                    CONTENTS   xvii


## 15.3    VIRTUAL LANs 458
         Membership 461
         Configuration 461
         Communication Between Switches              462
         IEEE Standard 462
         Advantages 463
## 15.4    RECOMMENDED READING                         463
         Books 463
         Site 463
## 15.5     KEY TERMS 463
## 15.6     SUMMARY 464
## 15.7     PRACTICE SET 464
         Review Questions    464
         Exercises 465

## Chapter 16         Wireless WANs: Cellular Telephone and
                            Satellite Networks 467
## 16.1    CELLULAR TELEPHONY                     467
        Frequency-Reuse Principle        467
        Transmitting 468
        Receiving 469
        Roaming 469
        First Generation 469
        Second Generation 470
        Third Generation 477
## 16.2    SATELLITE NETWORKS                     478
        Orbits 479
        Footprint 480
        Three Categories of Satellites    480
        GEO Satellites 481
        MEO Satellites 481
        LEO Satellites 484
## 16.3    RECOMMENDED READING                      487
        Books   487
## 16.4    KEY TERMS 487
## 16.5    SUMMARY 487
## 16.6    PRACTICE SET 488
        Review Questions    488
        Exercises 488

## Chapter 17          SONETISDH                491
## 17.1    ARCHITECTURE 491
        Signals 491
        SONET Devices 492
        Connections 493
## 17.2    SONET LAYERS           494
        Path Layer 494
        Line Layer 495
## Section Layer 495
        Photonic Layer 495
        Device-Layer Relationships       495

xviii   CONTENTS


## 17.3    SONET FRAMES           496
                      Frame, Byte, and Bit Transmission    496
                      STS-l Frame Format 497
                      Overhead Summary 501
                      Encapsulation 501
## 17.4    STS MULTIPLEXING 503
                      Byte Interleaving 504
                      Concatenated Signal 505
                      AddlDrop Multiplexer 506
## 17.5    SONET NETWORKS               507
                      Linear Networks 507
                      Ring Networks 509
                      Mesh Networks 510
## 17.6    VIRTUAL TRIBUTARIES                512
                      Types ofVTs    512
## 17.7    RECOMMENDED READING                      513
                      Books   513
## 17.8 KEY lERMS 513
## 17.9 SUMMARY 514
## 17.1 0 PRACTICE SET 514
                      Review Questions     514
                      Exercises 515

## Chapter 18         Virtual-Circuit Networks: Frame Relm' and ATM   517
## 18.1    FRAME RELAY           517
                      Architecture 518
                      Frame Relay Layers 519
                      Extended Address 521
                      FRADs 522
                      VOFR 522
                      LMI 522
                      Congestion Control and Quality of Service        522
## 18.2    ATM     523
                      Design Goals 523
                      Problems 523
                      Architecture 526
                      Switching 529
                      ATM Layers 529
                      Congestion Control and Quality of Service        535
## 18.3    ATM LANs       536
                      ATM LAN Architecture 536
                      LAN Emulation (LANE) 538
                      Client/Server Model 539
                      Mixed Architecture with Client/Server      540
## 18.4    RECOMMENDED READING                      540
                      Books   541
## 18.5   KEY lERMS 541
## 18.6   SUMMARY 541
## 18.7   PRACTICE SET 543
                      Review Questions     543
                      Exercises 543

                                                                        CONTENTS   xix


       PART 4       Network Layer           547
## Chapter 19           Netvl/ark Layer: Logical Addressing    549
## 19.1   IPv4ADDRESSES            549
       Address Space 550
       Notations 550
       Classful Addressing 552
       Classless Addressing 555
       Network Address Translation (NAT)     563
## 19.2   IPv6 ADDRESSES           566
       Structure 567
       Address Space 568
## 19.3   RECOMMENDED READING                  572
       Books 572
       Sites 572
       RFCs 572
## 19.4   KEY TERMS 572
## 19.5   SUMMARY 573
## 19.6   PRACTICE SET 574
       Review Questions 574
       Exercises 574
       Research Activities 577

## Chapter 20           Network Layer: Internet Protocol      579
## 20.1   INTERNETWORKING                579
       Need for Network Layer 579
       Internet as a Datagram Network 581
       Internet as a Connectionless Network 582
## 20.2   IPv4   582
       Datagram 583
       Fragmentation 589
       Checksum 594
       Options 594
## 20.3   IPv6   596
       Advantages 597
       Packet Format 597
       Extension Headers 602
## 20.4   TRANSITION FROM IPv4 TO IPv6                603
       Dual Stack 604
       Tunneling 604
       Header Translation    605
## 20.5   RECOMMENDED READING                  605
       Books 606
       Sites 606
       RFCs 606
## 20.6   KEY TERMS 606
## 20.7   SUMMARY 607
## 20.8   PRACTICE SET 607
       Review Questions 607
       Exercises 608
       Research Activities 609

xx   CONTENTS


## Chapter 21         Network Layer: Address Mapping, Error Reporting,
                                          and Multicasting 611
## 21.1   ADDRESS MAPPING               611
                       Mapping Logical to Physical Address: ARP 612
                       Mapping Physical to Logical Address: RARp, BOOTP, and DHCP   618
## 21.2   ICMP     621
                       Types of Messages 621
                       Message Format 621
                       Error Reporting 622
                       Query 625
                       Debugging Tools 627
## 21.3   IGMP     630
                       Group Management 630
                       IGMP Messages 631
                       Message Format 631
                       IGMP Operation 632
                       Encapsulation 635
                       Netstat Utility 637
## 21.4   ICMPv6      638
                       Error Reporting    638
                       Query 639
## 21.5   RECOMMENDED READING                       640
                       Books 641
                       Site 641
                       RFCs 641
## 21.6   KEYTERMS 641
## 21.7   SUMMARY 642
## 21.8   PRACTICE SET 643
                       Review Questions 643
                       Exercises 644
                       Research Activities 645

## Chapter 22         Network Layer: Delivery, Forwarding,
                                          and Routing 647
## 22.1   DELIVERY          647
                       Direct Versus Indirect Delivery     647
## 22.2   FORWARDING              648
                       Forwarding Techniques 648
                       Forwarding Process 650
                       Routing Table 655
## 22.3   UNICAST ROUTING PROTOCOLS                       658
                       Optimization 658
                       Intra- and Interdomain Routing      659
                       Distance Vector Routing 660
                       Link State Routing 666
                       Path Vector Routing 674
## 22.4   MULTICAST ROUTING PROTOCOLS                       678
                       Unicast, Multicast, and Broadcast     678
                       Applications 681
                       Multicast Routing 682
                       Routing Protocols 684

                                                                   CONTENTS   xxi


## 22.5   RECOMMENDED READING                 694
       Books 694
       Sites 694
       RFCs 694
## 22.6   KEY lERMS 694
## 22.7   SUMMARY 695
## 22.8   PRACTICE SET 697
       Review Questions 697
       Exercises 697
       Research Activities 699

       PART 5        Transport Layer           701
## Chapter 23       Process-fa-Process Delivery: UDp, TCp,
                        and SeTP         703
## 23.1   PROCESS-TO-PROCESS DELIVERY                   703
       Client/Server Paradigm 704
       Multiplexing and Demultiplexing 707
       Connectionless Versus Connection-Oriented Service     707
       Reliable Versus Unreliable 708
       Three Protocols 708
## 23.2   USER DATAGRAM PROTOCOL (UDP)                    709
       Well-Known Ports for UDP    709
       User Datagram 710
       Checksum 711
       UDP Operation 713
       Use ofUDP 715
## 23.3   TCP    715
       TCP Services 715
       TCP Features 719
       Segment 721
       A TCP Connection 723
       Flow Control 728
       Error Control 731
       Congestion Control 735
## 23.4   SCTP    736
       SCTP Services 736
       SCTP Features 738
       Packet Format 742
       An SCTP Association 743
       Flow Control 748
       Error Control 751
       Congestion Control 753
## 23.5   RECOMMENDED READING                753
       Books 753
       Sites 753
       RFCs 753
## 23.6   KEY lERMS 754
## 23.7   SUMMARY 754
## 23.8   PRACTICE SET 756
       Review Questions 756
       Exercises 757
       Research Activities 759

xxii   CONTENTS


## Chapter 24         Congestion Control and Quality (~j'Service   767
## 24.1   DATA lRAFFIC            761
                     Traffic Descriptor 76]
                     Traffic Profiles 762
## 24.2   CONGESTION             763
                     Network Performance          764
## 24.3   CONGESTION CONTROL                  765
                     Open-Loop Congestion Control 766
                     Closed-Loop Congestion Control 767
## 24.4   lWO EXAMPLES 768
                     Congestion Control in TCP 769
                     Congestion Control in Frame Relay 773
## 24.5   QUALITY OF SERVICE 775
                     Flow Characteristics     775
                     Flow Classes 776
## 24.6   TECHNIQUES TO IMPROVE QoS                      776
                     Scheduling 776
                     Traffic Shaping 777
                     Resource Reservation 780
                     Admission Control 780
## 24.7   INTEGRATED SERVICES                 780
                     Signaling 781
                     Flow Specification 781
                     Admission 781
                     Service Classes 781
                     RSVP 782
                     Problems with Integrated Services        784
## 24.8   DIFFERENTIATED SERVICES                    785
                     DS Field   785
## 24.9   QoS IN SWITCHED NETWORKS                       786
                     QoS in Frame Relay      787
                     QoS inATM 789
## 24.10 RECOMMENDED READING                       790
                     Books   791
## 24.11 KEY TERMS 791
## 24.12 SUMMARY 791
## 24.13 PRACTICE SET 792
                     Review Questions       792
                     Exercises 793


                     PART 6        Application Layer            795
## Chapter 25         DO/nain Name Svstem               797
## 25.1   NAME SPACE          798
                     Flat Name Space 798
                     Hierarchical Name Space 798
## 25.2   DOMAIN NAME SPACE                  799
                     Label 799
                     Domain Narne     799
                     Domain 801

                                                                     CONTENTS   xxiii


## 25.3    DISTRIBUTION OF NAME SPACE                       801
        Hierarchy of Name Servers 802
        Zone 802
        Root Server 803
        Primary and Secondary Servers 803
## 25.4    DNS IN THE INTERNET                803
        Generic Domains 804
        Country Domains 805
        Inverse Domain 805
## 25.5    RESOLUTION          806
        Resolver 806
        Mapping Names to Addresses 807
        Mapping Address to Names 807
        Recursive Resolution 808
        Iterative Resolution 808
        Caching 808
## 25.6    DNS MESSAGES           809
        Header   809
## 25.7    TYPES OF RECORDS               811
        Question Record 811
        Resource Record 811
## 25.8    REGISTRARS 811
## 25.9    DYNAMIC DOMAIN NAME SYSTEM (DDNS)                      812
## 25.10   ENCAPSULATION 812
## 25.11   RECOMMENDED READING 812
        Books 813
        Sites 813
        RFCs 813
## 25.12 KEY TERMS 813
## 25.13 SUMMARY 813
## 25.14 PRACTICE SET 814
        Review Questions    814
        Exercises 815

## Chapter 26         Remote Logging, Electronic Mail, and File Transfer   817
## 26.1    REMOTE LOGGING               817
        TELNET     817
## 26.2    ELECTRONIC MAIL              824
        Architecture 824
        User Agent 828
        Message Transfer Agent: SMTP 834
        Message Access Agent: POP and IMAP             837
        Web-Based Mail 839
## 26.3    FILE TRANSFER          840
        File Transfer Protocol (FTP)    840
        Anonymous FTP 844
## 26.4    RECOMMENDED READING                      845
        Books 845
        Sites 845
        RFCs 845
## 26.5    KEY lERMS 845
## 26.6    SUMMARY 846

xxiv   CONTENTS


## 26.7   PRACTICE SET         847
                    Review Questions 847
                    Exercises 848
                    Research Activities 848

## Chapter 27         WWW and HTTP           851
## 27.1   ARCHITECTURE           851
                    Client (Browser) 852
                    Server 852
                    Uniform Resource Locator     853
                    Cookies 853
## 27.2   WEB DOCUMENTS              854
                    Static Documents 855
                    Dynamic Documents 857
                    Active Documents 860
## 27.3   HTTP     861
                    HTTP Transaction 861
                    Persistent Versus Nonpersistent Connection   868
                    Proxy Server 868
## 27.4   RECOMMENDED READING                 869
                    Books 869
                    Sites 869
                    RFCs 869
## 27.5   KEY 1ERMS 869
## 27.6   SUMMARY 870
## 27.7   PRACTICE SET 871
                    Review Questions    871
                    Exercises 871

## Chapter 28         Network Management: SNMP           873
## 28.1   NETWORK MANAGEMENT SYSTEM                       873
                    Configuration Management 874
                    Fault Management 875
                    Performance Management 876
                    Security Management 876
                    Accounting Management 877
## 28.2   SIMPLE NETWORK MANAGEMENT PROTOCOL (SNMP)                   877
                    Concept 877
                    Management Components 878
                    Structure of Management Information    881
                    Management Information Base (MIB)      886
                    Lexicographic Ordering 889
                    SNMP 891
                    Messages 893
                    UDP Ports 895
                    Security 897
## 28.3   RECOMMENDED READING                 897
                    Books 897
                    Sites 897
                    RFCs 897
## 28.4   KEY 1ERMS 897
## 28.5   SUMMARY 898

                                                                     CONTENTS   xxv


## 28.6   PRACTICE SET            899
       Review Questions    899
       Exercises 899

## Chapter 29         Multimedia       901
## 29.1   DIGITIZING AUDIO AND VIDEO                 902
       Digitizing Audio 902
       Digitizing Video 902
## 29.2   AUDIO AND VIDEO COMPRESSION                      903
       Audio Compression 903
       Video Compression 904
## 29.3   STREAMING STORED AUDIO/VIDEO                      908
       First Approach: Using a Web Server 909
       Second Approach: Using a Web Server with Metafile 909
       Third Approach: Using a Media Server 910
       Fourth Approach: Using a Media Server and RTSP 911
## 29.4   STREAMING LIVE AUDIOIVIDEO 912
## 29.5   REAL-TIME INTERACTIVE AUDIOIVIDEO                       912
       Characteristics   912
## 29.6   RTP    916
       RTP Packet Format       917
       UDPPort 919
## 29.7   RTCP     919
       Sender Report 919
       Receiver Report 920
       Source Description Message 920
       Bye Message 920
       Application-Specific Message 920
       UDP Port 920
## 29.8   VOICE OVER IP           920
       SIP 920
       H.323 923
## 29.9   RECOMMENDED READING                  925
       Books 925
       Sites 925
## 29.10 KEY 1ERMS 925
## 29.11 SUMMARY 926
## 29.12 PRACTICE SET 927
       Review Questions 927
       Exercises 927
       Research Activities 928

       PART 7         Security       929
## Chapter 30         Cryptography       931
## 30.1   INTRODUCTION             931
       Definitions 931
       Two Categories 932
## 30.2   SYMMETRIC-KEY CRYPTOGRAPHY                       935
       Traditional Ciphers 935
       Simple Modem Ciphers 938

xxvi   CONTENTS


                    Modern Round Ciphers 940
                    Mode of Operation 945
## 30.3   ASYMMETRIC-KEY CRYPTOGRAPHY                     949
                    RSA 949
                    Diffie-Hellman   952
## 30.4   RECOMMENDED READING                 956
                    Books   956
## 30.5   KEY TERMS 956
## 30.6   SUMMARY 957
## 30.7   PRACTICE SET 958
                    Review Questions 958
                    Exercises 959
                    Research Activities 960

## Chapter 31       Network Security         961
## 31.1   SECURITY SERVICES            961
                    Message Confidentiality 962
                    Message Integrity 962
                    Message Authentication 962
                    Message Nonrepudiation 962
                    Entity Authentication 962
## 31.2   MESSAGE CONFIDENTIALITY                962
                    Confidentiality with Symmetric-Key Cryptography 963
                    Confidentiality with Asymmetric-Key Cryptography 963
## 31.3   MESSAGE INTEGRITY             964
                    Document and Fingerprint 965
                    Message and Message Digest 965
                    Difference 965
                    Creating and Checking the Digest 966
                    Hash Function Criteria 966
                    Hash Algorithms: SHA-1 967
## 31.4   MESSAGE AUTHENTICATION                 969
                    MAC     969
## 31.5   DIGITAL SIGNATURE             971
                    Comparison 97 I
                    Need for Keys 972
                    Process 973
                    Services 974
                    Signature Schemes 976
## 31.6   ENTITY AUTHENTICATION               976
                    Passwords 976
                    Challenge-Response     978
## 31.7   KEY MANAGEMENT               981
                    Symmetric-Key Distribution 981
                    Public-Key Distribution 986
## 31.8   RECOMMENDED READING                 990
                    Books   990
## 31.9 KEY TERMS 990
## 31.10 SUMMARY 991
## 31.11 PRACTICE SET 992
                    Review Questions 992
                    Exercises 993
                    Research Activities 994

                                                                   CONTENTS         xxvii


## Chapter 32              Security in the Internet: IPSec, SSUFLS, PGP, VPN,
                               and Firewalls 995
## 32.1   IPSecurity (lPSec)         996
       Two Modes 996
       Two Security Protocols 998
       Security Association 1002
       Internet Key Exchange (IKE) 1004
       Virtual Private Network 1004
## 32.2   SSLffLS          1008
       SSL Services 1008
       Security Parameters 1009
       Sessions and Connections 1011
       Four Protocols 10 12
       Transport Layer Security 1013
## 32.3   PGP       1014
       Security Parameters 1015
       Services 1015
       A Scenario 1016
       PGP Algorithms 1017
       Key Rings 1018
       PGP Certificates 1019
## 32.4   FIREWALLS           1021
       Packet-Filter Firewall 1022
       Proxy Firewall 1023
## 32.5   RECOMMENDED READING                      1024
       Books     1024
## 32.6   KEY lERMS 1024
## 32.7   SUMMARY 1025
## 32.8   PRACTICE SET 1026
       Review Questions         1026
       Exercises 1026

       Appendix A              Unicode        1029
A.l    UNICODE           1029
       Planes 1030
       Basic Multilingual Plane (BMP) 1030
       Supplementary Multilingual Plane (SMP) 1032
       Supplementary Ideographic Plane (SIP) 1032
       Supplementary Special Plane (SSP) 1032
       Private Use Planes (PUPs) 1032
A.2    ASCII      1032
       Some Properties of ASCII         1036

       Appendix B              Numbering Systems       1037
B.l    BASE 10: DECIMAL                1037
       Weights    1038
B.2    BASE 2: BINARY             1038
       Weights 1038
       Conversion 1038

xxviii   CONTENTS


              B.3      BASE 16: HEXADECIMAL              1039
                       Weights 1039
                       Conversion 1039
                       A Comparison 1040
              BA       BASE 256: IP ADDRESSES            1040
                       Weights 1040
                       Conversion 1040
              B.5      OTHER CONVERSIONS               1041
                       Binary and Hexadecimal 1041
                       Base 256 and Binary 1042

                       Appendix C        Mathenwtical Revietv          1043
              C.1      TRIGONOMETRIC FUNCTIONS                  1043
                       Sine Wave 1043
                       Cosine Wave 1045
                       Other Trigonometric Functions 1046
                       Trigonometric Identities 1046
              C.2      FOURIER ANALYSIS          1046
                       Fourier Series 1046
                       Fourier Transform 1048
              C.3      EXPONENT AND LOGARITHM                   1050
                       Exponential Function 1050
                       Logarithmic Function 1051

                       Appendix 0        8B/6T Code           1055
                       Appendix E        Telephone History           1059
                       Before 1984 1059
                       Between 1984 and 1996    1059
                       After 1996 1059

                       Appendix F        Contact Addresses           1061
                       Appendix G        RFCs      1063
                       Appendix H        UDP and TCP Ports             1065

               Acronyms         1067
               Glossary     1071
               References       1107
               Index     1111

Data communications and networking may be the fastest growing technologies in our
culture today. One of the ramifications of that growth is a dramatic increase in the number
of professions where an understanding of these technologies is essential for success-
and a proportionate increase in the number and types of students taking courses to learn
about them.

Features of the Book
Several features of this text are designed to make it particularly easy for students to
understand data communications and networking.

Structure
We have used the five-layer Internet model as the framework for the text not only because
a thorough understanding of the model is essential to understanding most current network-
ing theory but also because it is based on a structure of interdependencies: Each layer
builds upon the layer beneath it and supports the layer above it. In the same way, each con-
cept introduced in our text builds upon the concepts examined in the previous sections. The
Internet model was chosen because it is a protocol that is fully implemented.
     This text is designed for students with little or no background in telecommunica-
tions or data communications. For this reason, we use a bottom-up approach. With this
approach, students learn first about data communications (lower layers) before learning
about networking (upper layers).

Visual Approach
The book presents highly technical subject matter without complex formulas by using a
balance of text and figures. More than 700 figures accompanying the text provide a
visual and intuitive opportunity for understanding the material. Figures are particularly
important in explaining networking concepts, which are based on connections and
transmission. Both of these ideas are easy to grasp visually.

Highlighted Points
We emphasize important concepts in highlighted boxes for quick reference and imme-
diate attention.
                                                                                        xxix

xxx   PREFACE


                Examples and Applications
                When appropriate, we have selected examples to reflect true-to-life situations. For exam-
                ple, in Chapter 6 we have shown several cases of telecommunications in current telephone
                networks.

                Recommended Reading
                Each chapter includes a list of books and sites that can be used for further reading.

                Key Terms
                Each chapter includes a list of key terms for the student.

                Summary
                Each chapter ends with a summary of the material covered in that chapter. The sum-
                mary provides a brief overview of all the important points in the chapter.

                Practice Set
                Each chapter includes a practice set designed to reinforce and apply salient concepts. It
                consists of three parts: review questions, exercises, and research activities (only for
                appropriate chapters). Review questions are intended to test the student's first-level under-
                standing of the material presented in the chapter. Exercises require deeper understanding
                of the materiaL Research activities are designed to create motivation for further study.

                Appendixes
                The appendixes are intended to provide quick reference material or a review of materi-
                als needed to understand the concepts discussed in the book.

                Glossary and Acronyms
                The book contains an extensive glossary and a list of acronyms.

                Changes in the Fourth Edition
                The Fourth Edition has major changes from the Third Edition, both in the organization
                and in the contents.

                Organization
                The following lists the changes in the organization of the book:
                 1. Chapter 6 now contains multiplexing as well as spreading.
                 2. Chapter 8 is now totally devoted to switching.
                 3. The contents of Chapter 12 are moved to Chapter 11.
                 4. Chapter 17 covers SONET technology.
                 5. Chapter 19 discusses IP addressing.
                 6. Chapter 20 is devoted to the Internet Protocol.
                 7. Chapter 21 discusses three protocols: ARP, ICMP, and IGMP.
                 8. Chapter 28 is new and devoted to network management in the Internet.
                 9. The previous Chapters 29 to 31 are now Chapters 30 to 32.

                                                                        PREFACE        xxxi


Contents
We have revised the contents of many chapters including the following:
 1. The contents of Chapters 1 to 5 are revised and augmented. Examples are added to
    clarify the contents.
 2. The contents of Chapter 10 are revised and augmented to include methods of error
    detection and correction.
 3. Chapter 11 is revised to include a full discussion of several control link protocols.
 4. Delivery, forwarding, and routing of datagrams are added to Chapter 22.
 5. The new transport protocol, SCTP, is added to Chapter 23.
 6. The contents of Chapters 30, 31, and 32 are revised and augmented to include
    additional discussion about security issues and the Internet.
 7. New examples are added to clarify the understanding of concepts.

End Materials
 1. A section is added to the end of each chapter listing additional sources for study.
 2. The review questions are changed and updated.
 3. The multiple-choice questions are moved to the book site to allow students to self-test
    their knowledge about the contents of the chapter and receive immediate feedback.
 4. Exercises are revised and new ones are added to the appropriate chapters.
 5. Some chapters contain research activities.

Instructional Materials
Instructional materials for both the student and the teacher are revised and augmented.
The solutions to exercises contain both the explanation and answer including full col-
ored figures or tables when needed. The Powerpoint presentations are more compre-
hensive and include text and figures.

Contents
The book is divided into seven parts. The first part is an overview; the last part concerns
network security. The middle five parts are designed to represent the five layers of the
Internet model. The following summarizes the contents of each part.

Part One: Overview
The first part gives a general overview of data communications and networking. Chap-
ter 1 covers introductory concepts needed for the rest of the book. Chapter 2 introduces
the Internet model.

Part Two: Physical Layer
The second part is a discussion of the physical layer of the Internet model. Chapters 3
to 6 discuss telecommunication aspects of the physical layer. Chapter 7 introduces the
transmission media, which, although not part of the physical layer, is controlled by it.
## Chapter 8 is devoted to switching, which can be used in several layers. Chapter 9 shows
how two public networks, telephone and cable TV, can be used for data transfer.

xxxii   PREFACE


              Part Three: Data Link Layer
              The third part is devoted to the discussion of the data link layer of the Internet model.
## Chapter 10 covers error detection and correction. Chapters 11, 12 discuss issues related
              to data link control. Chapters 13 through 16 deal with LANs. Chapters 17 and] 8 are
              about WANs. LANs and WANs are examples of networks operating in the first two lay-
              ers of the Internet model.

              Part Four: Network Layer
              The fourth part is devoted to the discussion of the network layer of the Internet model.
## Chapter 19 covers IP addresses. Chapters 20 and 21 are devoted to the network layer
              protocols such as IP, ARP, ICMP, and IGMP. Chapter 22 discusses delivery, forwarding,
              and routing of packets in the Internet.

              Part Five: Transport Layer
              The fifth part is devoted to the discussion of the transport layer of the Internet model.
## Chapter 23 gives an overview of the transport layer and discusses the services and
              duties of this layer. It also introduces three transport-layer protocols: UDP, TCP, and
              SCTP. Chapter 24 discusses congestion control and quality of service, two issues
              related to the transport layer and the previous two layers.

              Part Six: Application Layer
              The sixth part is devoted to the discussion of the application layer of the Internet model.
## Chapter 25 is about DNS, the application program that is used by other application pro-
              grams to map application layer addresses to network layer addresses. Chapter 26 to 29
              discuss some common applications protocols in the Internet.

              Part Seven: Security
              The seventh part is a discussion of security. It serves as a prelude to further study in this
              subject. Chapter 30 briefly discusses cryptography. Chapter 31 introduces security
              aspects. Chapter 32 shows how different security aspects can be applied to three layers
              of the Internet model.

              Online Learning Center
              The McGraw-Hill Online Learning Center contains much additional material. Avail-
              able at www.mhhe.com/forouzan. As students read through Data Communications and
              Networking, they can go online to take self-grading quizzes. They can also access lec-
              ture materials such as PowerPoint slides, and get additional review from animated fig-
              ures from the book. Selected solutions are also available over the Web. The solutions to
              odd-numbered problems are provided to students, and instructors can use a password to
              access the complete set of solutions.
                   Additionally, McGraw-Hill makes it easy to create a website for your networking
              course with an exclusive McGraw-Hill product called PageOut. It requires no prior
              knowledge of HTML, no long hours, and no design skills on your part. Instead, Page:-
              Out offers a series of templates. Simply fill them with your course information and

                                                                       PREFACE        xxxiii


click on one of 16 designs. The process takes under an hour and leaves you with a pro-
fessionally designed website.
     Although PageOut offers "instant" development, the finished website provides pow-
erful features. An interactive course syllabus allows you to post content to coincide with
your lectures, so when students visit your PageOut website, your syllabus will direct them
to components of Forouzan's Online Learning Center, or specific material of your own.

How to Use the Book
This book is written for both an academic and a professional audience. The book can be
used as a self-study guide for interested professionals. As a textbook, it can be used for
a one-semester or one-quarter course. The following are some guidelines.
o Parts one to three are strongly recommended.
o Parts four to six can be covered if there is no following course in TCP/IP protocol.
o Part seven is recommended if there is no following course in network security.
Acknowledgments
It is obvious that the development of a book of this scope needs the support of many people.

Peer Review
The most important contribution to the development of a book such as this comes from
peer reviews. We cannot express our gratitude in words to the many reviewers who
spent numerous hours reading the manuscript and providing us with helpful comments
and ideas. We would especially like to acknowledge the contributions of the following
reviewers for the third and fourth editions of this book.

    Farid Ahmed, Catholic University
    Kaveh Ashenayi, University of Tulsa
    Yoris Au, University ofTexas, San Antonio
    Essie Bakhtiar, Clayton College & State University
    Anthony Barnard, University ofAlabama, Brimingham
    A.T. Burrell, Oklahoma State University
    Scott Campbell, Miami University
    Teresa Carrigan, Blackburn College
    Hwa Chang, Tufts University
    Edward Chlebus, Illinois Institute ofTechnology
    Peter Cooper, Sam Houston State University
    Richard Coppins, Virginia Commonwealth University
    Harpal Dhillon, Southwestern Oklahoma State University
    Hans-Peter Dommel, Santa Clara University
    M. Barry Dumas, Baruch College, CUNY
    William Figg, Dakota State University
    Dale Fox, Quinnipiac University
    Terrence Fries, Coastal Carolina University
    Errin Fulp, Wake Forest University

xxxiv   PREFACE


                  Sandeep Gupta, Arizona State University
                  George Hamer, South Dakota State University
                  James Henson, California State University, Fresno
                  Tom Hilton, Utah State University
                  Allen Holliday, California State University, Fullerton
                  Seyed Hossein Hosseini, University ofWisconsin, Milwaukee
                  Gerald Isaacs, Carroll College, Waukesha
                  Hrishikesh Joshi, DeVry University
                  E.S. Khosravi, Southern University
                  Bob Kinicki, Worcester Polytechnic University
                  Kevin Kwiat, Hamilton College
                  Ten-Hwang Lai, Ohio State University
                  Chung-Wei Lee, Auburn University
                  Ka-Cheong Leung, Texas Tech University
                  Gertrude Levine, Fairleigh Dickinson University
                  Alvin Sek See Lim, Auburn University
                  Charles Liu, California State University, Los Angeles
                  Wenhang Liu, California State University, Los Angeles
                  Mark Llewellyn, University of Central Florida
                  Sanchita Mal-Sarkar, Cleveland State University
                  Louis Marseille, Harford Community College
                  Kevin McNeill, University ofArizona
                  Arnold C. Meltzer, George Washington University
                  Rayman Meservy, Brigham Young University
                  Prasant Mohapatra, University of California, Davis
                  Hung Z Ngo, SUNY, Buffalo
                  Larry Owens, California State University, Fresno
                  Arnold Patton, Bradley University
                  Dolly Samson, Hawaii Pacific University
                  Joseph Sherif, California State University, Fullerton
                  Robert Simon, George Mason University
                  Ronald 1. Srodawa, Oakland University
                  Daniel Tian, California State University, Monterey Bay
                  Richard Tibbs, Radford University
                  Christophe Veltsos, Minnesota State University, Mankato
                  Yang Wang, University ofMaryland, College Park
                  Sherali Zeadally, Wayne State University

              McGraw-Hill Staff
              Special thanks go to the staff of McGraw-Hill. Alan Apt, our publisher, proved how a
              proficient publisher can make the impossible possible. Rebecca Olson, the developmen-
              tal editor, gave us help whenever we needed it. Sheila Frank, our project manager,
              guided us through the production process with enormous enthusiasm. We also thank
              David Hash in design, Kara Kudronowicz in production, and Patti Scott, the copy editor.

Overview


Objectives
Part 1 provides a general idea of what we will see in the rest of the book. Four major
concepts are discussed: data communications, networking, protocols and standards,
and networking models.
     Networks exist so that data may be sent from one place to another-the basic con-
cept of data communications. To fully grasp this subject, we must understand the data
communication components, how different types of data can be represented, and how
to create a data flow.
     Data communications between remote parties can be achieved through a process
called networking, involving the connection of computers, media, and networking
devices. Networks are divided into two main categories: local area networks (LANs)
and wide area networks (WANs). These two types of networks have different charac-
teristics and different functionalities. The Internet, the main focus of the book, is a
collection of LANs and WANs held together by internetworking devices.
     Protocols and standards are vital to the implementation of data communications
and networking. Protocols refer to the rules; a standard is a protocol that has been
adopted by vendors and manufacturers.
     Network models serve to organize, unify, and control the hardware and software com-
ponents of data communications and networking. Although the term "network model"
suggests a relationship to networking, the model also encompasses data communications.

Chapters
This part consists of two chapters: Chapter 1 and Chapter 2.

## Chapter 1
In Chapter 1, we introduce the concepts of data communications and networking. We dis-
cuss data communications components, data representation, and data flow. We then move
to the structure of networks that carry data. We discuss network topologies, categories
of networks, and the general idea behind the Internet. The section on protocols and
standards gives a quick overview of the organizations that set standards in data communi-
cations and networking.

## Chapter 2
The two dominant networking models are the Open Systems Interconnection (OSI) and
the Internet model (TCP/IP).The first is a theoretical framework; the second is the
actual model used in today's data communications. In Chapter 2, we first discuss the
OSI model to give a general background. We then concentrate on the Internet model,
which is the foundation for the rest of the book.

                                                                                                 I   I
                                                                                                 ,   I


CHAPTERl

     Introduction


     Data communications and networking are changing the way we do business and the way
     we live. Business decisions have to be made ever more quickly, and the decision makers
     require immediate access to accurate information. Why wait a week for that report
     from Germany to arrive by mail when it could appear almost instantaneously through
     computer networks? Businesses today rely on computer networks and internetworks.
     But before we ask how quickly we can get hooked up, we need to know how networks
     operate, what types of technologies are available, and which design best fills which set
     of needs.
          The development of the personal computer brought about tremendous changes for
     business, industry, science, and education. A similar revolution is occurring in data
     communications and networking. Technological advances are making it possible for
     communications links to carry more and faster signals. As a result, services are evolving
     to allow use of this expanded capacity. For example, established telephone services
     such as conference calling, call waiting, voice mail, and caller ID have been extended.
          Research in data communications and networking has resulted in new technolo-
     gies. One goal is to be able to exchange data such as text, audio, and video from all
     points in the world. We want to access the Internet to download and upload information
     quickly and accurately and at any time.
          This chapter addresses four issues: data communications, networks, the Internet,
     and protocols and standards. First we give a broad definition of data communications.
     Then we define networks as a highway on which data can travel. The Internet is dis-
     cussed as a good example of an internetwork (i.e., a network of networks). Finally, we
     discuss different types of protocols, the difference between protocols and standards,
     and the organizations that set those standards.


## 1.1     DATA COMMUNICATIONS
     When we communicate, we are sharing information. This sharing can be local or
     remote. Between individuals, local communication usually occurs face to face, while
     remote communication takes place over distance. The term telecommunication, which


                                                                                             3

4   CHAPTER 1    INTRODUCTION


                includes telephony, telegraphy, and television, means communication at a distance (tele
                is Greek for "far").
                      The word data refers to information presented in whatever form is agreed upon by
                the parties creating and using the data.
                      Data communications are the exchange of data between two devices via some
                form of transmission medium such as a wire cable. For data communications to occur,
                the communicating devices must be part of a communication system made up of a com-
                bination of hardware (physical equipment) and software (programs). The effectiveness
                of a data communications system depends on four fundamental characteristics: deliv-
                ery, accuracy, timeliness, and jitter.
                   I. Delivery. The system must deliver data to the correct destination. Data must be
                      received by the intended device or user and only by that device or user.
                 7     Accuracy. The system must deliver the data accurately. Data that have been
                       altered in transmission and left uncorrected are unusable.
                 3. Timeliness. The system must deliver data in a timely manner. Data delivered late are
                    useless. In the case of video and audio, timely delivery means delivering data as
                    they are produced, in the same order that they are produced, and without signifi-
                    cant delay. This kind of delivery is called real-time transmission.
                 -\.. Jitter. Jitter refers to the variation in the packet arrival time. It is the uneven delay in
                       the delivery of audio or video packets. For example, let us assume that video packets
                       are sent every 3D ms. If some of the packets arrive with 3D-ms delay and others with
                       4D-ms delay, an uneven quality in the video is the result.

                COinponents
                A data communications system has five components (see Figure 1.1).

                Figure 1.1 Five components ofdata communication

                                Rule 1:                                                        Rule 1:


                                                                       r
                                Rule 2:                                                        Rule 2:
                                          Protocol                                  Protocol
                                Rule n:
                                                     -1      Message
                                                                                               Rulen:


                                                             Medium


                     I. Message. The message is the information (data) to be communicated. Popular
                       forms of information include text, numbers, pictures, audio, and video.
                 I     Sender. The sender is the device that sends the data message. It can be a com-
                       puter, workstation, telephone handset, video camera, and so on.
                 3. Receiver. The receiver is the device that receives the message. It can be a com-
                    puter, workstation, telephone handset, television, and so on.
                 -1.. Transmission medium. The transmission medium is the physical path by which
                      a message travels from sender to receiver. Some examples of transmission media
                      include twisted-pair wire, coaxial cable, fiber-optic cable, and radio waves.

## SECTION 1.1    DATA COMMUNICATIONS             5


 5. Protocol. A protocol is a set of rules that govern data communications. It repre-
    sents an agreement between the communicating devices. Without a protocol, two
    devices may be connected but not communicating, just as a person speaking French
    cannot be understood by a person who speaks only Japanese.

Data Representation
Information today comes in different forms such as text, numbers, images, audio, and
video.

Text
In data communications, text is represented as a bit pattern, a sequence of bits (Os or
Is). Different sets of bit patterns have been designed to represent text symbols. Each set
is called a code, and the process of representing symbols is called coding. Today, the
prevalent coding system is called Unicode, which uses 32 bits to represent a symbol or
character used in any language in the world. The American Standard Code for Infor-
mation Interchange (ASCII), developed some decades ago in the United States, now
constitutes the first 127 characters in Unicode and is also referred to as Basic Latin.
Appendix A includes part of the Unicode.

Numbers
Numbers are also represented by bit patterns. However, a code such as ASCII is not used
to represent numbers; the number is directly converted to a binary number to simplify
mathematical operations. Appendix B discusses several different numbering systems.

Images
Images are also represented by bit patterns. In its simplest form, an image is composed
of a matrix of pixels (picture elements), where each pixel is a small dot. The size of the
pixel depends on the resolution. For example, an image can be divided into 1000 pixels
or 10,000 pixels. In the second case, there is a better representation of the image (better
resolution), but more memory is needed to store the image.
     After an image is divided into pixels, each pixel is assigned a bit pattern. The size
and the value of the pattern depend on the image. For an image made of only black-
and-white dots (e.g., a chessboard), a I-bit pattern is enough to represent a pixel.
     If an image is not made of pure white and pure black pixels, you can increase the
size of the bit pattern to include gray scale. For example, to show four levels of gray
scale, you can use 2-bit patterns. A black pixel can be represented by 00, a dark gray
pixel by 01, a light gray pixel by 10, and a white pixel by 11.
     There are several methods to represent color images. One method is called RGB,
so called because each color is made of a combination of three primary colors: red,
green, and blue. The intensity of each color is measured, and a bit pattern is assigned to
it. Another method is called YCM, in which a color is made of a combination of three
other primary colors: yellow, cyan, and magenta.

Audio
Audio refers to the recording or broadcasting of sound or music. Audio is by nature
different from text, numbers, or images. It is continuous, not discrete. Even when we

6   CHAPTER 1    INTRODUCTION


                use a microphone to change voice or music to an electric signal, we create a continuous
                signal. In Chapters 4 and 5, we learn how to change sound or music to a digital or an
                analog signal.

                Video
                Video refers to the recording or broadcasting of a picture or movie. Video can either be
                produced as a continuous entity (e.g., by a TV camera), or it can be a combination of
                images, each a discrete entity, arranged to convey the idea of motion. Again we can
                change video to a digital or an analog signal, as we will see in Chapters 4 and 5.

                Data Flow
                Communication between two devices can be simplex, half-duplex, or full-duplex as
                shown in Figure 1.2.


                Figure 1.2 Data flow (simplex, half-duplex, andfull-duplex)


                                                        Direction of data


                              Mainframe                                                Monitor

                             a. Simplex


                                                   Direction of data at time I
                                                                            ~


                                                   Direction of data at time 2
                             b. Half-duplex


                                                  Direction of data all the time
                                                                                   )


                             c. Full·duplex


                Simplex
                In simplex mode, the communication is unidirectional, as on a one-way street. Only one
                of the two devices on a link can transmit; the other can only receive (see Figure 1.2a).
                     Keyboards and traditional monitors are examples of simplex devices. The key-
                board can only introduce input; the monitor can only accept output. The simplex mode
                can use the entire capacity of the channel to send data in one direction.

                Half-Duplex
                In half-duplex mode, each station can both transmit and receive, but not at the same time. :
                When one device is sending, the other can only receive, and vice versa (see Figure 1.2b).

## SECTION 1.2    NETWORKS         7


     The half-duplex mode is like a one-lane road with traffic allowed in both direc-
tions. When cars are traveling in one direction, cars going the other way must wait. In a
half-duplex transmission, the entire capacity of a channel is taken over by whichever of
the two devices is transmitting at the time. Walkie-talkies and CB (citizens band) radios
are both half-duplex systems.
     The half-duplex mode is used in cases where there is no need for communication
in both directions at the same time; the entire capacity of the channel can be utilized for
each direction.

Full-Duplex
In full-duplex m.,lle (als@ called duplex), both stations can transmit and receive simul-
taneously (see Figure 1.2c).
     The full-duplex mode is like a tW<D-way street with traffic flowing in both direc-
tions at the same time. In full-duplex mode, si~nals going in one direction share the
capacity of the link: with signals going in the other din~c~on. This sharing can occur in
two ways: Either the link must contain two physically separate t:nmsmissiIDn paths, one
for sending and the other for receiving; or the capacity of the ch:arillilel is divided
between signals traveling in both directions.
     One common example of full-duplex communication is the telephone network.
When two people are communicating by a telephone line, both can talk and listen at the
same time.
     The full-duplex mode is used when communication in both directions is required
all the time. The capacity of the channel, however, must be divided between the two
directions.


## 1.2     NETWORKS
A network is a set of devices (often referred to as nodes) connected by communication
links. A node can be a computer, printer, or any other device capable of sending and/or
receiving data generated by other nodes on the network.

Distributed Processing
Most networks use distributed processing, in which a task is divided among multiple
computers. Instead of one single large machine being responsible for all aspects of a
process, separate computers (usually a personal computer or workstation) handle a
subset.

Network Criteria
A network must be able to meet a certain number of criteria. The most important of
these are performance, reliability, and security.

Performance
Performance can be measured in many ways, including transit time and response time.
Transit time is the amount of time required for a message to travel from one device to

8   CHAPTER 1    INTRODUCTION


                another. Response time is the elapsed time between an inquiry and a response. The per-
                formance of a network depends on a number of factors, including the number of users,
                the type of transmission medium, the capabilities of the connected hardware, and the
                efficiency of the software.
                     Performance is often evaluated by two networking metrics: throughput and delay.
                We often need more throughput and less delay. However, these two criteria are often
                contradictory. If we try to send more data to the network, we may increase throughput
                but we increase the delay because of traffic congestion in the network.

                Reliability
                In addition to accuracy of delivery, network reliability is measured by the frequency of
                failure, the time it takes a link to recover from a failure, and the network's robustness in
                a catastrophe.

                Security
                Network security issues include protecting data from unauthorized access, protecting
                data from damage and development, and implementing policies and procedures for
                recovery from breaches and data losses.

                Physical Structures
                Before discussing networks, we need to define some network attributes.

                Type of Connection
                A network is two or more devices connected through links. A link is a communications
                pathway that transfers data from one device to another. For visualization purposes, it is
                simplest to imagine any link as a line drawn between two points. For communication to
                occur, two devices must be connected in some way to the same link at the same time.
                There are two possible types of connections: point-to-point and multipoint.
                Point-to-Point A point-to-point connection provides a dedicated link between two
                devices. The entire capacity of the link is reserved for transmission between those two
                devices. Most point-to-point connections use an actual length of wire or cable to con-
                nect the two ends, but other options, such as microwave or satellite links, are also possi-
                ble (see Figure 1.3a). When you change television channels by infrared remote control,
                you are establishing a point-to-point connection between the remote control and the
                television's control system.
                Multipoint A multipoint (also called multidrop) connection is one in which more
                than two specific devices share a single link (see Figure 1.3b).
                     In a multipoint environment, the capacity of the channel is shared, either spatially
                or temporally. If several devices can use the link simultaneously, it is a spatially shared
                connection. If users must take turns, it is a timeshared connection.

                Physical Topology
                The term physical topology refers to the way in which a network is laid out physically.:
                1\vo or more devices connect to a link; two or more links form a topology. The topology

## SECTION 1.2   NETWORKS      9


Figure 1.3 Types of connections: point-to-point and multipoint


                                            Link


             a. Point-to-point


                                 Link


               Mainframe


             b. Multipoint


of a network is the geometric representation of the relationship of all the links and
linking devices (usually called nodes) to one another. There are four basic topologies
possible: mesh, star, bus, and ring (see Figure 1.4).


Figure 1.4 Categories of topology


Mesh In a mesh topology, every device has a dedicated point-to-point link to every
other device. The term dedicated means that the link carries traffic only between the
two devices it connects. To find the number of physical links in a fully connected mesh
network with n nodes, we first consider that each node must be connected to every
other node. Node 1 must be connected to n - I nodes, node 2 must be connected to n - 1
nodes, and finally node n must be connected to n - 1 nodes. We need n(n - 1) physical
links. However, if each physical link allows communication in both directions (duplex
mode), we can divide the number of links by 2. In other words, we can say that in a
mesh topology, we need

                                        n(n -1) /2


duplex-mode links.
    To accommodate that many links, every device on the network must have n - 1
input/output (VO) ports (see Figure 1.5) to be connected to the other n - 1 stations.

10   CHAPTER 1   INTRODUCTION


             Figure 1.5 A fully connected mesh topology (five devices)


                  A mesh offers several advantages over other network topologies. First, the use of
             dedicated links guarantees that each connection can carry its own data load, thus elimi-
             nating the traffic problems that can occur when links must be shared by multiple devices.
             Second, a mesh topology is robust. If one link becomes unusable, it does not incapaci-
             tate the entire system. Third, there is the advantage of privacy or security. When every
             message travels along a dedicated line, only the intended recipient sees it. Physical
             boundaries prevent other users from gaining access to messages. Finally, point-to-point
             links make fault identification and fault isolation easy. Traffic can be routed to avoid
             links with suspected problems. This facility enables the network manager to discover the
             precise location of the fault and aids in finding its cause and solution.
                  The main disadvantages of a mesh are related to the amount of cabling and the
             number of I/O ports required. First, because every device must be connected to every
             other device, installation and reconnection are difficult. Second, the sheer bulk of the
             wiring can be greater than the available space (in walls, ceilings, or floors) can accom-
             modate. Finally, the hardware required to connect each link (I/O ports and cable) can be
             prohibitively expensive. For these reasons a mesh topology is usually implemented in a
             limited fashion, for example, as a backbone connecting the main computers of a hybrid
             network that can include several other topologies.
                  One practical example of a mesh topology is the connection of telephone regional
             offices in which each regional office needs to be connected to every other regional office.
             Star Topology In a star topology, each device has a dedicated point-to-point link
             only to a central controller, usually called a hub. The devices are not directly linked to
             one another. Unlike a mesh topology, a star topology does not allow direct traffic
             between devices. The controller acts as an exchange: If one device wants to send data to
             another, it sends the data to the controller, which then relays the data to the other con-
             nected device (see Figure 1.6) .
                  A star topology is less expensive than a mesh topology. In a star, each device needs
             only one link and one I/O port to connect it to any number of others. This factor also
             makes it easy to install and reconfigure. Far less cabling needs to be housed, and addi-
             tions, moves, and deletions involve only one connection: between that device and the hub.
                  Other advantages include robustness. If one link fails, only that link is affected. All
             other links remain active. This factor also lends itself to easy fault identification and

## SECTION 1.2     NETWORKS         11


Figure 1.6 A star topology connecting four stations

                                           Hub


fault isolation. As long as the hub is working, it can be used to monitor link problems
and bypass defective links.
     One big disadvantage of a star topology is the dependency of the whole topology
on one single point, the hub. If the hub goes down, the whole system is dead.
     Although a star requires far less cable than a mesh, each node must be linked to a
central hub. For this reason, often more cabling is required in a star than in some other
topologies (such as ring or bus).
     The star topology is used in local-area networks (LANs), as we will see in Chapter 13.
High-speed LANs often use a star topology with a central hub.
Bus Topology The preceding examples all describe point-to-point connections. A bus
topology, on the other hand, is multipoint. One long cable acts as a backbone to link all
the devices in a network (see Figure 1.7).


Figure 1.7 A bus topology connecting three stations


                              Drop line   Drop line   Drop line
        Cable end 11I-----1. .- - - - -. .- - - - -. .         ----11 Cable end
                           Tap          Tap         Tap


     Nodes are connected to the bus cable by drop lines and taps. A drop line is a con-
nection running between the device and the main cable. A tap is a connector that either
splices into the main cable or punctures the sheathing of a cable to create a contact with
the metallic core. As a signal travels along the backbone, some of its energy is transformed
into heat. Therefore, it becomes weaker and weaker as it travels farther and farther. For
this reason there is a limit on the number of taps a bus can support and on the distance
between those taps.
     Advantages of a bus topology include ease of installation. Backbone cable can be
laid along the most efficient path, then connected to the nodes by drop lines of various
lengths. In this way, a bus uses less cabling than mesh or star topologies. In a star, for
example, four network devices in the same room require four lengths of cable reaching

12   CHAPTER 1   INTRODUCTION


             all the way to the hub. In a bus, this redundancy is eliminated. Only the backbone cable
             stretches through the entire facility. Each drop line has to reach only as far as the near-
             est point on the backbone.
                   Disadvantages include difficult reconnection and fault isolation. A bus is usually
             designed to be optimally efficient at installation. It can therefore be difficult to add new
             devices. Signal reflection at the taps can cause degradation in quality. This degradation
             can be controlled by limiting the number and spacing of devices connected to a given
             length of cable. Adding new devices may therefore require modification or replacement
             of the backbone.
                   In addition, a fault or break in the bus cable stops all transmission, even between
             devices on the same side of the problem. The damaged area reflects signals back in the
             direction of origin, creating noise in both directions.
                   Bus topology was the one of the first topologies used in the design of early local-
             area networks. Ethernet LANs can use a bus topology, but they are less popular now for
             reasons we will discuss in Chapter 13.
             Ring Topology In a ring topology, each device has a dedicated point-to-point con-
             nection with only the two devices on either side of it. A signal is passed along the ring
             in one direction, from device to device, until it reaches its destination. Each device in
             the ring incorporates a repeater. When a device receives a signal intended for another
             device, its repeater regenerates the bits and passes them along (see Figure 1.8).


             Figure 1.8 A ring topology connecting six stations


                                           Repeater                Repeater
                               Repeater                                         Repeater
                                           Repeater                Repeater


                  A ring is relatively easy to install and reconfigure. Each device is linked to only its
             immediate neighbors (either physically or logically). To add or delete a device requires
             changing only two connections. The only constraints are media and traffic consider-
             ations (maximum ring length and number of devices). In addition, fault isolation is sim-
             plified. Generally in a ring, a signal is circulating at all times. If one device does not
             receive a signal within a specified period, it can issue an alarm. The alarm alerts the
             network operator to the problem and its location.
                  However, unidirectional traffic can be a disadvantage. In a simple ring, a break in
             the ring (such as a disabled station) can disable the entire network. This weakness can
             be solved by using a dual ring or a switch capable of closing off the break.

## SECTION 1.2      NETWORKS       13


    Ring topology was prevalent when IBM introduced its local-area network Token
Ring. Today, the need for higher-speed LANs has made this topology less popular.
Hybrid Topology A network can be hybrid. For example, we can have a main star topol-
ogy with each branch connecting several stations in a bus topology as shown in Figure 1.9.


Figure 1.9 A hybrid topology: a star backbone with three bus networks


            Hub


Network Models
Computer networks are created by different entities. Standards are needed so that these
heterogeneous networks can communicate with one another. The two best-known stan-
dards are the OSI model and the Internet model. In Chapter 2 we discuss these two
models. The OSI (Open Systems Interconnection) model defines a seven-layer net-
work; the Internet model defines a five-layer network. This book is based on the Internet
model with occasional references to the OSI model.

Categories of Networks
Today when we speak of networks, we are generally referring to two primary catego-
ries: local-area networks and wide-area networks. The category into which a network
falls is determined by its size. A LAN normally covers an area less than 2 mi; a WAN can
be worldwide. Networks of a size in between are normally referred to as metropolitan-
area networks and span tens of miles.

Local Area Network
A local area network (LAN) is usually privately owned and links the devices in a single
office, building, or campus (see Figure 1.10). Depending on the needs of an organization
and the type of technology used, a LAN can be as simple as two PCs and a printer in
someone's home office; or it can extend throughout a company and include audio and
video peripherals. Currently, LAN size is limited to a few kilometers.

14   CHAPTER 1    INTRODUCTION


             Figure 1.10 An isolated IAN connecting 12 computers to a hub in a closet


                                                                                  Hub


                  LANs are designed to allow resources to be shared between personal computers or
             workstations. The resources to be shared can include hardware (e.g., a printer), software
             (e.g., an application program), or data. A common example of a LAN, found in many
             business environments, links a workgroup of task-related computers, for example, engi-
             neering workstations or accounting PCs. One of the computers may be given a large-
             capacity disk drive and may become a server to clients. Software can be stored on this
             central server and used as needed by the whole group. In this example, the size of the
             LAN may be determined by licensing restrictions on the number of users per copy of soft-
             ware, or by restrictions on the number of users licensed to access the operating system.
                  In addition to size, LANs are distinguished from other types of networks by their
             transmission media and topology. In general, a given LAN will use only one type of
             transmission medium. The most common LAN topologies are bus, ring, and star.
                  Early LANs had data rates in the 4 to 16 megabits per second (Mbps) range. Today,
             however, speeds are normally 100 or 1000 Mbps. LANs are discussed at length in
             Chapters 13, 14, and 15.
                  Wireless LANs are the newest evolution in LAN technology. We discuss wireless
             LANs in detail in Chapter 14.

                 Wide Area Network
             A wide area network (WAN) provides long-distance transmission of data, image, audio,
             and video information over large geographic areas that may comprise a country, a conti-
             nent, or even the whole world. In Chapters 17 and 18 we discuss wide-area networks in
             greater detail. A WAN can be as complex as the backbones that connect the Internet or as
             simple as a dial-up line that connects a home computer to the Internet. We normally refer
             to the first as a switched WAN and to the second as a point-to-point WAN (Figure 1.11).
             The switched WAN connects the end systems, which usually comprise a router (internet-
             working connecting device) that connects to another LAN or WAN. The point-to-point
             WAN is normally a line leased from a telephone or cable TV provider that connects a
             home computer or a small LAN to an Internet service provider (lSP). This type of WAN
             is often used to provide Internet access.

## SECTION 1.2         NETWORKS    15


Figure 1.11 WANs: a switched WAN and a point-to-point WAN
                                                                                                i   i


                                                                                                I


          a. Switched WAN


                                          Point-te-point                   ~d:
                                                                             :_:
                                              WAN             .c '     . --     cu::J::W

           ~   ii~~;-E=~~~·                                  "",
                                                              ., ..,~!
                                                                     ;~,j -,    E::J
                              Modem                                Modem        -
             Computer                                                               ISP
          b. Point-to-point WAN


An early example of a switched WAN is X.25, a network designed to provide con-
nectivity between end users. As we will see in Chapter 18, X.25 is being gradually
replaced by a high-speed, more efficient network called Frame Relay. A good example
of a switched WAN is the asynchronous transfer mode (ATM) network, which is a net-
work with fixed-size data unit packets called cells. We will discuss ATM in Chapter 18.
Another example ofWANs is the wireless WAN that is becoming more and more popu-
lar. We discuss wireless WANs and their evolution in Chapter 16.

Metropolitan Area Networks
A metropolitan area network (MAN) is a network with a size between a LAN and a
WAN. It normally covers the area inside a town or a city. It is designed for customers
who need a high-speed connectivity, normally to the Internet, and have endpoints
spread over a city or part of city. A good example of a MAN is the part of the telephone
company network that can provide a high-speed DSL line to the customer. Another
example is the cable TV network that originally was designed for cable TV, but today
can also be used for high-speed data connection to the Internet. We discuss DSL lines
and cable TV networks in Chapter 9.

Interconnection of Networks: Internetwork
Today, it is very rare to see a LAN, a MAN, or a LAN in isolation; they are con-
nected to one another. When two or more networks are connected, they become an
internetwork, or internet.
     As an example, assume that an organization has two offices, one on the east coast
and the other on the west coast. The established office on the west coast has a bus topology
LAN; the newly opened office on the east coast has a star topology LAN. The president of
the company lives somewhere in the middle and needs to have control over the company

16   CHAPTER 1    INTRODUCTION


             from her horne. To create a backbone WAN for connecting these three entities (two
             LANs and the president's computer), a switched WAN (operated by a service provider
             such as a telecom company) has been leased. To connect the LANs to this switched
             WAN, however, three point-to-point WANs are required. These point-to-point WANs
             can be a high-speed DSL line offered by a telephone company or a cable modern line
             offered by a cable TV provider as shown in Figure 1.12.

             Figure 1.12 A heterogeneous network made offour WANs and two LANs

                                                         President
                                                              _....
                                                         1
                                                         ..


                                           Point-to-point:
                                                   WAN    :
                                                              ••
                                                                   , ' , Mod,m


                                                          •
                                          MOdem~~'


                                                                                 •
                                                                                 ~ Point-to-point
                                                                                  ~
                                                                                     . WAN

                             •':, Point-to-point
                              ':.   WAN
                               •


                                                                                 LAN

                                           LAN


## 1.3   THE INTERNET
             The Internet has revolutionized many aspects of our daily lives. It has affected the way
             we do business as well as the way we spend our leisure time. Count the ways you've
             used the Internet recently. Perhaps you've sent electronic mail (e-mail) to a business
             associate, paid a utility bill, read a newspaper from a distant city, or looked up a local
             movie schedule-all by using the Internet. Or maybe you researched a medical topic,
             booked a hotel reservation, chatted with a fellow Trekkie, or comparison-shopped for a
             car. The Internet is a communication system that has brought a wealth of information to
             our fingertips and organized it for our use.
                  The Internet is a structured, organized system. We begin with a brief history of the
             Internet. We follow with a description of the Internet today.

## SECTION 1.3    THE INTERNET        17


A Brief History
A network is a group of connected communicating devices such as computers and
printers. An internet (note the lowercase letter i) is two or more networks that can com-
municate with each other. The most notable internet is called the Internet (uppercase
letter I), a collaboration of more than hundreds of thousands of interconnected net-
works. Private individuals as well as various organizations such as government agen-
cies, schools, research facilities, corporations, and libraries in more than 100 countries
use the Internet. Millions of people are users. Yet this extraordinary communication sys-
tem only came into being in 1969.
     In the mid-1960s, mainframe computers in research organizations were stand-
alone devices. Computers from different manufacturers were unable to communicate
with one another. The Advanced Research Projects Agency (ARPA) in the Depart-
ment of Defense (DoD) was interested in finding a way to connect computers so that
the researchers they funded could share their findings, thereby reducing costs and elim-
inating duplication of effort.
     In 1967, at an Association for Computing Machinery (ACM) meeting, ARPA pre-
sented its ideas for ARPANET, a small network of connected computers. The idea was
that each host computer (not necessarily from the same manufacturer) would be
attached to a specialized computer, called an inteiface message processor (IMP). The
IMPs, in tum, would be connected to one another. Each IMP had to be able to commu-
nicate with other IMPs as well as with its own attached host.
     By 1969, ARPANET was a reality. Four nodes, at the University of California at
Los Angeles (UCLA), the University of California at Santa Barbara (UCSB), Stanford
Research Institute (SRI), and the University of Utah, were connected via the IMPs to
form a network. Software called the Network Control Protocol (NCP) provided com-
munication between the hosts.
     In 1972, Vint Cerf and Bob Kahn, both of whom were part of the core ARPANET
group, collaborated on what they called the Internetting Projec1. Cerf and Kahn's land-
mark 1973 paper outlined the protocols to achieve end-to-end delivery of packets. This
paper on Transmission Control Protocol (TCP) included concepts such as encapsula-
tion, the datagram, and the functions of a gateway.
     Shortly thereafter, authorities made a decision to split TCP into two protocols:
Transmission Control Protocol (TCP) and Internetworking Protocol (lP). IP would
handle datagram routing while TCP would be responsible for higher-level functions
such as segmentation, reassembly, and error detection. The internetworking protocol
became known as TCPIIP.


The Internet Today
The Internet has come a long way since the 1960s. The Internet today is not a simple
hierarchical structure. It is made up of many wide- and local-area networks joined by
connecting devices and switching stations. It is difficult to give an accurate represen-
tation of the Internet because it is continually changing-new networks are being
added, existing networks are adding addresses, and networks of defunct companies are
being removed. Today most end users who want Internet connection use the services of
Internet service providers (lSPs). There are international service providers, national

18   CHAPTER 1   INTRODUCTION


             service providers, regional service providers, and local service providers. The Internet
             today is run by private companies, not the government. Figure 1.13 shows a conceptual
             (not geographic) view of the Internet.


             Figure 1.13 Hierarchical organization of the Internet


                                                           National
                                                             ISP


                                                 a. Structure of a national ISP


                               National
                                 ISP


                                          National
                                           ISP

                                              b. Interconnection of national ISPs


             International Internet Service Providers
             At the top of the hierarchy are the international service providers that connect nations
             together.


             National Internet Service Providers
             The national Internet service providers are backbone networks created and main-
             tained by specialized companies. There are many national ISPs operating in North
             America; some of the most well known are SprintLink, PSINet, UUNet Technology,
             AGIS, and internet Mel. To provide connectivity between the end users, these back-
             bone networks are connected by complex switching stations (normally run by a third
             party) called network access points (NAPs). Some national ISP networks are also
             connected to one another by private switching stations called peering points. These
             normally operate at a high data rate (up to 600 Mbps).

## SECTION 1.4     PROTOCOLS AND STANDARDS               19


Regional Internet Service Providers
Regional internet service providers or regional ISPs are smaller ISPs that are connected
to one or more national ISPs. They are at the third level of the hierarchy with a smaller
data rate.

Local Internet Service Providers
Local Internet service providers provide direct service to the end users. The local
ISPs can be connected to regional ISPs or directly to national ISPs. Most end users are
connected to the local ISPs. Note that in this sense, a local ISP can be a company that
just provides Internet services, a corporation with a network that supplies services to its
own employees, or a nonprofit organization, such as a college or a university, that runs
its own network. Each of these local ISPs can be connected to a regional or national
service provider.


## 1.4     PROTOCOLS AND STANDARDS
In this section, we define two widely used terms: protocols and standards. First, we
define protocol, which is synonymous with rule. Then we discuss standards, which are
agreed-upon rules.

Protocols
In computer networks, communication occurs between entities in different systems. An
entity is anything capable of sending or receiving information. However, two entities can-
not simply send bit streams to each other and expect to be understood. For communication
to occur, the entities must agree on a protocol. A protocol is a set of rules that govern data
communications. A protocol defines what is communicated, how it is communicated, and
when it is communicated. The key elements of a protocol are syntax, semantics, and timing.
o Syntax. The term syntax refers to the structure or format of the data, meaning the
     order in which they are presented. For example, a simple protocol might expect the
     first 8 bits of data to be the address of the sender, the second 8 bits to be the address
     of the receiver, and the rest of the stream to be the message itself.
o Semantics. The word semantics refers to the meaning of each section of bits.
     How is a particular pattern to be interpreted, and what action is to be taken based
     on that interpretation? For example, does an address identify the route to be taken
     or the final destination of the message?
o Timing. The term timing refers to two characteristics: when data should be sent
     and how fast they can be sent. For example, if a sender produces data at 100 Mbps
     but the receiver can process data at only 1 Mbps, the transmission will overload the
     receiver and some data will be lost.

Standards
Standards are essential in creating and maintaining an open and competitive market for
equipment manufacturers and in guaranteeing national and international interoperability
of data and telecommunications technology and processes. Standards provide guidelines

20   CHAPTER 1       INTRODUCTION


             to manufacturers, vendors, government agencies, and other service providers to ensure
             the kind of interconnectivity necessary in today's marketplace and in international com-
             munications. Data communication standards fall into two categories: de facto (meaning
             "by fact" or "by convention") and de jure (meaning "by law" or "by regulation").
             o    De facto. Standards that have not been approved by an organized body but have
                  been adopted as standards through widespread use are de facto standards. De facto
                  standards are often established originally by manufacturers who seek to define the
                  functionality of a new product or technology.
             o De jure. Those standards that have been legislated by an officially recognized body
                  are de jure standards.


             Standards Organizations
             Standards are developed through the cooperation of standards creation committees,
             forums, and government regulatory agencies.

             Standards Creation Committees
             While many organizations are dedicated to the establishment of standards, data tele-
             communications in North America rely primarily on those published by the following:
             o  International Organization for Standardization (ISO). The ISO is a multinational
                body whose membership is drawn mainly from the standards creation committees
                of various governments throughout the world. The ISO is active in developing
                cooperation in the realms of scientific, technological, and economic activity.
             o International Telecommunication Union-Telecommunication Standards
                Sector (ITU-T). By the early 1970s, a number of countries were defining national
                standards for telecommunications, but there was still little international compati-
                bility. The United Nations responded by forming, as part of its International
                Telecommunication Union (ITU), a committee, the Consultative Committee
                for International Telegraphy and Telephony (CCITT). This committee was
                devoted to the research and establishment of standards for telecommunications in
                general and for phone and data systems in particular. On March 1, 1993, the name
                of this committee was changed to the International Telecommunication Union-
                Telecommunication Standards Sector (ITU-T).
                 o
                American National Standards Institute (ANSI). Despite its name, the American
                National Standards Institute is a completely private, nonprofit corporation not affili-
                 ated with the U.S. federal government. However, all ANSI activities are undertaken
                 with the welfare of the United States and its citizens occupying primary importance.
             o Institute of Electrical and Electronics Engineers (IEEE). The Institute of
                 Electrical and Electronics Engineers is the largest professional engineering society in
                 the world. International in scope, it aims to advance theory, creativity, and product
                 quality in the fields of electrical engineering, electronics, and radio as well as in all
                 related branches of engineering. As one of its goals, the IEEE oversees the develop-
                 ment and adoption of international standards for computing and communications.
                 o
                 Electronic Industries Association (EIA). Aligned with ANSI, the Electronic
                 Industries Association is a nonprofit organization devoted to the promotion of

## SECTION 1.5    RECOMMENDED READING               21


    electronics manufacturing concerns. Its activities include public awareness education
    and lobbying efforts in addition to standards development. In the field of information
    technology, the EIA has made significant contributions by defining physical connec-
    tion interfaces and electronic signaling specifications for data communication.

Forums
Telecommunications technology development is moving faster than the ability of stan-
dards committees to ratify standards. Standards committees are procedural bodies and
by nature slow-moving. To accommodate the need for working models and agreements
and to facilitate the standardization process, many special-interest groups have devel-
oped forums made up of representatives from interested corporations. The forums
work with universities and users to test, evaluate, and standardize new technologies. By
concentrating their efforts on a particular technology, the forums are able to speed
acceptance and use of those technologies in the telecommunications community. The
forums present their conclusions to the standards bodies.

Regulatory Agencies
All communications technology is subject to regulation by government agencies such
as the Federal Communications Commission (FCC) in the United States. The pur-
pose of these agencies is to protect the public interest by regulating radio, television,
and wire/cable communications. The FCC has authority over interstate and interna-
tional commerce as it relates to communications.

Internet Standards
An Internet standard is a thoroughly tested specification that is useful to and adhered
to by those who work with the Internet. It is a formalized regulation that must be fol-
lowed. There is a strict procedure by which a specification attains Internet standard
status. A specification begins as an Internet draft. An Internet draft is a working docu-
ment (a work in progress) with no official status and a 6-month lifetime. Upon recom-
mendation from the Internet authorities, a draft may be published as a Request for
Comment (RFC). Each RFC is edited, assigned a number, and made available to all
interested parties. RFCs go through maturity levels and are categorized according to
their requirement level.


## 1.5      RECOMMENDED READING
For more details about subjects discussed in this chapter, we recommend the following
books and sites. The items enclosed in brackets [...] refer to the reference list at the end
of the book.

Books
The introductory materials covered in this chapter can be found in [Sta04] and [PD03].
[Tan03] discusses standardization in Section 1.6.

22   CHAPTER 1   INTRODUCTION


             Sites
             The following sites are related to topics discussed in this chapter.
             o www.acm.org/sigcomm/sos.html            This site gives the status of varililus networking
                   standards.
             o     www.ietf.org/   The Internet Engineering Task Force (IETF) home page.


             RFCs
             The following site lists all RFCs, including those related to IP and TCP. In future chap-
             ters we cite the RFCs pertinent to the chapter material.
             o www.ietf.org/rfc.html


## 1.6      KEY TERMS
             Advanced Research Projects                       forum
               Agency (ARPA)                                  full-duplex mode, or duplex
             American National Standards                      half-duplex mode
                Institute (ANSI)                             hub
             American Standard Code for                      image
                Information Interchange (ASCII)
                                                             Institute of Electrical and Electronics
             ARPANET                                            Engineers (IEEE)
             audio                                           International Organization for
             backbone                                           Standardization (ISO)
             Basic Latin                                     International Telecommunication
             bus topology                                       Union-Telecommunication
             code                                               Standards Sector (ITU-T)
             Consultative Committee for                      Internet
                International Telegraphy                     Internet draft
                and Telephony (CCITT)                        Internet service provider (ISP)
             data                                            Internet standard
             data communications                             internetwork or internet
             de facto standards                              local area network (LAN)
             de jure standards                               local Internet service providers
             delay                                           mesh topology
             distributed processing                          message
             Electronic Industries Association (EIA)         metropolitan area network (MAN)
             entity                                          multipoint or multidrop connection
             Federal Communications Commission               national Internet service provider
                (FCC)                                        network

## SECTION 1.7    SUMMARY         23


network access points (NAPs)                  sender
node                                          simplex mode
performance                                   star topology
physical topology                             syntax
point-to-point connection                     telecommunication
protocol                                      throughput
receiver                                      timing
regional ISP                                  Transmission Control Protocol!
reliability                                      Internetworking Protocol (TCPIIP)
Request for Comment (RFC)                     transmission medium
ROB                                           Unicode
ring topology                                 video
security                                      wide area network (WAN)
semantics                                     YCM


## 1.7    SUMMARY
o Data communications are the transfer of data from one device to another via some
    form of transmission medium.
o   A data communications system must transmit data to the correct destination in an
    accurate and timely manner.
o   The five components that make up a data communications system are the message,
    sender, receiver, medium, and protocol.
o   Text, numbers, images, audio, and video are different forms of information.
o   Data flow between two devices can occur in one of three ways: simplex, half-duplex,
    or full-duplex.
o   A network is a set of communication devices connected by media links.
o   In a point-to-point connection, two and only two devices are connected by a
    dedicated link. In a multipoint connection, three or more devices share a link.
o   Topology refers to the physical or logical arrangement of a network. Devices may
    be arranged in a mesh, star, bus, or ring topology.
o   A network can be categorized as a local area network or a wide area network.
o   A LAN is a data communication system within a building, plant, or campus, or
    between nearby buildings.
o   A WAN is a data communication system spanning states, countries, or the whole
    world.
o   An internet is a network of networks.
o   The Internet is a collection of many separate networks.
o   There are local, regional, national, and international Internet service providers.
o   A protocol is a set of rules that govern data communication; the key elements of
    a protocol are syntax, semantics, and timing.

24   CHAPTER 1    INTRODUCTION


             o Standards are necessary to ensure that products from different manufacturers can
                    work together as expected.
             o      The ISO, ITD-T, ANSI, IEEE, and EIA are some of the organizations involved
                    in standards creation.
             o      Forums are special-interest groups that quickly evaluate and standardize new
                    technologies.
             o      A Request for Comment is an idea or concept that is a precursor to an Internet
                    standard.


## 1.8    PRACTICE SET
             Review Questions
                  1. Identify the five components of a data communications system.
                  2. What are the advantages of distributed processing?
                  3. What are the three criteria necessary for an effective and efficient network?
                  4. What are the advantages of a multipoint connection over a point-to-point
                      connection?
                  5. What are the two types of line configuration?
                  6. Categorize the four basic topologies in terms of line configuration.
                  7. What is the difference between half-duplex and full-duplex transmission modes?
                  8. Name the four basic network topologies, and cite an advantage of each type.
                  9. For n devices in a network, what is the number of cable links required for a mesh,
                      ring, bus, and star topology?
                 10. What are some of the factors that determine whether a communication system is a
                      LAN or WAN?
                 1 I. What is an internet? What is the Internet?
                 12. Why are protocols needed?
                 13. Why are standards needed?

             Exercises
                 14. What is the maximum number of characters or symbols that can be represented by
                     Unicode?
                 15. A color image uses 16 bits to represent a pixel. What is the maximum number of
                     different colors that can be represented?
                 16. Assume six devices are arranged in a mesh topology. How many cables are needed?
                     How many ports are needed for each device?
                 17. For each of the following four networks, discuss the consequences if a connection fails.
                     a. Five devices arranged in a mesh topology
                     b. Five devices arranged in a star topology (not counting the hub)
                     c. Five devices arranged in a bus topology
                     d. Five devices arranged in a ring topology

## SECTION 1.8    PRACTICE SET        25


18. You have two computers connected by an Ethernet hub at home. Is this a LAN, a
    MAN, or a WAN? Explain your reason.
19. In the ring topology in Figure 1.8, what happens if one of the stations is unplugged?
20. In the bus topology in Figure 1.7, what happens if one ofthe stations is unplugged?
21. Draw a hybrid topology with a star backbone and three ring networks.
22. Draw a hybrid topology with a ring backbone and two bus networks.
23. Performance is inversely related to delay. When you use the Internet, which of the
    following applications are more sensitive to delay?
    a. Sending an e-mail
    b. Copying a file
    c. Surfing the Internet
24. When a party makes a local telephone call to another party, is this a point-to-point
    or multipoint connection? Explain your answer.
25. Compare the telephone network and the Internet. What are the similarities? What
    are the differences?

Research Activities
26. Using the site \\iww.cne.gmu.edu/modules/network/osi.html, discuss the OSI model.
27. Using the site www.ansi.org, discuss ANSI's activities.
28. Using the site www.ieee.org, discuss IEEE's activities.
29. Using the site www.ietf.org/, discuss the different types of RFCs.


## CHAPTER 2

      Network Models


      A network is a combination of hardware and software that sends data from one location
      to another. The hardware consists of the physical equipment that carries signals from
      one point of the network to another. The software consists of instruction sets that make
      possible the services that we expect from a network.
           We can compare the task of networking to the task of solving a mathematics problem
      with a computer. The fundamental job of solving the problem with a computer is done
      by computer hardware. However, this is a very tedious task if only hardware is involved.
      We would need switches for every memory location to store and manipulate data. The
      task is much easier if software is available. At the highest level, a program can direct
      the problem-solving process; the details of how this is done by the actual hardware can
      be left to the layers of software that are called by the higher levels.
           Compare this to a service provided by a computer network. For example, the task
      of sending an e-mail from one point in the world to another can be broken into several
      tasks, each performed by a separate software package. Each software package uses the
      services of another software package. At the lowest layer, a signal, or a set of signals, is
      sent from the source computer to the destination computer.
           In this chapter, we give a general idea of the layers of a network and discuss the
      functions of each. Detailed descriptions of these layers follow in later chapters.


## 2.1     LAYERED TASKS
      We use the concept of layers in our daily life. As an example, let us consider two
      friends who communicate through postal maiL The process of sending a letter to a
      friend would be complex if there were no services available from the post office. Fig-
      ure 2.1 shows the steps in this task.


                                                                                                27

28   CHAPTER 2       NETWORK MODELS


             Figure 2.1        Tasks involved in sending a letter

                                          Sender                                                     Receiver


                                           t                                                            t
                                            I                                                           t
                                                                                              The letter is picked up,
                                  The letter is written,
                                 put in an envelope, and            Higher layers               removed from the
                                  dropped in a mailbox.

                                            I                                                           -,
                                                                                               envelope, and read.


                                                                                                The letter is carried
                                   The letter is carried
                                    from the mailbox                Middle layers               from the post office
                                     to a post office.                                             to the mailbox.

                                            I                                                            I
                                  The letter is delivered                                      The letter is delivered
                                  to a carrier by the post           Lower layers                 from the carrier
                                         office.                                                 to the post office.

                                            •                  The parcel is carried from
                                                                                                         II


                                                             the source to the destination.


                 Sender, Receiver, and Carrier
             In Figure 2.1 we have a sender, a receiver, and a carrier that transports the letter. There
             is a hierarchy of tasks.

             At the Sellder Site
                 Let us first describe, in order, the activities that take place at the sender site.
                 o   Higher layer. The sender writes the letter, inserts the letter in an envelope, writes
                      the sender and receiver addresses, and drops the letter in a mailbox.
                 o   Middle layer. The letter is picked up by a letter carrier and delivered to the post
                     office.
                 o   Lower layer. The letter is sorted at the post office; a carrier transports the letter.

                 011 the Way
                 The letter is then on its way to the recipient. On the way to the recipient's local post
                 office, the letter may actually go through a central office. In addition, it may be trans-
                 ported by truck, train, airplane, boat, or a combination of these.

                 At the Receiver Site
                 o Lower layer. The carrier transports the letter to the post office.
                 o Middle layer. The letter is sorted and delivered to the recipient's mailbox.
                 o Higher layer. The receiver picks up the letter, opens the envelope, and reads it.

## SECTION 2.2       THE OS! MODEL      29


Hierarchy
According to our analysis, there are three different activities at the sender site and
another three activities at the receiver site. The task of transporting the letter between
the sender and the receiver is done by the carrier. Something that is not obvious
immediately is that the tasks must be done in the order given in the hierarchy. At the
sender site, the letter must be written and dropped in the mailbox before being picked
up by the letter carrier and delivered to the post office. At the receiver site, the letter
must be dropped in the recipient mailbox before being picked up and read by the
recipient.

Services
Each layer at the sending site uses the services of the layer immediately below it. The
sender at the higher layer uses the services of the middle layer. The middle layer uses
the services of the lower layer. The lower layer uses the services of the carrier.
     The layered model that dominated data communications and networking literature
before 1990 was the Open Systems Interconnection (OSI) model. Everyone believed
that the OSI model would become the ultimate standard for data communications, but
this did not happen. The TCPIIP protocol suite became the dominant commercial archi-
tecture because it was used and tested extensively in the Internet; the OSI model was
never fully implemented.
     In this chapter, first we briefly discuss the OSI model, and then we concentrate on
TCPIIP as a protocol suite.


## 2.2        THE OSI MODEL
Established in 1947, the International Standards Organization (ISO) is a multinational
body dedicated to worldwide agreement on international standards. An ISO standard
that covers all aspects of network communications is the Open Systems Interconnection
model. It was first introduced in the late 1970s. An open system is a set of protocols that
allows any two different systems to communicate regardless of their underlying archi-
tecture. The purpose of the OSI model is to show how to facilitate communication
between different systems without requiring changes to the logic of the underlying hard-
ware and software. The OSI model is not a protocol; it is a model for understanding and
designing a network architecture that is flexible, robust, and interoperable.


                        ISO is the organization. OSI is the model.


     The OSI model is a layered framework for the design of network systems that
allows communication between all types of computer systems. It consists of seven sep-
arate but related layers, each of which defines a part of the process of moving information
across a network (see Figure 2.2). An understanding of the fundamentals of the OSI
model provides a solid basis for exploring data communications.

30   CHAPTER 2 NETWORK MODELS


             Figure 2.2   Seven layers of the OSI model


                                      71              Application


                                      61              Presentation


                                      51                   Session


                                      41                  Transport


                                                          Network
                                      31

                                                          Data link
                                      21

                                      1   I                Physical


             Layered Architecture
             The OSI model is composed of seven ordered layers: physical (layer 1), data link (layer 2),
             network (layer 3), transport (layer 4), session (layer 5), presentation (layer 6), and
             application (layer 7). Figure 2.3 shows the layers involved when a message is sent from
             device A to device B. As the message travels from A to B, it may pass through many
             intermediate nodes. These intermediate nodes usually involve only the first three layers
             of the OSI model.
                  In developing the model, the designers distilled the process of transmitting data to
             its most fundamental elements. They identified which networking functions had related
             uses and collected those functions into discrete groups that became the layers. Each
             layer defines a family of functions distinct from those of the other layers. By defining
             and localizing functionality in this fashion, the designers created an architecture that is
             both comprehensive and flexible. Most importantly, the OSI model allows complete
             interoperability between otherwise incompatible systems.
                  Within a single machine, each layer calls upon the services of the layer just below
             it. Layer 3, for example, uses the services provided by layer 2 and provides services for
             layer 4. Between machines, layer x on one machine communicates with layer x on
             another machine. This communication is governed by an agreed-upon series of rules
             and conventions called protocols. The processes on each machine that communicate at
             a given layer are called peer-to-peer processes. Communication between machines is
             therefore a peer-to-peer process using the protocols appropriate to a given layer.


             Peer-to-Peer Processes
             At the physical layer, communication is direct: In Figure 2.3, device A sends a stream
             of bits to device B (through intermediate nodes). At the higher layers, however, com-
             munication must move down through the layers on device A, over to device B, and then

## SECTION 2.2   THE OSI MODEL          31


Figure 2.3      The interaction between layers in the OSI model

              Device                                                            Device
                A                                                                 B

                                  Intermediate            Intermediate
                                      node                    node


                                    Peer-to-peer protocol Oth layer)
    7     Application        ------------------------                        Application     7
         7-6 interface                                                       7-6 interface
                                    Peer-to-peer protocol (6th layer)
    6     Presentation       ------------------------                        Presentation    6
         6-5 interface                                                       6-5 interface
                                    Peer-to-peer protocol (5th layer)
    5         Session        ------------------------                          Session       5
         5-4 interface                                                       5-4 interface
                                    Peer-to-peer protocol (4th layer)
    4        Transport       ------------------------                         Transport      4
         4-3 interface                                                       4-3 interface
    3        Network                                                           Network       3
         3-2 interface                                                       3-2 interface
    2        Data link                                                        Data link      2
         2-1 interface                                                       2-1 interface
             Physical                                                          Physical

                                        Physical communication


back up through the layers. Each layer in the sending device adds its own information
to the message it receives from the layer just above it and passes the whole package to
the layer just below it.
     At layer I the entire package is converted to a form that can be transmitted to the
receiving device. At the receiving machine, the message is unwrapped layer by layer,
with each process receiving and removing the data meant for it. For example, layer 2
removes the data meant for it, then passes the rest to layer 3. Layer 3 then removes the
data meant for it and passes the rest to layer 4, and so on.

Interfaces Between Layers
The passing of the data and network information down through the layers of the send-
ing device and back up through the layers of the receiving device is made possible by
an interface between each pair of adjacent layers. Each interface defines the informa-
tion and services a layer must provide for the layer above it. Well-defined interfaces and
layer functions provide modularity to a network. As long as a layer provides the
expected services to the layer above it, the specific implementation of its functions can
be modified or replaced without requiring changes to the surrounding layers.

Organization of the Layers
The seven layers can be thought of as belonging to three subgroups. Layers I, 2, and
3-physical, data link, and network-are the network support layers; they deal with

32   CHAPTER 2   NETWORK MODELS


             the physical aspects of moving data from one device to another (such as electrical
             specifications, physical connections, physical addressing, and transport timing and
             reliability). Layers 5, 6, and 7-session, presentation, and application-can be
             thought of as the user support layers; they allow interoperability among unrelated
             software systems. Layer 4, the transport layer, links the two subgroups and ensures
             that what the lower layers have transmitted is in a form that the upper layers can use.
             The upper OSI layers are almost always implemented in software; lower layers are a
             combination of hardware and software, except for the physical layer, which is mostly
             hardware.
                  In Figure 2.4, which gives an overall view of the OSI layers, D7 means the data
             unit at layer 7, D6 means the data unit at layer 6, and so on. The process starts at layer
             7 (the application layer), then moves from layer to layer in descending, sequential
             order. At each layer, a header, or possibly a trailer, can be added to the data unit.
             Commonly, the trailer is added only at layer 2. When the formatted data unit passes
             through the physical layer (layer 1), it is changed into an electromagnetic signal and
             transported along a physical link.


             Figure 2.4 An exchange using the OS! model


                                    ~                                                               :HiiD7l
                                                                                                    t---~


                                   ~ D6 I                                                      ~~§J    D6   I
                                                                                                1
                            ~            D5    I                                           :Hs-
                                                                                           r- _J      D5    I
                           ~           D4      I                                       :H4j       D4- - -I
                                                                                       r--- . - - -
                                                                                        l
                     ~              D3         I                                   r-- J - - - = -D3= - - - -I
                                                                                   :-Hi

                    ~             D2           •                          :HiJ
                                                                          1- - -
                                                                                              D2            ~.j!
                                                                                                            .10--1
                 @IQj 010101010101101010000010000 I                 :_~i§j 010101010101101010000010000 I


                                  L...                Trn",m;"io" =dium                       1
                  Upon reaching its destination, the signal passes into layer 1 and is transformed
             back into digital form. The data units then move back up through the OSI layers. As
             each block of data reaches the next higher layer, the headers and trailers attached to it at
             the corresponding sending layer are removed, and actions appropriate to that layer are
             taken. By the time it reaches layer 7, the message is again in a form appropriate to the
             application and is made available to the recipient.

## SECTION 2.3         LAYERS IN THE OSI MODEL             33


Encapsulation
Figure 2.3 reveals another aspect of data communications in the OSI model: encapsula-
tion. A packet (header and data) at level 7 is encapsulated in a packet at level 6. The
whole packet at level 6 is encapsulated in a packet at level 5, and so on.
     In other words, the data portion of a packet at level N - 1 carries the whole packet
(data and header and maybe trailer) from level N. The concept is called encapsulation;
level N - 1 is not aware of which part of the encapsulated packet is data and which part
is the header or trailer. For level N - 1, the whole packet coming from level N is treated
as one integral unit.


## 2.3      LAYERS IN THE OSI MODEL
In this section we briefly describe the functions of each layer in the OSI model.

Physical Layer
The physical layer coordinates the functions required to carry a bit stream over a physi-
cal medium. It deals with the mechanical and electrical specifications of the interface and
transmission medium. It also defines the procedures and functions that physical devices
and interfaces have to perform for transmission to Occur. Figure 2.5 shows the position of
the physical layer with respect to the transmission medium and the data link layer.


Figure 2.5 Physical layer

                    From data link layer                             To data link layer


    Physical                                                                              Physical
       layer                                                                              layer


                                           Transmission medium


                   The physical layer is responsible for movements of
                    individual bits from one hop (node) to the next.

      The physical layer is also concerned with the following:
o     Physical characteristics of interfaces and medium. The physical layer defines
      the characteristics of the interface between the devices and the transmission
      medium. It also defines the type of transmission medium.
o     Representation of bits. The physical layer data consists of a stream of bits
      (sequence of Os or 1s) with no interpretation. To be transmitted, bits must be

34   CHAPTER 2       NETWORK MODELS


                      encoded into signals--electrical or optical. The physical layer defines the type of
                      encoding (how Os and Is are changed to signals).
             o        Data rate. The transmission rate-the number of bits sent each second-is also
                      defined by the physical layer. In other words, the physical layer defines the dura-
                      tion of a bit, which is how long it lasts.
             o        Synchronization of bits. The sender and receiver not only must use the same bit
                      rate but also must be synchronized at the bit level. In other words, the sender and
                      the receiver clocks must be synchronized.
             o        Line configuration. The physical layer is concerned with the connection of
                      devices to the media. In a point-to-point configuration, two devices are connected
                      through a dedicated link. In a multipoint configuration, a link is shared among
                      several devices.
             o        Physical topology. The physical topology defines how devices are connected to
                      make a network. Devices can be connected by using a mesh topology (every device
                      is connected to every other device), a star topology (devices are connected through
                      a central device), a ring topology (each device is connected to the next, forming a
                      ring), a bus topology (every device is on a common link), or a hybrid topology (this
                      is a combination of two or more topologies).
                 o    Transmission mode. The physical layer also defines the direction of transmission
                      between two devices: simplex, half-duplex, or full-duplex. In simplex mode, only
                      one device can send; the other can only receive. The simplex mode is a one-way
                      communication. In the half-duplex mode, two devices can send and receive, but
                      not at the same time. In a full-duplex (or simply duplex) mode, two devices can
                      send and receive at the same time.


                 Data Link Layer
                 The data link layer transforms the physical layer, a raw transmission facility, to a reli-
                 able link. It makes the physical layer appear error-free to the upper layer (network
                 layer). Figure 2.6 shows the relationship of the data link layer to the network and phys-
                 icallayers.


                 Figure 2.6 Data link layer

                                         From network layer                 To network layer


                                                                      H2


                       Data link layer                                                           Data link layer

                                         To physical layer                 From physical layer

## SECTION 2.3             LAYERS IN THE OSI MODEL     35


    The data link layer is responsible for moving frames from one hop (node) to the next.

    Other responsibilities of the data link layer include the following:
[I Framing. The data link layer divides the stream of bits received from the network
    layer into manageable data units called frames.
o   Physical addressing. If frames are to be distributed to different systems on the
    network, the data link layer adds a header to the frame to define the sender and/or
    receiver of the frame. If the frame is intended for a system outside the sender's
    network, the receiver address is the address of the device that connects the network
    to the next one.
D Flow control. If the rate at which the data are absorbed by the receiver is less than
    the rate at which data are produced in the sender, the data link layer imposes a flow
    control mechanism to avoid overwhelming the receiver.
o Error control. The data link layer adds reliability to the physical layer by adding
    mechanisms to detect and retransmit damaged or lost frames. It also uses a mecha-
    nism to recognize duplicate frames. Error control is normally achieved through a
    trailer added to the end of the frame.
D Access control. When two or more devices are connected to the same link, data
    link layer protocols are necessary to determine which device has control over the
    link at any given time.
Figure 2.7 illustrates hop-to-hop (node-to-node) delivery by the data link layer.


Figure 2.7 Hop-fa-hop delivery

                                                                                                  End
                                                                                             system

                  End
                 system
                  r
                               Link                                                           End
                                                                                             system
                   A                                                                          r
                                                                                   Link
                                                                        E                          F
                        Hop-ta-hop delivery       Hop-to-hop delivery       Hop-to-hop delivery


                   A                          B                         E                          F
                             Data link                 Data link                Data link

                              Physical                 Physical                 Physical

                    Hop-to-hop delivery           Hop-to-hop delivery        Hop-to-hop delivery


     As the figure shows, communication at the data link layer occurs between two
adjacent nodes. To send data from A to F, three partial deliveries are made. First, the
data link layer at A sends a frame to the data link layer at B (a router). Second, the data

36   CHAPTER 2       NETWORK MODELS


             link layer at B sends a new frame to the data link layer at E. Finally, the data link layer
             at E sends a new frame to the data link layer at F. Note that the frames that are
             exchanged between the three nodes have different values in the headers. The frame from
             A to B has B as the destination address and A as the source address. The frame from B to
             E has E as the destination address and B as the source address. The frame from E to F
             has F as the destination address and E as the source address. The values of the trailers
             can also be different if error checking includes the header of the frame.

             Network Layer
             The network layer is responsible for the source-to-destination delivery of a packet,
             possibly across multiple networks (links). Whereas the data link layer oversees the
             delivery of the packet between two systems on the same network (links), the network
             layer ensures that each packet gets from its point of origin to its final destination.
                  If two systems are connected to the same link, there is usually no need for a net-
             work layer. However, if the two systems are attached to different networks (links) with
             connecting devices between the networks (links), there is often a need for the network
             layer to accomplish source-to-destination delivery. Figure 2.8 shows the relationship of
             the network layer to the data link and transport layers.


             Figure 2.8 Network layer

                                      From transport layer
                                                  I                                                    ...I
                                                                                                To transport layer


                        ~:
                                1

                                                 Data
                                                         -,,-_1

                                                             .1 Packet
                                                                                          .
                                                                         ',,- - -H-3- - _]1..
                                                                                          .
                                                                                               jI
                                                                                            D a t a , . Packet
                        I                                     I
                                                                         i------ '-----'-------1
                      Network                                                                                        Network
                                          ...,
                      layer                                                                                             layer
                                    To data link layer                                     From data link layer


                                    The network layer is responsible for the delivery of individual
                                        packets from the source host to the destination host.

                      Other responsibilities of the network layer include the following:
                 o    Logical addressing. The physical addressing implemented by the data link layer
                      handles the addressing problem locally. If a packet passes the network boundary,
                      we need another addressing system to help distinguish the source and destination
                      systems. The network layer adds a header to the packet coming from the upper
                      layer that, among other things, includes the logical addresses of the sender and
                      receiver. We discuss logical addresses later in this chapter.
                 o    Routing. When independent networks or links are connected to create intemetworks
                      (network of networks) or a large network, the connecting devices (called routers

## SECTION 2.3             LAYERS IN THE OSI MODEL       37


    or switches) route or switch the packets to their final destination. One of the func-
    tions of the network layer is to provide this mechanism.
    Figure 2.9 illustrates end-to-end delivery by the network layer.


Figure 2.9 Source-to-destination delivery

                                                                                                End
                                                                                               system
                                                                                                r
                 End
                system
                 r
                                                                                                End
                                                                    Intermediate               system
                     A                                                                              r
                                                                       system
                                                                                     Link
                                                                          E                             F
                          HOP-lO-hop delivery       Hop-to-hop delivery       HOp-lO-hop delivery

                                            Source-to-destination delivery


                     A
                                Network

                               Data link
                                            -   B
                                                         Network

                                                        Data link
                                                                       -  E
                                                                                   Network

                                                                                   Data link
                                                                                                        F


                                Physical                 Physical                  Physical


                     I.                     Source-to-destination delivery
                                                                                                    ,I

As the figure shows, now we need a source-to-destination delivery. The network layer
at A sends the packet to the network layer at B. When the packet arrives at router B, the
router makes a decision based on the final destination (F) of the packet. As we will see
in later chapters, router B uses its routing table to find that the next hop is router E. The
network layer at B, therefore, sends the packet to the network layer at E. The network
layer at E, in tum, sends the packet to the network layer at F.

Transport Layer
The transport layer is responsible for process-to-process delivery of the entire mes-
sage. A process is an application program running on a host. Whereas the network layer
oversees source-to-destination delivery of individual packets, it does not recognize
any relationship between those packets. It treats each one independently, as though
each piece belonged to a separate message, whether or not it does. The transport layer,
on the other hand, ensures that the whole message arrives intact and in order, overseeing
both error control and flow control at the source-to-destination level. Figure 2.10 shows
the relationship of the transport layer to the network and session layers.

38   CHAPTER 2       NETWORK MODELS


             Figure 2.10          Transport layer

                                        From session layer                                  To session layer

                                                                                                               \
                                                                                                                \
                                                                                                                    \
                                                                                                                     \
                              /    /     I       I    \        \                /
                                                                            /


                       IH4 (Data rIH4 f Data r IH4) Data 1              CH!lData I
                       I          I I           I I                I    I           I
                                                             Segments                                          Segments
                      Transport                                                                                 Transport
                      layer       To network layer                                  From network layer              layer


                 The transport layer is responsible for the delivery of a message from one process to another.


                      Other responsibilities of the transport layer include the following:
                 o    Service-point addressing. Computers often run several programs at the same
                      time. For this reason, source-to-destination delivery means delivery not only from
                      one computer to the next but also from a specific process (running program) on
                      one computer to a specific process (running program) on the other. The transport
                      layer header must therefore include a type of address called a service-point
                      address (or port address). The network layer gets each packet to the correct
                      computer; the transport layer gets the entire message to the correct process on
                      that computer.
                 o    Segmentation and reassembly. A message is divided into transmittable segments,
                      with each segment containing a sequence number. These numbers enable the trans-
                      port layer to reassemble the message correctly upon arriving at the destination and
                      to identify and replace packets that were lost in transmission.
                 o    Connection control. The transport layer can be either connectionless or connection-
                      oriented. A connectionless transport layer treats each segment as an independent
                      packet and delivers it to the transport layer at the destination machine. A connection-
                      oriented transport layer makes a connection with the transport layer at the destina-
                      tion machine first before delivering the packets. After all the data are transferred,
                      the connection is terminated.
                 o    Flow control. Like the data link layer, the transport layer is responsible for flow
                      control. However, flow control at this layer is performed end to end rather than
                      across a single link.
                 o    Error control. Like the data link layer, the transport layer is responsible for
                      error control. However, error control at this layer is performed process-to-
                      process rather than across a single link. The sending transport layer makes sure
                      that the entire message arrives at the receiving transport layer without error
                      (damage, loss, or duplication). Error correction is usually achieved through
                      retransmission.

## SECTION 2.3           LAYERS IN THE OSI MODEL                                                     39


Figure 2.11 illustrates process-to-process delivery by the transport layer.


Figure 2.11                            Reliable process-to-process delivery of a message

                                   Processes                                                       Processes


                                   I                                                                       \
                               I                                                                               \
                           ,
                           I                                                                                       \


                         ,,
                                                                                                                       \
                                                                                                                           \
                                                                                                                               \


                    ,
                        ,/ ~~~~,....-----<
                                       I
                                                                    An internet           )-----~~~~'C)\\
                                                                                                       I                           \
                                                                                                                                       \
                /                      I                                                               I                                   \
            ,                          I-.I.----------------------.J.I                                                                         \
        /                              I                          Network layer                        I                                           \
                                                                                                                                                       \
    ,                                                          Host-to-host delivery                                                                       \

    L                                                                                                                                                          ~
                                                                  Transport layer
                                                            Process-to-process delivery


Session Layer
The services provided by the first three layers (physical, data link, and network) are
not sufficient for some processes. The session layer is the network dialog controller.
It establishes, maintains, and synchronizes the interaction among communicating
systems.

                         The session layer is responsible for dialog control and synchronization.


            Specific responsibilities of the session layer include the following:
o           Dialog control. The session layer allows two systems to enter into a dialog. It
            allows the communication between two processes to take place in either half-
            duplex (one way at a time) or full-duplex (two ways at a time) mode.
o           Synchronization. The session layer allows a process to add checkpoints, or syn-
            Chronization points, to a stream of data. For example, if a system is sending a file
            of 2000 pages, it is advisable to insert checkpoints after every 100 pages to ensure
            that each 100-page unit is received and acknowledged independently. In this case,
            if a crash happens during the transmission of page 523, the only pages that need to
            be resent after system recovery are pages 501 to 523. Pages previous to 501 need
            not be resent. Figure 2.12 illustrates the relationship of the session layer to the
            transport and presentation layers.

Presentation Layer
The presentation layer is concerned with the syntax and semantics of the information
exchanged between two systems. Figure 2.13 shows the relationship between the pre-
sentation layer and the application and session layers.

40   CHAPTER 2       NETWORK MODELS


             Figure 2.12 Session layer

                                                         From presentation layer                                                To presentation layer


                                                 I
                                                                          1                                                  ~i1-,
                                                                                                                                 ,
                                                                                                                         I             I
                                             /                    ;f            t                                    I               II         I
                                         /                      I~             II          I                     I
                                                                                                                                  1/          I I                       I


                         ~ .•. l
                                                                                                             I
                                                                                          I              I                       I I         I I                       I
                                                                                                                                                                      I


                         1


                     Session
                               syn                        syn                 syn
                                                                                          I       I


                                                                                               Session
                                                                                                                               •
                                                                                                                               syn          syn
                                                                                                                                                ~')~:{~~ ,
                                                                                                                                                  r' ~"'''   9   ~,
                                                                                                                                                                      II
                                                                                                                                                                      syn
                                                                                                                                                                      I


                     layer                                                                     layer
                                                     To transport layer                                                  From transport layer


             Figure 2.13 Presentation layer

                                                          From application layer


                                                       ;.......,.
                                                       1
                                                                          I

                                                                                    --1
                                                                                                                                       .
                                                                                                                             To application layer


                                                                                                                                       I
                                     ~l
                                     I
                                                               . . , "J)8,tfi~~. ,.J
                                                                    i

                                                                                      I


                        Presentation                                                                                                                Presentation
                                                                    ...
                        layer                                                                                                                              layer
                                                         To session layer                                            From session layer


                      The presentation layer is responsible for translation, compression, and encryption.


                       Specific responsibilities of the presentation layer include the following:
                 o     Translation. The processes (running programs) in two systems are usually exchang-
                       ing information in the form of character strings, numbers, and so on. The infonna-
                       tion must be changed to bit streams before being transmitted. Because different
                       computers use different encoding systems, the presentation layer is responsible for
                       interoperability between these different encoding methods. The presentation layer
                       at the sender changes the information from its sender-dependent format into a
                       common format. The presentation layer at the receiving machine changes the
                       common format into its receiver-dependent format.
                 o     Encryption. To carry sensitive information, a system must be able to ensure
                       privacy. Encryption means that the sender transforms the original information to

## SECTION 2.3     LAYERS IN THE OSI MODEL               41


    another form and sends the resulting message out over the network. Decryption
    reverses the original process to transform the message back to its original form.
o   Compression. Data compression reduces the number of bits contained in the
    information. Data compression becomes particularly important in the transmission
    of multimedia such as text, audio, and video.

Application Layer
The application layer enables the user, whether human or software, to access the net-
work. It provides user interfaces and support for services such as electronic mail,
remote file access and transfer, shared database management, and other types of distrib-
uted information services.
    Figure 2.14 shows the relationship of the application layer to the user and the pre-
sentation layer. Of the many application services available, the figure shows only three:
XAOO (message-handling services), X.500 (directory services), and file transfer,
access, and management (FTAM). The user in this example employs XAOO to send an
e-mail message.


Figure 2.14 Application layer

                          User                                   User
                   (human or program)                     (human or program)


                                                                  Data' ~:.


     Application                                                                 Application
     layer                                                                             layer

              To presentation layer                    From presentation layer


           The application layer is responsible for providing services to the user.


    Specific services provided by the application layer include the following:
o   Network virtual terminal. A network virtual terminal is a software version of
    a physical terminal, and it allows a user to log on to a remote host. To do so, the
    application creates a software emulation of a terminal at the remote host. The
    user's computer talks to the software terminal which, in turn, talks to the host,
    and vice versa. The remote host believes it is communicating with one of its own
    terminals and allows the user to log on.

42   CHAPTER 2     NETWORK MODELS


             o File transfer, access, and management. This application allows a user to access
                     files in a remote host (to make changes or read data), to retrieve files from a remote
                     computer for use in the local computer, and to manage or control files in a remote
                     computer locally.
             o       Mail services. This application provides the basis for e-mail forwarding and
                     storage.
             o       Directory services. This application provides distributed database sources and
                     access for global information about various objects and services.

             Summary of Layers
             Figure 2.15 shows a summary of duties for each layer.


             Figure 2.15 Summary of layers

                                                                            To allow access to network
                                                          Application
                                                                            resources
                        To translate, encrypt, and
                                                          Presentation
                        compress data
                                                                            To establish, manage, and
                                                            Session
                                                                            terminate sessions
                        To provide reliable process-to-
                        process message delivery and       Transport
                        error recovery                                      To move packets from source
                                                           Network          to destination; to provide
                                                                            internetworking
                        To organize bits into frames;
                                                           Data link
                        to provide hop-to-hop delivery
                                                                            To transmit bits over a medium;
                                                            Physical        to provide mechanical and
                                                                            electrical specifications


## 2.4     TCP/IP PROTOCOL SUITE
                 The TCPIIP protocol suite was developed prior to the OSI model. Therefore, the lay-
                 ers in the TCP/IP protocol suite do not exactly match those in the OSI model. The
                 original TCP/IP protocol suite was defined as having four layers: host-to-network,
                 internet, transport, and application. However, when TCP/IP is compared to OSI, we can
                 say that the host-to-network layer is equivalent to the combination of the physical and
                 data link layers. The internet layer is equivalent to the network layer, and the applica-
                 tion layer is roughly doing the job of the session, presentation, and application layers
                 with the transport layer in TCPIIP taking care of part of the duties of the session layer.
                 So in this book, we assume that the TCPIIP protocol suite is made of five layers: physi-
                 cal, data link, network, transport, and application. The first four layers provide physical
                 standards, network interfaces, internetworking, and transport functions that correspond
                 to the first four layers of the OSI model. The three topmost layers in the OSI model,
                 however, are represented in TCPIIP by a single layer called the application layer (see
                 Figure 2.16).

## SECTION 2.4          TCPIIP PROTOCOL SUITE        43


Figure 2.16 TCPIIP and OSI model

  IApplication                                       Applications
                                                                                               J
  I Presentation


  ISession         8GB8GB                                                             ... ]
                                                                                          1
  I Transport        SC_TP_ _!
                   ___                        IL-.-__    TC_P_ _        II       UD_P_ _    II
                   I   ICMP   II   IGMP   I
   Network
   (internet)                                            IP
                                                                             I RARP II ARP I
  I Data link                                   Protocols defined by
                                              the underlying networks
                                                                                               J
  I Physical
                                                  (host-to-network)
                                                                                               1
    TCP/IP is a hierarchical protocol made up of interactive modules, each of which
provides a specific functionality; however, the modules are not necessarily interdepen-
dent. Whereas the OSI model specifies which functions belong to each of its layers,
the layers of the TCP/IP protocol suite contain relatively independent protocols that
can be mixed and matched depending on the needs of the system. The term hierarchi-
cal means that each upper-level protocol is supported by one or more lower-level
protocols.
     At the transport layer, TCP/IP defines three protocols: Transmission Control
Protocol (TCP), User Datagram Protocol (UDP), and Stream Control Transmission
Protocol (SCTP). At the network layer, the main protocol defined by TCP/IP is the
Internetworking Protocol (IP); there are also some other protocols that support data
movement in this layer.

Physical and Data Link Layers
At the physical and data link layers, TCPIIP does not define any specific protocol. It
supports all the standard and proprietary protocols. A network in a TCPIIP internetwork
can be a local-area network or a wide-area network.

Network Layer
At the network layer (or, more accurately, the internetwork layer), TCP/IP supports
the Internetworking Protocol. IP, in turn, uses four supporting protocols: ARP,
RARP, ICMP, and IGMP. Each of these protocols is described in greater detail in later
chapters.

44   CHAPTER 2     NETWORK MODELS


             Internetworking Protocol (IP)
             The Internetworking Protocol (IP) is the transmission mechanism used by the TCP/IP
             protocols. It is an unreliable and connectionless protocol-a best-effort delivery service.
             The term best effort means that IP provides no error checking or tracking. IP assumes
             the unreliability of the underlying layers and does its best to get a transmission through
             to its destination, but with no guarantees.
                   IP transports data in packets called datagrams, each of which is transported sepa-
             rately. Datagrams can travel along different routes and can arrive out of sequence or be
             duplicated. IP does not keep track of the routes and has no facility for reordering data-
             grams once they arrive at their destination.
                   The limited functionality of IP should not be considered a weakness, however. IP
             provides bare-bones transmission functions that free the user to add only those facilities
             necessary for a given application and thereby allows for maximum efficiency. IP is dis-
             cussed in Chapter 20.

             Address Resolution Protocol
             The Address Resolution Protocol (ARP) is used to associate a logical address with a
             physical address. On a typical physical network, such as a LAN, each device on a link
             is identified by a physical or station address, usually imprinted on the network interface
             card (NIC). ARP is used to find the physical address of the node when its Internet
             address is known. ARP is discussed in Chapter 21.

             Reverse Address Resolution Protocol
             The Reverse Address Resolution Protocol (RARP) allows a host to discover its Inter-
             net address when it knows only its physical address. It is used when a computer is con-
             nected to a network for the first time or when a diskless computer is booted. We discuss
             RARP in Chapter 21.

             Internet Control Message Protocol
             The Internet Control Message Protocol (ICMP) is a mechanism used by hosts and
             gateways to send notification of datagram problems back to the sender. ICMP sends
             query and error reporting messages. We discuss ICMP in Chapter 21.

                 Internet Group Message Protocol
             The Internet Group Message Protocol (IGMP) is used to facilitate the simultaneous
             transmission of a message to a group of recipients. We discuss IGMP in Chapter 22.

                 Transport Layer
                 Traditionally the transport layer was represented in TCP/IP by two protocols: TCP and
                 UDP. IP is a host-to-host protocol, meaning that it can deliver a packet from one
                 physical device to another. UDP and TCP are transport level protocols responsible
                 for delivery of a message from a process (running program) to another process. A new
                 transport layer protocol, SCTP, has been devised to meet the needs of some newer
                 applications.

## SECTION 2.5 ADDRESSING   45


User Datagram Protocol
The User Datagram Protocol (UDP) is the simpler of the two standard TCPIIP transport
protocols. It is a process-to-process protocol that adds only port addresses, checksum
error control, and length information to the data from the upper layer. UDP is discussed
in Chapter 23.

Transmission Control Protocol
The Transmission Control Protocol (TCP) provides full transport-layer services to
applications. TCP is a reliable stream transport protocol. The term stream, in this con-
text, means connection-oriented: A connection must be established between both ends
of a transmission before either can transmit data.
     At the sending end of each transmission, TCP divides a stream of data into smaller
units called segments. Each segment includes a sequence number for reordering after
receipt, together with an acknowledgment number for the segments received. Segments
are carried across the internet inside of IP datagrams. At the receiving end, TCP col-
lects each datagram as it comes in and reorders the transmission based on sequence
numbers. TCP is discussed in Chapter 23.

Stream Control Transmission Protocol
The Stream Control Transmission Protocol (SCTP) provides support for newer
applications such as voice over the Internet. It is a transport layer protocol that com-
bines the best features of UDP and TCP. We discuss SCTP in Chapter 23.

Application Layer
The application layer in TCPIIP is equivalent to the combined session, presentation,
and application layers in the OSI modeL Many protocols are defined at this layer. We
cover many of the standard protocols in later chapters.


## 2.5     ADDRESSING
Four levels of addresses are used in an internet employing the TCP/IP protocols:
physical (link) addresses, logical (IP) addresses, port addresses, and specific
addresses (see Figure 2.17).


Figure 2.17 Addresses in TCPIIP


                                            Addresses

                                                I
                    I               I                       I                I
                Physical         Logical                  Port           Specific
                addresses       addresses               addresses        addresses

46   CHAPTER 2     NETWORK MODELS


                 Each address is related to a specific layer in the TCPIIP architecture, as shown in
             Figure 2.18.


             Figure 2.18 Relationship of layers and addresses in TCPIIP


                           Appli"tio" I,,",     II       p=,=                11-----.-•      Specific
                                                                                          ' -addresses
                                                                                              --..I


                             T""port I,,",      IEJG [j~ 1-----.-•                             Port
                                                                                          ' -addresses
                                                                                              --..I


                                                           IPand
                                                                                      .       Logical
                              Network layer
                                                 I     other protocols
                                                                             I               addresses


                              Data link layer
                                                        Underlying
                                                                                              Physical
                                                ~        physical            ~               addresses
                                                         networks
                              Physical layer


                 Physical Addresses
             The physical address, also known as the link address, is the address of a node as defined
             by its LAN or WAN. It is included in the frame used by the data link layer. It is the
             lowest-level address.
                  The physical addresses have authority over the network (LAN or WAN). The size
             and format of these addresses vary depending on the network. For example, Ethernet
             uses a 6-byte (48-bit) physical address that is imprinted on the network interface card
             (NIC). LocalTalk (Apple), however, has a I-byte dynamic address that changes each
             time the station comes up.

             Example 2.1
                 In Figure 2.19 a node with physical address 10 sends a frame to a node with physical address 87.
                 The two nodes are connected by a link (bus topology LAN). At the data link layer, this frame
                 contains physical (link) addresses in the header. These are the only addresses needed. The rest of
                 the header contains other information needed at this level. The trailer usually contains extra bits
                 needed for error detection. As the figure shows, the computer with physical address lOis the
                 sender, and the computer with physical address 87 is the receiver. The data link layer at the
                 sender receives data from an upper layer. It encapsulates the data in a frame, adding a header and
                 a trailer. The header, among other pieces of information, carries the receiver and the sender phys-
                 ical (link) addresses. Note that in most data link protocols, the destination address, 87 in this
                 case, comes before the source address (10 in this case).
                       We have shown a bus topology for an isolated LAN. In a bus topology, the frame is propa-
                 gated in both directions (left and right). The frame propagated to the left dies when it reaches the
                 end of the cable if the cable end is terminated appropriately. The frame propagated to the right is

## SECTION 2.5   ADDRESSING         47


Figure 2.19 Physical addresses

               Sender                                                               Receiver

                                    _ _ 28                            "
                                                                 53 _ _


                                          Destination address does
                                           not match; the packet is
                                                   dropped
                                                    •••
                                                    LAN


sent to every station on the network. Each station with a physical addresses other than 87 drops
the frame because the destination address in the frame does not match its own physical address.
The intended destination computer, however, finds a match between the destination address in the
frame and its own physical address. The frame is checked, the header and trailer are dropped, and
the data part is decapsulated and delivered to the upper layer.


Example 2.2
As we will see in Chapter 13, most local-area networks use a 48-bit (6-byte) physical address
written as 12 hexadecimal digits; every byte (2 hexadecimal digits) is separated by a colon, as
shown below:


                                      07:01:02:01 :2C:4B
                        A 6-byte (12 hexadecimal digits) physical address


Logical Addresses
Logical addresses are necessary for universal communications that are independent of
underlying physical networks. Physical addresses are not adequate in an internetwork
environment where different networks can have different address formats. A universal
addressing system is needed in which each host can be identified uniquely, regardless
of the underlying physical network.
     The logical addresses are designed for this purpose. A logical address in the Internet
is currently a 32-bit address that can uniquely define a host connected to the Internet. No
two publicly addressed and visible hosts on the Internet can have the same IP address.

Example 2.3
Figure 2.20 shows a part of an internet with two routers connecting three LANs. Each device
(computer or router) has a pair of addresses (logical and physical) for each connection. In this
case, each computer is connected to only one link and therefore has only one pair of addresses.
Each router, however, is connected to three networks (only two are shown in the figure). So each
router has three pairs of addresses, one for each connection. Although it may obvious that each
router must have a separate physical address for each connection, it may not be obvious why it
needs a logical address for each connection. We discuss these issues in Chapter 22 when we dis-
cuss routing.

48   CHAPTER 2   NETWORK MODELS


             Figure 2.20 IP addresses

                             AI 10
                                                                   To another XJ44
                                                                     network


                                                    -~~_~I~I J R o u t e r l l
                                                   ~tE]
                                              LAN 1


                                                                                   LAN 2


                                              LAN 3


                                                 Ph)sical
                                                addl'esscs
                                                 changed           To another
                                                                     network    Y/55
                             P/95


                  The computer with logical address A and physical address 10 needs to send a
             packet to the computer with logical address P and physical address 95. We use letters to
             show the logical addresses and numbers for physical addresses, but note that both are
             actually numbers, as we will see later in the chapter.
                  The sender encapsulates its data in a packet at the network layer and adds two logical
             addresses (A and P). Note that in most protocols, the logical source address comes before
             the logical destination address (contrary to the order of physical addresses). The network
             layer, however, needs to find the physical address of the next hop before the packet can be
             delivered. The network layer consults its routing table (see Chapter 22) and finds the
             logical address of the next hop (router I) to be F. The ARP discussed previously finds
             the physical address of router 1 that corresponds to the logical address of 20. Now the
             network layer passes this address to the data link layer, which in tum, encapsulates the
             packet with physical destination address 20 and physical source address 10.
                  The frame is received by every device on LAN 1, but is discarded by all except
             router 1, which finds that the destination physical address in the frame matches with its
             own physical address. The router decapsulates the packet from the frame to read the log-
             ical destination address P. Since the logical destination address does not match the
             router's logical address, the router knows that the packet needs to be forwarded. The

## SECTION 2.5      ADDRESSING            49


router consults its routing table and ARP to find the physical destination address of the
next hop (router 2), creates a new frame, encapsulates the packet, and sends it to router 2.
     Note the physical addresses in the frame. The source physical address changes
from 10 to 99. The destination physical address changes from 20 (router 1 physical
address) to 33 (router 2 physical address). The logical source and destination addresses
must remain the same; otherwise the packet will be lost.
     At router 2 we have a similar scenario. The physical addresses are changed, and a
new frame is sent to the destination computer. When the frame reaches the destination,
the packet is decapsulated. The destination logical address P matches the logical address
of the computer. The data are decapsulated from the packet and delivered to the upper
layer. Note that although physical addresses will change from hop to hop, logical
addresses remain the same from the source to destination. There are some exceptions to
this rule that we discover later in the book.

                     The physical addresses will change from hop to hop,
                      but the logical addresses usually remain the same.


Port Addresses
The IP address and the physical address are necessary for a quantity of data to travel
from a source to the destination host. However, arrival at the destination host is not the
final objective of data communications on the Internet. A system that sends nothing but
data from one computer to another is not complete. Today, computers are devices that
can run multiple processes at the same time. The end objective of Internet communica-
tion is a process communicating with another process. For example, computer A can
communicate with computer C by using TELNET. At the same time, computer A com-
municates with computer B by using the File Transfer Protocol (FTP). For these pro-
cesses to receive data simultaneously, we need a method to label the different processes.
In other words, they need addresses. In the TCPIIP architecture, the label assigned to a
process is called a port address. A port address in TCPIIP is 16 bits in length.

Example 2.4
Figure 2.21 shows two computers communicating via the Internet. The sending computer is run-
ning three processes at this time with port addresses a, b, and c. The receiving computer is running
two processes at this time with port addresses j and k. Process a in the sending computer needs to
communicate with process j in the receiving computer. Note that although both computers are
using the same application, FTP, for example, the port addresses are different because one is a client
program and the other is a server program, as we will see in Chapter 23. To show that data from
process a need to be delivered to process j, and not k, the transport layer encapsulates data from
the application layer in a packet and adds two port addresses (a and j), source and destination. The
packet from the transport layer is then encapsulated in another packet at the network layer with
logical source and destination addresses (A and P). Finally, this packet is encapsulated in a frame
with the physical source and destination addresses of the next hop. We have not shown the physi-
cal addresses because they change from hop to hop inside the cloud designated as the Internet.
Note that although physical addresses change from hop to hop, logical and port addresses remain
the same from the source to destination. There are some exceptions to this rule that we discuss
later in the book.

50   CHAPTER 2     NETWORK MODELS


             Figure 2.21 Port addresses

                                   abc                                                  j     k


                                        DD                                           DD

                                                   - - - - Data link layer - - - -


                                                                Internet


                                       The physical addresses change from hop to hop,
                                 but the logical and port addresses usually remain the same.

             Example 2.5
                 As we will see in Chapter 23, a port address is a 16-bit address represented by one decimal num-
                 her as shown.

                                                                753
                                     A 16-bit port address represented as one single number


                 Specific Addresses
                 Some applications have user-friendly addresses that are designed for that specific address.
                 Examples include the e-mail address (for example, forouzan@fhda.edu) and the Universal
                 Resource Locator (URL) (for example, www.mhhe.com). The first defines the recipient of
                 an e-mail (see Chapter 26); the second is used to find a document on the World Wide Web
                 (see Chapter 27). These addresses, however, get changed to the corresponding port and
                 logical addresses by the sending computer, as we will see in Chapter 25.


## 2.6      RECOMMENDED READING
                 For more details about subjects discussed in this chapter, we recommend the following
                 books and sites. The items enclosed in brackets, [...] refer to the reference list at the
                 end of the text.

## SECTION 2. 7 KEY TERMS         51


Books
Network models are discussed in Section 1.3 of [Tan03], Chapter 2 of [For06], Chapter 2
of [Sta04], Sections 2.2 and 2.3 of [GW04], Section 1.3 of [PD03], and Section 1.7 of
[KR05]. A good discussion about addresses can be found in Section 1.7 of [Ste94].

Sites
The following site is related to topics discussed in this chapter.
o www.osi.org! Information about OS1.
RFCs
The following site lists all RFCs, including those related to IP and port addresses.
o www.ietLorg/rfc.html

## 2.7     KEY TERMS
access control                                   Open Systems Interconnection (OSI)
Address Resolution Protocol (ARP)                   model
application layer                                peer-to-peer process
best-effort delivery                             physical addressing
bits                                             physical layer
connection control                               port address
data link layer                                  presentation layer
encoding                                         process-to-process delivery
error                                            Reverse Address Resolution Protocol
error control                                       (RARP)
flow control                                     routing
frame                                            segmentation
header                                           session layer
hop-to-hop delivery                              source-to-destination delivery
host-to-host protocol                            Stream Control Transmission Protocol
                                                    (SCTP)
interface
                                                 synchronization point
Internet Control Message Protocol
   (ICMP)                                        TCPIIP protocol suite
Internet Group Message Protocol (IGMP)           trailer
logical addressing                               Transmission Control Protocol (TCP)
mail service                                     transmission rate
network layer                                    transport layer
node-to-node delivery                            transport level protocols
open system                                      User Datagram Protocol (UDP)

52   CHAPTER 2     NETWORK MODELS


## 2.8       SUMMARY
             o The International Standards Organization created a model called the Open Systems
                   Interconnection, which allows diverse systems to communicate.
             U     The seven-layer OSI model provides guidelines for the development of universally
                   compatible networking protocols.
             o     The physical, data link, and network layers are the network support layers.
             o     The session, presentation, and application layers are the user support layers.
             D     The transport layer links the network support layers and the user support layers.
             o     The physical layer coordinates the functions required to transmit a bit stream over
                   a physical medium.
             o     The data link layer is responsible for delivering data units from one station to the
                   next without errors.
             o     The network layer is responsible for the source-to-destination delivery of a packet
                   across multiple network links.
             [J    The transport layer is responsible for the process-to-process delivery of the entire
                   message.
             D     The session layer establishes, maintains, and synchronizes the interactions between
                   communicating devices.
             U     The presentation layer ensures interoperability between communicating devices
                   through transformation of data into a mutually agreed upon format.
             o     The application layer enables the users to access the network.
             o     TCP/IP is a five-layer hierarchical protocol suite developed before the OSI model.
             U     The TCP/IP application layer is equivalent to the combined session, presentation,
                   and application layers of the OSI model.
             U     Four levels of addresses are used in an internet following the TCP/IP protocols: phys-
                   ical (link) addresses, logical (IP) addresses, port addresses, and specific addresses.
             o     The physical address, also known as the link address, is the address of a node as
                   defined by its LAN or WAN.
             L,J   The IP address uniquely defines a host on the Internet.
             U     The port address identifies a process on a host.
             o     A specific address is a user-friendly address.


## 2.9       PRACTICE SET
             Review Questions
                 I. List the layers of the Internet model.
                 2. Which layers in the Internet model are the network support layers?
                 3. Which layer in the Internet model is the user support layer?
                 4. What is the difference between network layer delivery and transport layer delivery?

## SECTION 2.9   PRACTICE SET       53


 5. What is a peer-to-peer process?
 6. How does information get passed from one layer to the next in the Internet
    model?
 7. What are headers and trailers, and how do they get added and removed?
 X. What are the concerns of the physical layer in the Internet model?
 9. What are the responsibilities of the data link layer in the Internet model?
10. What are the responsibilities of the network layer in the Internet model?
II. What are the responsibilities of the transport layer in the Internet model?
12. What is the difference between a port address, a logical address, and a physical
    address?
13. Name some services provided by the application layer in the Internet model.
14. How do the layers of the Internet model correlate to the layers of the OSI model?


Exercises
15. How are OSI and ISO related to each other?
16. Match the following to one or more layers of the OSI model:
     a. Route determination
     b. Flow control
     c. Interface to transmission media
     d. Provides access for the end user
I 7. Match the following to one or more layers of the OSI model:
     a. Reliable process-to-process message delivery
     b. Route selection
     c. Defines frames
     d. Provides user services such as e-mail and file transfer
     e. Transmission of bit stream across physical medium
\ 8. Match the following to one or more layers of the OSl model:
     a. Communicates directly with user's application program
     b. Error correction and retransmission
     c. Mechanical, electrical, and functional interface
     d. Responsibility for carrying frames between adjacent nodes
I 9. Match the following to one or more layers of the OSI model:
     a. Format and code conversion services
     b. Establishes, manages, and terminates sessions
     c. Ensures reliable transmission of data
     d. Log-in and log-out procedures
     e. Provides independence from differences in data representation
20. In Figure 2.22, computer A sends a message to computer D via LANl, router Rl,
     and LAN2. Show the contents of the packets and frames at the network and data
     link layer for each hop interface.

54   CHAPTER 2     NETWORK MODELS


             Figure 2.22 Exercise 20


                                                               Rl

                                       Sender           8/42


                                                LAN 1               LAN 2   Sender


                 21. In Figure 2.22, assume that the communication is between a process running at
                     computer A with port address i and a process running at computer D with port
                     address j. Show the contents of packets and frames at the network, data link, and
                     transport layer for each hop.
                 22. Suppose a computer sends a frame to another computer on a bus topology LAN.
                     The physical destination address of the frame is corrupted during the transmission.
                     What happens to the frame? How can the sender be informed about the situation?
                 23. Suppose a computer sends a packet at the network layer to another computer
                     somewhere in the Internet. The logical destination address of the packet is cor-
                     rupted. What happens to the packet? How can the source computer be informed of
                     the situation?
                 24. Suppose a computer sends a packet at the transport layer to another computer
                     somewhere in the Internet. There is no process with the destination port address
                     running at the destination computer. What will happen?
                 25. If the data link layer can detect errors between hops, why do you think we need
                     another checking mechanism at the transport layer?

             Research Activities
                 26. Give some advantages and disadvantages of combining the session, presentation,
                     and application layer in the OSI model into one single application layer in the
                     Internet model.
                 27. Dialog control and synchronization are two responsibilities of the session layer in
                     the OSI model. Which layer do you think is responsible for these duties in the
                     Internet model? Explain your answer.
                 28. Translation, encryption, and compression are some of the duties of the presentation
                     layer in the OSI model. Which layer do you think is responsible for these duties in
                     the Internet model? Explain your answer.
                 29. There are several transport layer models proposed in the OSI model. Find all of
                     them. Explain the differences between them.
                 30. There are several network layer models proposed in the OSI model. Find all of
                     them. Explain the differences between them.

Physical Layer
and Media


Objectives
We start the discussion of the Internet model with the bottom-most layer, the physical
layer. It is the layer that actually interacts with the transmission media, the physical part
of the network that connects network components together. This layer is involved in
physically carrying information from one node in the network to the next.
     The physical layer has complex tasks to perform. One major task is to provide
services for the data link layer. The data in the data link layer consists of Os and I s orga-
nized into frames that are ready to be sent across the transmission medium. This stream
of Os and I s must first be converted into another entity: signals. One of the services pro-
vided by the physical layer is to create a signal that represents this stream of bits.
     The physical layer must also take care of the physical network, the transmission
medium. The transmission medium is a passive entity; it has no internal program or
logic for control like other layers. The transmission medium must be controlled by the
physical layer. The physical layer decides on the directions of data flow. The physical
layer decides on the number of logical channels for transporting data coming from
different sources.
     In Part 2 of the book, we discuss issues related to the physical layer and the trans-
mission medium that is controlled by the physical layer. In the last chapter of Part 2, we
discuss the structure and the physical layers of the telephone network and the cable
network.


                     Part 2 of the book is devoted to the physical layer
                                and the transmission media.

Chapters
This part consists of seven chapters: Chapters 3 to 9.

## Chapter 3
## Chapter 3 discusses the relationship between data, which are created by a device, and
electromagnetic signals, which are transmitted over a medium.

## Chapter 4
## Chapter 4 deals with digital transmission. We discuss how we can covert digital or
analog data to digital signals.

## Chapter 5
## Chapter 5 deals with analog transmission. We discuss how we can covert digital or
analog data to analog signals.

## Chapter 6
## Chapter 6 shows how we can use the available bandwidth efficiently. We discuss two
separate, but related topics, multiplexing and spreading.

## Chapter 7
After explaining some ideas about data and signals and how we can use them effi-
ciently, we discuss the characteristics of transmission media, both guided and
unguided, in this chapter. Although transmission media operates under the physical
layer, they are controlled by the physical layer.

## Chapter 8
Although the previous chapters in this part are issues related to the physical layer or
transmission media, Chapter 8 discusses switching, a topic that can be related to several
layers. We have included this topic in this part of the book to avoid repeating the dis-
cussion for each layer.

## Chapter 9
## Chapter 9 shows how the issues discussed in the previous chapters can be used in actual
networks. In this chapter, we first discuss the telephone network as designed to carry
voice. We then show how it can be used to carry data. Second, we discuss the cable net-
work as a television network. We then show how it can also be used to carry data.

## CHAPTER 3

      Data and Signals


      One of the major functions of the physical layer is to move data in the form of electro-
      magnetic signals across a transmission medium. Whether you are collecting numerical
      statistics from another computer, sending animated pictures from a design workstation,
      or causing a bell to ring at a distant control center, you are working with the transmis-
      sion of data across network connections.
           Generally, the data usable to a person or application are not in a form that can be
      transmitted over a network. For example, a photograph must first be changed to a form
      that transmission media can accept. Transmission media work by conducting energy
      along a physical path.

               To be transmitted, data must be transformed to electromagnetic signals.


## 3.1     ANALOG AND DIGITAL
      Both data and the signals that represent them can be either analog or digital in form.

      Analog and Digital Data
      Data can be analog or digital. The term analog data refers to information that is contin-
      uous; digital data refers to information that has discrete states. For example, an analog
      clock that has hour, minute, and second hands gives information in a continuous form;
      the movements of the hands are continuous. On the other hand, a digital clock that
      reports the hours and the minutes will change suddenly from 8:05 to 8:06.
           Analog data, such as the sounds made by a human voice, take on continuous values.
      When someone speaks, an analog wave is created in the air. This can be captured by a
      microphone and converted to an analog signal or sampled and converted to a digital
      signal.
           Digital data take on discrete values. For example, data are stored in computer
      memory in the form of Os and 1s. They can be converted to a digital signal or modu-
      lated into an analog signal for transmission across a medium.


                                                                                               57

58   CHAPTER 3     DATA AND SIGNALS


                   Data can be analog or digital. Analog data are continuous and take continuous values.
                                 Digital data have discrete states and take discrete values.


             Analog and Digital Signals
             Like the data they represent, signals can be either analog or digital. An analog signal
             has infinitely many levels of intensity over a period of time. As the wave moves from
             value A to value B, it passes through and includes an infinite number of values along its
             path. A digital signal, on the other hand, can have only a limited number of defined
             values. Although each value can be any number, it is often as simple as 1 and O.
                  The simplest way to show signals is by plotting them on a pair of perpendicular
             axes. The vertical axis represents the value or strength of a signal. The horizontal axis
             represents time. Figure 3.1 illustrates an analog signal and a digital signal. The curve
             representing the analog signal passes through an infinite number of points. The vertical
             lines of the digital signal, however, demonstrate the sudden jump that the signal makes
             from value to value.


                       Signals can be analog or digital. Analog signals can have an infinite number of
                         values in a range; digital signals can have only a limited number of values.


             Figure 3.1          Comparison ofanalog and digital signals


                    Value                                       Value


                                                                    -


                                                      Time                                            Time

                                                                                              '----

                  a. Analog signal                             b. Digital signal


             Periodic and Nonperiodic Signals
                 Both analog and digital signals can take one of two forms: periodic or nonperiodic
                 (sometimes refer to as aperiodic, because the prefix a in Greek means "non").
                      A periodic signal completes a pattern within a measurable time frame, called a
                 period, and repeats that pattern over subsequent identical periods. The completion of
                 one full pattern is called a cycle. A nonperiodic signal changes without exhibiting a pat-
                 tern or cycle that repeats over time.
                      Both analog and digital signals can be periodic or nonperiodic. In data communi-
                 cations, we commonly use periodic analog signals (because they need less bandwidth,

## SECTION 3.2     PERIODIC ANALOG SIGNALS              59


as we will see in Chapter 5) and nonperiodic digital signals (because they can represent
variation in data, as we will see in Chapter 6).

                    In data communications, we commonly use periodic
                       analog signals and nonperiodic digital signals.


## 3.2     PERIODIC ANALOG SIGNALS
Periodic analog signals can be classified as simple or composite. A simple periodic
analog signal, a sine wave, cannot be decomposed into simpler signals. A composite
periodic analog signal is composed of multiple sine waves.

Sine Wave
The sine wave is the most fundamental form of a periodic analog signal. When we
visualize it as a simple oscillating curve, its change over the course of a cycle is smooth
and consistent, a continuous, rolling flow. Figure 3.2 shows a sine wave. Each cycle
consists of a single arc above the time axis followed by a single arc below it.


Figure 3.2    A sine wave


                Value


                                                                          Time


             We discuss a mathematical approach to sine waves in Appendix C.

    A sine wave can be represented by three parameters: the peak amplitude, the fre-
quency, and the phase. These three parameters fully describe a sine wave.

Peak Amplitude
The peak amplitude of a signal is the absolute value of its highest intensity, propor-
tional to the energy it carries. For electric signals, peak amplitude is normally measured
in volts. Figure 3.3 shows two signals and their peak amplitudes.

Example 3.1
The power in your house can be represented by a sine wave with a peak amplitude of 155 to 170 V.
However, it is common knowledge that the voltage of the power in U.S. homes is 110 to 120 V.

60   CHAPTER 3     DATA AND SIGNALS


             Figure 3.3        Two signals with the same phase and frequency, but different amplitudes


                                 Amplitude

                                             Peak amplitude


                                                                                              Time


                               a. A signal with high peak amplitude


                                 Amplitude


                                                                                               Time
                               b. A signal with low peak amplitude


             This discrepancy is due to the fact that these are root mean square (rms) values. The signal is
             squared and then the average amplitude is calculated. The peak value is equal to 2112 x rms
             value.


             Example 3.2
                 The voltage of battery is a constant; this constant value can be considered a sine wave, as we will
                 see later. For example, the peak value of an AA battery is normally 1.5 V.

             Period and Frequency
                 Period refers to the amount of time, in seconds, a signal needs to complete 1 cycle.
                 Frequency refers to the number of periods in I s. Note that period and frequency are just
                 one characteristic defined in two ways. Period is the inverse of frequency, and frequency
                 is the inverse of period, as the following formulas show.


                                                            1                 1
                                                         f= -         and   T=-
                                                              T               f


                                       Frequency and period are the inverse of each other.


                      Figure 3.4 shows two signals and their frequencies.

## SECTION 3.2       PERIODIC ANALOG SIGNALS              61


Figure 3.4      Two signals with the same amplitude and phase, but different frequencies


                 Amplitude
                                    12 periods in Is-----+- Frequency is 12 Hz
                                                        1s


                                                                                           Time


                   Period:   n  s

                a. A signal with a frequency of 12 Hz


                 Amplitude
                                    6 periods in Is-----+- Frequency is 6 Hz
                                                        1s

                                                                                 I   •••


                                                                                           Time

                          T
                      Period:   ts
                b. A signal with a frequency of 6 Hz


    Period is formally expressed in seconds. Frequency is formally expressed in
Hertz (Hz), which is cycle per second. Units of period and frequency are shown in
Table 3.1.

Table 3.1      Units ofperiod andfrequency

         Unit                          Equivalent                        Unit                Equivalent
 Seconds (s)                               1s                  Hertz (Hz)                         1 Hz
 Milliseconds (ms)                         10-3 s              Kilohertz (kHz)                    103 Hz
 Microseconds (Ils)                        10-6 s              Megahertz (MHz)                    106 Hz
 Nanoseconds (ns)                          10-9 s              Gigahertz (GHz)                    109 Hz
 Picoseconds (ps)                          10- 12 s            Terahertz (THz)                    10 12 Hz


Example 3.3
The power we use at home has a frequency of 60 Hz (50 Hz in Europe). The period of this sine
wave can be determined as follows:


                      T=     1= =      1
                                      60
                                                                            3
## 0.0166 s = 0.0166 x 10 ms = 16.6 illS


     This means that the period of the power for our lights at home is 0.0116 s, or 16.6 ms. Our
eyes are not sensitive enough to distinguish these rapid changes in amplitude.

62   CHAPTER 3     DATA AND SIGNALS


             Example 3.4
             Express a period of 100 ms in microseconds.

             Solution
             From Table 3.1 we find the equivalents of 1 ms (l ms is 10-3 s) and 1 s (1 sis 106118). We make
             the following substitutions:

                          100 ms:;;::; 100 X 10-3 s:;;::; 100 X 10-3 X 106 JlS:;;::; 102 X 10-3 X 106 JlS :::::: 105 JlS


             Example 3.5
             The period of a signal is 100 ms. What is its frequency in kilohertz?

             Solution
             First we change lOO ms to seconds, and then we calculate the frequency from the period (1 Hz =
             10-3 kHz).


                                                      100 ms = 100 X 10-3 S = 10-1 S

                                      f= 1. = _1_ Hz = 10 Hz = 10 X 10-3 kHz = 10-2 kHz
                                           T      10- 1


             More About Frequency
             We already know that frequency is the relationship of a signal to time and that the frequency
             of a wave is the number of cycles it completes in 1 s. But another way to look at frequency
             is as a measurement of the rate of change. Electromagnetic signals are oscillating wave-
             forms; that is, they fluctuate continuously and predictably above and below a mean energy
             level. A 40-Hz signal has one-half the frequency of an 80-Hz signal; it completes 1 cycle in
             twice the time of the 80-Hz signal, so each cycle also takes twice as long to change from its
             lowest to its highest voltage levels. Frequency, therefore, though described in cycles per sec-
             ond (hertz), is a general measurement of the rate of change of a signal with respect to time.

                    Frequency is the rate of change with respect to time. Change in a short span of time
                       means high frequency. Change over a long span of time means low frequency.

                 If the value of a signal changes over a very short span of time, its frequency is
             high. If it changes over a long span of time, its frequency is low.

                 Two Extremes
                 What if a signal does not change at all? What if it maintains a constant voltage level for the
                 entire time it is active? In such a case, its frequency is zero. Conceptually, this idea is a sim-
                 ple one. If a signal does not change at all, it never completes a cycle, so its frequency is a Hz.
                      But what if a signal changes instantaneously? What if it jumps from one level to
                 another in no time? Then its frequency is infinite. In other words, when a signal changes
                 instantaneously, its period is zero; since frequency is the inverse of period, in this case,
                 the frequency is 1/0, or infinite (unbounded).

## SECTION 3.2     PERiODIC ANALOG SIGNALS             63


                   If a signal does not change at all, its frequency is zero.
                If a signal changes instantaneously, its frequency is infinite.


Phase
The term phase describes the position of the waveform relative to time O. If we think of
the wave as something that can be shifted backward or forward along the time axis,
phase describes the amount of that shift. It indicates the status of the first cycle.

              Phase describes the position of the waveform relative to time O.


     Phase is measured in degrees or radians [360° is 2n rad; 1° is 2n/360 rad, and 1 rad
is 360/(2n)]. A phase shift of 360° corresponds to a shift of a complete period; a phase
shift of 180° corresponds to a shift of one-half of a period; and a phase shift of 90° cor-
responds to a shift of one-quarter of a period (see Figure 3.5).


Figure 3.5    Three sine waves with the same amplitude andfrequency, but different phases


                                                                             •
                                                                           Time

             a. 0 degrees


                     *AAL
                1!4TO\J~
              b. 90 degrees
                                                                             ~
                                                                           Time


                                                                             )I

                                                                           Time


             c. 180 degrees


    Looking at Figure 3.5, we can say that
    I. A sine wave with a phase of 0° starts at time 0 with a zero amplitude. The
       amplitude is increasing.
    2. A sine wave with a phase of 90° starts at time 0 with a peak amplitude. The
       amplitude is decreasing.

64   CHAPTER 3   DATA AND SIGNALS


                3. A sine wave with a phase of 180° starts at time 0 with a zero amplitude. The
                    amplitude is decreasing.
             Another way to look at the phase is in terms of shift or offset. We can say that
                 1. A sine wave with a phase of 0° is not shifted.
                2. A sine wave with a phase of 90° is shifted to the left by ! cycle. However, note
                                                                               4
                    that the signal does not really exist before time O.
                  3. A sine wave with a phase of 180° is shifted to the left by ~ cycle. However, note
                     that the signal does not really exist before time O.

             Example 3.6
             A sine wave is offset ~ cycle with respect to time O. What is its phase in degrees and radians?

             Solution
             We know that 1 complete cycle is 360°. Therefore,        i cycle is
                                     ! x 360;::; 60° =60 x 2n tad;::; ~ fad;::; 1.046 rad
                                     6                      360            3


             Wavelength
             Wavelength is another characteristic of a signal traveling through a transmission
             medium. Wavelength binds the period or the frequency of a simple sine wave to the
             propagation speed of the medium (see Figure 3.6).


             Figure 3.6     Wavelength and period

                                                                               Wavelength
                          Transmission medium   /   "
                                                    '- "~         /   " '- :.          ':
                                                                                            Direction of
                                                                                            propagation


                  While the frequency of a signal is independent of the medium, the wavelength
             depends on both the frequency and the medium. Wavelength is a property of any type
             of signal. In data communications, we often use wavelength to describe the transmis-
             sion of light in an optical fiber. The wavelength is the distance a simple signal can travel
             in one period.
                  Wavelength can be calculated if one is given the propagation speed (the speed of
             light) and the period of the signal. However, since period and frequency are related to
             each other, if we represent wavelength by A, propagation speed by c (speed of light), and
             frequency by 1, we get

                                                .              •        propagation speed
                           Wavelength = propagatJon speed x perJod ;::;    {\
                                                                             requency

## SECTION 3.2             PERIODIC ANALOG SIGNALS    6S


     The propagation speed of electromagnetic signals depends on the medium and on
the frequency of the signal. For example, in a vacuum, light is propagated with a speed
of 3 x 108 mls. That speed is lower in air and even lower in cable.
     The wavelength is normally measured in micrometers (microns) instead of meters.
For example, the wavelength of red light (frequency = 4 x 10 14) in air is

                                                    8
                                 c   3xlO             -6
                              A= - =     14
                                            =0.75 x 10 m=0.75!J.m
                                    f       4x 10

In a coaxial or fiber-optic cable, however, the wavelength is shorter (0.5 !Jm) because the
propagation speed in the cable is decreased.

Time and Frequency Domains
A sine wave is comprehensively defined by its amplitude, frequency, and phase. We
have been showing a sine wave by using what is called a time-domain plot. The
time-domain plot shows changes in signal amplitude with respect to time (it is an
amplitude-versus-time plot). Phase is not explicitly shown on a time-domain plot.
     To show the relationship between amplitude and frequency, we can use what is
called a frequency-domain plot. A frequency-domain plot is concerned with only the
peak value and the frequency. Changes of amplitude during one period are not shown.
Figure 3.7 shows a signal in both the time and frequency domains.


Figure 3.7 The time-domain andfrequency-domain plots ofa sine wave


        Amplitude
                                            Frequency: 6 Hz

             Peak value: 5 V
           5 ----------


                                                                                            Time
                                                                                             (s)

       a. A sine wave in the time domain (peak value: 5 V, frequency: 6 Hz)


         Amplitude

                Peak value: 5 V


           5 --; -1-1--; --1--1'--+-1-----111--+1-----111--+1-+-1-+1-+-1                      ~.
            r   1 2     3 4     5 6     7    8   9 10 11 12 13 14                         Frequency
                                                                                             (Hz)

       b. The same sine wave in the frequency domain (peak value: 5 V, frequency: 6 Hz)

66   CHAPTER 3    DATA AND SIGNALS


                  It is obvious that the frequency domain is easy to plot and conveys the information
             that one can find in a time domain plot. The advantage of the frequency domain is that
             we can immediately see the values of the frequency and peak amplitude. A complete
             sine wave is represented by one spike. The position of the spike shows the frequency;
             its height shows the peak amplitude.


                                   A complete sine wave in the time domain can be represented
                                         by one single spike in the frequency domain.


             Example 3.7
             The frequency domain is more compact and useful when we are dealing with more than one sine
             wave. For example, Figure 3.8 shows three sine waves, each with different amplitude and fre-
             quency. All can be represented by three spikes in the frequency domain.


             Figure 3.8         The time domain and frequency domain of three sine waves


                                                                           Amplitude


                                                                            15 -

                                                                            10 -
                                                                             5-
                                                                                         I
                                                                                   o     8        16      Frequency


                 a. Time-domain representation of three sine waves with   b. Frequency-domain representation of
                    frequencies 0, 8, and 16                                 the same three signals

             ---------------------------------------


                 Composite Signals
             So far, we have focused on simple sine waves. Simple sine waves have many applica-
             tions in daily life. We can send a single sine wave to carry electric energy from one
             place to another. For example, the power company sends a single sine wave with a fre-
             quency of 60 Hz to distribute electric energy to houses and businesses. As another
             example, we can use a single sine wave to send an alarm to a security center when a
             burglar opens a door or window in the house. In the first case, the sine wave is carrying
             energy; in the second, the sine wave is a signal of danger.
                  If we had only one single sine wave to convey a conversation over the phone, it
             would make no sense and carry no information. We would just hear a buzz. As we will
             see in Chapters 4 and 5, we need to send a composite signal to communicate data. A
             composite signal is made of many simple sine waves.


                           A singleafrequency sine wave is not useful in data communications;
                       we need to send a composite signal, a signal made of many simple sine waves.

## SECTION 3.2     PERIODIC ANALOG SIGNALS               67


    In the early 1900s, the French mathematician Jean-Baptiste Fourier showed that
any composite signal is actually a combination of simple sine waves with different fre-
quencies, amplitudes, and phases. Fourier analysis is discussed in Appendix C; for our
purposes, we just present the concept.

         According to Fourier analysis, any composite signal is a combination of
          simple sine waves with different frequencies, amplitudes, and phases.
                      Fourier analysis is discussed in Appendix C.


     A composite signal can be periodic or nonperiodic. A periodic composite signal
can be decomposed into a series of simple sine waves with discrete frequencies-
frequencies that have integer values (1, 2, 3, and so on). A nonperiodic composite sig-
nal can be decomposed into a combination of an infinite number of simple sine waves
with continuous frequencies, frequencies that have real values.


     If the composite signal is periodic, the decomposition gives a series of signals with
       discrete frequencies; if the composite signal is nonperiodic, the decomposition
               gives a combination of sine waves with continuous frequencies.


Example 3.8
Figure 3.9 shows a periodic composite signal with frequency f This type of signal is not typical
of those found in data communications.We can consider it to be three alarm systems, each with a
different frequency. The analysis of this signal can give us a good understanding of how to
decompose signals.


Figure 3.9 A composite periodic signal


                                                                                 ...
                                                                                       Time


       It is very difficult to manually decompose this signal into a series of simple sine waves.
However, there are tools, both hardware and software, that can help us do the job. We are not con-
cerned about how it is done; we are only interested in the result. Figure 3.10 shows the result of
decomposing the above signal in both the time and frequency domains.
       The amplitude of the sine wave with frequency f is almost the same as the peak amplitude of
the composite signal. The amplitude of the sine wave with frequency 3f is one-third of that of the
first, and the amplitude of the sine wave with frequency 9f is one-ninth of the first. The frequency

68   CHAPTER 3   DATA AND SIGNALS


             Figure 3.10 Decomposition ofa composite periodic signal in the time and frequency domains

                              Amplitude                                                         -    Frequency 1
                                                                                                -    Frequency 31
                                                                                                -    Frequency 91


                                                                                                                 Time


                             a. Time-domain decomposition of a composite signal


                              Amplitude


                                      WL...-----'3~L...-------9L-'!---------T~i~e
                             b. Frequency-domain decomposition of the composite signal


             of the sine wave with frequency f is the same as the frequency of the composite signal; it is called
             the fundamental frequency, or first harmonic. The sine wave with frequency 3fhas a frequency
             of 3 times the fundamental frequency; it is called the third harmonic. The third sine wave with fre-
             quency 9fhas a frequency of 9 times the fundamental frequency; it is called the ninth harmonic.
                   Note that the frequency decomposition of the signal is discrete; it has frequenciesf, 3f, and
             9f Because f is an integral number, 3f and 9f are also integral numbers. There are no frequencies
             such as 1.2f or 2.6f The frequency domain of a periodic composite signal is always made of dis-
             crete spikes.


             Example 3.9
             Figure 3.11 shows a nonperiodic composite signal. It can be the signal created by a microphone or a
             telephone set when a word or two is pronounced. In this case, the composite signal cannot be peri-
             odic, because that implies that we are repeating the same word or words with exactly the same tone.


             Figure 3.11 The time and frequency domains ofa nonperiodic signal

                  Amplitude                                              Amplitude
                                                                                         Amplitude for sine
                                                                                         wave of frequency 1


                        IA       IA                ,
                                                                                         1
                                                 v         Time                                                4 kHz    Frequency


                 a. Time domain                                        b. Frequency domain

## SECTION 3.2        PERIODIC ANALOG SIGNALS     69


     In a time-domain representation of this composite signal, there are an infinite num-
ber of simple sine frequencies. Although the number of frequencies in a human voice is
infinite, the range is limited. A normal human being can create a continuous range of
frequencies between 0 and 4 kHz.
     Note that the frequency decomposition of the signal yields a continuous curve.
There are an infinite number of frequencies between 0.0 and 4000.0 (real values). To find
the amplitude related to frequency J, we draw a vertical line atfto intersect the envelope
curve. The height of the vertical line is the amplitude of the corresponding frequency.


Bandwidth
The range of frequencies contained in a composite signal is its bandwidth. The band-
width is normally a difference between two numbers. For example, if a composite signal
contains frequencies between 1000 and 5000, its bandwidth is 5000 - 1000, or 4000.


              The bandwidth of a composite signal is the difference between the
                 highest and the lowest frequencies contained in that signal.


    Figure 3.12 shows the concept of bandwidth. The figure depicts two composite
signals, one periodic and the other nonperiodic. The bandwidth of the periodic signal
contains all integer frequencies between 1000 and 5000 (1000, 100 I, 1002, ...). The band-
width of the nonperiodic signals has the same range, but the frequencies are continuous.


Figure 3.12     The bandwidth ofperiodic and nonperiodic composite signals


           Amplitude


                   1000                                                  5000   Frequency
                                   Bandwidth = 5000 - 1000 = 4000 Hz
                     I·                                                   ·1
         a. Bandwidth of a periodic signal


           Amplitude


                   1000                                                  5000   Frequency
                                   Bandwidth = 5000 - 1000 = 4000 Hz
                     I·                                                   ·1
          b. Bandwidth of a nonperiodic signal

70   CHAPTER 3     DATA AND SIGNALS


             Example 3.10
             If a periodic signal is decomposed into five sine waves with frequencies of 100, 300, 500, 700,
             and 900 Hz, what is its bandwidth? Draw the spectrum, assuming all components have a maxi-
             mum amplitude of 10 V.
             Solution
             Letfh be the highest frequency, fl the lowest frequency, and B the bandwidth. Then

                                                    B =fh - it = 900 - 100 = 800 Hz

             The spectrum has only five spikes, at 100, 300, 500, 700, and 900 Hz (see Figure 3.13).


             Figure 3.13        The bandwidthfor Example 3.10

                                  Amplitude


                                 10+-----]
                                              100               300       500        700      900        Frequency
                                               I,                                             -I
                                                             Bandwidth = 900 - 100 = 800 Hz


             Example 3.11
             A periodic signal has a bandwidth of 20 Hz. The highest frequency is 60 Hz. What is the lowest
             frequency? Draw the spectrum if the signal contains all frequencies of the same amplitude.

             Solution
             Letfh be the highest frequency,fz the lowest frequency, and B the bandwidth. Then

                                      B =fh - fz    :::::}     20 =60 - it      =}   .ft =60 - 20 =40 Hz

             The spectrum contains all integer frequencies. We show this by a series of spikes (see Figure 3.14).


                 Figure 3.14    The bandwidth for Example 3.11


                                 III
                                 4041 42                                                      585960             Frequency

                                 I,                 Bandwidth = 60 - 40 = 20 Hz
                                                                                                    ·1
                                                                                                                    (Hz)


             Example 3.12
                 A nonperiodic composite signal has a bandwidth of 200 kHz, with a middle frequency of
                 140 kHz and peak amplitude of 20 V. The two extreme frequencies have an amplitude of 0. Draw
                 the frequency domain of the signal.

                                                      SECT/ON 3.3      DIGITAL SIGNALS           71


Solution
The lowest frequency must be at 40 kHz and the highest at 240 kHz. Figure 3.15 shows the fre-
quency domain and the bandwidth.

Figure 3.15     The bandwidth for Example 3.12

             Amplitude


                   40 kHz                 140kHz                   240 kHz    Frequency


Example 3. J3
An example of a nonperiodic composite signal is the signal propagated by an AM radio station, In
the United States, each AM radio station is assigned a lO-kHz bandwidth. The total bandwidth ded-
icated to AM radio ranges from 530 to 1700 kHz. We will show the rationale behind this lO-kHz
bandwidth in Chapter 5.

Example 3. J4
Another example of a nonperiodic composite signal is the signal propagated by an FM radio sta-
tion. In the United States, each FM radio station is assigned a 200-kHz bandwidth. The total
bandwidth dedicated to FM radio ranges from 88 to 108 MHz. We will show the rationale behind
this 200-kHz bandwidth in Chapter 5.

Example 3./5
Another example of a nonperiodic composite signal is the signal received by an old-fashioned
analog black-and-white TV. A TV screen is made up of pixels (picture elements) with each pixel
being either white or black. The screen is scanned 30 times per second. (Scanning is actually
60 times per second, but odd lines are scanned in one round and even lines in the next and then
interleaved.) If we assume a resolution of 525 x 700 (525 vertical lines and 700 horizontal lines),
which is a ratio of 3: 4, we have 367,500 pixels per screen. If we scan the screen 30 times per sec-
ond, this is 367,500 x 30 = 11,025,000 pixels per second. The worst-case scenario is alternating
black and white pixels. In this case, we need to represent one color by the minimum amplitude
and the other color by the maximum amplitude. We can send 2 pixels per cycle. Therefore, we
need 11,025,000/2 = 5,512,500 cycles per second, or Hz. The bandwidth needed is 5.5124 MHz.
This worst-case scenario has such a low probability of occurrence that the assumption is that we
need only 70 percent of this bandwidth, which is 3.85 MHz. Since audio and synchronization sig-
nals are also needed, a 4-MHz bandwidth has been set aside for each black and white TV chan-
nel. An analog color TV channel has a 6-MHz bandwidth.


## 3.3      DIGITAL SIGNALS
In addition to being represented by an analog signal, information can also be repre-
sented by a digital signal. For example, a I can be encoded as a positive voltage and a 0
as zero voltage. A digital signal can have more than two levels. In this case, we can

72   CHAPTER 3   DATA AND SIGNALS


             send more than 1 bit for each level. Figure 3.16 shows two signals, one with two levels
             and the other with four.

             Figure 3.16       Two digital signals: one with two signal levels and the other with four signal levels


                              Amplitude                             8 bits sent in I s,
                                                                     Bit rate = 8 bps


                                       1    I   0    I      1   I       I    I   0     I    0    I       0    I   1     I
                                            I        I          I            I         I         I            I         I
                         Levell                                                        I         I
                                                                I                      I         I
                                                                                       I         I

                                                                                                                             ...
                                                                I
                                                                I                      I         I
                                                                I                      I         I
                         Levell
                                            I        I          I            I         I             I        I
                                            I        I          I            I         I             I        I
                                                                                                                       I s         Tim e
                                            I        I          I            I         I             I        I


                      a. A digital signal with two levels


                             Amplitude
                                                                    I 6 b"Its sent III
                                                                                   "1 s,
                                                                     Bit rate = 16 bps

                                      II   I    10   I   01     [     01    I    00         00   [       00   I   10    I
                                                     I          I           I                    I            I         I
                                           ,I
                        Lev el4                      I          I           I                    I            I         I


                        Level3             I         I
                                                     I
                                                                I
                                                                I
                                                                [
                                                                            I
                                                                            I
                                                                            I
                                                                                                 I
                                                                                                 I
                                                                                                 I
                                                                                                              I
                                                                                                              I
                                                                                                                        I
                                                                                                                        I

                                           I                    I           I                    [
                                                                                                                       I ...
                                            I                   I           I                    I
                                            I                   I           I                    I
                                                                                                                       I s         Tim e
                        Lev ell             I                                                    I


                        Levell
                                            I
                                            I
                                            I
                                                     I
                                                     I
                                                     I
                                                                [
                                                                [
                                                                I
                                                                            I                    [
                                                                                                 I

                                            [        I          I            I                   I            I


                      b. A digital signal with four levels


                  We send 1 bit per level in part a of the figure and 2 bits per level in part b of the
             figure. In general, if a signal has L levels, each level needs log2L bits.

                    Appendix C reviews information about exponential and logarithmic functions.


             Example 3.16
             A digital signal has eight levels. How many bits are needed per level? We calculate the number
             of bits from the formula

                                                 Number of bits per level                  =log2 8 =3
             Each signal level is represented by 3 bits.

             Example 3.17
             A digital signal has nine levels. How many bits are needed per level? We calculate the number of
             bits by using the formula. Each signal level is represented by 3.17 bits. However, this answer is
             not realistic. The number of bits sent per level needs to be an integer as well as a power of 2. For
             this example, 4 bits can represent one level.

## SECTION 3.3      DIGITAL SIGNALS          73


Bit Rate
Most digital signals are nonperiodic, and thus period and frequency are not appropri-
ate characteristics. Another term-bit rate (instead ofjrequency)-is used to describe
digital signals. The bit rate is the number of bits sent in Is, expressed in bits per
second (bps). Figure 3.16 shows the bit rate for two signals.

Example 3.18
Assume we need to download text documents at the rate of 100 pages per minute. What is the
required bit rate of the channel?

Solution
A page is an average of 24 lines with 80 characters in each line. If we assume that one character
requires 8 bits, the bit rate is

                        100 x 24 x 80 x 8 =1,636,000 bps =1.636 Mbps

Example 3.19
A digitized voice channel, as we will see in Chapter 4, is made by digitizing a 4-kHz bandwidth
analog voice signal. We need to sample the signal at twice the highest frequency (two samples
per hertz). We assume that each sample requires 8 bits. What is the required bit rate?

Solution
The bit rate can be calculated as

                              2 x 4000 x 8 =64,000 bps =64 kbps


Example 3.20
What is the bit rate for high-definition TV (HDTV)?

Solution
HDTV uses digital signals to broadcast high quality video signals. The HDTV Screen is normally
a ratio of 16 : 9 (in contrast to 4 : 3 for regular TV), which means the screen is wider. There are
1920 by 1080 pixels per screen, and the screen is renewed 30 times per second. Twenty-four bits
represents one color pixel. We can calculate the bit rate as

                       1920 x 1080 x 30 x 24 = 1,492,992,000 or 1.5 Gbps

The TV stations reduce this rate to 20 to 40 Mbps through compression.


Bit Length
We discussed the concept of the wavelength for an analog signal: the distance one cycle
occupies on the transmission medium. We can define something similar for a digital
signal: the bit length. The bit length is the distance one bit occupies on the transmis-
sion medium.

                         Bit length =propagation speed x bit duration

74   CHAPTER 3     DATA AND SIGNALS


             Digital Signal as a Composite Analog Signal
             Based on Fourier analysis, a digital signal is a composite analog signal. The bandwidth
             is infinite, as you may have guessed. We can intuitively corne up with this concept when
             we consider a digital signal. A digital signal, in the time domain, comprises connected
             vertical and horizontal line segments. A vertical line in the time domain means a fre-
             quency of infinity (sudden change in time); a horizontal line in the time domain means a
             frequency of zero (no change in time). Going from a frequency of zero to a frequency of
             infinity (and vice versa) implies all frequencies in between are part of the domain.
                   Fourier analysis can be used to decompose a digital signal. If the digital signal is
             periodic, which is rare in data communications, the decomposed signal has a frequency-
             domain representation with an infinite bandwidth and discrete frequencies. If the digital
             signal is nonperiodic, the decomposed signal still has an infinite bandwidth, but the fre-
             quencies are continuous. Figure 3.17 shows a periodic and a nonperiodic digital signal
             and their bandwidths.

                 Figure 3.17 The time andfrequency domains ofperiodic and nonperiodic digital signals
                                                                                                 ---- - - - - - - - - - - - -


                    -            .---          .---


                                                             ...
                                                               Time
                                                                      Lu
                                                                      /      3/   5f
                                                                                       I
                                                                                       7f
                                                                                            I
                                                                                            9f
                                                                                                     I
                                                                                                   Ilf
                                                                                                          I
                                                                                                         I3f
                                                                                                               ... ..
                                                                                                                 Frequency


                          '---          '---          '---

                  a. Time and frequency domains of perIodic digital signal


                    b~) ~~~-----=------+-.                     Time   o                                          Frequency

                  b. Time and frequency domains of nonperiodic digital signal


                      Note that both bandwidths are infinite, but the periodic signal has discrete frequen-
                 cies while the nonperiodic signal has continuous frequencies.

                 Transmission of Digital Signals
                 The previous discussion asserts that a digital signal, periodic or nonperiodic, is a com-
                 posite analog signal with frequencies between zero and infinity. For the remainder of
                 the discussion, let us consider the case of a nonperiodic digital signal, similar to the
                 ones we encounter in data communications. The fundamental question is, How can we
                 send a digital signal from point A to point B? We can transmit a digital signal by using
                 one of two different approaches: baseband transmission or broadband transmission
                 (using modulation).

## SECTION 3.3   DIGITAL SIGNALS   75


Baseband Transmission
Baseband transmission means sending a digital signal over a channel without changing
the digital signal to an analog signal. Figure 3.18 shows baseband transmission.


Figure 3.18 Baseband transmission


                                   -----D                         •
                                            Digital signal

                                 &i;;~;;;;_;;;~
                                              Channel
                                                                           a
            A digital signal is a composite analog signal with an infinite bandwidth.

    Baseband transmission requires that we have a low-pass channel, a channel with a
bandwidth that starts from zero. This is the case if we have a dedicated medium with a
bandwidth constituting only one channel. For example, the entire bandwidth of a cable
connecting two computers is one single channel. As another example, we may connect
several computers to a bus, but not allow more than two stations to communicate at a
time. Again we have a low-pass channel, and we can use it for baseband communication.
Figure 3.19 shows two low-pass channels: one with a narrow bandwidth and the other
with a wide bandwidth. We need to remember that a low-pass channel with infinite band-
width is ideal, but we cannot have such a channel in real life. However, we can get close.


Figure 3.19 Bandwidths of two low-pass channels


        o
   a. Low-pass channel, wide bandwidth


        o
   b. Low-pass channel, narrow bandwidth


    Let us study two cases of a baseband communication: a low-pass channel with a
wide bandwidth and one with a limited bandwidth.

76   CHAPTER 3     DATA AND SIGNALS


             Case 1: Low-Pass Channel with Wide Bandwidth
             If we want to preserve the exact form of a nonperiodic digital signal with vertical seg-
             ments vertical and horizontal segments horizontal, we need to send the entire spectrum,
             the continuous range of frequencies between zero and infinity. This is possible if we
             have a dedicated medium with an infinite bandwidth between the sender and receiver
             that preserves the exact amplitude of each component of the composite signal.
             Although this may be possible inside a computer (e.g., between CPU and memory), it
             is not possible between two devices. Fortunately, the amplitudes of the frequencies at
             the border of the bandwidth are so small that they can be ignored. This means that if we
             have a medium, such as a coaxial cable or fiber optic, with a very wide bandwidth, two
             stations can communicate by using digital signals with very good accuracy, as shown in
             Figure 3.20. Note that!i is close to zero, andh is very high.


             Figure 3.20         Baseband transmission using a dedicated medium

                        Input signal bandwidth


                    ,<::;S>:,:, ,... -, :.">~            ~.~:~' ... '-.;:.~
                                                      Jw_,
                                                            '" ,,"
                                                                     ,",
                                                                           "
                                                                            L
                                                    Bandwidth supported by medium    Output signal bandwidth


                                                                                    _C c:~::.:.~.•.•.. c<l
                    o                                                                 II                   h


                             Input signal               Wide-bandwidth channel             Output signal


                  Although the output signal is not an exact replica of the original signal, the data
             can still be deduced from the received signal. Note that although some of the frequen-
             cies are blocked by the medium, they are not critical.


                  Baseband transmission of a digital signal that preserves the shape of the digital signal is
                   possible only if we have a low-pass channel with an infinite or very wide bandwidth.


                 Example 3.21
             An example of a dedicated channel where the entire bandwidth of the medium is used as one single
             channel is a LAN. Almost every wired LAN today uses a dedicated channel for two stations com-
             municating with each other. In a bus topology LAN with multipoint connections, only two stations
             can communicate with each other at each moment in time (timesharing); the other stations need to
             refrain from sending data. In a star topology LAN, the entire channel between each station and the
             hub is used for communication between these two entities. We study LANs in Chapter 14.

                 Case 2: Low-Pass Channel with Limited Bandwidth
                 In a low-pass channel with limited bandwidth, we approximate the digital signal with
                 an analog signal. The level of approximation depends on the bandwidth available.
                 Rough Approximation Let us assume that we have a digital signal of bit rate N. If we
                 want to send analog signals to roughly simulate this signal, we need to consider the worst
                 case, a maximum number of changes in the digital signal. This happens when the signal

## SECTION 3.3                             DIGITAL SIGNALS                     77


carries the sequence 01010101 ... or the sequence 10101010· ... To simulate these two
cases, we need an analog signal of frequency f = N12. Let 1 be the positive peak value and
o be the negative peak value. We send 2 bits in each cycle; the frequency of the analog
signal is one-half of the bit rate, or N12. However, just this one frequency cannot make all
patterns; we need more components. The maximum frequency is NI2. As an example of
this concept, let us see how a digital signal with a 3-bit pattern can be simulated by using
analog signals. Figure 3.21 shows the idea. The two similar cases (000 and 111) are simu-
lated with a signal with frequency f = 0 and a phase of 180° for 000 and a phase of 0° for
111. The two worst cases (010 and 101) are simulated with an analog signal with fre-
quency f = NI2 and phases of 180° and 0°. The other four cases can only be simulated with
an analog signal with f = NI4 and phases of 180°, 270°, 90°, and 0°. In other words, we
need a channel that can handle frequencies 0, N14, and NI2. This rough approximation is
referred to as using the first harmonic (NI2) frequency. The required bandwidth is

                                               Bandwidth = lJ. - 0 = lJ.
                                                               2                    2


Figure 3.21 Rough approximation ofa digital signal using the first harmonic for worst case

                                     Amplitude

                                                 Bandwidth == ~


                                          o              N/4       N/2      Frequency

    Digital: bit rate N             Digital: bit rate N              Digital: bit rate N                          Digital: bit rate N


                                               o~
                                                                       ~
                                                                                                                    *
      1° 1         0   I   0 1       I   0 1
      I  1             I     1       I     1                          I                             I
      I
      ,
      I
         1
         1
              ,
                       I

                       !
                             1
                             !       :, :,       ,   ,
                                                                     -I--
                                                                      I
                                                                       J    I           I
                                                                                                    1
                                                                                                    I                ,I     ,     ,I
      1
      1
              1
              I
                       I
                       I
                       ., ,,
                             1
                             1
                                     I
                                     I
                                           I
                                           I     n
                                                 I   I                 1
                                                                       1

                                                                       MM
                                                                                {"'\j:                               I~
                                                                                                                     II I I
      i
      I
      ,
               i
              ,I
                       i     I
                                     ,~l
                                       , ,           .
                                                     I
                                                                       , , , ,                                       ,~~~
                                                                                                                       , , ,
  Analog:f = 0, p = 180          Analog:f==N/4,p= 180             Analog:j==N/2, p == 180                       Analog:j==N/4, p == 270

    Digital: bit rate N             Digital: bit rate N              Digital: bit rate N                           Digital: bit rate N

      1   I   I    o 101             I   1 I   o1 1I                   1

                                                                       : ,
                                                                           1 I 1
                                                                                            I   °       I
                                                                                                                     I    1 1 I   I    I   1


                                    -R=R-
                                                                                                                     i      i     I        i

     -A=±i
      :       •        ~     1
                                                                       1
                                                                       ,    ,
                                                                                I
                                                                                I
                                                                                        8-                           I
                                                                                                                     I
                                                                                                                     ,
                                                                                                                            I
                                                                                                                            1
                                                                                                                            ,
                                                                                                                                  I
                                                                                                                                  I
                                                                                                                                  ,
                                                                                                                                           I
                                                                                                                                           1
                                                                                                                                           ,
                                                                                                                                           ,
      1       I        I                                               I    I                           I                   !     1

                                     AA
                             I                                                          j                            I
                                                                       ~II                                           I      I     I        I
      ~
      ,1~
        , ,   .                      I
                                     ,, .
                                      M              ,
                                                     I                 :~N
                                                                       J, ,             J
                                                                                                                     I
                                                                                                                     ,
                                                                                                                     I
                                                                                                                            I
                                                                                                                            1
                                                                                                                            ,
                                                                                                                                  i
                                                                                                                                  I
                                                                                                                                  ,
                                                                                                                                           I
                                                                                                                                           ,I
  Analog:f=N/4, p = 90            Analog:j== N/2, P = 0            Analog:f=N/4,p== 0                             Analog: j == 0, p = 0


Better Approximation To make the shape of the analog signal look more like that
of a digital signal, we need to add more harmonics of the frequencies. We need to
increase the bandwidth. We can increase the bandwidth to 3N12, 5N12, 7NI2, and so on.
Figure 3.22 shows the effect of this increase for one of the worst cases, the pattern 010.

78   CHAPTER 3     DATA AND SIGNALS


             Figure 3.22 Simulating a digital signal with three first harmonics


                           Amplitude                                           5N
                                                                   Bandwidth = T


                              W_I
                              o N/4 NI2                      3N/4
                                                                                     I'--- I
                                                                                    3N12      5N/4
                                                                                                         1~..
                                                                                                         5N12   Frequency

                                       Digital: bit rate N                                    Analog:/= NI2 and 3N12


                                                                                               cf':U __
                               I
                                   0      I
                                                1    I
                                                         0     I                                     I
                               I                               I
                               I                               I
                               I                               I


                                                                                             .U~
                               I                               I
                               I                               I
                               I                               I
                                                               I
                                                     I                                               I
                               I          I


                                  v=s
                                          I                                                          I


                               .\2 :V     I


                                       Analog:! = N/2
                                                                                             f t~-
                                                                                             .~      1

                                                                                           Analog:!= N12, 3N12, and 5NI2


             Note that we have shown only the highest frequency for each hannonic. We use the first,
             third, and fifth hannonics. The required bandwidth is now 5NJ2, the difference between the
             lowest frequency 0 and the highest frequency 5NJ2. As we emphasized before, we need
             to remember that the required bandwidth is proportional to the bit rate.


                     In baseband transmission, the required bandwidth is proportional to the bit rate;
                                 if we need to send bits faster, we need more bandwidth.


                      By using this method, Table 3.2 shows how much bandwidth we need to send data
                 at different rates.

                          Table 3.2           Bandwidth requirements

                                    Bit                      Harmonic                 Harmonics            Harmonics
                                   Rate                         1                        1,3                1,3,5
                           n = 1 kbps                    B=500Hz                    B= 1.5 kHz           B=2.5 kHz
                           n = 10 kbps                   B=5 kHz                    B= 15kHz             B= 25 kHz
                           n = 100 kbps                  B= 50kHz                   B = 150 kHz          B= 250 kHz


             Example 3.22
                 What is the required bandwidth of a low-pass channel if we need to send 1 Mbps by using base-
                 band transmission?

## SECTION 3.3    DIGITAL SIGNALS          79


Solution
The answer depends on the accuracy desired.
    a. The minimum bandwidth, a rough approximation, is B =: bit rate /2, or 500 kHz. We need
       a low-pass channel with frequencies between 0 and 500 kHz.
    b. A better result can be achieved by using the first and the third harmonics with the required
       bandwidth B =: 3 x 500 kHz =: 1.5 MHz.
    c. Still a better result can be achieved by using the first, third, and fifth harmonics with
       B =: 5 x 500 kHz =0 2.5 MHz.

Example 3.23
We have a low-pass channel with bandwidth 100 kHz. What is the maximum bit rate of this
channel?

Solution
The maximum bit rate can be achieved if we use the first harmonic. The bit rate is 2 times the
available bandwidth, or 200 kbps.


Broadband Transmission (Using Modulation)
Broadband transmission or modulation means changing the digital signal to an analog
signal for transmission. Modulation allows us to use a bandpass channel-a channel with
a bandwidth that does not start from zero. This type of channel is more available than a
low-pass channel. Figure 3.23 shows a bandpass channel.


Figure 3.23     Bandwidth ofa bandpass channel

              Amplitude


                 1_~~.               Bandpass channel                       Frequency


     Note that a low-pass channel can be considered a bandpass channel with the lower
frequency starting at zero.
     Figure 3.24 shows the modulation of a digital signal. In the figure, a digital signal is
converted to a composite analog signal. We have used a single-frequency analog signal
(called a carrier); the amplitude of the carrier has been changed to look like the digital
signal. The result, however, is not a single-frequency signal; it is a composite signal, as
we will see in Chapter 5. At the receiver, the received analog signal is converted to digital,
and the result is a replica of what has been sent.


  If the available channel is a bandpass channel~ we cannot send the digital signal directly to
  the channel; we need to convert the digital signal to an analog signal before transmission.

80   CHAPTER 3     DATA AND SIGNALS


             Figure 3.24 Modulation ofa digital signal for transmission on a bandpass channel

                         0                              _                                                 D'--                       ~.
                             Input digi tal signal                                                           Output digital signal


                                                     DigitaUanalog                         Analog/digital
                                                     converter                                 con verter t--~'>'''''''--


                       Input analog signal bandwidth                 Available bandwidth              Output analog signal bandwidth
                                                                                                              /       -,>:~,;:>~

                             L           "

                                                                      Bandpass channel
                         -   - I

                             Input analog signal                                                              Input analog signal


             Example 3.24
             An example of broadband transmission using modulation is the sending of computer data through
             a telephone subscriber line, the line connecting a resident to the central telephone office. These
             lines, installed many years ago, are designed to carry voice (analog signal) with a limited band-
             width (frequencies between 0 and 4 kHz). Although this channel can be used as a low-pass chan-
             nel, it is normally considered a bandpass channel. One reason is that the bandwidth is so narrow
             (4 kHz) that if we treat the channel as low-pass and use it for baseband transmission, the maximum
             bit rate can be only 8 kbps. The solution is to consider the channel a bandpass channel, convert the
             digital signal from the computer to an analog signal, and send the analog signal. We can install two
             converters to change the digital signal to analog and vice versa at the receiving end. The converter,
             in this case, is called a modem (modulator/demodulator), which we discuss in detail in Chapter 5.

             Example 3.25
             A second example is the digital cellular telephone. For better reception, digital cellular phones
             convert the analog voice signal to a digital signal (see Chapter 16). Although the bandwidth allo-
             cated to a company providing digital cellular phone service is very wide, we still cannot send the
             digital signal without conversion. The reason is that we only have a bandpass channel available
             between caller and callee. For example, if the available bandwidth is Wand we allow lOOO cou-
             ples to talk simultaneously, this means the available channel is WIlOOO, just part of the entire
             bandwidth. We need to convert the digitized voice to a composite analog signal before sending.
             The digital cellular phones convert the analog audio signal to digital and then convert it again to
             analog for transmission over a bandpass channel.


## 3.4     TRANSMISSION IMPAIRMENT
                 Signals travel through transmission media, which are not petfect. The impetfection causes
                 signal impairment. This means that the signal at the beginning of the medium is not the
                 same as the signal at the end of the medium. What is sent is not what is received. Three
                 causes of impairment are attenuation, distortion, and noise (see Figure 3.25).

## SECTION 3.4           TRANSMISSION IMPAIRMENT     81


Figure 3.25    Causes of impairment


Attenuation
Attenuation means a loss of energy. When a signal, simple or composite, travels
through a medium, it loses some of its energy in overcoming the resistance of the
medium. That is why a wire carrying electric signals gets warm, if not hot, after a
while. Some of the electrical energy in the signal is converted to heat. To compensate
for this loss, amplifiers are used to amplify the signal. Figure 3.26 shows the effect of
attenuation and amplification.


Figure 3.26 Attenuation

               Original                         Attenuated             Amplified


                                                                      -Affi
                Point 1   Transmission medium     Point 2                Point 3


Decibel
To show that a signal has lost or gained strength, engineers use the unit of the decibel.
The decibel (dB) measures the relative strengths of two signals or one signal at two dif-
ferent points. Note that the decibel is negative if a signal is attenuated and positive if a
signal is amplified.


Variables PI and P 2 are the powers of a signal at points 1 and 2, respectively. Note that
some engineering books define the decibel in terms of voltage instead of power. In this
case, because power is proportional to the square of the voltage, the formula is dB =
20 log 10 (V2IV1). In this text, we express dB in terms of power.

82   CHAPTER 3     DATA AND SIGNALS


             Example 3.26
             Suppose a signal travels through a transmission medium and its power is reduced to one-half.
             This means that P 2 = ~ PI' In this case, the attenuation (loss of power) can be calculated as


                                    1010glO - z = 1010gl0 - - = 10 Iogl o 0.5 = 10(-0.3) = -3 dB
                                             P                  0.5PI
                                             PI                  PI


             A loss of 3 dB (-3 dB) is equivalent to losing one-half the power.

             Example 3.27
             A signal travels through an amplifier, and its power is increased 10 times. This means that Pz =
             1OP I' In this case, the amplification (gain of power) can be calculated as


             Example 3.28
             One reason that engineers use the decibel to measure the changes in the strength of a signal is that
             decibel numbers can be added (or subtracted) when we are measuring several points (cascading)
             instead of just two. In Figure 3.27 a signal travels from point 1 to point 4. The signal is attenuated
             by the time it reaches point 2. Between points 2 and 3, the signal is amplified. Again, between
             points 3 and 4, the signal is attenuated. We can find the resultant decibel value for the signal just
             by adding the decibel measurements between each set of points.


             Figure 3.27            Decibels for Example 3.28

                                                                        I dB

                                            dB _ _• •
                             1 _ :_---'--'-=-.3                         7dB                 -3 dB
                                                         1
                                                                 ----'----
                                                                                 'I'                      :1

                          Point 1      Transmission   Point 2                  Point 3   Transmission   Point 4
                                         medium                                            medium


                      In this case, the decibel value can be calculated as

                                                             dB=-3+7-3=+1

             The signal has gained in power.

             Example 3.29
                 Sometimes the decibel is used to measure signal power in milliwatts. In this case, it is referred to
                 as dB m and is calculated as dB m = 10 loglO Pm' where Pm is the power in milliwatts. Calculate
                 the power of a signal if its dB m = -30.

## SECTION 3.4    TRANSMISSION IMPAIRMENT                83


Solution
We can calculate the power in the signal as

                                            dB m = 10 log 10 Pm = -30
                                       loglO Pm := -3      Pm = 10-3 rnW


Example 3.30
The loss in a cable is usually defined in decibels per kilometer (dB/km). If the signal at the
beginning of a cable with -0.3 dBlkm has a power of 2 mW, what is the power of the signal
at 5 km?

Solution
The loss in the cable in decibels is 5 x (-0.3)::: -1.5 dB. We can calculate the power as


Distortion
Distortion means that the signal changes its form or shape. Distortion can occur in a
composite signal made of different frequencies. Each signal component has its own
propagation speed (see the next section) through a medium and, therefore, its own
delay in arriving at the final destination. Differences in delay may create a difference in
phase if the delay is not exactly the same as the period duration. In other words, signal
components at the receiver have phases different from what they had at the sender. The
shape of the composite signal is therefore not the same. Figure 3.28 shows the effect of
distortion on a composite signal.


Figure 3.28       Distortion


           Composite signal                                                        Composite signal
               sent                                                                   received


                                       Components,            Components,
                                         in phase             out of phase

                       At the sender                                     At the receiver

84   CHAPTER 3     DATA AND SIGNALS


             Noise
             Noise is another cause of impairment. Several types of noise, such as thermal noise,
             induced noise, crosstalk, and impulse noise, may corrupt the signal. Thermal noise is
             the random motion of electrons in a wire which creates an extra signal not originally
             sent by the transmitter. Induced noise comes from sources such as motors and appli-
             ances. These devices act as a sending antenna, and the transmission medium acts as the
             receiving antenna. Crosstalk is the effect of one wire on the other. One wire acts as a
             sending antenna and the other as the receiving antenna. Impulse noise is a spike (a sig-
             nal with high energy in a very short time) that comes from power lines, lightning, and so
             on. Figure 3.29 shows the effect of noise on a signal. We discuss error in Chapter 10.


             Figure 3.29        Noise

                                Transmitted                   Noise


                                     I                                                    I
                                     I                                                    I
                                                                                          I

                                                                                         •
                                     I


                                    •
                                  Point 1              Transmission medium             Point 2


             Signal-to-Noise Ratio (SNR)
             As we will see later, to find the theoretical bit rate limit, we need to know the ratio of
             the signal power to the noise power. The signal-to-noise ratio is defined as

                                                      =
                                                 SNR average signal power
                                                     average noise power


                 We need to consider the average signal power and the average noise power because
             these may change with time. Figure 3.30 shows the idea of SNR.
                  SNR is actually the ratio of what is wanted (signal) to what is not wanted (noise).
             A high SNR means the signal is less corrupted by noise; a low SNR means the signal is
             more corrupted by noise.
                  Because SNR is the ratio of two powers, it is often described in decibel units,
             SNRdB , defined as


                                                    SNRcm = lOloglo SNR


                 Example 3.31
                 The power of a signal is 10 mW and the power of the noise is 1 /lW; what are the values of SNR
                 and SNRdB ?

## SECTION 3.5   DATA RATE LIMITS   85


Figure 3.30         Two cases of SNR: a high SNR and a low SNR


                        Signal                       Noise
                -


             a. Large SNR


                                                     Noise              Signal + noise


             b. Small SNR


Solution
The values of SNR and SN~B can be calculated as follows:


                                   SNR = 10.000 flW = 10 000
                                              ImW           '
                             SNRdB = 10 loglO 10,000 = 10 loglO 104 = 40


Example 3.32
The values of SNR and SNRdB for a noiseless channel are


                                       SNR   = signal power =    <>0

                                                      o
                                       SNRdB = 10 loglO 00 = <>0


      We can never achieve this ratio in real life; it is an ideal.


## 3.5       DATA RATE LIMITS
A very important consideration in data communications is how fast we can send data, in
bits per second. over a channel. Data rate depends on three factors:
 1. The bandwidth available
 2. The level of the signals we use
 3. The quality of the channel (the level of noise)
Two theoretical formulas were developed to calculate the data rate: one by Nyquist for
a noiseless channel. another by Shannon for a noisy channel.

86   CHAPTER 3     DATA AND SIGNALS


             Noiseless Channel: Nyquist Bit Rate
             For a noiseless channel, the Nyquist bit rate formula defines the theoretical maximum
             bit rate

                                                BitRate = 2 x bandwidth x 10g2 L


             In this formula, bandwidth is the bandwidth of the channel, L is the number of signal
             levels used to represent data, and BitRate is the bit rate in bits per second.
                  According to the formula, we might think that, given a specific bandwidth, we can
             have any bit rate we want by increasing the number of signa11eve1s. Although the idea
             is theoretically correct, practically there is a limit. When we increase the number of sig-
             nal1eve1s, we impose a burden on the receiver. If the number of levels in a signal is just 2,
             the receiver can easily distinguish between a 0 and a 1. If the level of a signal is 64, the
             receiver must be very sophisticated to distinguish between 64 different levels. In other
             words, increasing the levels of a signal reduces the reliability of the system.

                           Increasing the levels of a signal may reduce the reliability of the system.


             Example 3.33
             Does the Nyquist theorem bit rate agree with the intuitive bit rate described in baseband
             transmission?

             Solution
             They match when we have only two levels. We said, in baseband transmission, the bit rate is 2
             times the bandwidth if we use only the first harmonic in the worst case. However, the Nyquist
             formula is more general than what we derived intuitively; it can be applied to baseband transmis-
             sion and modulation. Also, it can be applied when we have two or more levels of signals.


             Example 3.34
             Consider a noiseless channel with a bandwidth of 3000 Hz transmitting a signal with two signal
             levels. The maximum bit rate can be calculated as

                                             BitRate =2 x 3000 x log2 2 = 6000 bps


                 Example 3.35
                 Consider the same noiseless channel transmitting a signal with four signal levels (for each level,
                 we send 2 bits). The maximum bit rate can be calculated as

                                             BitRate   =2 x 3000 X log2 4 = 12,000 bps

                 Example 3.36
                 We need to send 265 kbps over a noiseless channel with a bandwidth of 20 kHz. How many sig-
                 nallevels do we need?

## SECTION 3.5       DATA RATE LIMITS          87


Solution
We can use the Nyquist formula as shown:


                                  265,000 =2 X 20,000 X logz L
                            log2 L = 6.625   L =2 6.625 = 98.7 levels

Since this result is not a power of 2, we need to either increase the number of levels or reduce
the bit rate. If we have 128 levels, the bit rate is 280 kbps. If we have 64 levels, the bit rate is
240 kbps.


Noisy Channel: Shannon Capacity
In reality, we cannot have a noiseless channel; the channel is always noisy. In 1944,
Claude Shannon introduced a formula, called the Shannon capacity, to determine the
theoretical highest data rate for a noisy channel:

                             Capacity = bandwidth X log2 (1 + SNR)

     In this formula, bandwidth is the bandwidth of the channel, SNR is the signal-to-
noise ratio, and capacity is the capacity of the channel in bits per second. Note that in the
Shannon formula there is no indication of the signal level, which means that no matter
how many levels we have, we cannot achieve a data rate higher than the capacity of the
channel. In other words, the formula defines a characteristic of the channel, not the method
of transmission.

Example 3.37
Consider an extremely noisy channel in which the value of the signal-to-noise ratio is almost
zero. In other words, the noise is so strong that the signal is faint. For this channel the capacity C
is calculated as


                   C =B log2 (1 + SNR) =B 10gz (l + 0) = B log2 1 ::;;: B x 0 :;;;; 0

    This means that the capacity of this channel is zero regardless of the bandwidth. In other
words, we cannot receive any data through this channel.

Example 3.38
We can calculate the theoretical highest bit rate of a regular telephone line. A telephone line nor-
mally has a bandwidth of 3000 Hz (300 to 3300 Hz) assigned for data communications. The sig-
nal-to-noise ratio is usually 3162. For this channel the capacity is calculated as

                 C = B log2 (1 + SNR) = 3000 log2 (l + 3162) = 3000 log2 3163
                                  :::::: 3000 x 11.62 = 34,860 bps

     This means that the highest bit rate for a telephone line is 34.860 kbps. If we want to send
data faster than this, we can either increase the bandwidth of the line or improve the signal-to-
noise ratio.

88   CHAPTER 3     DATA AND SIGNALS


             Example 3.39
             The signal-to-noise ratio is often given in decibels. Assume that SN~B = 36 and the channel
             bandwidth is 2 MHz. The theoretical channel capacity can be calculated as


                        SNRdB = 10 loglO SNR . . .    SNR = lOSNRoB/10     ...    SNR::; 10 3.6 = 3981
                                   C =B log2 (1+ SNR) = 2 X 106 X log2 3982 = 24 Mbps


             Example 3.40
             For practical purposes, when the SNR is very high, we can assume that SNR + I is almost the
             same as SNR. In these cases, the theoretical channel capacity can be simplified to


                                                              SNR dB
                                                      C=BX - - =
                                                                 3

             For example, we can calculate the theoretical capacity of the previous example as


                                                           36
                                                C= 2 MHz X - =24 Mbps
                                                            3


             Using Both Limits
             In practice, we need to use both methods to find the limits and signal levels. Let us show
             this with an example.

             Example 3.41
             We have a channel with a I-MHz bandwidth. The SNR for this channel is 63. What are the appro-
             priate bit rate and signal level?
             Solution
             First, we use the Shannon formula to find the upper limit.


                               C =B log2 (l + SNR) = 106 log2 (1 + 63) = 106 10g2 64 = 6 Mbps


                      The Shannon formula gives us 6 Mbps, the upper limit. For better performance we choose
                 something lower, 4 Mbps, for example. Then we use the Nyquist formula to find the number of
                 signal levels.


                                         4Mbps=2x 1 MHz x log2 L          ...    L=4


                                      The Shannon capacity gives us the upper limit;
                                the Nyquist formula tells us how many signal levels we need.

## SECTION 3.6       PERFORMANCE             89


## 3.6      PERFORMANCE
Up to now, we have discussed the tools of transmitting data (signals) over a network
and how the data behave. One important issue in networking is the performance of the
network-how good is it? We discuss quality of service, an overall measurement of
network performance, in greater detail in Chapter 24. In this section, we introduce
terms that we need for future chapters.

Bandwidth
One characteristic that measures network performance is bandwidth. However, the term
can be used in two different contexts with two different measuring values: bandwidth in
hertz and bandwidth in bits per second.

Bandwidth in Hertz
We have discussed this concept. Bandwidth in hertz is the range of frequencies con-
tained in a composite signal or the range of frequencies a channel can pass. For exam-
ple, we can say the bandwidth of a subscriber telephone line is 4 kHz.

Bandwidth in Bits per Seconds
The term bandwidth can also refer to the number of bits per second that a channel, a
link, or even a network can transmit. For example, one can say the bandwidth of a Fast
Ethernet network (or the links in this network) is a maximum of 100 Mbps. This means
that this network can send 100 Mbps.

Relationship
There is an explicit relationship between the bandwidth in hertz and bandwidth in bits
per seconds. Basically, an increase in bandwidth in hertz means an increase in bandwidth
in bits per second. The relationship depends on whether we have baseband transmission
or transmission with modulation. We discuss this relationship in Chapters 4 and 5.

  In networking, we use the term bandwidth in two contexts.

  o The first, bandwidth in hertz, refers to the range of frequencies in a composite
       signal or the range of frequencies that a channel can pass.
  o    The second, bandwidth in bits per second, refers to the speed of bit transmis-
       sion in a channel or link.


Example 3.42
The bandwidth of a subscriber line is 4 kHz for voice or data. The bandwidth of this line for data trans-
mission can be up to 56,000 bps using a sophisticated modem to change the digital signal to analog.

Example 3.43
If the telephone company improves the quality of the line and increases the bandwidth to 8 kHz,
we can send 112,000 bps by using the same technology as mentioned in Example 3.42.

90   CHAPTER 3     DATA AND SIGNALS


             Throughput
             The throughput is a measure of how fast we can actually send data through a network.
             Although, at first glance, bandwidth in bits per second and throughput seem the same,
             they are different. A link may have a bandwidth of B bps, but we can only send T bps
             through this link with T always less than B. In other words, the bandwidth is a potential
             measurement of a link; the throughput is an actual measurement of how fast we can
             send data. For example, we may have a link with a bandwidth of 1 Mbps, but the
             devices connected to the end of the link may handle only 200 kbps. This means that we
             cannot send more than 200 kbps through this link.
                  Imagine a highway designed to transmit 1000 cars per minute from one point
             to another. However, if there is congestion on the road, this figure may be reduced to
             100 cars per minute. The bandwidth is 1000 cars per minute; the throughput is 100 cars
             per minute.

             Example 3.44
             A network with bandwidth of 10 Mbps can pass only an average of 12,000 frames per minute
             with each frame carrying an average of 10,000 bits. What is the throughput of this network?

             Solution
             We can calculate the throughput as


                                         Throughput = 12,000 x 10,000 = 2 Mbps
                                                               60

             The throughput is almost one-fifth of the bandwidth in this case.


                 Latency (Delay)
             The latency or delay defines how long it takes for an entire message to completely
             arrive at the destination from the time the first bit is sent out from the source. We can
             say that latency is made of four components: propagation time, transmission time,
             queuing time and processing delay.

                     Latency = propagation time + transmission time + queuing time + processing delay

                 Propagation Time
                 Propagation time measures the time required for a bit to travel from the source to the
                 destination. The propagation time is calculated by dividing the distance by the propaga-
                 tion speed.

                                          Propagation time =       Dist:mce
                                                               Propagation speed

                      The propagation speed of electromagnetic signals depends on the medium and on
                 the frequency of the signaL For example, in a vacuum, light is propagated with a speed
                 of 3 x 108 mfs. It is lower in air; it is much lower in cable.

## SECTION 3.6      PERFORMANCE           91


Example 3.45
What is the propagation time if the distance between the two points is 12,000 km? Assume the
propagation speed to be 2.4 x 10 8 mls in cable.
Solution
We can calculate the propagation time as

                                 ..        12000 x 1000
                         Propagation tIme = '
                                                     8
                                                        =50 ms
## 2.4 x 10

The example shows that a bit can go over the Atlantic Ocean in only 50 ms if there is a direct
cable between the source and the destination.

Tra/lsmissio/l Time
In data communications we don't send just 1 bit, we send a message. The first bit may
take a time equal to the propagation time to reach its destination; the last bit also may
take the same amount of time. However, there is a time between the first bit leaving the
sender and the last bit arriving at the receiver. The first bit leaves earlier and arrives ear-
lier; the last bit leaves later and arrives later. The time required for transmission of a
message depends on the size of the message and the bandwidth of the channel.


                             Transmission time = Message size
                                                 Bandwidth


Example 3.46
What are the propagation time and the transmission time for a 2.5-kbyte message (an e-mail) if
the bandwidth of the network is 1 Gbps? Assume that the distance between the sender and the
receiver is 12,000 km and that light travels at 2.4 x 108 mls.

Solution
We can calculate the propagation and transmission time as

                                  ..       12000 x 1000
                          PropagatIon Hme = ~.4 x 108   = 50 ms
                                 ...
                        TranSIlllSSlOn tIme = 2500 9x 8 =.
                                                         0 020 ms
                                                10

Note that in this case, because the message is short and the bandwidth is high, the
dominant factor is the propagation time, not the transmission time. The transmission
time can be ignored.

Example 3.47
What are the propagation time and the transmission time for a 5-Mbyte message (an image) if the
bandwidth of the network is 1 Mbps? Assume that the distance between the sender and the
receiver is 12,000 km and that light travels at 2.4 x 10 8 mls.

92   CHAPTER 3   DATA AND SIGNALS


             Solution
             We can calculate the propagation and transmission times as

                                                  .,         12 000 X 1000
                                          PropagatIon tIme ::::'       8:::: 50 ms
                                                               2.4x 10
                                             ..      .       5,000,000 x 8 40
                                     TranSffilSSlOn tIme::::        6     :::: S
                                                                  10

             Note that in this case, because the message is very long and the bandwidth is not very
             high, the dominant factor is the transmission time, not the propagation time. The propa-
             gation time can be ignored.

             Queuing Time
             The third component in latency is the queuing time, the time needed for each interme-
             diate or end device to hold the message before it can be processed. The queuing time is
             not a fixed factor; it changes with the load imposed on the network. When there is
             heavy traffic on the network, the queuing time increases. An intermediate device, such
             as a router, queues the arrived messages and processes them one by one. If there are
             many messages, each message will have to wait.


             Bandwidth-Delay Product
             Bandwidth and delay are two performance metrics of a link. However, as we will see in
             this chapter and future chapters, what is very important in data communications is the
             product of the two, the bandwidth-delay product. Let us elaborate on this issue, using
             two hypothetical cases as examples.
             o Case 1. Figure 3.31 shows case 1.
             Figure 3.31    Filling the link with bits for case 1

                                 Sender                                                       Receiver

                                                 Bandwidth: 1 bps   Delay: 5 s
                                                      Bandwidth x delay = 5 bits
                                                                                                 _...

                                                                1st bit            ~


                                                                                       1st bit

                                           1s                                            1s


                  Let US assume that we have a link with a bandwidth of 1 bps (unrealistic, but good
                  for demonstration purposes). We also assume that the delay of the link is 5 s (also
                  unrealistic). We want to see what the bandwidth-delay product means in this case.

## SECTION 3.6      PERFORMANCE    93


    Looking at figure, we can say that this product 1 x 5 is the maximum number of
    bits that can fill the link. There can be no more than 5 bits at any time on the link.
o   Case 2. Now assume we have a bandwidth of 4 bps. Figure 3.32 shows that there
    can be maximum 4 x 5 = 20 bits on the line. The reason is that, at each second,
    there are 4 bits on the line; the duration of each bit is 0.25 s.


Figure 3.32 Filling the link with bits in case 2

                                                                                              Receiver
                                                                                                r
                                               Bandwidth: 4 bps        Delay: 5 s
                                                      Bandwidth x delay = 20 bits


               After 1 s
                           I---'-----'----.l..-.L-l

               After 2 s


               After 4 s


                                     1s               1s          1s          1s         1s


      The above two cases show that the product of bandwidth and delay is the number of
bits that can fill the link. This measurement is important if we need to send data in bursts
and wait for the acknowledgment of each burst before sending the next one. To use the
maximum capability of the link, we need to make the size of our burst 2 times the product
of bandwidth and delay; we need to fill up the full-duplex channel (two directions). The
sender should send a burst of data of (2 x bandwidth x delay) bits. The sender then waits
for receiver acknowledgment for part of the burst before sending another burst. The
amount 2 x bandwidth x delay is the number of bits that can be in transition at any time.


       The bandwidth~delay product defines the number of bits that can rdl the link.


Example 3.48
We can think about the link between two points as a pipe. The cross section of the pipe represents
the bandwidth, and the length of the pipe represents the delay. We can say the volume of the pipe
defines the bandwidth-delay product, as shown in Figure 3.33.


Figure 3.33 Concept of bandwidth-delay product

                                                                         Length: delay

                   Cross section: bandwidth

94   CHAPTER 3   DATA AND SIGNALS


             Jitter
             Another performance issue that is related to delay is jitter. We can roughly say that jitter
             is a problem if different packets of data encounter different delays and the application
             using the data at the receiver site is time-sensitive (audio and video data, for example).
             If the delay for the first packet is 20 ms, for the second is 45 ms, and for the third is
             40 ms, then the real-time application that uses the packets endures jitter. We discuss jitter
             in greater detail in Chapter 29.


## 3.7      RECOMMENDED READING
             For more details about subjects discussed in this chapter, we recommend the following
             books. The items in brackets [...] refer to the reference list at the end of the text.


             Books
             Data and signals are elegantly discussed in Chapters 1 to 6 of [Pea92]. [CouOl] gives
             an excellent coverage about signals in Chapter 2. More advanced materials can be
             found in [Ber96]. [Hsu03] gives a good mathematical approach to signaling. Complete
             coverage of Fourier Analysis can be found in [Spi74]. Data and signals are discussed in
## Chapter 3 of [Sta04] and Section 2.1 of [Tan03].


## 3.8      KEY TERMS
             analog                                           Fourier analysis
             analog data                                      frequency
             analog signal                                    frequency-domain
             attenuation                                      fundamental frequency
             bandpass channel                                 harmonic
             bandwidth                                        Hertz (Hz)
             baseband transmission                            jitter
             bit rate                                         low-pass channel
             bits per second (bps)                            noise
             broadband transmission                           nonperiodic signal
             composite signal                                 Nyquist bit rate
             cycle                                            peak amplitude
             decibel (dB)                                     period
             digital                                          periodic signal
             digital data                                     phase
             digital signal                                   processing delay
             distortion                                       propagation speed

## SECTION 3.9    SUMMARY        95


propagation time                                sine wave
queuing time                                    throughput
Shannon capacity                                time-domain
signal                                          transmission time
signal-to-noise ratio (SNR)                     wavelength


## 3.9      SUMMARY
o Data must be transformed to electromagnetic signals to be transmitted.
o Data can be analog or digital. Analog data are continuous and take continuous
      values. Digital data have discrete states and take discrete values.
o     Signals can be analog or digital. Analog signals can have an infinite number of
      values in a range; digital ,signals can have only a limited number of values.
o     In data communications, we commonly use periodic analog signals and nonperi-
      odic digital signals.
o     Frequency and period are the inverse of each other.
o     Frequency is the rate of change with respect to time.
o     Phase describes the position of the waveform relative to time O.
o     A complete sine wave in the time domain can be represented by one single spike in
      the frequency domain.
o     A single-frequency sine wave is not useful in data communications; we need to
      send a composite signal, a signal made of many simple sine waves.
o     According to Fourier analysis, any composite signal is a combination of simple
      sine waves with different frequencies, amplitudes, and phases.
o     The bandwidth of a composite signal is the difference between the highest and the
      lowest frequencies contained in that signal.
o     A digital signal is a composite analog signal with an infinite bandwidth.
o     Baseband transmission of a digital signal that preserves the shape of the digital
      signal is possible only if we have a low-pass channel with an infinite or very wide
      bandwidth.
o     If the available channel is a bandpass channel, we cannot send a digital signal
      directly to the channel; we need to convert the digital signal to an analog signal
      before transmission.
o     For a noiseless channel, the Nyquist bit rate formula defines the theoretical maxi-
      mum bit rate. For a noisy channel, we need to use the Shannon capacity to find the
      maximum bit rate.
o     Attenuation, distortion, and noise can impair a signal.
o     Attenuation is the loss of a signal's energy due to the resistance of the medium.
o     Distortion is the alteration of a signal due to the differing propagation speeds of
      each of the frequencies that make up a signal.
o     Noise is the external energy that corrupts a signal.
o     The bandwidth-delay product defines the number of bits that can fill the link.

96   CHAPTER 3     DATA AND SIGNALS


## 3.10         PRACTICE SET
             Review Questions
                  1. What is the relationship between period and frequency?
                  2. What does the amplitude of a signal measure? What does the frequency of a signal
                     measure? What does the phase of a signal measure?
                  3. How can a composite signal be decomposed into its individual frequencies?
                 4. Name three types of transmission impairment.
                  5. Distinguish between baseband transmission and broadband transmission.
                  6. Distinguish between a low-pass channel and a band-pass channel.
                  7. What does the Nyquist theorem have to do with communications?
                  8. What does the Shannon capacity have to do with communications?
                  9. Why do optical signals used in fiber optic cables have a very short wave length?
                 10. Can we say if a signal is periodic or nonperiodic by just looking at its frequency
                     domain plot? How?
                 11. Is the frequency domain plot of a voice signal discrete or continuous?
                 12. Is the frequency domain plot of an alarm system discrete or continuous?
                 13. We send a voice signal from a microphone to a recorder. Is this baseband or broad-
                     band transmission?
                 14. We send a digital signal from one station on a LAN to another station. Is this base-
                     band or broadband transmission?
                 15. We modulate several voice signals and send them through the air. Is this baseband
                     or broadband transmission?

             Exercises
                 16. Given the frequencies listed below, calculate the corresponding periods.
                     a. 24Hz
                     b. 8 MHz
                     c. 140 KHz
                 17. Given the following periods, calculate the corresponding frequencies.
                     a. 5 s
                     b. 12 Jls
                     c. 220 ns
                 18. What is the phase shift for the foIlowing?
                     a. A sine wave with the maximum amplitude at time zero
                     b. A sine wave with maximum amplitude after 1/4 cycle
                     c. A sine wave with zero amplitude after 3/4 cycle and increasing
                 19. What is the bandwidth of a signal that can be decomposed into five sine waves
                     with frequencies at 0, 20, 50, 100, and 200 Hz? All peak amplitudes are the same.
                     Draw the bandwidth.

## SECTION 3.10     PRACTICE SET    97


20. A periodic composite signal with a bandwidth of 2000 Hz is composed of two sine
    waves. The first one has a frequency of 100 Hz with a maximum amplitude of 20 V;
    the second one has a maximum amplitude of 5 V. Draw the bandwidth.
21. Which signal has a wider bandwidth, a sine wave with a frequency of 100 Hz or a
    sine wave with a frequency of 200 Hz?
22. What is the bit rate for each of the following signals?
    a. A signal in which 1 bit lasts 0.001 s
    b. A signal in which 1 bit lasts 2 ms
    c. A signal in which 10 bits last 20 J-ls
23. A device is sending out data at the rate of 1000 bps.
    a. How long does it take to send out 10 bits?
    b. How long does it take to send out a single character (8 bits)?
    c. How long does it take to send a file of 100,000 characters?
24. What is the bit rate for the signal in Figure 3.34?


Figure 3.34 Exercise 24

                                           16 ns


            ---t=:i--J~-...;..---+-.....;.--.;....-d ... ~
                         1                                                    TI~


25. What is the frequency of the signal in Figure 3.35?


Figure 3.35 Exercise 25

                I,                   4ms               .1
                1                                         I

                V\ f\ f\ f\ f\ f\ f\ f\ : ...
                  \TV V VVV V~                                       Time


26. What is the bandwidth of the composite signal shown in Figure 3.36.


Figure 3.36 Exercise 26


                                                                  Frequency

                     5       5   5   5     5   I

9S   CHAPTER 3     DATA AND SIGNALS


                 27. A periodic composite signal contains frequencies from 10 to 30 KHz, each with an
                      amplitude of 10 V. Draw the frequency spectrum.
                 2K. A non-periodic composite signal contains frequencies from 10 to 30 KHz. The
                      peak amplitude is 10 V for the lowest and the highest signals and is 30 V for the
                      20-KHz signal. Assuming that the amplitudes change gradually from the minimum
                      to the maximum, draw the frequency spectrum.
                 20. A TV channel has a bandwidth of 6 MHz. If we send a digital signal using one
                      channel, what are the data rates if we use one harmonic, three harmonics, and five
                      harmonics?
                 30. A signal travels from point A to point B. At point A, the signal power is 100 W. At
                      point B, the power is 90 W. What is the attenuation in decibels?
                 31. The attenuation of a signal is -10 dB. What is the final signal power if it was origi-
                      nally 5 W?
                 32. A signal has passed through three cascaded amplifiers, each with a 4 dB gain.
                      What is the total gain? How much is the signal amplified?
                 33. If the bandwidth of the channel is 5 Kbps, how long does it take to send a frame of
                      100,000 bits out of this device?
                 3cf. The light of the sun takes approximately eight minutes to reach the earth. What is
                      the distance between the sun and the earth?
                 35. A signal has a wavelength of 1 11m in air. How far can the front of the wave travel
                      during 1000 periods?
                 36. A line has a signal-to-noise ratio of 1000 and a bandwidth of 4000 KHz. What is
                      the maximum data rate supported by this line?
                 37. We measure the performance of a telephone line (4 KHz of bandwidth). When the
                      signal is 10 V, the noise is 5 mV. What is the maximum data rate supported by this
                      telephone line?
                 3X. A file contains 2 million bytes. How long does it take to download this file using a
                     56-Kbps channel? 1-Mbps channel?
                 39. A computer monitor has a resolution of 1200 by 1000 pixels. If each pixel uses
                     1024 colors, how many bits are needed to send the complete contents of a screen?
                 40. A signal with 200 milliwatts power passes through 10 devices, each with an average
                     noise of 2 microwatts. What is the SNR? What is the SNRdB ?
                 4 I. If the peak voltage value of a signal is 20 times the peak voltage value of the noise,
                      what is the SNR? What is the SNR dB ?
                 42. What is the theoretical capacity of a channel in each of the following cases:
                      a. Bandwidth: 20 KHz         SNRdB =40
                      b. Bandwidth: 200 KHz SNRdB =4
                      c. Bandwidth: 1 MHz         SNRdB =20
                 43. We need to upgrade a channel to a higher bandwidth. Answer the following
                      questions:
                      a. How is the rate improved if we double the bandwidth?
                      b. How is the rate improved if we double the SNR?

## SECTION 3.10     PRACTICE SET         99


44. We have a channel with 4 KHz bandwidth. If we want to send data at 100 Kbps,
       what is the minimum SNRdB ? What is SNR?
45. What is the transmission time of a packet sent by a station if the length of the
       packet is 1 million bytes and the bandwidth of the channel is 200 Kbps?
46. What is the length of a bit in a channel with a propagation speed of 2 x 108 mls if
       the channel bandwidth is
       a. 1 Mbps?
       h. 10 Mbps?
       c. 100 Mbps?
-1- 7. How many bits can fit on a link with a 2 ms delay if the bandwidth of the link is
       a. 1 Mbps?
       h. 10 Mbps?
       c. 100 Mbps?
-1-X. What is the total delay (latency) for a frame of size 5 million bits that is being sent
       on a link with 10 routers each having a queuing time of 2 Ils and a processing time
       of 1 Ils. The length of the link is 2000 Km. The speed of light inside the link is 2 x
       108 mls. The link has a bandwidth of 5 Mbps. Which component of the total delay
       is dominant? Which one is negligible?


## CHAPTER 4

      Digital Transmission


      A computer network is designed to send information from one point to another. This
      information needs to be converted to either a digital signal or an analog signal for trans-
      mission. In this chapter, we discuss the first choice, conversion to digital signals; in
## Chapter 5, we discuss the second choice, conversion to analog signals.
           We discussed the advantages and disadvantages of digital transmission over analog
      transmission in Chapter 3. In this chapter, we show the schemes and techniques that
      we use to transmit data digitally. First, we discuss digital-to-digital conversion tech-
      niques, methods which convert digital data to digital signals. Second, we discuss analog-
      to-digital conversion techniques, methods which change an analog signal to a digital
      signaL Finally, we discuss transmission modes.


## 4.1     DIGITAL~TO~DIGITAL CONVERSION
      In Chapter 3, we discussed data and signals. We said that data can be either digital or
      analog. We also said that signals that represent data can also be digital or analog. In this
## section, we see how we can represent digital data by using digital signals. The conver-
      sion involves three techniques: line coding, block coding, and scrambling. Line coding
      is always needed~ block coding and scrambling mayor may not be needed.

      Line Coding
      Line coding is the process of converting digital data to digital signals. We assume that
      data, in the form of text, numbers, graphical images, audio, or video, are stored in com-
      puter memory as sequences of bits (see Chapter 1). Line coding converts a sequence of
      bits to a digital signal. At the sender, digital data are encoded into a digital signal; at the
      receiver, the digital data are recreated by decoding the digital signal. Figure 4.1 shows
      the process.

      Characteristics
      Before discussing different line coding schemes, we address their common characteristics.


                                                                                                 101

102   CHAPTER 4   DIGITAL TRANSMISSION


             Figure 4.1      Line coding and decoding

                                   Sender                                                            Receiver


                    Digital data                                                                                Digital data
                                                                Digital signal
                  1°101". 101 1                                                                             1°101 •• ' 101 1


             Signal Element Versus Data Element Let us distinguish between a data element
             and a signal element. In data communications, our goal is to send data elements. A
             data element is the smallest entity that can represent a piece of information: this is the
             bit. In digital data communications, a signal element carries data elements. A signal
             element is the shortest unit (timewise) of a digital signal. In other words, data elements
             are what we need to send; signal elements are what we can send. Data elements are
             being carried; signal elements are the carriers.
                  We define a ratio r which is the number of data elements carried by each signal ele-
             ment. Figure 4.2 shows several situations with different values of r.


              Figure 4.2 Signal element versus data element

                                         I data element                                  I data element

                                                   o                                           o

                               ~-
                                                element                                     2 signal
                                                                                            elements
                           a. One data element per one signal                b. One data element per two signal
                              element (r = 1)                                           (r t)
                                                                                elements =


                                         2 data elements                                4 data elements

                                    II      I     01       II                                 1101
                                            I

                                   ---'
                               -l=:F            I signal
                                                                                 ---16_-    3 signal
                                                element                                     elements
                           c. Two data elements per one signal               d. Four data elements per three signal
                              element (r = 2)                                           (r 1)
                                                                                elements =


                   In part a of the figure, one data element is carried by one signal element (r = 1). In
              part b of the figure, we need two signal elements (two transitions) to carry each data

## SECTION 4.1      DIGITAL-TO-DIGITAL CONVERSION              103


element (r = ! ). We will see later that the extra signal element is needed to guarantee
               2
synchronization. In part c of the figure, a signal element carries two data elements (r = 2).
Finally, in part d, a group of 4 bits is being carried by a group of three signal elements
(r = ~ ). For every line coding scheme we discuss, we will give the value of r.
     3                                                          .
     An analogy may help here. Suppose each data element IS a person who needs to be
carried from one place to another. We can think of a signal element as a vehicle that can
carry people. When r = 1, it means each person is driving a vehicle. When r > 1, it
means more than one person is travelling in a vehicle (a carpool, for example). We can
also have the case where one person is driving a car and a trailer (r = ~ ).
Data Rate Versus Signal Rate The data rate defines the number of data elements
(bits) sent in Is. The unit is bits per second (bps). The signal rate is the number of sig-
nal elements sent in Is. The unit is the baud. There are several common terminologies
used in the literature. The data rate is sometimes called the bit rate; the signal rate is
sometimes called the pulse rate, the modulation rate, or the baud rate.
     One goal in data communications is to increase the data rate while decreasing the
signal rate. Increasing the data rate increases the speed of transmission; decreasing the
signal rate decreases the bandwidth requirement. In our vehicle-people analogy, we
need to carry more people in fewer vehicles to prevent traffic jams. We have a limited
bandwidth in our transportation system.
     We now need to consider the relationship between data rate and signal rate (bit rate
and baud rate). This relationship, of course, depends on the value of r. It also depends
on the data pattern. If we have a data pattern of all 1s or all Os, the signal rate may be
different from a data pattern of alternating Os and Is. To derive a formula for the rela-
tionship, we need to define three cases: the worst, best, and average. The worst case is
when we need the maximum signal rate; the best case is when we need the minimum.
In data communications, we are usually interested in the average case. We can formu-
late the relationship between data rate and signal rate as

                                             1
                                    S =c xNx -         baud
                                             r

where N is the data rate (bps); c is the case factor, which varies for each case; S is the
number of signal elements; and r is the previously defined factor.

Example 4.1
A signal is carrying data in which one data element is encoded as one signal element (r = 1). If
the bit rate is 100 kbps, what is the average value of the baud rate if c is between 0 and l?

Solution
We assume that the average value of c is ~. The baud rate is then

                               111
                    S =c x N x - = - x 100,000 x -1 = 50,000 =50 kbaud
                               r   2

Bandwidth We discussed in Chapter 3 that a digital signal that carries infonnation is
nonperiodic. We also showed that the bandwidth of a nonperiodic signal is continuous
with an infinite range. However, most digital signals we encounter in real life have a

104   CHAPTER 4     DIGITAL TRANSMISSION


             bandwidth with finite values. In other words, the bandwidth is theoretically infinite, but
             many of the components have such a small amplitude that they can be ignored. The
             effective bandwidth is finite. From now on, when we talk about the bandwidth of a dig-
             ital signal, we need to remember that we are talking about this effective bandwidth.

                  Although the actual bandwidth ofa digital signal is infinite, the effective bandwidth is finite.


                  We can say that the baud rate, not the bit rate, determines the required bandwidth
             for a digital signal. If we use the transpOltation analogy, the number of vehicles affects
             the traffic, not the number of people being carried. More changes in the signal mean
             injecting more frequencies into the signal. (Recall that frequency means change and
             change means frequency.) The bandwidth reflects the range of frequencies we need.
             There is a relationship between the baud rate (signal rate) and the bandwidth. Band-
             width is a complex idea. When we talk about the bandwidth, we normally define a
             range of frequencies. We need to know where this range is located as well as the values
             of the lowest and the highest frequencies. In addition, the amplitude (if not the phase)
             of each component is an impOltant issue. In other words, we need more information
             about the bandwidth than just its value; we need a diagram of the bandwidth. We will
             show the bandwidth for most schemes we discuss in the chapter. For the moment, we
             can say that the bandwidth (range of frequencies) is proportional to the signal rate
             (baud rate). The minimum bandwidth can be given as

                                                                           1
                                                        B min =: c >< N >< -
                                                                          r

                     We can solve for the maximum data rate if the bandwidth of the channel is given.

                                                                  1
                                                         N max = - xBxr
                                                                 c

             Example 4.2
              The maximum data rate of a channel (see Chapter 3) is N max = 2 >< B >< log2L (defined by the
              Nyquist formula). Does this agree with the previous formula for N max ?

              Solution
              A signal with L levels actually can carry log2 L bits per level. If each level corresponds to one sig-
              nal element and we assume the average case (c = ~), then we have


              Baseline Wandering In decoding a digital signal, the receiver calculates a running
              average of the received signal power. This average is called the baseline. The incoming
              signal power is evaluated against this baseline to determine the value of the data ele-
              ment. A long string of Os or 1s can cause a drift in the baseline (baseline wandering)
              and make it difficult for the receiver to decode correctly. A good line coding scheme
              needs to prevent baseline wandering.

## SECTION 4.1         DIGITAL-TO-DIGITAL CONVERSION          105


DC Components When the voltage level in a digital signal is constant for a while,
the spectrum creates very low frequencies (results of Fourier analysis). These fre-
quencies around zero, called DC (direct-current) components, present problems for a
system that cannot pass low frequencies or a system that uses electrical coupling
(via a transformer). For example, a telephone line cannot pass frequencies below
200 Hz. Also a long-distance link may use one or more transformers to isolate
different parts of the line electrically. For these systems, we need a scheme with no
DC component.

Self-synchronization To correctly interpret the signals received from the sender,
the receiver's bit intervals must correspond exactly to the sender's bit intervals. If the
receiver clock is faster or slower, the bit intervals are not matched and the receiver might
misinterpret the signals. Figure 4.3 shows a situation in which the receiver has a shorter
bit duration. The sender sends 10110001, while the receiver receives 110111 000011.


Figure 4.3    Effect of lack ofsynchronization


                                 J                               J       I
                             o   I
                                 I
                                                     o       o : 0       :
                                 I                               J       I
                                                                 I       1""'"----;
                                                                 I


                                                                                         Time

               a.Sent


                        I                 I                                  I
                        I                 I                                  I
                   1 I                  1 I 1    0       0   0       0   1   I   1
                        I                 I                                  I


                                                                                         Time

               b. Received


    A self-synchronizing digital signal includes timing information in the data being
transmitted. This can be achieved if there are transitions in the signal that alert the
receiver to the beginning, middle, or end of the pulse. If the receiver's clock is out of
synchronization, these points can reset the clock.

Example 4.3
In a digital transmission, the receiver clock is 0.1 percent faster than the sender clock. How many
extra bits per second does the receiver receive if the data rate is 1 kbps? How many if the data
rate is 1 Mbps?

Solution
At 1 kbps, the receiver receives 1001 bps instead of 1000 bps.

                   1000 bits sent             1001 bits received                 1 extra bps

106   CHAPTER 4   DIGITAL TRANSMISSION


             At 1 Mbps, the receiver receives 1,001,000 bps instead of 1,000,000 bps.

                        1,000,000 bits sent        1,001,000 bits received            1000 extra bps

             Built-in Error Detection It is desirable to have a built-in error-detecting capability
             in the generated code to detect some of or all the errors that occurred during transmis-
             sion. Some encoding schemes that we will discuss have this capability to some extent.
             Immunity to Noise and Interference Another desirable code characteristic is a code               I


             that is immune to noise and other interferences. Some encoding schemes that we will
             discuss have this capability.
             Complexity A complex scheme is more costly to implement than a simple one. For
             example, a scheme that uses four signal levels is more difficult to interpret than one that
             uses only two levels.

              Line Coding Schemes
             We can roughly divide line coding schemes into five broad categories, as shown in
             Figure 4.4.


              Figure 4.4 Line coding schemes


                                                    Unipolar        --NRZ


                                                                          NRZ, RZ, and biphase (Manchester.
                                                      Polar
                                                                          and differential Manchester)


                         Line coding                 Bipolar        - - AMI and pseudoternary


                                                    Multilevel      - - 2B/IQ, 8B/6T, and 4U-PAM5


                                                  Multitransition   - - MLT-3


                  There are several schemes in each category. We need to be familiar with all
              schemes discussed in this section to understand the rest of the book. This section can be
              used as a reference for schemes encountered later.

              Unipolar Scheme
              In a unipolar scheme, all the signal levels are on one side of the time axis, either above
              or below.
              NRZ (Non-Return-to-Zero) Traditionally, a unipolar scheme was designed as a
              non-return-to-zero (NRZ) scheme in which the positive voltage defines bit I and the
              zero voltage defines bit O. It is called NRZ because the signal does not return to zero at
              the middle of the bit. Figure 4.5 show a unipolar NRZ scheme.

## SECTION 4.1              DIGITAL-TO-DIGITAL CONVERSION                    107


Figure 4.5    Unipolar NRZ scheme

                  Amplitude

                         1    f   0        :   1   I       0
                    v         f                    I


                    o 1------'1---1---1--+---.--_ _
                                                               I   Time   Nonnalized power


     Compared with its polar counterpart (see the next section), this scheme is very
costly. As we will see shortly, the normalized power (power needed to send 1 bit per
unit line resistance) is double that for polar NRZ. For this reason, this scheme is nor-
mally not used in data communications today.

Polar Schemes
In polar schemes, the voltages are on the both sides of the time axis. For example, the
voltage level for 0 can be positive and the voltage level for I can be negative.
Non-Return-to-Zero (NRZ) In polar NRZ encoding, we use two levels of voltage
amplitude. We can have two versions of polar NRZ: NRZ-Land NRZ-I, as shown in
Figure 4.6. The figure also shows the value of r, the average baud rate, and the band-
width. In the first variation, NRZ-L (NRZ-Level), the level of the voltage determines
the value of the bit. In the second variation, NRZ-I (NRZ-Invert), the change or lack of
change in the level of the voltage determines the value of the bit. If there is no change,
the bit is 0; if there is a change, the bit is 1.


Figure 4.6 Polar NRZ-L and NRZ-I schemes


             011                         1 : 1         0                    T=:= 1             Save "'NIl
              I
              I                            I
                                           I                                   p
   NRZ-L f--+--1---I---+--I---1------t----'--~


                                                                               ~illdWidth
                                            Time

                                                                          0:
   NRZ-I f-----I----J---I---+--+--+----+----'--~
                                             Time                          o   G""Iil""""'~I=-=-"""'r'
                                                                               o         I
                                                                                                       ~
                                                                                                    -----'l..
                                                                                                   2 fIN

         o No inversion: Next bit is 0   • Inversion: Next bit is 1


        In NRZ-L the level of the voltage determines the value of the bit. In NRZ-I
           the inversion or the lack of inversion determines the value of the bit.


    Let us compare these two schemes based on the criteria we previously defined.
Although baseline wandering is a problem for both variations, it is twice as severe in
NRZ- L. If there is a long sequence of Os or Is in NRZ-L, the average signal power

108   CHAPTER 4   DIGITAL TRANSMISSION


             becomes skewed. The receiver might have difficulty discerning the bit value. In NRZ-I
             this problem occurs only for a long sequence of as. If somehow we can eliminate the
             long sequence of as, we can avoid baseline wandering. We will see shortly how this can
             be done.
                  The synchronization problem (sender and receiver clocks are not synchronized)
             also exists in both schemes. Again, this problem is more serious in NRZ-L than in
             NRZ-I. While a long sequence of as can cause a problem in both schemes, a long
             sequence of 1s affects only NRZ-L.
                  Another problem with NRZ-L occurs when there is a sudden change of polarity in
             the system. For example, if twisted-pair cable is the medium, a change in the polarity of
             the wire results in all as interpreted as I s and all I s interpreted as as. NRZ-I does not
             have this problem. Both schemes have an average signal rate of NI2 Bd.

                           NRZ-L and NRZ-J both have an average signal rate of NI2 Bd.

                  Let us discuss the bandwidth. Figure 4.6 also shows the normalized bandwidth for
             both variations. The vertical axis shows the power density (the power for each I Hz of
             bandwidth); the horizontal axis shows the frequency. The bandwidth reveals a very
             serious problem for this type of encoding. The value of the power density is velY high
             around frequencies close to zero. This means that there are DC components that carry a
             high level of energy. As a matter of fact, most of the energy is concentrated in frequen-
             cies between a and NIl. This means that although the average of the signal rate is N12,
             the energy is not distributed evenly between the two halves.

                               NRZ-L and NRZ-J both have a DC component problem.

             Example 4.4
             A system is using NRZ-I to transfer 10-Mbps data. What are the average signal rate and mini-
             mum bandwidth?
             Solution
             The average signal rate is S = NI2 = 500 kbaud. The minimum bandwidth for this average baud
             rate is Bnlin = S = 500 kHz.
             Return to Zero (RZ) The main problem with NRZ encoding occurs when the sender
             and receiver clocks are not synchronized. The receiver does not know when one bit has
             ended and the next bit is starting. One solution is the return-to-zero (RZ) scheme,
             which uses three values: positive, negative, and zero. In RZ, the signal changes not
             between bits but during the bit. In Figure 4.7 we see that the signal goes to 0 in the mid-
             dle of each bit. It remains there until the beginning of the next bit. The main disadvan-
             tage of RZ encoding is that it requires two signal changes to encode a bit and therefore
             occupies greater bandwidth. The same problem we mentioned, a sudden change of
             polarity resulting in all as interpreted as 1s and all 1s interpreted as as, still exist here,
             but there is no DC component problem. Another problem is the complexity: RZ uses
             three levels of voltage, which is more complex to create and discern. As a result of all
             these deficiencies, the scheme is not used today. Instead, it has been replaced by the
             better-performing Manchester and differential Manchester schemes (discussed next).

## SECTION 4.1               DIGITAL-TO-DIGITAL CONVERSION                        109


Figure 4.7 Polar RZ scheme


           Amplitude
                                                                                                p


                                                                                         o:lL
                       o       l
                               l
                                                                    1   l
                                                                        1
                               l                                        l


                                                                            Time
                                                                                            o                         I   ~
                                                                                                o        1            2 fiN


Biphase: Manchester and Differential Manchester The idea of RZ (transition at
the middle of the bit) and the idea of NRZ-L are combined into the Manchester scheme.
In Manchester encoding, the duration of the bit is divided into two halves. The voltage
remains at one level during the first half and moves to the other level in the second half.
The transition at the middle of the bit provides synchronization. Differential Manchester,
on the other hand, combines the ideas of RZ and NRZ-I. There is always a transition at
the middle of the bit, but the bit values are determined at the beginning of the bit. If the
next bit is 0, there is a transition; if the next bit is 1, there is none. Figure 4.8 shows
both Manchester and differential Manchester encoding.


Figure 4.8          Polar biphase: Manchester and differential Manchester schemes


                           (           Ois   L                lis    S )
                               I         I         I          I         I        I
                       0       I
                                   1     I
                                              0    I
                                                        0     I
                                                                    1   I
                                                                             1   I

                   .....       I         I         I          I
                                                                     _, --4
                                                                        I        I
                               I
                               I
                               I
                                   r+-   I
                                                   1,...-     I
                                                              1
                                                              I                  I
                                                                                                     p
   Manchester                                                                    I
                               I         I                    I
                                                                                     Time
                           l..+-         I
                                         I        -I
                                                            -+-         I-
                                                                                 I
                                                                                 I
                                                                                                    11       Bandwidth
                               I         I         l          I         I        I

                                                                                                    O.~~~
   Differential
                           r¢-
                               I
                                         I,....    1,...-     I
                                                              I
                                                              I      rt-         I
                                                                                 I
                                                                                 I
                                                                                                     o            1
                                                                                                                                 )0

                                                                                                                              2 fiN
   Manchester
                   ~
                               I
                               1
                               1
                               1
                                   ~
                                         I        -I
                                                              I
                                                            L...¢-
                                                              I
                                                                        I
                                                                        I
                                                                        I
                                                                        I
                                                                                 I
                                                                                 I

                                                                                 I
                                                                                     Time


                  o No inversion: Next bit is 1                   • Inversion: Next bit is 0


                  In Manchester and differential Manchester encoding, the transition
                         at the middle of the bit is used for synchronization.


     The Manchester scheme overcomes several problems associated with NRZ-L, and
differential Manchester overcomes several problems associated with NRZ-I. First, there
is no baseline wandering. There is no DC component because each bit has a positive and

110   CHAPTER 4     DIGITAL TRANSMISSION


             negative voltage contribution. The only drawback is the signal rate. The signal rate for
             Manchester and differential Manchester is double that for NRZ. The reason is that there is
             always one transition at the middle of the bit and maybe one transition at the end of each
             bit. Figure 4.8 shows both Manchester and differential Manchester encoding schemes.
             Note that Manchester and differential Manchester schemes are also called biphase
             schemes.

                  The minimum bandwidth ofManchester and differential Manchester is 2 times that of NRZ.


             Bipolar Schemes
             In bipolar encoding (sometimes called multilevel binary), there are three voltage lev-
             els: positive, negative, and zero. The voltage level for one data element is at zero, while
             the voltage level for the other element alternates between positive and negative.

                           In bipolar encoding, we use three levels: positive, zero, and negative.


             AMI and Pseudoternary Figure 4.9 shows two variations of bipolar encoding: AMI
             and pseudoternary. A common bipolar encoding scheme is called bipolar alternate
             mark inversion (AMI). In the term alternate mark inversion, the word mark comes
             from telegraphy and means 1. So AMI means alternate I inversion. A neutral zero volt-
             age represents binary O. Binary Is are represented by alternating positive and negative
             voltages. A variation of AMI encoding is called pseudoternary in which the 1 bit is
             encoded as a zero voltage and the 0 bit is encoded as alternating positive and negative
             voltages.


              Figure 4.9      Bipolar schemes: AMI and pseudoternary

                         Amplitude
                                                                               r= 1
                                o    I
                                     I
                                         I
                                         I
                                             (I   o   I
                                                      I     :   (I
                                                      I     I
                                                      I     I                     p
                         AMI r--~-~--1--+----+---;-+
                                                  Time


                  Pseudoternary I-----+--~----If----t--...,....-____r--+
                                                                    Time


                   The bipolar scheme was developed as an alternative to NRZ. The bipolar scheme
              has the same signal rate as NRZ, but there is no DC component. The NRZ scheme has
              most of its energy concentrated near zero frequency, which makes it unsuitable for
              transmission over channels with poor performance around this frequency. The concen-
              tration of the energy in bipolar encoding is around frequency N12. Figure 4.9 shows the
              typical energy concentration for a bipolar scheme.

## SECTION 4.1    DIGITAL-TO-DIGITAL CONVERSION              111


      One may ask why we do not have DC component in bipolar encoding. We can
answer this question by using the Fourier transform, but we can also think about it intu-
itively. If we have a long sequence of 1s, the voltage level alternates between positive
and negative; it is not constant. Therefore, there is no DC component. For a long
sequence of Os, the voltage remains constant, but its amplitude is zero, which is the
same as having no DC component. In other words, a sequence that creates a constant
zero voltage does not have a DC component.
      AMI is commonly used for long-distance communication, but it has a synchroniza-
tion problem when a long sequence of Os is present in the data. Later in the chapter, we
will see how a scrambling technique can solve this problem.

Multilevel Schemes
The desire to increase the data speed or decrease the required bandwidth has resulted in
the creation of many schemes. The goal is to increase the number of bits per baud by
encoding a pattern of m data elements into a pattern of n signal elements. We only have
two types of data elements (Os and Is), which means that a group of m data elements
can produce a combination of 2m data patterns. We can have different types of signal
elements by allowing different signal levels. If we have L different levels, then we can
produce L n combinations of signal patterns. If 2 m = L n, then each data pattern is
encoded into one signal pattern. If 2m < L n , data patterns occupy only a subset of signal
patterns. The subset can be carefully designed to prevent baseline wandering, to pro-
vide synchronization, and to detect errors that occurred during data transmission. Data
encoding is not possible if 2 m > L n because some of the data patterns cannot be
encoded.
     The code designers have classified these types of coding as mBnL, where m is the
length of the binary pattern, B means binary data, n is the length of the signal pattern,
and L is the number of levels in the signaling. A letter is often used in place of L: B
(binary) for L = 2, T (ternary) for L = 3, and Q (quaternary) for L = 4. Note that the first
two letters define the data pattern, and the second two define the signal pattern.


    In mBnL schemes, a pattern of m data elements is encoded as a pattern of n signal
                             elements in which 2m ::::; Ln.


2BIQ The first mBnL scheme we discuss, two binary, one quaternary (2BIQ), uses
data patterns of size 2 and encodes the 2-bit patterns as one signal element belonging
to a four-level signal. In this type of encoding m = 2, n = 1, and L = 4 (quatemary). Fig-
ure 4.10 shows an example of a 2B 1Q signal.
     The average signal rate of 2BlQ is S = N/4. This means that using 2BIQ, we can
send data 2 times faster than by using NRZ-L. However, 2B lQ uses four different sig-
nal levels, which means the receiver has to discern four different thresholds. The
reduced bandwidth comes with a price. There are no redundant signal patterns in this
scheme because 22 = 4 1.
     As we will see in Chapter 9, 2BIQ is used in DSL (Digital Subscriber Line) tech-
nology to provide a high-speed connection to the Internet by using subscriber telephone
lines.

112   CHAPTER 4   DIGITAL TRANSMISSION


             Figure 4.10      Multilevel: 2B1Q scheme

                                                                    Previous level:     Previous level:
                                                                       positive            negative

                                                        Next               Next              Next
                                                        bits               level             level
                                                         00                 +1                   -I
                                                         01                 +3                   -3
                                                         10                 -I                   +1
                                                         II                 -3                   +3
                                                                          Transition table


                              00   I   II     0]    I   HI     I    0]                                                  Save =N14
                                   I                I          I
                                   I                I
                        +3         I                I                                            p
                                   I                I
                                   I                I
                        +1
                                                               I                           1 \              Bandwidth
                        ~1                                     I             Time
                                                               I
## 0.5
                                                               I
                        -3                                      I                            o          -
                                   I
                                   I
                                                    I
                                                    I
                                                                I
                                                               ,I
                                                                                                 o    1/2                   2 fiN

                                   Assuming positive original level


              8B6T A very interesting scheme is eight binary, six ternary (8B6T). This code is used
              with 100BASE-4T cable, as we will see in Chapter 13. The idea is to encode a pattern of
              8 bits as a pattern of 6 signal elements, where the signal has three levels (ternary). In this
              type of scheme, we can have 2 8 = 256 different data patterns and 36 =478 different signal
              patterns. The mapping table is shown in Appendix D. There are 478 - 256 =222 redundant
              signal elements that provide synchronization and error detection. Part of the redundancy is
              also used to provide DC balance. Each signal pattern has a weight of 0 or +1 DC values. This
              means that there is no pattern with the weight -1. To make the whole stream Dc-balanced,
              the sender keeps track of the weight. If two groups of weight 1 are encountered one after
              another, the first one is sent as is, while the next one is totally inverted to give a weight of -1.
                   Figure 4.11 shows an example of three data patterns encoded as three signal pat-
              terns. The three possible signal levels are represented as -,0, and +. The first 8-bit pat-
              tern 00010001 is encoded as the signal pattern -0-0++ with weight 0; the second 8-bit
              pattern 010 10011 is encoded as - + - + + 0 with weight +1. The third bit pattern should
              be encoded as + - - + 0 + with weight + 1. To create DC balance, the sender inverts the
              actual signal. The receiver can easily recognize that this is an inverted pattern because
              the weight is -1. The pattern is inverted before decoding.

              Figure 4.11 Multilevel: 8B6T scheme

                               OOOIO()O(                                 01()10011                            O!OIOO()()            I
                                                                                                                                    I

                  +v                                                                                                       Inverted:
                                                                                                                            pattern :
                   o +----.--,--..,.....---l---I-+--I--I----L---r--t-----..--r-----It---r----..
                                                                                                                                        Time
                  -v
                                -0-0++                               -+-++0                                  +--+0+

## SECTION 4.1         DIGITAL-TO-DIGITAL CONVERSION                  113


    The average signal rate of the scheme is theoretically Save = ! X N X §; in practice
the minimum bandwidth is very close to 6N18.                      2       8

4D-PAMS The last signaling scheme we discuss in this category is called four-
dimensional five-level pulse amplitude modulation (4D-PAM5). The 4D means that data
is sent over four wires at the same time. It uses five voltage levels, such as -2, -1, 0, 1, and 2.
However, one level, level 0, is used only for forward error detection (discussed in Chap-
ter 10). If we assume that the code is just one-dimensional, the four levels create something
similar to 8B4Q. In other words, an 8-bit word is translated to a signal element of four differ-
ent levels. The worst signal rate for this imaginary one-dimensional version is N X 4/8, or N12.
      The technique is designed to send data over four channels (four wires). This means
the signal rate can be reduced to N18, a significant achievement. All 8 bits can be fed into a
wire simultaneously and sent by using one signal element. The point here is that the four
signal elements comprising one signal group are sent simultaneously in a four-dimensional
setting. Figure 4.12 shows the imaginary one-dimensional and the actual four-dimensional
implementation. Gigabit LANs (see Chapter 13) use this technique to send 1-Gbps data
over four copper cables that can handle 125 Mbaud. This scheme has a lot of redundancy
in the signal pattern because 2 8 data patterns are matched to 44 = 256 signal patterns. The
extra signal patterns can be used for other purposes such as error detection.

Figure 4.12 Multilevel: 4D-PAM5 scheme

                     00011110              1 Gbps
                                                                     250 Mbps
                                                                                Wire 1 (125 MBd)


                                                                     250 Mbps
                                                                                Wire 2 (125 MBd)
    +2
    +1
                                                                     250 Mbps
                                                                                Wire 3 (125 MBd)
    -1
    -2

                                                                     250 Mbps
                                                                                Wire 4 (125 MBd)


Multiline Transmission: MLT-3
NRZ-I and differential Manchester are classified as differential encoding but use two transi-
tion rules to encode binary data (no inversion, inversion). If we have a signal with more than
two levels, we can design a differential encoding scheme with more than two transition
rules. MLT-3 is one of them. The multiline transmission, three level (MLT-3) scheme
uses three levels (+ v, 0, and - V) and three transition rules to move between the levels.
  1. If the next bit is 0, there is no transition.
 2. If the next bit is 1 and the current level is not 0, the next level is 0.
 3. If the next bit is 1 and the cutTent level is 0, the next level is the opposite of the last
    nonzero level.

114   CHAPTER 4     DIGITAL TRANSMISSION


             The behavior of MLT-3 can best be described by the state diagram shown in Figure 4.13.
             The three voltage levels (-V, 0, and +V) are shown by three states (ovals). The transition
             from one state (level) to another is shown by the connecting lines. Figure 4.13 also
             shows two examples of an MLT-3 signal.


             Figure 4.13            Multitransition: MLT-3 scheme


                          01110111101111
                           1 I   I I  I 1
                   +V                        I      I
                                             I      I
                    OV   r--__- - - t -      I      I
                                           --t--+-------j--_   __+_~
                                                                                                    Next bit: 0
                                                                : Time
                   -v                                           1
                                                                I              Next bit: 1
                  a. Typical case


                                     1                                                           Last
                                                                                              non-zero     non-zero
                   +v
                                                                                Next bit: 0   level: + V   level: - V   Next bit: 0
                    OV l----+O---i--r--
                                                                            c. Transition states
                   -v
                  b. Worse case


                   One might wonder why we need to use MLT-3, a scheme that maps one bit to one
              signal element. The signal rate is the same as that for NRZ-I, but with greater complexity
              (three levels and complex transition rules). It turns out that the shape of the signal in this
              scheme helps to reduce the required bandwidth. Let us look at the worst-case scenario, a
              sequence of I s. In this case, the signal element pattern +VO - VO is repeated every 4 bits.
              A nonperiodic signal has changed to a periodic signal with the period equal to 4 times the
              bit duration. This worst-case situation can be simulated as an analog signal with a fre-
              quency one-fourth of the bit rate. In other words, the signal rate for MLT-3 is one-fourth
              the bit rate. This makes MLT-3 a suitable choice when we need to send 100 Mbps on a
              copper wire that cannot support more than 32 MHz (frequencies above this level create
              electromagnetic emissions). MLT-3 and LANs are discussed in Chapter 13.

              Summary of Line Coding Schemes
              We summarize in Table 4.1 the characteristics of the different schemes discussed.

              Table 4.1           Summary of line coding schemes

                                                        Bandwidth
                     Category              Scheme       (average)                             Characteristics
                  Unipolar                NRZ           B=N/2            Costly, no self-synchronization iflong Os or Is, DC
                                          NRZ-L         B=N/2            No self-synchronization if long Os or 1s, DC
                  Unipolar                NRZ-I         B=N/2            No self-synchronization for long aS, DC
                                          Biphase       B=N              Self-synchronization, no DC, high bandwidth

## SECTION 4.1            DIGITAL-TO-DIGITAL CONVERSION             115


Table 4.1     Summary of line coding schemes (continued)

                                Bandwidth
   Category         Scheme      (average)                                 Characteristics
 Bipolar           AMI          B=NI2             No self-synchronization for long OS, DC
                   2BIQ         B=N/4             No self-synchronization for long same double bits
 Multilevel        8B6T         B = 3N/4          Self-synchronization, no DC
                   4D-PAM5      B=N/8             Self-synchronization, no DC
 Multiline         MLT-3        B=N/3             No self-synchronization for long Os


Block Coding
We need redundancy to ensure synchronization and to provide some kind of inherent
error detecting. Block coding can give us this redundancy and improve the perfor-
mance of line coding. In general, block coding changes a block of m bits into a block
of n bits, where n is larger than m. Block coding is referred to as an mB/nB encoding
technique.

                   Block coding is normally referred to as mBlnB coding;
                      it replaces each m~bit group with an n~bit group.

     The slash in block encoding (for example, 4B/5B) distinguishes block encoding
from multilevel encoding (for example, 8B6T), which is written without a slash. Block
coding normally involves three steps: division, substitution, and combination. In the
division step, a sequence of bits is divided into groups of m bits. For example, in 4B/5B
encoding, the original bit sequence is divided into 4-bit groups. The heart of block cod-
ing is the substitution step. In this step, we substitute an m-bit group for an n-bit group.
For example, in 4B/5B encoding we substitute a 4-bit code for a 5-bit group. Finally,
the n-bit groups are combined together to form a stream. The new stream has more bits
than the original bits. Figure 4.14 shows the procedure.


Figure 4.14      Block coding concept

                                 Division of a stream into m-bit groups
                               m bits        m bits               m bits
                             [110"'111000'''11 ••• 1010'''11

                                                  11
                                              m&-to-nB
                                             substitution

                                                  Jl
                          1010"'10111000'''00 1 1... 1° 11 ''.1111
                             n bits    n bits            n bits
                                  Combining n-bit groups into a stream

116   CHAPTER 4    DIGITAL TRANSMISSION


             4B/5B
             The four binary/five binary (4B/5B) coding scheme was designed to be used in com-
             bination with NRZ-I. Recall that NRZ-I has a good signal rate, one-half that of the
             biphase, but it has a synchronization problem. A long sequence of as can make the
             receiver clock lose synchronization. One solution is to change the bit stream, prior to
             encoding with NRZ-I, so that it does not have a long stream of as. The 4B/5B scheme
             achieves this goal. The block-coded stream does not have more that three consecutive
             as, as we will see later. At the receiver, the NRZ- I encoded digital signal is first
             decoded into a stream of bits and then decoded to remove the redundancy. Figure 4.15
             shows the idea.


             Figure 4.15      Using block coding 4B/5B with NRZ-I line coding scheme

                         Sender                                                          Receiver


                                                      Digital signal

                                                   --::Ft:F-
                                                           Link


                  In 4B/5B, the 5-bit output that replaces the 4-bit input has no more than one leading
             zero (left bit) and no more than two trailing zeros (right bits). So when different groups
             are combined to make a new sequence, there are never more than three consecutive         as.
             (Note that NRZ-I has no problem with sequences of Is.) Table 4.2 shows the corre-
             sponding pairs used in 4B/5B encoding. Note that the first two columns pair a 4-bit
             group with a 5-bit group. A group of 4 bits can have only 16 different combinations
             while a group of 5 bits can have 32 different combinations. This means that there are 16
             groups that are not used for 4B/5B encoding. Some of these unused groups are used for
             control purposes; the others are not used at all. The latter provide a kind of error detec-
             tion. If a 5-bit group arrives that belongs to the unused portion of the table, the receiver
             knows that there is an error in the transmission.

              Table 4.2 4B/5B mapping codes
                  Data Sequence    Encoded Sequence               Control Sequence     Encoded Sequence
                      0000                11110           Q (Quiet)                         00000
                      0001               01001            I (Idle)                          11111
                      0010                10100           H (Halt)                          00100
                      0011                10101           J (Start delimiter)               11000
                      0100               01010            K (Start delimiter)               10001
                      0101               01011            T (End delimiter)                 01101

## SECTION 4.1          DIGITAL-TO-DIGITAL CONVERSION       117


Table 4.2 4B/5B mapping codes (continued)

  Data Sequence      Encoded Sequence                 Control Sequence   Encoded Sequence
       0110                 01110                 S (Set)                     11001
       0111                 01111                 R (Reset)                   00111
       1000                 10010
       1001                 10011
       1010                 10110
       1011                 10111
       1100                 11 010
       1101                 11011
       1110                 11100
       1111                 11101


     Figure 4.16 shows an example of substitution in 4B/5B coding. 4B/5B encoding
solves the problem of synchronization and overcomes one of the deficiencies of NRZ-1.
However, we need to remember that it increases the signal rate of NRZ-1. The redun-
dant bits add 20 percent more baud. Still, the result is less than the biphase scheme
which has a signal rate of 2 times that of NRZ-1. However, 4B/5B block encoding does
not solve the DC component problem of NRZ-1. If a DC component is unacceptable, we
need to use biphase or bipolar encoding.


Figure 4.16    Substitution in 48/5B block coding

                                              4-bit blocks

                          I 1 1 1 1 I ••• I 000 I I I 0000 1
                                                                     I


                                              I                  I
           11111    ~l   1 1 1 10    LI
                                      ':
                                           1110 1
                                            "0'
                                                                          oooo~    r
                                              5-bit blocks


Example 4.5
We need to send data at a 1-Mbps rate. What is the minimum required bandwidth, using a combi-
nation of 4B/5B and NRZ-I or Manchester coding?

Solution
First 4B/5B block coding increases the bit rate to 1.25 Mbps. The minimum bandwidth using
NRZ-I is NI2 or 625 kHz. The Manchester scheme needs a minimum bandwidth of 1 MHz. The
first choice needs a lower bandwidth, but has a DC component problem; the second choice needs
a higher bandwidth, but does not have a DC component problem.

118   CHAPTER 4   DIGITAL TRANSMISSION


             8RIlOR
             The eight binary/ten binary (SBIlOB) encoding is similar to 4B/5B encoding except
             that a group of 8 bits of data is now substituted by a lO-bit code. It provides greater
             error detection capability than 4B/5B. The 8BIlOB block coding is actually a combina-
             tion of 5B/6B and 3B/4B encoding, as shown in Figure 4.17.

             Figure 4.17 8B/lOB block encoding

                                         8B/IOB encoder


                                                                          &-+--+-IO-bit block
                           8-bit block


                  The most five significant bits of a 10-bit block is fed into the 5B/6B encoder; the
             least 3 significant bits is fed into a 3B/4B encoder. The split is done to simplify the
             mapping table. To prevent a long run of consecutive Os or Is, the code uses a disparity
             controller which keeps track of excess Os over Is (or Is over Os). If the bits in the cur-
             rent block create a disparity that contributes to the previous disparity (either direction),
             then each bit in the code is complemented (a 0 is changed to a 1 and a 1 is changed to a 0).
             The coding has 2 10 - 28 = 768 redundant groups that can be used for disparity checking
             and error detection. In general, the technique is superior to 4B/5B because of better
             built-in error-checking capability and better synchronization.

             Scramblin~
             Biphase schemes that are suitable for dedicated links between stations in a LAN are not
             suitable for long-distance communication because of their wide bandwidth requirement.
             The combination of block coding and NRZ line coding is not suitable for long-distance
             encoding either, because of the DC component. Bipolar AMI encoding, on the other
             hand, has a narrow bandwidth and does not create a DC component. However, a long
             sequence of Os upsets the synchronization. If we can find a way to avoid a long sequence
             of Os in the original stream, we can use bipolar AMI for long distances. We are looking
             for a technique that does not increase the number of bits and does provide synchroniza-
             tion. We are looking for a solution that substitutes long zero-level pulses with a combi-
             nation of other levels to provide synchronization. One solution is called scrambling. We
             modify part of the AMI rule to include scrambling, as shown in Figure 4.18. Note that
             scrambling, as opposed to block coding, is done at the same time as encoding. The
             system needs to insert the required pulses based on the defined scrambling rules. Two
             common scrambling techniques are B8ZS and HDB3.

             R8ZS
              Bipolar with S-zero substitution (BSZS) is commonly used in North America. In
              this technique, eight consecutive zero-level voltages are replaced by the sequence

## SECTION 4.1      DIGITAL-TO-DIGITAL CONVERSION                            119


Figure 4.18 AMI used with scrambling

                    Sender                                                            Receiver


                                           Violated digital signal

                                           --=ftF-


OOOVBOVB. The V in the sequence denotes violation; this is a nonzero voltage that
breaks an AMI rule of encoding (opposite polarity from the previous). The B in the
sequence denotes bipolm; which means a nonzero level voltage in accordance with the
AMI rule. There are two cases, as shown in Figure 4.19.


Figure 4.19     Two cases ofB8ZS scrambling technique


                                                               I       000          000          0     ~
                                                                   :t i:t
                                                                       "j
                                                                                    ::
                                                                                    I' t
                                                                                                ~ ~ i ,'" :
                                                                                                j  1       1
                                                                   1    t   I       I B I       I VI   ':1
                                                                   I    {   I   I                          1
                                                                   10 10 101                0              I


         a. Previous level is positive.                  b. Previous level is negative.


     Note that the scrambling in this case does not change the bit rate. Also, the tech-
nique balances the positive and negative voltage levels (two positives and two nega-
tives), which means that the DC balance is maintained. Note that the substitution may
change the polarity of a 1 because, after the substitution, AMI needs to follow its rules.


                  B8ZS substitutes eight consecutive zeros with OOOVBOVB.


     One more point is worth mentioning. The letter V (violation) or B (bipolar) here is
relative. The V means the same polarity as the polarity of the previous nonzero pulse; B
means the polarity opposite to the polarity of the previous nonzero pulse.

HDB3
High-density bipolar 3-zero (HDB3) is commonly used outside of North America. In this
technique, which is more conservative than B8ZS, four consecutive zero-level voltages are
replaced with a sequence of OOOV or BOO\: The reason for two different substitutions is to

120   CHAPTER 4     DIGITAL TRANSMISSION


             maintain the even number of nonzero pulses after each substitution. The two rules can be
             stated as follows:
                  1. If the number of nonzero pulses after the last substitution is odd, the substitution
                     pattern will be OOOV, which makes the total number of nonzero pulses even.
                  2. If the number of nonzero pulses after the last substitution is even, the substitution
                     pattern will be BOOV, which makes the total number of nonzero pulses even.
             Figure 4.20 shows an example.


              Figure 4.20 Different situations in HDB3 scrambling technique

                                                 First               Second                 Third
                                              substitution         substitution          substitution


                                          t
                                         Even
                                                             t t
                                                        Even Odd                  Even                  Even


                   There are several points we need to mention here. First, before the first substitu-
              tion, the number of nonzero pulses is even, so the first substitution is BODY. After this
              substitution, the polarity of the 1 bit is changed because the AMI scheme, after each
              substitution, must follow its own rule. After this bit, we need another substitution,
              which is OOOV because we have only one nonzero pulse (odd) after the last substitution.
              The third substitution is BOOV because there are no nonzero pulses after the second
              substitution (even).


                          HDB3 substitutes four consecutive zeros with OOOV or BOOV depending
                              on the number of nonzero pulses after the last substitution.


## 4.2        ANALOG-TO-DIGITAL CONVERSION
              The techniques described in Section 4.1 convert digital data to digital signals. Some-
              times, however, we have an analog signal such as one created by a microphone or cam-
              era. We have seen in Chapter 3 that a digital signal is superior to an analog signal. The
              tendency today is to change an analog signal to digital data. In this section we describe
              two techniques, pulse code modulation and delta modulation. After the digital data are
              created (digitization), we can use one of the techniques described in Section 4.1 to con-
              vert the digital data to a digital signal.

## SECTION 4.2             ANALOG-TO-DIGITAL CONVERSION                                  121


Pulse Code Modulation (PCM)
The most common technique to change an analog signal to digital data (digitization)
is called pulse code modulation (PCM). A PCM encoder has three processes, as shown
in Figure 4.21.


Figure 4.21     Components of PCM encoder

                                                                 Quantized signal

                                                          ~'-'-T
                                                            !    .• ··1······   :t i ~ 'i
                                                          t=lJl::I::=t=J;.:;=~,
                         peM encoder


  ~. HAnalog signal
                            Sampling;            I   Quantizing         J-         Encoding   J4   11 "'11°°1
                                                                                                    Digital data


                              tuL            I
                                       PAM signal
                                                 .    I    I.,


 1. The analog signal is sampled.
 2. The sampled signal is quantized.
 3. The quantized values are encoded as streams of bits.

Sampling
The first step in PCM is sampling. The analog signal is sampled every Ts s, where Ts is
the sample interval or period. The inverse of the sampling interval is called the sam-
pling rate or sampling frequency and denoted by is, where is = IITs' There are three
sampling methods-ideal, natural, and flat-top-as shown in Figure 4.22.
     In ideal sampling, pulses from the analog signal are sampled. This is an ideal sam-
pling method and cannot be easily implemented. In natural sampling, a high-speed
switch is turned on for only the small period of time when the sampling occurs. The
result is a sequence of samples that retains the shape of the analog signal. The most
common sampling method, called sample and hold, however, creates flat-top samples
by using a circuit.
     The sampling process is sometimes referred to as pulse amplitude modulation
(PAM). We need to remember, however, that the result is still an analog signal with
nonintegral values.
Sampling Rate One important consideration is the sampling rate or frequency. What
are the restrictions on Ts ? This question was elegantly answered by Nyquist. According
to the Nyquist theorem, to reproduce the original analog signal, one necessary condition
is that the sampling rate be at least twice the highest frequency in the original signal.

122   CHAPTER 4    DIGITAL TRANSMISSION


             Figure 4.22           Three different sampling methods for PCM


                  Amplitude                                                         Amplitude

                                          ,~Analog signal                                                /           Analog signal
                                            ...                                                              ...
                                                                         Time

                       "         ~s


               a. Ideal sampling                                                   b. Natural sampling

                                                   Amplitude


                                                  c. Flat-top sampling


                                   According to the Nyquist theorem, the sampling rate must be
                                   at least 2 times the highest frequency contained in the signal.

                   We need to elaborate on the theorem at this point. First, we can sample a signal
              only if the signal is band-limited. In other words, a signal with an infinite bandwidth
              cannot be sampled. Second, the sampling rate must be at least 2 times the highest fre-
              quency, not the bandwidth. If the analog signal is low-pass, the bandwidth and the
              highest frequency are the same value. If the analog signal is bandpass, the bandwidth
              value is lower than the value of the maximum frequency. Figure 4.23 shows the value
              of the sampling rate for two types of signals.


              Figure 4.23          Nyquist sampling rate for low-pass and bandpass signals
             -------------------------------------

                              Amplitude

                                                                  Nyquist rate = 2 x fm"x

                                                                     Low-pass signal

                                f rnin                                                                             f max Frequency

                              Amplitude

                                                                  Nyquist rate =2 x fmax

                                                                     Bandpass signal

                                  o                       f min                                                         Frequency

## SECTION 4.2   ANALOG-TO-DIGITAL CONVERSION                                                     123


Example 4.6
For an intuitive example of the Nyquist theorem, let us sample a simple sine wave at three sam-
pling rates: fs = 4f (2 times the Nyquist rate )'/s = 2f (Nyquist rate), and f s = f (one-half the
Nyquist rate). Figure 4.24 shows the sampling and the subsequent recovery of the signal.


Figure 4.24 Recovery of a sampled sine wave for different sampling rates


                                                                 •...
                                                                 ,                      ,     •....                   •...
                                                                                                                      ,
                                                        ,
                                                            ,,
                                                                         .   ,, ,,,
                                                                                   , ,,,
                                                                                                  .,            ,,
                                                                                                                   ,,,         .
                                                                              .¥,                      ,      ,,


     a. Nyquist rate sampling:fs = 2f
                                                                                                       '".'

                                                                 ,.,.
                                                        ,
                                                            ,,       ,
                                                                         '           ,;   ".
                                                                                          ,     ,,
                                                                                                                      •
                                                                                                                    ,, ,,
                                                                                                                  ,, , ,


     b. Oversampling:fs = 4f


                                                        .....        ,

                                                                                     "
                                                                                                                          .'
                                                                                                       '   ....
     c. Undersampling: f s = f


      It can be seen that sampling at the Nyquist rate can create a good approximation of the orig-
inal sine wave (part a). Oversampling in part b can also create the same approximation, but it is
redundant and unnecessary. Sampling below the Nyquist rate (part c) does not produce a signal
that looks like the original sine wave.


Example 4.7
As an interesting example, let us see what happens if we sample a periodic event such as the revolu-
tion of a hand of a clock. The second hand of a clock has a period of 60 s. According to the Nyquist
theorem, we need to sample the hand (take and send a picture) every 30 s (Ts = ~ Tor f s = 2f). In
Figure 4.25a, the sample points, in order, are 12, 6, 12, 6, 12, and 6. The receiver of the samples
cannot tell if the clock is moving forward or backward. In part b, we sample at double the Nyquist
rate (every 15 s). The sample points, in order, are 12,3,6, 9, and 12. The clock is moving forward.
In part c, we sample below the Nyquist rate (Ts = ~ Torfs = ~f). The sample points, in order, are 12,
9,6,3, and 12. Although the clock is moving forward, the receiver thinks that the clock is moving
backward.

124   CHAPTER 4   DIGITAL TRANSMISSION


             Figure 4.25 Sampling of a clock with only one hand

                                                                                        Samples can mean that
                                                                                        the clock is moving
                                                                                        either forward or
                                                                                        backward.
                                                                                        (12-6-12-6-12)

                  a. Sampling at Nyquist rate:   T !T
                                                 s=


                   rnG2
                   U 9:-3 \JY~U                       ~~rn                              Samples show clock
                                                                                        is moving forward.
                                                                                        (12·3-6-9-12)


                  b. Oversampling (above Nyquist rate): Ts = ~T


                   rn~~~rn
                   ug\J)~U
                                                                                        Samples show clock
                                                                                        is moving backward.
                                                                                        (12-9-6-3-12)


                  c. Undersampling (below Nyquist rate): Ts = ~T


             Example 4.8
              An example related to Example 4.7 is the seemingly backward rotation of the wheels of a forward-
              moving car in a movie. This can be explained by undersampling. A movie is filmed at 24 frames
              per second. If a wheel is rotating more than 12 times per second, the undersampling creates the
              impression of a backward rotation.


              Example 4.9
              Telephone companies digitize voice by assuming a maximum frequency of 4000 Hz. The sam-
              pling rate therefore is 8000 samples per second.


              Example 4.10
              A complex low-pass signal has a bandwidth of 200 kHz. What is the minimum sampling rate for
              this signal?

              Solution
              The bandwidth of a low-pass signal is between 0 andj, where f is the maximum frequency in the
              signal. Therefore, we can sample this signal at 2 times the highest frequency (200 kHz). The sam-
              pling rate is therefore 400,000 samples per second.


              Example 4.1 J
              A complex bandpass signal has a bandwidth of 200 kHz. What is the minimum sampling rate for
              this signal?

## SECTION 4.2            ANALOG-TO-DIGITAL CONVERSION                                125


Solution
We cannot find the minimum sampling rate in this case because we do not know where the band-
width starts or ends. We do not know the maximum frequency in the signal.

Quantization
The result of sampling is a series of pulses with amplitude values between the maxi-
mum and minimum amplitudes of the signal. The set of amplitudes can be infinite with
nonintegral values between the two limits. These values cannot be used in the encoding
process. The following are the steps in quantization:
 1. We assume that the original analog signal has instantaneous amplitudes between
    Vmin and Vmax'
 2. We divide the range into L zones, each of height ~ (delta).
                                                        Vmax      -
                                                                rnin   V
                                                 ~    = -==-:::--=
                                                             L

 3. We assign quantized values of 0 to L - I to the midpoint of each zone.
 4. We approximate the value of the sample amplitude to the quantized values.
As a simple example, assume that we have a sampled signal and the sample ampli-
tudes are between -20 and +20 V. We decide to have eight levels (L = 8). This means
that ~ = 5 V. Figure 4.26 shows this example.

Figure 4.26          Quantization and encoding of a sampled signal

  Quantization        Normalized
  codes                amplitude

                       46.
      7                                                         19.7
                       36.

                       26.                                                       11.0
      5
## 7.5

                         Ol--------L...---L...------lL...-----''------,,---,-----,-----,_
                                                                                                               ,1
                                                                                                              1
                                                                                      Time
      2                -6. -6.1                                 -5.5             -6,0
                      -26.                                                     -9.4
                                                                                                    -11.3 '
                      -36.

                      -4.11
  Normalized             -1.22     1.50        3.24      3.94              2.20         -1.10   -2.26    -1.88      -1.20
  PAM values
  Normalized            -1.50      1.50        3.50      3.50              2.50         -1.50   -2.50    -1.50      -1.50
  quantized values
  Normalized            -0.38       o         +0.26     -0.44          +0.30            -0.40   -0.24    +0.38      -0.30
  error
  Quantization code          2      5           7           7               6             2                    2      2

  Encoded words           010      101         111       111               110           010     001          010    ow

126   CHAPTER 4   DIGITAL TRANSMISSION


                  We have shown only nine samples using ideal sampling (for simplicity). The
             value at the top of each sample in the graph shows the actual amplitude. In the chart,
             the first row is the normalized value for each sample (actual amplitude/.:1). The quan-
             tization process selects the quantization value from the middle of each zone. This
             means that the normalized quantized values (second row) are different from the nor-
             malized amplitudes. The difference is called the normalized error (third row). The
             fourth row is the quantization code for each sample based on the quantization levels
             at the left of the graph. The encoded words (fifth row) are the final products of the
             conversion.
             Quantization Levels In the previous example, we showed eight quantization levels.
             The choice of L, the number of levels, depends on the range of the amplitudes of the
             analog signal and how accurately we need to recover the signal. If the amplitude of a
             signal fluctuates between two values only, we need only two levels; if the signal, like
             voice, has many amplitude values, we need more quantization levels. In audio digitiz-
             ing, L is normally chosen to be 256; in video it is normally thousands. Choosing
             lower values of L increases the quantization error if there is a lot of fluctuation in the
             signal.
             Quantization Error One important issue is the error created in the quantization pro-
             cess. (Later, we will see how this affects high-speed modems.) Quantization is an
             approximation process. The input values to the quantizer are the real values; the output
             values are the approximated values. The output values are chosen to be the middle
             value in the zone. If the input value is also at the middle of the zone, there is no quanti-
             zation error; otherwise, there is an error. In the previous example, the normalized
             amplitude of the third sample is 3.24, but the normalized quantized value is 3.50. This
             means that there is an error of +0.26. The value of the error for any sample is less than
             .:112. In other words, we have -.:112 -::;; error -::;; .:112.
                    The quantization error changes the signal-to-noise ratio of the signal, which in turn
             reduces the upper limit capacity according to Shannon.
                    It can be proven that the contribution of the quantization error to the SNRdB of
             the signal depends on the number of quantization levels L, or the bits per sample nb' as
             shown in the following formula:

                                               SNRdB =6.02nb + 1.76 dB


              Example 4.12
              What is the SNRdB in the example of Figure 4.26?

              Solution
              We can use the formula to find the quantization. We have eight levels and 3 bits per sample, so
              SNRdB = 6.02(3) + 1.76 = 19.82 dB. Increasing the number of levels increases the SNR.


              Example 4.13
              A telephone subscriber line must have an SN~B above 40. What is the minimum number of bits
              per sample?

## SECTION 4.2       ANALOG-TO-DIGITAL CONVERSION            127


Solution
We can calculate the number of bits as

                          SN~:::: 6.02nb + 1.76:::: 40    ..... n:::: 6.35

Telephone companies usually assign 7 or 8 bits per sample.

Uniform Versus Nonuniform Quantization For many applications, the distribu-
tion of the instantaneous amplitudes in the analog signal is not uniform. Changes in
amplitude often occur more frequently in the lower amplitudes than in the higher
ones. For these types of applications it is better to use nonuniform zones. In other
words, the height of ~ is not fixed; it is greater near the lower amplitudes and less
near the higher amplitudes. Nonuniform quantization can also be achieved by using a
process called companding and expanding. The signal is companded at the sender
before conversion; it is expanded at the receiver after conversion. Companding means
reducing the instantaneous voltage amplitude for large values; expanding is the oppo-
site process. Companding gives greater weight to strong signals and less weight to
weak ones. It has been proved that nonuniform quantization effectively reduces the
SNRdB of quantization.

Encoding
The last step in PCM is encoding. After each sample is quantized and the number of
bits per sample is decided, each sample can be changed to an llb-bit code word. In Fig-
ure 4.26 the encoded words are shown in the last row. A quantization code of 2 is
encoded as 010; 5 is encoded as 101; and so on. Note that the number of bits for each
sample is determined from the number of quantization levels. If the number of quanti-
zation levels is L, the number of bits is llb = log2 L. In our example L is 8 and llb is
therefore 3. The bit rate can be found from the formula


               Bit rate :::: sampling rate x number of bits per sample:::: is x nb


Example 4.14
We want to digitize the human voice. What is the bit rate, assuming 8 bits per sample?

Solution
The human voice normally contains frequencies from 0 to 4000 Hz. So the sampling rate and bit
rate are calculated as follows:


                          Sampling rate :::: 4000 x 2 :::: 8000 samples/s
                          Bit rate == 8000 x 8 :::: 64,000 bps == 64 kbps


Original Signal Recovery
The recovery of the original signal requires the PCM decoder. The decoder first uses
circuitry to convert the code words into a pulse that holds the amplitude until the next
pulse. After the staircase signal is completed, it is passed through a low-pass filter to

128   CHAPTER 4     DIGITAL TRANSMISSION


             smooth the staircase signal into an analog signal. The filter has the same cutoff fre-
             quency as the original signal at the sender. If the signal has been sampled at (or
             greater than) the Nyquist sampling rate and if there are enough quantization levels,
             the original signal will be recreated. Note that the maximum and minimum values of
             the original signal can be achieved by using amplification. Figure 4.27 shows the
             simplified process.


             Figure 4.27     Components of a PCM decoder


                                 Amplitude


                                     ~TI~'
                               PCM decoder
                                                                         Amplitude
                                                                                               Analog signal
                                                                                             ......... ,
                                                                                                           ..,
                                                                   %'
                                                       "
                                  Make and                                              ''
                  !lloool100r- -+ connect
                                   samples
                                                        Low-pass
                                                          filter
                                                                             ,
                                                                                 ,'
                                                                                    "                        ,   .,,                Time

                                                                                                                         -.- .. , .. '
                    Digital data
                                                                                                                     ,


             PCM Bandwidth
             Suppose we are given the bandwidth of a low-pass analog signal. If we then digitize the
             signal, what is the new minimum bandwidth of the channel that can pass this digitized
             signal? We have said that the minimum bandwidth of a line-encoded signal is Bmin = ex
             N x (lIr). We substitute the value of N in this formula:

                                             1 1 1
                               B min = c x N x - = c X nb xis x - =c x nb x 2 x Banalog x -
                                              r                r                                                 r


              When lIr = I (for a NRZ or bipolar signal) and c = (12) (the average situation), the
              minimum bandwidth is


              This means the minimum bandwidth of the digital signal is nb times greater than the
              bandwidth of the analog signal. This is the price we pay for digitization.

              Example 4.15
              We have a low-pass analog signal of 4 kHz. If we send the analog signal, we need a channel with
              a minimum bandwidth of 4 kHz. If we digitize the signal and send 8 bits per sample, we need a
              channel with a minimum bandwidth of 8 X 4 kHz = 32 kHz.

## SECTION 4.2      ANALOG-TO-DIGITAL CONVERSION            129


Maximum Data Rate of a Channel
In Chapter 3, we discussed the Nyquist theorem which gives the data rate of a channel
as N max = 2 x B x log2 L. We can deduce this rate from the Nyquist sampling theorem
by using the following arguments.
 1. We assume that the available channel is low-pass with bandwidth B.
 2. We assume that the digital signal we want to send has L levels, where each level is
    a signal element. This means r = 1/10g2 L.
 3. We first pass the digital signal through a low-pass filter to cut off the frequencies
    above B Hz.
 4. We treat the resulting signal as an analog signal and sample it at 2 x B samples per
    second and quantize it using L levels. Additional quantization levels are useless
    because the signal originally had L levels.
 S. The resulting bit rate is N = fs x nb = 2 x B x log2 L. This is the maximum band-
    width; if the case factor c increases, the data rate is reduced.

                                 N max ::::: 2 x B x logzL bps


Minimum Required Bandwidth
The previous argument can give us the minimum bandwidth if the data rate and the
number of signal levels are fixed. We can say

                                   B . =       N          Hz
                                    mm     2xlogz L


Delta Modulation (DM)
PCM is a very complex technique. Other techniques have been developed to reduce
the complexity of PCM. The simplest is delta modulation. PCM finds the value of the
signal amplitude for each sample; DM finds the change from the previous sample. Fig-
ure 4.28 shows the process. Note that there are no code words here; bits are sent one
after another.

Figure 4.28     The process of delta modulation

              Amplitude


               ~.
                o
               T

         ?enerated
        bmary data .1_~_1                         0   0   0    0   0   0   1_1. Time

130   CHAPTER 4   DIGITAL TRANSMISSION


             Modulator
             The modulator is used at the sender site to create a stream of bits from an analog signal.
             The process records the small positive or negative changes, called delta O. If the delta is
             positive, the process records a I; if it is negative, the process records a O. However, the
             process needs a base against which the analog signal is compared. The modulator
             builds a second signal that resembles a staircase. Finding the change is then reduced to
             comparing the input signal with the gradually made staircase signal. Figure 4.29 shows
             a diagram of the process.


             Figure 4.29 Delta modulation components

                                           OM modulator


                    ~
                   t~ . . I---+---~compraor
                                      a     -----.-+-~I I •.. I 100
                                                             t   ...
                                                                                            Digital data
                      Analog signal


                  The modulator, at each sampling interval, compares the value of the analog signal
             with the last value of the staircase signal. If the amplitude of the analog signal is larger,
             the next bit in the digital data is 1; otherwise, it is O. The output of the comparator, how-
             ever, also makes the staircase itself. If the next bit is I, the staircase maker moves the
             last point of the staircase signal 0 up; it the next bit is 0, it moves it 0 down. Note that we
             need a delay unit to hold the staircase function for a period between two comparisons.

             Demodulator
             The demodulator takes the digital data and, using the staircase maker and the delay
             unit, creates the analog signal. The created analog signal, however, needs to pass
             through a low-pass filter for smoothing. Figure 4.30 shows the schematic diagram.


             Figure 4.30 Delta demodulation components

                                        OM demodulator


                       11"'1100
                         Digital data
                                                                                   Analog signal

## SECTION 4.3   TRANSMISSION MODES        131


Adaptive DA1
A better performance can be achieved if the value of 0 is not fixed. In adaptive delta
modulation, the value of 0 changes according to the amplitude of the analog signal.

Quantization Error
It is obvious that DM is not perfect. Quantization error is always introduced in the pro-
cess. The quantization error of DM, however, is much less than that for PCM.


## 4.3     TRANSMISSION MODES
Of primary concern when we are considering the transmission of data from one device
to another is the wiring, and of primary concern when we are considering the wiring is
the data stream. Do we send 1 bit at a time; or do we group bits into larger groups and,
if so, how? The transmission of binary data across a link can be accomplished in either
parallel or serial mode. In parallel mode, multiple bits are sent with each clock tick.
In serial mode, 1 bit is sent with each clock tick. While there is only one way to send
parallel data, there are three subclasses of serial transmission: asynchronous, synchro-
nous, and isochronous (see Figure 4.31).


Figure 4.31    Data transmission and modes


                             Data transmission


Parallel Transmission
Binary data, consisting of Is and Os, may be organized into groups of n bits each.
Computers produce and consume data in groups of bits much as we conceive of and use
spoken language in the form of words rather than letters. By grouping, we can send
data n bits at a time instead of 1. This is called parallel transmission.
     The mechanism for parallel transmission is a conceptually simple one: Use n wires
to send n bits at one time. That way each bit has its own wire, and all n bits of one
group can be transmitted with each clock tick from one device to another. Figure 4.32
shows how parallel transmission works for n = 8. Typically, the eight wires are bundled
in a cable with a connector at each end.
     The advantage of parallel transmission is speed. All else being equal, parallel
transmission can increase the transfer speed by a factor of n over serial transmission.

132   CHAPTER 4   DIGITAL TRANSMISSION


              Figure 4.32   Parallel transmission


                                               The 8 bits are sent together

                                                           ,--" j/                                 ,/'-,.
                                                       I    v
                                                            <
                                                                    \                          I            \
                                               f                                               I                \
                                                                        1
                                                            <           1
                                               I
                                               I            v
                                Sender                                  I                                               Receiver
                                                            v
                                               I                        j
                                                            v           I
                                                   \                                           \
                                                            <
                                                       \            I                      A'\  /
                                                           '::/                         / / "-J
                                                                              We need eight lines


              But there is a significant disadvantage: cost. Parallel transmission requires n communi-
              cation lines (wires in the example) just to transmit the data stream. Because this is
              expensive, parallel transmission is usually limited to short distances.

              Serial Transmission
              In serial transmission one bit follows another, so we need only one communica-
              tion channel rather than n to transmit data between two communicating devices (see
              Figure 4.33).


              Figure 4.33   Serial transmission


                                                                            The 8 bits are sent
                                                                            one after another.
                                           o                                                                        o
                                           1                                                                        1
                                           1                    o                 00010                             1
                                 Sender    0 -1-----------+1
                                           o                                                                        g Receiver
                                           o                                                                        o
                                           1                                 We need only                           1
                                           o                                one line (wire).                        o

                                          Parallel/serial                                           Serial/parallel
                                            converter                                                 converter


                   The advantage of serial over parallel transmission is that with only one communi-
              cation channel, serial transmission reduces the cost of transmission over parallel by
              roughly a factor of n.
                   Since communication within devices is parallel, conversion devices are required at
              the interface between the sender and the line (parallel-to-serial) and between the line
              and the receiver (serial-to-parallel).
                   Serial transmission occurs in one of three ways: asynchronous, synchronous, and
              isochronous.

## SECTION 4.3      TRANSMISSION MODES           133


Asynchronous Transmission
Asynchronous transmission is so named because the timing of a signal is unimportant.
Instead, information is received and translated by agreed upon patterns. As long as those
patterns are followed, the receiving device can retrieve the information without regard
to the rhythm in which it is sent. Patterns are based on grouping the bit stream into
bytes. Each group, usually 8 bits, is sent along the link as a unit. The sending system
handles each group independently, relaying it to the link whenever ready, without regard
to a timer.
      Without synchronization, the receiver cannot use timing to predict when the next
group will arrive. To alert the receiver to the arrival of a new group, therefore, an extra
bit is added to the beginning of each byte. This bit, usually a 0, is called the start bit.
To let the receiver know that the byte is finished, 1 or more additional bits are appended
to the end of the byte. These bits, usually I s, are called stop bits. By this method, each
byte is increased in size to at least 10 bits, of which 8 bits is information and 2 bits or
more are signals to the receiver. In addition, the transmission of each byte may then be
followed by a gap of varying duration. This gap can be represented either by an idle
channel or by a stream of additional stop bits.

   In asynchronous transmission, we send 1 start bit (0) at the beginning and 1 or more
       stop bits (Is) at the end of each byte. There may be a gap between each byte.


     The start and stop bits and the gap alert the receiver to the beginning and end of
each byte and allow it to synchronize with the data stream. This mechanism is called
asynchronous because, at the byte level, the sender and receiver do not have to be syn-
chronized. But within each byte, the receiver must still be synchronized with the
incoming bit stream. That is, some synchronization is required, but only for the dura-
tion of a single byte. The receiving device resynchronizes at the onset of each new byte.
When the receiver detects a start bit, it sets a timer and begins counting bits as they
come in. After n bits, the receiver looks for a stop bit. As soon as it detects the stop bit,
it waits until it detects the next start bit.

               Asynchronous here means "asynchronous at the byte level;'
              but the bits are still synchronized; their durations are the same.

     Figure 4.34 is a schematic illustration of asynchronous transmission. In this exam-
ple, the start bits are as, the stop bits are 1s, and the gap is represented by an idle line
rather than by additional stop bits.
     The addition of stop and start bits and the insertion of gaps into the bit stream
make asynchronous transmission slower than forms of transmission that can operate
without the addition of control information. But it is cheap and effective, two advan-
tages that make it an attractive choice for situations such as low-speed communication.
For example, the connection of a keyboard to a computer is a natural application for
asynchronous transmission. A user types only one character at a time, types extremely
slowly in data processing terms, and leaves unpredictable gaps of time between each
character.

134   CHAPTER 4   DIGITAL TRANSMISSION


             Figure 4.34     Asynchronous transmission

                                                               Direction of flow


                                                           "or ~     n",      ~rt bit
                                                             ~1'_111l1011          0

                       Sender                                                                           Receiver
                                  01 101   I 0 I @j 1111101 1 0 W000101 11 0 11 11 1
                                                ~~ r ~~
                                                                   Gaps between
                                                                    data units


             Synchronous Transmission
             In synchronous transmission, the bit stream is combined into longer "frames," which
             may contain multiple bytes. Each byte, however, is introduced onto the transmission
             link without a gap between it and the next one. It is left to the receiver to separate the
             bit stream into bytes for decoding purposes. In other words, data are transmitted as an
             unbroken string of 1s and Os, and the receiver separates that string into the bytes, or
             characters, it needs to reconstruct the information.

                  In synchronous transmission, we send bits one after another without start or stop
                         bits or gaps. It is the responsibility of the receiver to group the bits.

                  Figure 4.35 gives a schematic illustration of synchronous transmission. We have
             drawn in the divisions between bytes. In reality, those divisions do not exist; the sender
             puts its data onto the line as one long string. If the sender wishes to send data in separate
             bursts, the gaps between bursts must be filled with a special sequence of Os and Is that
             means idle. The receiver counts the bits as they arrive and groups them in 8-bit units.


              Figure 4.35       Synchronous transmission


                                                               Direction of flow

                                                   Frame                                      Frame
                                                                                              1,----tReceiver
                       Sender     1 10 1 I I   I   111111011111110110       I··· j 111101111 11 1 1 1


                   Without gaps and start and stop bits, there is no built-in mechanism to help the
              receiving device adjust its bit synchronization midstream. Timing becomes very impor-
              tant, therefore, because the accuracy of the received information is completely dependent
              on the ability of the receiving device to keep an accurate count of the bits as they come in.

## SECTION 4.5     KEY TERMS       135


     The advantage of synchronous transmission is speed. With no extra bits or gaps to
introduce at the sending end and remove at the receiving end, and, by extension, with
fewer bits to move across the link, synchronous transmission is faster than asynchro-
nous transmission. For this reason, it is more useful for high-speed applications such as
the transmission of data from one computer to another. Byte synchronization is accom-
plished in the data link layer.
     We need to emphasize one point here. Although there is no gap between characters
in synchronous serial transmission, there may be uneven gaps between frames.

Isochronous
In real-time audio and video, in which uneven delays between frames are not accept-
able, synchronous transmission fails. For example, TV images are broadcast at the rate
of 30 images per second; they must be viewed at the same rate. If each image is sent
by using one or more frames, there should be no delays between frames. For this type
of application, synchronization between characters is not enough; the entire stream of
bits must be synchronized. The isochronous transmission guarantees that the data
arrive at a fixed rate.


## 4.4     RECOMMENDED READING
For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [...] refer to the reference list at the end of the text.

Books
Digital to digital conversion is discussed in Chapter 7 of [Pea92], Chapter 3 of
[CouOl], and Section 5.1 of [Sta04]. Sampling is discussed in Chapters 15, 16, 17, and
18 of [Pea92], Chapter 3 of [CouO!], and Section 5.3 of [Sta04]. [Hsu03] gives a good
mathematical approach to modulation and sampling. More advanced materials can be
found in [Ber96].


## 4.5     KEY TERMS
adaptive delta modulation                      bit rate
alternate mark inversion (AMI)                 block coding
analog-to-digital conversion                   companding and expanding
asynchronous transmission                      data element
baseline                                       data rate
baseline wandering                             DC component
baud rate                                      delta modulation (DM)
biphase                                        differential Manchester
bipolar                                        digital-to-digital conversion
bipolar with 8-zero substitution (B8ZS)        digitization

136   CHAPTER 4   DIGITAL TRANSMISSION


             eight binary/ten binary (8B/lOB)                 pulse amplitude modulation (PAM)
             eight-binary, six-ternary (8B6T)                 pulse code modulation (PCM)
             four binary/five binary (4B/5B)                  pulse rate
             four dimensional, five-level pulse               quantization
                amplitude modulation (4D-PAM5)                quantization error
             high-density bipolar 3-zero (HDB3)               return to zero (RZ)
             isochronous transmission                         sampling
             line coding                                      sampling rate
             Manchester                                       scrambling
             modulation rate                                  self-synchronizing
             multilevel binary                                serial transmission
             multiline transmission, 3 level (MLT-3)          signal element
              nonreturn to zero (NRZ)                         signal rate
             nonreturn to zero, invert (NRZ-I)                start bit
             nonreturn to zero, level (NRZ-L)                 stop bit
             Nyquist theorem                                  synchronous transmission
             parallel transmission                            transmission mode
             polar                                            two-binary, one quaternary (2B I Q)
             pseudoternary                                    unipolar


## 4.6      SUMMARY
             o Digital-to-digital conversion involves three techniques: line coding, block coding,
                   and scrambling.
             o Line coding is the process of converting digital data to a digital signal.
             o We can roughly divide line coding schemes into five broad categories: unipolar,
                   polar, bipolar, multilevel, and multitransition.
             o     Block coding provides redundancy to ensure synchronization and inherent error
                   detection. Block coding is normally referred to as mB/nB coding; it replaces each
                   m-bit group with an n-bit group.
             o Scrambling provides synchronization without increasing the number of bits. Two
                   common scrambling techniques are B8ZS and HDB3.
             o     The most common technique to change an analog signal to digital data (digitiza-
                   tion) is called pulse code modulation (PCM).
             o     The first step in PCM is sampling. The analog signal is sampled every Ts s, where Ts
                   is the sample interval or period. The inverse of the sampling interval is called the
                   sampling rate or sampling frequency and denoted by fs, where fs = lITs. There are
                   three sampling methods-ideal, natural, and flat-top.
             o According to the Nyquist theorem, to reproduce the original analog signal, one
                   necessary condition is that the sampling rate be at least twice the highest frequency
                   in the original signal.

## SECTION 4.7     PRACTICE SET         137


o Other sampling techniques have been developed to reduce the complexity of PCM.
      The simplest is delta modulation. PCM finds the value of the signal amplitude for
      each sample; DM finds the change from the previous sample.
o     While there is only one way to send parallel data, there are three subclasses of
      serial transmission: asynchronous, synchronous, and isochronous.
o     In asynchronous transmission, we send 1 start bit (0) at the beginning and 1 or
      more stop bits (1 s) at the end of each byte.
o     In synchronous transmission, we send bits one after another without start or stop
      bits or gaps. It is the responsibility of the receiver to group the bits.
o     The isochronous mode provides synchronized for the entire stream of bits must. In
      other words, it guarantees that the data arrive at a fixed rate.


## 4.7      PRACTICE SET
Review Questions
 1. List three techniques of digital-to-digital conversion.
 2. Distinguish between a signal element and a data element.
 3. Distinguish between data rate and signal rate.
 4. Define baseline wandering and its effect on digital transmission.
 5. Define a DC component and its effect on digital transmission.
 6. Define the characteristics of a self-synchronizing signal.
 7. List five line coding schemes discussed in this book.
 8. Define block coding and give its purpose.
 9. Define scrambling and give its purpose.
10. Compare and contrast PCM and DM.
11. What are the differences between parallel and serial transmission?
12. List three different techniques in serial transmission and explain the differences.

Exercises
13. Calculate the value of the signal rate for each case in Figure 4.2 if the data rate is
    1 Mbps and c = 1/2.
14. In a digital transmission, the sender clock is 0.2 percent faster than the receiver clock.
    How many extra bits per second does the sender send if the data rate is 1 Mbps?
15. Draw the graph of the NRZ-L scheme using each of the following data streams,
    assuming that the last signa11evel has been positive. From the graphs, guess the
    bandwidth for this scheme using the average number of changes in the signal level.
    Compare your guess with the corresp.onding entry in Table 4.1.
    a. 00000000
    b. 11111111
    c. 01010101
    d. 00110011

138   CHAPTER 4   DIGITAL TRANSMISSION


              16. Repeat Exercise 15 for the NRZ-I scheme.
              17. Repeat Exercise 15 for the Manchester scheme.
              18. Repeat Exercise 15 for the differential Manchester scheme.
              19. Repeat Exercise 15 for the 2B 1Q scheme, but use the following data streams.
                  a. 0000000000000000
                  b. 1111111111111111
                  c. 0101010101010101
                  d. 0011001100110011
              20. Repeat Exercise 15 for the MLT-3 scheme, but use the following data streams.
                  a. 00000000
                  b. 11111111
                  c. 01010101
                  d. 00011000
              21. Find the 8-bit data stream for each case depicted in Figure 4.36.


              Figure 4.36 Exercise 21


                                   t
                                                                          Time


                                  a. NRZ-I


                                                                          Time


                                  b. differential Manchester


                                                                          Time


                                  c.AMI


              22. An NRZ-I signal has a data rate of 100 Kbps. Using Figure 4.6, calculate the value
                  of the normalized energy (P) for frequencies at 0 Hz, 50 KHz, and 100 KHz.
              23. A Manchester signal has a data rate of 100 Kbps. Using Figure 4.8, calculate the
                  value of the normalized energy (P) for frequencies at 0 Hz, 50 KHz, 100 KHz.

## SECTION 4. 7   PRACTICE SET      139


24. The input stream to a 4B/5B block encoder is 0100 0000 0000 0000 0000 OOOI.
    Answer the following questions:
    a. What is the output stream?
    b. What is the length of the longest consecutive sequence of Os in the input?
    c. What is the length of the longest consecutive sequence of Os in the output?
25. How many invalid (unused) code sequences can we have in 5B/6B encoding? How
    many in 3B/4B encoding?
26. What is the result of scrambling the sequence 11100000000000 using one of the
    following scrambling techniques? Assume that the last non-zero signal level has
    been positive.
    a. B8ZS
    b. HDB3 (The number of nonzero pules is odd after the last substitution)
27. What is the Nyquist sampling rate for each of the following signals?
    a. A low-pass signal with bandwidth of 200 KHz?
    b. A band-pass signal with bandwidth of 200 KHz if the lowest frequency is
       100 KHz?
28. We have sampled a low-pass signal with a bandwidth of 200 KHz using 1024 levels
    of quantization.
    a. Calculate the bit rate of the digitized signal.
    b. Calculate the SNRdB for this signal.
    c. Calculate the PCM bandwidth of this signal.
29. What is the maximum data rate of a channel with a bandwidth of 200 KHz if we
    use four levels of digital signaling.
30. An analog signal has a bandwidth of 20 KHz. If we sample this signal and send it
    through a 30 Kbps channel what is the SNRdB ?
31. We have a baseband channel with a I-MHz bandwidth. What is the data rate for
    this channel if we use one of the following line coding schemes?
    a. NRZ-L
    b. Manchester
    c. MLT-3
    d. 2B1Q
32. We want to transmit 1000 characters with each character encoded as 8 bits.
    a. Find the number of transmitted bits for synchronous transmission.
    b. Find the number of transmitted bits for asynchronous transmission.
    c. Find the redundancy percent in each case.


CHAPTERS

     Analog Transmission


     In Chapter 3, we discussed the advantages and disadvantages of digital and analog trans-
     mission. We saw that while digital transmission is very desirable, a low-pass channel is
     needed. We also saw that analog transmission is the only choice if we have a bandpass
     channel. Digital transmission was discussed in Chapter 4; we discuss analog transmis-
     sion in this chapter.
           Converting digital data to a bandpass analog signal.is traditionally called digital-
     to-analog conversion. Converting a low-pass analog signal to a bandpass analog signal
     is traditionally called analog-to-analog conversion. In this chapter, we discuss these two
     types of conversions.


## 5.1       DIGITAL-TO-ANALOG CONVERSION
     Digital-to-analog conversion is the process of changing one of the characteristics of
     an analog signal based on the information in digital data. Figure 5.1 shows the rela-
     tionship between the digital information, the digital-to-analog modulating process,
     and the resultant analog signal.


     Figure 5.1       Digital-to-analog conversion

                          Sender                                       Receiver


                                                Analog signal
           Digital data                                                           Digital data
                                                                              1°101 ... 1011

                                                     Link


                                                                                                 141

142   CHAPTER 5   ANALOG TRANSMISSION


                  As discussed in Chapter 3, a sine wave is defined by three characteristics: amplitude,
             frequency, and phase. When we vary anyone of these characteristics, we create a differ-
             ent version of that wave. So, by changing one characteristic of a simple electric signal, we
             can use it to represent digital data. Any of the three characteristics can be altered in this
             way, giving us at least three mechanisms for modulating digital data into an analog signal:
             amplitude shift keying (ASK), frequency shift keying (FSK), and phase shift keying
             (PSK). In addition, there is a fourth (and better) mechanism that combines changing both
             the amplitude and phase, called quadrature amplitude modulation (QAM). QAM
             is the most efficient of these options and is the mechanism commonly used today (see
             Figure 5.2).


              Figure 5.2    Types ofdigital-to-analog conversion


                                                      Digital-to-analog
                                                        conversion


                                               Quadrature amplitude modulation
                               "'------
                                                           (QAM)


              Aspects of Digital-to-Analog Conversion
              Before we discuss specific methods of digital-to-analog modulation, two basic issues
              must be reviewed: bit and baud rates and the carrier signal.

             Data Element Versus Signal Element
              In Chapter 4, we discussed the concept of the data element versus the signal element.
              We defined a data element as the smallest piece of information to be exchanged, the
              bit. We also defined a signal element as the smallest unit of a signal that is constant.
              Although we continue to use the same terms in this chapter, we will see that the nature
              of the signal element is a little bit different in analog transmission.

             Data Rate Versus Signal Rate
              We can define the data rate (bit rate) and the signal rate (baud rate) as we did for digital
              transmission. The relationship between them is


                                                    S=Nx!          baud
                                                              r

              where N is the data rate (bps) and r is the number of data elements carried in one signal
              element. The value of r in analog transmission is r = log2 L, where L is the type of sig-
              nal element, not the level. The same nomenclature is used to simplify the comparisons.

## SECTION 5.1    DIGITAL-TO-ANALOG CONVERSION                143


       Bit rate is the number of bits per second. Baud rate is the number of signal
             elements per second. In the analog transmission of digital data,
                      the baud rate is less than or equal to the bit rate.

     The same analogy we used in Chapter 4 for bit rate and baud rate applies here. In
transportation, a baud is analogous to a vehicle, and a bit is analogous to a passenger.
We need to maximize the number of people per car to reduce the traffic.

Example 5.1
An analog signal carries 4 bits per signal element. If 1000 signal elements are sent per second,
find the bit rate.

Solution
In this case, r = 4, S = 1000, and N is unknown. We can find the value of N from


                    S=Nx!             or   N=Sxr= 1000 x 4 =4000 bps
                             r


Example 5.2
An analog signal has a bit rate of 8000 bps and a baud rate of 1000 baud. How many data elements
are carried by each signal element? How many signal elements do we need?

Solution
In this example, S = 1000, N = 8000, and rand L are unknown. We find first the value of rand
then the value of L.

                            1                  N  8000   .
                        S=Nx-              r = - =-- =8 bltslbaud
                                  r            S  1000
                        r= logzL           L= y= 28 = 256


Bandwidth
The required bandwidth for analog transmission of digital data is proportional to the
signal rate except for FSK, in which the difference between the carrier signals needs to
be added. We discuss the bandwidth for each technique.

Carrier Signal
In analog transmission, the sending device produces a high-frequency signal that acts
as a base for the information signal. This base signal is called the carrier signal or car-
rier frequency. The receiving device is tuned to the frequency of the carrier signal that it
expects from the sender. Digital information then changes the carrier signal by modify-
ing one or more of its characteristics (amplitude, frequency, or phase). This kind of
modification is called modulation (shift keying).

Amplitude Shift Keying
In amplitude shift keying, the amplitude of the carrier signal is varied to create signal
elements. Both frequency and phase remain constant while the amplitude changes.

144   CHAPTER 5     ANALOG TRANSMISSION


             Binary ASK (BASK)
             Although we can have several levels (kinds) of signal elements, each with a different
             amplitude, ASK is normally implemented using only two levels. This is referred to as
             binary amplitude shift keying or on-off keying (OOK). The peak amplitude of one sig-
             nallevel is 0; the other is the same as the amplitude of the carrier frequency. Figure 5.3
             gives a conceptual view of binary ASK.


             Figure 5.3            Binmy amplitude shift keying

                  Amplitude                      Bit rate: 5
                                         o            1                       o                  r=:= 1   S=N   B=(I +d)S

                                                                                      I
                                                                                      I   Time
                                                                                      I
                        1 signal      1 signal     I signal     I signal   I signal   I
                                                                                      I
                        element       element      element      element    element    I


                                                     1s
                                                 Baud rate: 5


              Bandwidth for ASK Figure 5.3 also shows the bandwidth for ASK. Although the
              carrier signal is only one simple sine wave, the process of modulation produces a
              nonperiodic composite signal. This signal, as was discussed in Chapter 3, has a contin-
              uous set of frequencies. As we expect, the bandwidth is proportional to the signal rate
              (baud rate). However, there is normally another factor involved, called d, which
              depends on the modulation and filtering process. The value of d is between 0 and 1. This
              means that the bandwidth can be expressed as shown, where 5 is the signal rate and the B
              is the bandwidth.

                                                                   B =(1 +d) x S

                   The formula shows that the required bandwidth has a minimum value of 5 and a
              maximum value of 25. The most important point here is the location of the bandwidth.
              The middle of the bandwidth is where Ie the carrier frequency, is located. This means if
              we have a bandpass channel available, we can choose our Ie so that the modulated
              signal occupies that bandwidth. This is in fact the most important advantage of digital-
              to-analog conversion. We can shift the resulting bandwidth to match what is available.
              Implementation The complete discussion of ASK implementation is beyond the
              scope of this book. However, the simple ideas behind the implementation may help us
              to better understand the concept itself. Figure 5.4 shows how we can simply implement
              binary ASK.
                   If digital data are presented as a unipolar NRZ (see Chapter 4) digital signal with a
              high voltage of I V and a low voltage of 0 V, the implementation can achieved by
              multiplying the NRZ digital signal by the carrier signal coming from an oscillator.
              When the amplitude of the NRZ signal is 1, the amplitude of the carrier frequency is

## SECTION 5.1            DIGITAL-TO-ANALOG CONVERSION        145


Figure 5.4 Implementation of binary ASK

             I
             I
                 0                          o


                     Carrier signal
                           I


held; when the amplitude of the NRZ signal is 0, the amplitude of the carrier frequency
IS zero.


Example 5.3
We have an available bandwidth of 100 kHz which spans from 200 to 300 kHz. What are the car-
rier frequency and the bit rate if we modulated our data by using ASK with d = I?

Solution
The middle of the bandwidth is located at 250 kHz. This means that our carrier frequency can be
atfe = 250 kHz. We can use the formula for bandwidth to find the bit rate (with d = 1 and r = 1).


             B = (l + d) x S = 2 x N X!
                                                 r
                                                     =2 X N =100 kHz ...... N =50 kbps

Example 5.4
In data communications, we normally use full-duplex links with communication in both direc-
tions. We need to divide the bandwidth into two with two carrier frequencies, as shown in Fig-
ure 5.5. The figure shows the positions of two carrier frequencies and the bandwidths.The
available bandwidth for each direction is now 50 kHz, which leaves us with a data rate of 25 kbps
in each direction.


Figure 5.5 Bandwidth offull-duplex ASK used in Example 5.4

                                       I' B = 50 kHz '11   B = 50 kHz 'I


                               ~"~~~ ~,~Jf:
                                      200       (225)        (275)
                                                                     L300


Multilevel ASK
The above discussion uses only two amplitude levels. We can have multilevel ASK in
which there are more than two levels. We can use 4,8, 16, or more different amplitudes
for the signal and modulate the data using 2, 3, 4, or more bits at a time. In these cases,

146   CHAPTER 5     ANALOG TRANSMISSION


                                    =
             r = 2, r = 3, r 4, and so on. Although this is not implemented with pure ASK, it is
             implemented with QAM (as we will see later).

             Frequency Shift Keying
             In frequency shift keying, the frequency of the carrier signal is varied to represent data.
             The frequency of the modulated signal is constant for the duration of one signal ele-
             ment, but changes for the next signal element if the data element changes. Both peak
             amplitude and phase remain constant for all signal elements.

             Binary FSK (BFSK)
             One way to think about binary FSK (or BFSK) is to consider two carrier frequencies. In
             Figure 5.6, we have selected two carrier frequencies,f} and12. We use the first carrier if
             the data element is 0; we use the second if the data element is 1. However, note that this
             is an unrealistic example used only for demonstration purposes. Normally the carrier
             frequencies are very high, and the difference between them is very small.


              Figure 5.6           Binary frequency shift keying


                  Amplitude
                                                Bit rate: 5                          r=l      S=N     B=(1+d)S+2t-.j
                              1         Il                                   Il


                        1 signal     1 signal   1 signal       1 signal   1 signal
                        element      element    element        element    element    o   +-~--1-L....JL..--l--..I...-_

                                                                                         o       It          h
                                                    Is
                                                Baud rate: 5                                      I' 21-.!   -I


                  As Figure 5.6 shows, the middle of one bandwidth isJI and the middle of the other
             is h. Both JI and 12 are il/ apart from the midpoint between the two bands. The differ-
             ence between the two frequencies is 211f

             Bandwidth for BFSK Figure 5.6 also shows the bandwidth of FSK. Again the car-
             rier signals are only simple sine waves, but the modulation creates a nonperiodic com-
             posite signal with continuous frequencies. We can think of FSK as two ASK signals,
             each with its own carrier frequency Cil or h). If the difference between the two fre-
             quencies is 211j, then the required bandwidth is

                                                                B=(l+d)xS+2iij

                   What should be the minimum value of 211/? In Figure 5.6, we have chosen a value
              greater than (l + d)S. It can be shown that the minimum value should be at least S for
              the proper operation of modulation and demodulation.

## SECTION 5.1      DIGITAL-TO-ANALOG CONVERSION                   147


Example 5.5
We have an available bandwidth of 100 kHz which spans from 200 to 300 kHz. What should be
the carrier frequency and the bit rate if we modulated our data by using FSK with d = 1?

Solution
This problem is similar to Example 5.3, but we are modulating by using FSK. The midpoint of
the band is at 250 kHz. We choose 2~f to be 50 kHz; this means

       B = (1 + d) x S + 28f = 100 - .        2S =50 kHz S = 25 kbaud          N;;;; 25 kbps


Compared to Example 5.3, we can see the bit rate for ASK is 50 kbps while the bit rate for FSK is
25 kbps.

Implementation There are two implementations of BFSK: noncoherent and coher-
ent. In noncoherent BFSK, there may be discontinuity in the phase when one signal
element ends and the next begins. In coherent BFSK, the phase continues through the
boundary of two signal elements. Noncoherent BFSK can be implemented by treating
BFSK as two ASK modulations and using two carrier frequencies. Coherent BFSK can
be implemented by using one voltage-controlled oscillator (VeO) that changes its fre-
quency according to the input voltage. Figure 5.7 shows the simplified idea behind the
second implementation. The input to the oscillator is the unipolar NRZ signal. When
the amplitude of NRZ is zero, the oscillator keeps its regular frequency; when the
amplitude is positive, the frequency is increased.


Figure 5.7 Implementation of BFSK


           1     o             1      o


                                                    _lD1_I_I_I_-;"~1 veo I~
                                                                Voltage-controlled
                                                                    oscillator


Multilevel FSK
Multilevel modulation (MFSK) is not uncommon with the FSK method. We can use
more than two frequencies. For example, we can use four different frequenciesfIJ2,!3,
and 14 to send 2 bits at a time. To send 3 bits at a time, we can use eight frequencies.
And so on. However, we need to remember that the frequencies need to be 2~1 apart.
For the proper operation of the modulator and demodulator, it can be shown that the
minimum value of 2~lneeds to be S. We can show that the bandwidth with d = 0 is

                         B;;;; (l + d) x S + (L - 1)24{ - .   B =Lx S

148   CHAPTER 5     ANALOG TRANSMISSION


             Example 5.6
             We need to send data 3 bits at a time at a bit rate of 3 Mbps. The carrier frequency is
             10 MHz. Calculate the number of levels (different frequencies), the baud rate, and the
             bandwidth.
             Solution
             We can have L =23 = 8. The baud rate is S =3 MHz/3 = 1000 Mbaud. This means that the carrier
             frequencies must be 1 MHz apart (211f = 1 MHz). The bandwidth is B =8 x 1000 = 8000. Figure 5.8
             shows the allocation of frequencies and bandwidth.


             Figure 5.8 Bandwidth ofMFSK used in Example 5.6

                                                                              Bandwidth = 8 MHz
                              I'                                                                                                 'I
                         -(.-----.."--,,I~~~lf5~~1       I: I--Ji~~l~;~r'·' ·t':~                                I
                                                                                                                      r~~'¥'::L
                                   II              h               h            14 j~   15        16            h           is
## 6.5         7.5             8.5             9.5  HI 10.5       11.5         12.5     13.5
                                   MHz         MHz             MHz             MHz MHz MHz        MHz          MHz      MHz


              Phase Shift Keying
              In phase shift keying, the phase of the carrier is varied to represent two or more differ-
              ent signal elements. Both peak amplitude and frequency remain constant as the phase
              changes. Today, PSK is more common than ASK or FSK. However, we will see
              Sh0l1ly that QAM, which combines ASK and PSK, is the dominant method of digital-
              to-analog modulation.

              Binary PSK (BPSK)
              The simplest PSK is binary PSK, in which we have only two signal elements, one with
              a phase of 0°, and the other with a phase of 180°. Figure 5.9 gives a conceptual view
              of PSK. Binary PSK is as simple as binary ASK with one big advantage-it is less


              Figure 5.9           Binary phase shift keying

                  Amplitude                            Bit rate: 5
                                           o                              1            I)                r=1          S=N        B= {I + d)S


                        I signal        I signal        I signal       I signal     I signal
                        element         element         element        element      element

                                                         I s
                                                     Baud rate: 5

## SECTION 5.1   DIGITAL-TO-ANALOG CONVERSION                         149


susceptible to noise. In ASK, the criterion for bit detection is the amplitude of the sig-
nal; in PSK, it is the phase. Noise can change the amplitude easier than it can change
the phase. In other words, PSK is less susceptible to noise than ASK. PSK is superior to
FSK because we do not need two carrier signals.

Bandwidth Figure 5.9 also shows the bandwidth for BPSK. The bandwidth is the
same as that for binary ASK, but less than that for BFSK. No bandwidth is wasted for
separating two carrier signals.

Implementation The implementation of BPSK is as simple as that for ASK. The rea-
son is that the signal element with phase 180° can be seen as the complement of the sig-
nal element with phase 0°. This gives us a clue on how to implement BPSK. We use
the same idea we used for ASK but with a polar NRZ signal instead of a unipolar NRZ
signal, as shown in Figure 5.10. The polar NRZ signal is multiplied by the carrier fre-
quency; the 1 bit (positive voltage) is represented by a phase starting at 0°; the a bit
(negative voltage) is represented by a phase starting at 180°.


Figure 5.10 Implementation of BASK


                o               1     o
                                                 -=t:f=tt     Multiplier ~
                           I
                           I                    ------.t        X I---'-;';';"";";"':":"';";';'~
                     Carrie~ signal


                                                                   *f     c


Quadrature PSK (QPSK)
The simplicity of BPSK enticed designers to use 2 bits at a time in each signal element,
thereby decreasing the baud rate and eventually the required bandwidth. The scheme is
called quadrature PSK or QPSK because it uses two separate BPSK modulations; one
is in-phase, the other quadrature (out-of-phase). The incoming bits are first passed
through a serial-to-parallel conversion that sends one bit to one modulator and the next
bit to the other modulator. If the duration of each bit in the incoming signal is T, the
duration of each bit sent to the corresponding BPSK signal is 2T. This means that the
bit to each BPSK signal has one-half the frequency of the original signal. Figure 5.11
shows the idea.
     The two composite signals created by each multiplier are sine waves with the
same frequency, but different phases. When they are added, the result is another sine
wave, with one of four possible phases: 45°, -45°, 135°, and -135°. There are four
kinds of signal elements in the output signal (L = 4), so we can send 2 bits per signal
element (r = 2).

150   CHAPTER 5    ANALOG TRANSMISSION


             Figure 5.11            QPSK and its implementation


                    00        1U         01        1 I

                     o        1          o          1


                                     I         I         I
                                     I         I         I


                  ·p·,J\-:/YfAf\f~-tPtj'}/f'J\-lllJ~
                          I          I         I         I
                          I          I         I         I
                          I          I         I         I
                     o    :   0      I         I         I
                          I


                   -135       -45        135       45


             Example 5.7
              Find the bandwidth for a signal transmitting at 12 Mbps for QPSK. The value of d = O.

              Solution
              For QPSK, 2 bits is carried by one signal element. This means that r = 2. So the signal rate (baud
              rate) is S = N x (lIr) = 6 Mbaud. With a value of d = 0, we have B = S = 6 MHz.


              Constellation Diagram
              A constellation diagram can help us define the amplitude and phase of a signal element,
              particularly when we are using two carriers (one in-phase and one quadrature), The
              diagram is useful when we are dealing with multilevel ASK, PSK, or QAM (see next
## section). In a constellation diagram, a signal element type is represented as a dot. The
              bit or combination of bits it can carry is often written next to it.
                   The diagram has two axes. The horizontal X axis is related to the in-phase carrier;
              the vertical Y axis is related to the quadrature carrier. For each point on the diagram,
              four pieces of information can be deduced. The projection of the point on the X axis
              defines the peak amplitude of the in-phase component; the projection of the point on
              the Y axis defines the peak amplitude of the quadrature component. The length of the
              line (vector) that connects the point to the origin is the peak amplitude of the signal
              element (combination of the X and Y components); the angle the line makes with the
              X axis is the phase of the signal element. All the information we need, can easily be found
              on a constellation diagram. Figure 5.12 shows a constellation diagram.

## SECTION 5.1                         DIGITAL-TO-ANALOG CONVERSION                                   151


Figure 5.12 Concept of a constellation diagram

                        Y (Quadrature carrier)

                                             -----------~
                                                                            ,
                                                                                ,    I
                           f+-<   --'                               ~e.~~            I
                            o     l=:                          • ..:S5~              I
                           ~ ~                                ?f"                    I
                            B 8..                     ~<$'/                          I
                           :.::: E                   . ,
                            0.. 0
                            E 0
                                                   #1"',
                                               ~:<::>,'
                                                                                     I
                                                                                     I
                                                                                     I
                           « C)l              V,                                     I
                                             "        Angle: phase                   I
                                         ,                                           I
                       _ _---L+_-----.J'----                                        ---'--~   X (In-phase carrier)
                                                Amplitude of
                                                I component


Example 5.8
Show the constellation diagrams for an ASK (OOK), BPSK, and QPSK signals.

Solution
Figure 5.13 shows the three constellation diagrams.


Figure 5.13 Three constellation diagrams


                                                                                                            01'-
                                                                                                                       ~-   -,
                                                                                                                                 .11
                            -
                                                                                                             /                     \


                 0
                            -.
                              I                       -
                                                      -.
                                                          0                              -
                                                                                         .-
                                                                                         1
                                                                                                               1

                                                                                                               \

                                                                                                            00. ,
                                                                                                                   \
                                                                                                                                 __~1O
                                                                                                                                       \


                                                                                                                                       I


      a.ASK(OOK)                             b.BPSK                                                   c.QPSK


Let us analyze each case separately:
 a. For ASK, we are using only an in-phase carrier. Therefore, the two points should be on the
     X axis. Binary 0 has an amplitude of 0 V; binary 1 has an amplitude of 1 V (for example).
     The points are located at the origin and at 1 unit.
  h. BPSK also uses only an in-phase carrier. However, we use a polar NRZ signal for modu-
     lation. It creates two types of signal elements, one with amplitude 1 and the other with
     amplitude -1. This can be stated in other words: BPSK creates two different signal elements,
     one with amplitude I V and in phase and the other with amplitude 1 V and 1800 out of phase.
  c. QPSK uses two carriers, one in-phase and the other quadrature. The point representing 11 is
     made of two combined signal elements, both with an amplitude of 1 V. One element is rep-
     resented by an in-phase carrier, the other element by a quadrature carrier. The amplitude of
     the final signal element sent for this 2-bit data element is 2 112 , and the phase is 45°. The
     argument is similar for the other three points. All signal elements have an amplitude of 2112,
     but their phases are different (45°, 135°, -135°, and -45°). Of course, we could have chosen
     the amplitude of the carrier to be 1/(21/2) to make the final amplitudes 1 V.

152   CHAPTER 5    ANALOG TRANSMISSION


              Quadrature Amplitude Modulation
             PSK is limited by the ability of the equipment to distinguish small differences in phase.
             This factor limits its potential bit rate. So far, we have been altering only one of the
             three characteristics of a sine wave at a time; but what if we alter two? Why not com-
             bine ASK and PSK? The idea of using two carriers, one in-phase and the other quadra-
             ture, with different amplitude levels for each carrier is the concept behind quadrature
             amplitude modulation (QAM).

                            Quadrature amplitude modulation is a combination of ASK and PSK.


                  The possible variations of QAM are numerous. Figure 5.14 shows some of these
             schemes. Figure 5.14a shows the simplest 4-QAM scheme (four different signal ele-
             ment types) using a unipolar NRZ signal to modulate each carrier. This is the same
             mechanism we used for ASK (OOK). Part b shows another 4-QAM using polar NRZ,
             but this is exactly the same as QPSK. Part c shows another QAM-4 in which we used a
             signal with two positive levels to modulate each of the two carriers. Finally, Figure 5.14d
             shows a 16-QAM constellation of a signal with eight levels, four positive and four
             negative.


              Figure 5.14       Constellation diagrams for some QAMs


                            t •             •        •                  • •         • •      ••• •••
                            L
                            I~
                                                                        • •         • •
                                                                                    • •       • •
                                            •        •                              • •        • •
                  a.4·QAM               b.4-QAM               c.4.QAM            d.16·QAM


              Bandwidth for QAM
              The minimum bandwidth required for QAM transmission is the same as that required
              for ASK and PSK transmission. QAM has the same advantages as PSK over ASK.


## 5.2       ANALOG-TO-ANALOG CONVERSION
              Analog-to-analog conversion, or analog modulation, is the representation of analog
              information by an analog signal. One may ask why we need to modulate an analog sig-
              nal; it is already analog. Modulation is needed if the medium is bandpass in nature or if
              only a bandpass channel is available to us. An example is radio. The government assigns
              a narrow bandwidth to each radio station. The analog signal produced by each station is
              a low-pass signal, all in the same range. To be able to listen to different stations, the
              low-pass signals need to be shifted, each to a different range.

## SECTION 5.2     ANALOG-TO-ANALOG CONVERSION               153


    Analog-to-analog conversion can be accomplished in three ways: amplitude
modulation (AM), frequency modulation (FM), and phase modulation (PM). FM
and PM are usually categorized together. See Figure 5.15.


Figure 5.15    Types ofanalog-to-analog modulation


                                       Analog-lo-analog
                                         conversion


                                     Frequency modulation


Amplitude Modulation
In AM transmission, the carrier signal is modulated so that its amplitude varies with the
changing amplitudes of the modulating signal. The frequency and phase of the carrier
remain the same; only the amplitude changes to follow variations in the information. Fig-
ure 5.16 shows how this concept works. The modulating signal is the envelope of the carrier.


Figure 5.16 Amplitude modulation


                                                            Jj:L
                                                                     BAM=2B


                                                            o            I
                                                                        1;


As Figure 5.16 shows, AM is normally implemented by using a simple multiplier
because the amplitude of the carrier signal needs to be changed according to the ampli-
tude of the modulating signal.

AM Bandwidth
Figure 5.16 also shows the bandwidth of an AM signal. The modulation creates a band-
width that is twice the bandwidth of the modulating signal and covers a range centered
on the carrier frequency. However, the signal components above and below the carrier

154   CHAPTER 5   ANALOG TRANSMISSION


             frequency carry exactly the same information. For this reason, some implementations
             discard one-half of the signals and cut the bandwidth in half.


                                The total bandwIdth required for AM can be determined
                                  from the bandwidth of the audio signal: BAM = 2B.
             ------------------_~-~,~_-


             Stalldard Balldwidth Allocatioll for AiH l(adio
             The bandwidth of an audio signal (speech and music) is usually 5 kHz. Therefore, an
             AM radio station needs a bandwidth of 10kHz. In fact, the Federal Communications
             Commission (FCC) allows 10 kHz for each AM station.
                  AM stations are allowed carrier frequencies anywhere between 530 and 1700 kHz
             (1.7 MHz). However, each station's carrier frequency must be separated from those on
             either side of it by at least 10 kHz (one AM bandwidth) to avoid interference. If one
             station uses a carrier frequency of 1100 kHz, the next station's carrier frequency cannot
             be lower than 1110 kHz (see Figure 5.17).

              Figure 5.17      AM band allocation


                         530                   I'
                                                             _ _*_*_*_ . . . . I . . . . -.....
                                                            ,I
                                                                                                   =u.;[IJ
                                                                                            t-'"....
                                                                                                        1700
                         kHz                        10kHz                                               kHz


              Frequency Modulation
              In FM transmission, the frequency of the carrier signal is modulated to follow the chang-
              ing voltage level (amplitude) of the modulating signal. The peak amplitude and phase of
              the carrier signal remain constant, but as the amplitude of the information signal
              changes, the frequency of the carrier changes correspondingly. Figure 5.18 shows the
              relationships of the modulating signal, the carrier signal, and the resultant FM signal.
                   As Figure 5.18 shows, FM is nOimalIy implemented by using a voltage-controlled
              oscillator as with FSK. The frequency of the oscillator changes according to the input
              voltage which is the amplitude of the modulating signal.

              FiH Balldwidth
              Figure 5.18 also shows the bandwidth of an FM signal. The actual bandwidth is diffi-
              cult to determine exactly, but it can be shown empirically that it is several times that
              of the analog signal or 2(1 + ~)B where ~ is a factor depends on modulation technique
              with a common value of 4.


                            The total bandwidth required for FM can be determined from
                                 the bandwidth of the audio signal: B FM = 2(1 + j3 )B.

## SECTION 5.2     ANALOG-TO-ANALOG CONVERSION                     155


:Figure 5.1 g    Frequency modulation
                                         ------------ ----------

  Amplitude
       Modulating signal (audio)


                                                                         I veo I~.-
                                                   Time
                                                          _C".
                                                           __  "0-----,J~~

                                                                      VOltage-controlled
                                                                          oscillator
                                                   Time

                                                                       B," = 2(1 +filR
        FM signal
         n!

                                                   Time
                                                               D:L
                                                                o                  I
                                                                                  Ie


                ------        ------_._-----------------


,c.,'twllhm! Bandwidth A.llo('((tiOll for F,\f Radio
The bandwidth of an audio signal (speech and music) broadcast in stereo is almost
15 kHz. The FCC allows 200 kHz (0.2 MHz) for each station. This mean ~ = 4 with
some extra guard band. FM stations are allowed carrier frequencies anywhere between
88 and 108 MHz. Stations must be separated by at least 200 kHz to keep their band-
widths from overlapping. To create even more privacy, the FCC requires that in a given
area, only alternate bandwidth allocations may be used. The others remain unused to pre-
vent any possibility of two stations interfering with each other. Given 88 to 108 MHz as
a range, there are 100 potential PM bandwidths in an area, of which 50 can operate at
anyone time. Figure 5.19 illustrates this concept.


Figure 5.19         FM band allocation
                                                                          ------_.               __ ._--

         ,--_t,-e
        88
                 _I st~~on              Ie
                                        t
                                                   ...         Ie
                                                               t
                                                                             No
                                                                        station
                                                                                           108
       MHz
                                   I- 200 kHz ,I                                           MHz


Phast' ,\ loduiation
In PM transmission, the phase of the carrier signal is modulated to follow the changing
voltage level (amplitude) of the modulating signal. The peak amplitude and frequency
of the carrier signal remain constant, but as the amplitude of the information signal
changes, the phase of the carrier changes correspondingly. It can proved mathemati-
cally (see Appendix C) that PM is the same as FM with one difference. In FM, the
instantaneous change in the carrier frequency is proportional to the amplitude of the

156   CHAPTER 5     ANALOG TRANSMISSION


             modulating signal; in PM the instantaneous change in the carrier frequency is propor-
             tional to the derivative of the amplitude of the modulating signal. Figure 5.20 shows the
             relationships of the modulating signal, the carrier signal, and the resultant PM signal.


             Figure 5.20 Phase modulation

                  Amplitude

                        Modulating signal (audio)


                                                       Time                   I VCOI~
                                                                                 r

                                                                   ~
                                                                        'J
                                                                                  I
                                                                              1 dldt
                                                        Time                  1        I
                        PM signal


                                                        Time


                   As Figure 5.20 shows, PM is normally implemented by using a voltage-controlled
              oscillator along with a derivative. The frequency of the oscillator changes according to
              the derivative of the input voltage which is the amplitude of the modulating signal.

             PM Bandwidth
              Figure 5.20 also shows the bandwidth of a PM signal. The actual bandwidth is difficult
              to determine exactly, but it can be shown empirically that it is several times that of the
              analog signal. Although, the formula shows the same bandwidth for FM and PM, the
              value of ~ is lower in the case of PM (around 1 for narrowband and 3 for wideband).

                    The total bandwidth required for PM can be determined from the bandwidth and
                            maximum amplitude of the modulating signal: BpM = 2(1 + ~ )B.


## 5.3         RECOMMENDED READING
              For more details about subjects discussed in this chapter, we recommend the following
              books. The items in brackets [...] refer to the reference list at the end of the text.

              Books
              Digital-to-analog conversion is discussed in Chapter 14 of [Pea92], Chapter 5 of
              [CouOl], and Section 5.2 of [Sta04]. Analog-to-analog conversion is discussed in
              Chapters 8 to 13 of [Pea92], Chapter 5 of [CouOl], and Section 5.4 of [Sta04]. [Hsu03]

## SECTION 5.5     SUMMARY         157


gives a good mathematical approach to all materials discussed in this chapter. More
advanced materials can be found in [Ber96].


## 5.4      KEY TERMS
amplitude modulation (AM)                          frequency modulation (PM)
amplitude shift keying (ASK)                       frequency shift keying (FSK)
analog-to-analog conversion                        phase modulation (PM)
carrier signal                                     phase shift keying (PSK)
constellation diagram                              quadrature amplitude modulation
digi tal-to-analog conversion                         (QAM)


## 5.5      SUMMARY
o Digital-to-analog conversion is the process of changing one of the characteristics
      of an analog signal based on the information in the digital data.
o     Digital-to-analog conversion can be accomplished in several ways: amplitude shift
      keying (ASK), frequency shift keying (FSK), and phase shift keying (PSK).
      Quadrature amplitude modulation (QAM) combines ASK and PSK.
o     In amplitude shift keying, the amplitude of the carrier signal is varied to create signal
      elements. Both frequency and phase remain constant while the amplitude changes.
o     In frequency shift keying, the frequency of the carrier signal is varied to represent
      data. The frequency of the modulated signal is constant for the duration of one sig-
      nal element, but changes for the next signal element if the data element changes.
      Both peak amplitude and phase remain constant for all signal elements.
o     In phase shift keying, the phase of the carrier is varied to represent two or more dif-
      ferent signal elements. Both peak amplitude and frequency remain constant as the
      phase changes.
o     A constellation diagram shows us the amplitude and phase of a signal element,
      particularly when we are using two carriers (one in-phase and one quadrature).
o     Quadrature amplitude modulation (QAM) is a combination of ASK and PSK.
      QAM uses two carriers, one in-phase and the other quadrature, with different
      amplitude levels for each carrier.
o     Analog-to-analog conversion is the representation of analog information by an
      analog signal. Conversion is needed if the medium is bandpass in nature or if only
      a bandpass bandwidth is available to us.
o     Analog-to-analog conversion can be accomplished in three ways: amplitude modu-
      lation (AM), frequency modulation (FM), and phase modulation (PM).
o     In AM transmission, the carrier signal is modulated so that its amplitude varies with the
      changing amplitudes of the modulating signal. The frequency and phase of the carrier
      remain the same; only the amplitude changes to follow variations in the information.
o     In PM transmission, the frequency of the carrier signal is modulated to follow the
      changing voltage level (amplitude) of the modulating signal. The peak amplitude

158   CHAPTER 5    ANALOG TRANSMISSION


                    and phase of the carrier signal remain constant, but as the amplitude of the infor-
                    mation signal changes, the frequency of the carrier changes correspondingly.
              o     In PM transmission, the phase of the carrier signal is modulated to follow the
                    changing voltage level (amplitude) of the modulating signal. The peak amplitude
                    and frequency of the carrier signal remain constant, but as the amplitude of the
                    information signal changes, the phase of the carrier changes correspondingly.


## 5.6       PRACTICE SET
              Review Questions
                  1. Define analog transmission.
                  2. Define carrier signal and its role in analog transmission.
                  3. Define digital-to-analog conversion.
                  4. Which characteristics of an analog signal are changed to represent the digital signal
                     in each of the following digital-to-analog conversion?
                     a. ASK
                     b. FSK
                     c. PSK
                     d. QAM
                  5. Which of the four digital-to-analog conversion techniques (ASK, FSK, PSK or
                     QAM) is the most susceptible to noise? Defend your answer.
                  6. Define constellation diagram and its role in analog transmission.
                  7. What are the two components of a signal when the signal is represented on a con- .
                     stellation diagram? Which component is shown on the horizontal axis? Which is
                     shown on the vertical axis?
                  8. Define analog-to-analog conversion?
                  9. Which characteristics of an analog signal are changed to represent the lowpass analog
                     signal in each of the following analog-to-analog conversions?
                     a. AM
                     b. FM
                     c. PM
              ] 0. Which of the three analog-to-analog conversion techniques (AM, FM, or PM) is
                   the most susceptible to noise? Defend your answer.

              Exercises
              11. Calculate the baud rate for the given bit rate and type of modulation.
                  a. 2000 bps, FSK
                  b. 4000 bps, ASK
                  c. 6000 bps, QPSK
                  d. 36,000 bps, 64-QAM

## SECTION 5.6    PRACTICE SET       159


12. Calculate the bit rate for the given baud rate and type of modulation.
    a. 1000 baud, FSK
    b. 1000 baud, ASK
    c. 1000 baud, BPSK
    d. 1000 baud, 16-QAM
13. What is the number of bits per baud for the following techniques?
    a. ASK with four different amplitudes
    b. FSK with 8 different frequencies
    c. PSK with four different phases
    d. QAM with a constellation of 128 points.
14. Draw the constellation diagram for the following:
    a. ASK, with peak amplitude values of 1 and 3
    b. BPSK, with a peak amplitude value of 2
    c. QPSK, with a peak amplitude value of 3
    d. 8-QAM with two different peak amplitude values, I and 3, and four different
       phases.
15. Draw the constellation diagram for the following cases. Find the peak amplitude
    value for each case and define the type of modulation (ASK, FSK, PSK, or QAM).
    The numbers in parentheses define the values of I and Q respectively.
    a. Two points at (2, 0) and (3, 0).
    b. Two points at (3, 0) and (-3, 0).
    c. Four points at (2, 2), (-2, 2), (-2, -2), and (2, -2).
    d. Two points at (0 , 2) and (0, -2).
16. How many bits per baud can we send in each of the following cases if the signal
    constellation has one of the following number of points?
    a. 2
    b. 4
    c. 16
    d. 1024
17. What is the required bandwidth for the following cases if we need to send 4000 bps?
    Let d = 1.
    a. ASK
    b. FSK with 2~f = 4 KHz
    c. QPSK
    d. 16-QAM
18. The telephone line has 4 KHz bandwidth. What is the maximum number of bits we
    can send using each of the following techniques? Let d = O.
    a. ASK
    b. QPSK
    c. 16-QAM
    d.64-QAM

160   CHAPTER 5   ANALOG TRANSMISSION


              19. A corporation has a medium with a I-MHz bandwidth (lowpass). The corporation
                  needs to create 10 separate independent channels each capable of sending at least
                  10 Mbps. The company has decided to use QAM technology. What is the mini-
                  mum number of bits per baud for each channel? What is the number of points in
                  the constellation diagram for each channel? Let d = O.
              20. A cable company uses one of the cable TV channels (with a bandwidth of 6 MHz)
                  to provide digital communication for each resident. What is the available data rate
                  for each resident if the company uses a 64-QAM technique?
              21. Find the bandwidth for the following situations if we need to modulate a 5-KHz
                  voice.
                  a. AM
                  b. PM (set ~ =5)
                  c. PM (set ~ = 1)
              22. Find the total number of channels in the corresponding band allocated by FCC.
                  a. AM
                  b. FM

## CHAPTER 6

      Bandwidth Utilization:
      Multiplexing and Spreading

      In real life, we have links with limited bandwidths. The wise use of these bandwidths
      has been, and will be, one of the main challenges of electronic communications. How-
      ever, the meaning of wise may depend on the application. Sometimes we need to combine
      several low-bandwidth channels to make use of one channel with a larger bandwidth.
      Sometimes we need to expand the bandwidth of a channel to achieve goals such as
      privacy and antijamming. In this chapter, we explore these two broad categories of
      bandwidth utilization: multiplexing and spreading. In multiplexing, our goal is effi-
      ciency; we combine several channels into one. In spreading, our goals are privacy and
      antijamming; we expand the bandwidth of a channel to insert redundancy, which is
      necessary to achieve these goals.


         Bandwidth utilization is the wise use of available bandwidth to achieve specific goals.
                             Efficiency can be achieved by multiplexing;
                       privacy and antijamming can be achieved by spreading.


## 6.1     MULTIPLEXING
      Whenever the bandwidth of a medium linking two devices is greater than the band-
      width needs of the devices, the link can be shared. Multiplexing is the set of techniques
      that allows the simultaneous transmission of multiple signals across a single data link.
      As data and telecommunications use increases, so does traffic. We can accommodate
      this increase by continuing to add individual links each time a new channel is needed;
      or we can install higher-bandwidth links and use each to carry multiple signals. As
      described in Chapter 7, today's technology includes high-bandwidth media such as
      optical fiber and terrestrial and satellite microwaves. Each has a bandwidth far in excess
      of that needed for the average transmission signal. If the bandwidth of a link is greater
      than the bandwidth needs of the devices connected to it, the bandwidth is wasted. An
      efficient system maximizes the utilization of all resources; bandwidth is one of the
      most precious resources we have in data communications.


                                                                                                   161

162   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


                  In a multiplexed system, n lines share the bandwidth of one link. Figure 6.1 shows
             the basic format of a multiplexed system. The lines on the left direct their transmission
             streams to a multiplexer (MUX), which combines them into a single stream (many-to-
             one). At the receiving end, that stream is fed into a demultiplexer (DEMUX), which
             separates the stream back into its component transmissions (one-to-many) and
             directs them to their corresponding lines. In the figure, the word link refers to the
             physical path. The word channel refers to the portion of a link that carries a transmis-
             sion between a given pair of lines. One link can have many (n) channels.


             Figure 6.1 Dividing a link into channels


                                   ~ MUX: Multiplexer                                  /
                                           DEMUX: Demultiplexer                            D
                                       M
                                                                                ,          E

                                                                                                    ···
                                       U                                                   M
                              •
                   n Input
                      lines   ··       X
                                                          I link, 11 channels
                                                                                           U
                                                                                           X
                                                                                                          n Output
                                                                                                          lines


                                   /                                                   ~


                 There are three basic multiplexing techniques: frequency-division multiplexing,
             wavelength-division multiplexing, and time-division multiplexing. The first two are
             techniques designed for analog signals, the third, for digital signals (see Figure 6.2).


             Figure 6.2 Categories ofmultiplexing


                                                             Multiplexing

                                                                    I
                                       I                            I                      I
                              Frequency-division
                                 multiplexing
                                   Analog
                                                   I     Wavelength-division
                                                            multiplexing
                                                                  Analog
                                                                                    Time-division
                                                                                     multiplexing
                                                                                       Digital


                  Although some textbooks consider carrier division multiple access (COMA) as a
             fourth multiplexing category, we discuss COMA as an access method (see Chapter 12).

              Frequency-Division Multiplexing
             Frequency-division multiplexing (FDM) is an analog technique that can be applied
             when the bandwidth of a link (in hertz) is greater than the combined bandwidths of
             the signals to be transmitted. In FOM, signals generated by each sending device modu-
             late different carrier frequencies. These modulated signals are then combined into a single
             composite signal that can be transported by the link. Carrier frequencies are separated by
             sufficient bandwidth to accommodate the modulated signal. These bandwidth ranges are
             the channels through which the various signals travel. Channels can be separated by

## SECTION 6.1   MULTIPLEXING   163


strips of unused bandwidth-guard bands-to prevent signals from overlapping. In
addition, carrier frequencies must not interfere with the original data frequencies.
     Figure 6.3 gives a conceptual view of FDM. In this illustration, the transmission path
is divided into three parts, each representing a channel that carries one transmission.


Figure 6.3     Frequency-division multiplexing


                                                                         D
                        M                     Channel J                  E
          Input                                                               Output
                        U                     Chanllel2                  M
           lines                                                              Jines
                        X                                                U
                                                                         X


    We consider FDM to be an analog multiplexing technique; however, this does not
mean that FDM cannot be used to combine sources sending digital signals. A digital
signal can be converted to an analog signal (with the techniques discussed in Chapter 5)
before FDM is used to multiplex them.

         FDM is an analog multiplexing technique that combines analog signals.


Multiplexing Process
Figure 6.4 is a conceptual illustration of the multiplexing process. Each source gener-
ates a signal of a similar frequency range. Inside the multiplexer, these similar signals
modulates different carrier frequencies (/1,12, and h). The resulting modulated signals
are then combined into a single composite signal that is sent out over a media link that
has enough bandwidth to accommodate it.


Figure 6.4         FDM process


                              Modulator
                            /\/\/\/\
                              V \TV\)
                              Carrier!1


                              Modulator
                            flOflflflflflfl
                            VVlJl)l) VVV
                              Carrierh


                              Modulator
                            U!UUUUA!!!A
         Baseband           mvmvmnm
       analog signals         Carrierh

164   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Demultiplexing Process
             The demultiplexer uses a series of filters to decompose the multiplexed signal into its
             constituent component signals. The individual signals are then passed to a demodulator
             that separates them from their carriers and passes them to the output lines. Figure 6.5 is
             a conceptual illustration of demultiplexing process.


             Figure 6.5    FDM demultiplexing example


                                                             ~
                                                               /--                  ,        Demodulator
                                                                                            AAAA
                                                               \                              VVVV
                                                              -
                                                                                    '
                                                                                               Carrier!l
                                                                    \    "
                                                                                        :==D=e=m=o=d=ul=at=or==~
                                                             "                  \            AAAAAnAA
                                                                                             vvvvvvvv
                                                '----~       ....       ~'.
                                                                         ~~   /1'              Carrierh
                                                         •

                                                                                             Demodulator
                                                                                            AA!!AAAAAAAAAA!!
                                                                                             mvmvmmn
                                                                                              Carrierh
                                                                                                                     Baseband
                                                                                                                   analog signals


             Example 6.1
             Assume that a voice channel occupies a bandwidth of 4 kHz. We need to combine three voice
             channels into a link with a bandwidth of 12 kHz, from 20 to 32 kHz. Show the configuration,
             using the frequency domain. Assume there are no guard bands.

             Solution
             We shift (modulate) each of the three voice channels to a different bandwidth, as shown in Fig-
             ure 6.6. We use the 20- to 24-kHz bandwidth for the first channel, the 24- to 28-kHz bandwidth
             for the second channel, and the 28- to 32-kHz bandwidth for the third one. Then we combine
             them as shown in Figure 6.6. At the receiver, each channel receives the entire signal, using a
             filter to separate out its own signal. The first channel uses a filter that passes frequencies
             between 20 and 24 kHz and filters out (discards) any other frequencies. The second channel
             uses a filter that passes frequencies between 24 and 28 kHz, and the third channel uses a filter
             that passes frequencies between 28 and 32 kHz. Each channel then shifts the frequency to start
             from zero.

             Example 6.2
             Five channels, each with a lOa-kHz bandwidth, are to be multiplexed together. What is the mini-
             mum bandwidth of the link if there is a need for a guard band of 10kHz between the channels to
             prevent interference?

              Solution
             For five channels, we need at least four guard bands. This means that the required bandwidth is at
             least 5 x 100 + 4 x 10 = 540 kHz, as shown in Figure 6.7.

## SECTION 6.1         MULTIPLEXING   165


Figure 6.6    Example 6.1

                                                                   Shift and combine


                                            Higher-bandwidth link


                                         Bandpass
                                           filter

                                         Bandpass
                                           filter
                                                    -_.._-
                                                       20     24


                                                              24    28


Figure 6.7    Example 6.2

                        Guard band
                         of 10 kHz

                I. 100 kHz   -Ill'   100kHz _I


                I·                                  540 kHz


Example 6.3
Four data channels (digital), each transmitting at I Mbps, use a satellite channel of I MHz.
Design an appropriate configuration, using FDM.

Solution
The satellite channel is analog. We divide it into four channels, each channel having a 2S0-kHz
bandwidth. Each digital channel of I Mbps is modulated such that each 4 bits is modulated to
1 Hz. One solution is 16-QAM modulation. Figure 6.8 shows one possible configuration.

The Analog Carrier System
To maximize the efficiency of their infrastructure, telephone companies have tradition-
ally multiplexed signals from lower-bandwidth lines onto higher-bandwidth lines. In this
way, many switched or leased lines can be combined into fewer but bigger channels. For
analog lines, FDM is used.

166   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Figure 6.8    Example 6.3

                                  I Mbps                         250 kHz
                                  Digital                         Analog

                                  I Mbps                         250 kHz
                                  Digital                         Analog                       I MHz
                                  I Mbps                         250 kHz
                                  Digital                         Analog

                                  I Mbps                         250 kHz
                                  Digital                         Analog


                 One of these hierarchical systems used by AT&T is made up of groups, super-
             groups, master groups, and jumbo groups (see Figure 6.9).


              Figure 6.9   Analog hierarchy


                                                 48 kHz
                                            12 voice channels


                                            Group


                                                         F
                                                         D t------i~                                          16.984 MHz
                                                         M      en                                         3600 voice channels
                                                                g. ----i~ F     Master group
                                                                ~         D
                                                                ~ ----:l.~1 M      §.-          ~ F          Jumbo
                                                                                                              group
                                                                :=:                ~-           ..-jD
                                                                                  !:l                  M
                                                                                   ~-
                                                                                   E
                                                                                          ..... ~
                                                                                  '.Q -   . . . . .~


                   In this analog hierarchy, 12 voice channels are multiplexed onto a higher-bandwidth
              line to create a group. A group has 48 kHz of bandwidth and supports 12 voice channels.
                    At the next level, up to five groups can be multiplexed to create a composite signal
              called a supergroup. A supergroup has a bandwidth of 240 kHz and supports up to
              60 voice channels. Supergroups can be made up of either five groups or 60 independent
              voice channels.
                    At the next level, 10 supergroups are multiplexed to create a master group. A
              master group must have 2.40 MHz of bandwidth, but the need for guard bands between
              the supergroups increases the necessary bandwidth to 2.52 MHz. Master groups support
              up to 600 voice channels.
                   Finally, six master groups can be combined into a jumbo group. A jumbo group
              must have 15.12 MHz (6 x 2.52 MHz) but is augmented to 16.984 MHz to allow for
              guard bands between the master groups.

## SECTION 6.1     MULTIPLEXING           167


Other Applications of FDM
A very common application of FDM is AM and FM radio broadcasting. Radio uses the
air as the transmission medium. A special band from 530 to 1700 kHz is assigned to AM
radio. All radio stations need to share this band. As discussed in Chapter 5, each AM sta-
tion needs 10kHz of bandwidth. Each station uses a different carrier frequency, which
means it is shifting its signal and multiplexing. The signal that goes to the air is a combi-
nation of signals. A receiver receives all these signals, but filters (by tuning) only the one
which is desired. Without multiplexing, only one AM station could broadcast to the com-
mon link, the air. However, we need to know that there is physical multiplexer or demulti-
plexer here. As we will see in Chapter 12 multiplexing is done at the data link layer.
     The situation is similar in FM broadcasting. However, FM has a wider band of 88
to 108 MHz because each station needs a bandwidth of 200 kHz.
     Another common use of FDM is in television broadcasting. Each TV channel has
its own bandwidth of 6 MHz.
     The first generation of cellular telephones (still in operation) also uses FDM. Each
user is assigned two 30-kHz channels, one for sending voice and the other for receiving.
The voice signal, which has a bandwidth of 3 kHz (from 300 to 3300 Hz), is modulated by
using FM. Remember that an FM signal has a bandwidth 10 times that of the modulating
signal, which means each channel has 30 kHz (10 x 3) of bandwidth. Therefore, each user
is given, by the base station, a 60-kHz bandwidth in a range available at the time of the call.

Example 6.4
The Advanced Mobile Phone System (AMPS) uses two bands. The first band of 824 to 849 MHz
is used for sending, and 869 to 894 MHz is used for receiving. Each user has a bandwidth of
30 kHz in each direction. The 3-kHz voice is modulated using FM, creating 30 kHz of modulated
signal. How many people can use their cellular phones simultaneously?

Solution
Each band is 25 MHz. If we divide 25 MHz by 30 kHz, we get 833.33. In reality, the band is divided
into 832 channels. Of these, 42 channels are used for control, which means only 790 channels are
available for cellular phone users. We discuss AMPS in greater detail in Chapter 16.

Implementation
FDM can be implemented very easily. In many cases, such as radio and television
broadcasting, there is no need for a physical multiplexer or demultiplexer. As long as
the stations agree to send their broadcasts to the air using different carrier frequencies,
multiplexing is achieved. In other cases, such as the cellular telephone system, a base
station needs to assign a carrier frequency to the telephone user. There is not enough
bandwidth in a cell to permanently assign a bandwidth range to every telephone user.
When a user hangs up, her or his bandwidth is assigned to another caller.

Wavelength-Division Multiplexing
Wavelength-division multiplexing (WDM) is designed to use the high-data-rate
capability of fiber-optic cable. The optical fiber data rate is higher than the data rate of
metallic transmission cable. Using a fiber-optic cable for one single line wastes the
available bandwidth. Multiplexing allows us to combine several lines into one.

168   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


                  WDM is conceptually the same as FDM, except that the multiplexing and demulti-
             plexing involve optical signals transmitted through fiber-optic channels. The idea is the
             same: We are combining different signals of different frequencies. The difference is
             that the frequencies are very high.
                  Figure 6.10 gives a conceptual view of a WDM multiplexer and demultiplexer.
             Very narrow bands of light from different sources are combined to make a wider band
             of light. At the receiver, the signals are separated by the demultiplexer.


             Figure 6.10          Wavelength-division multiplexing


                            AI
                                       fl                                               f\.       AI

                            AZ
                                       fl                 flflfl                        fl        Az
                                                           Ai + Az + A3

                            A:J
                                       fl                                               fl        A:J


                       WDM is an analog multiplexing technique to combine optical signals.


                  Although WDM technology is very complex, the basic idea is very simple. We
             want to combine multiple light sources into one single light at the multiplexer and do
             the reverse at the demultiplexer. The combining and splitting of light sources are easily
             handled by a prism. Recall from basic physics that a prism bends a beam of light based
             on the angle of incidence and the frequency. Using this technique, a multiplexer can be
             made to combine several input beams of light, each containing a narrow band of fre-
             quencies, into one output beam of a wider band of frequencies. A demultiplexer can
             also be made to reverse the process. Figure 6.11 shows the concept.


             :Figure 6.11         Prisms in wavelength-division multiplexing and demultiplexing


                                                          Fiber-optic cable


                                        Multiplexer                            Demultiplexer


                  One application of WDM is the SONET network in which multiple optical
             fiber lines are multiplexed and demultiplexed. We discuss SONET in Chapter 17.
                  A new method, called dense WDM (DWDM), can multiplex a very large number
             of channels by spacing channels very close to one another. It achieves even greater
             efficiency.

## SECTION 6.1                    MULTIPLEXING   169


Synchronous Time-Division Multiplexing
Time-division multiplexing (TDM) is a digital process that allows several connections
to share the high bandwidth of a linle Instead of sharing a portion of the bandwidth as in
FDM, time is shared. Each connection occupies a portion of time in the link. Figure 6.12
gives a conceptual view of TDM. Note that the same link is used as in FDM; here, how-
ever, the link is shown sectioned by time rather than by frequency. In the figure, portions
of signals 1,2,3, and 4 occupy the link sequentially.


Figure 6.12    TDM


                                                               Data flow

                      2                                                        .                              D    2
                          M                               ~,
                                                                                                              E J--..::--{§:~

                      3
                          U
                          X
                                4     3 2          1    t'3                 l'4321M
                                                                                   U                               3
              r=:~---l                                                                                        X t---~=~-~_
                              t--L-L-.l...--'--=.........-"'=..L...;;...J...-...l...-...l...-...J.........j


     Note that in Figure 6.12 we are concerned with only multiplexing, not switching.
This means that all the data in a message from source 1 always go to one specific desti-
nation, be it 1, 2, 3, or 4. The delivery is fixed and unvarying, unlike switching.
     We also need to remember that TDM is, in principle, a digital multiplexing technique.
Digital data from different sources are combined into one timeshared link. However, this
does not mean that the sources cannot produce analog data; analog data can be sampled,
changed to digital data, and then multiplexed by using TDM.


                  TDM is a digital multiplexing technique for combining
                    several low-rate channels into one high-rate one.


    We can divide TDM into two different schemes: synchronous and statistical. We first
discuss synchronous TDM and then show how statistical TDM differs. In synchronous
TDM, each input connection has an allotment in the output even if it is not sending data.

Time Slots and Frames
In synchronous TDM, the data flow of each input connection is divided into units, where
each input occupies one input time slot. A unit can be 1 bit, one character, or one block of
data. Each input unit becomes one output unit and occupies one output time slot. How-
ever, the duration of an output time slot is n times shorter than the duration of an input
time slot. If an input time slot is T s, the output time slot is Tin s, where n is the number
of connections. In other words, a unit in the output connection has a shorter duration; it
travels faster. Figure 6.13 shows an example of synchronous TDM where n is 3.

170   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Figure 6.13         Synchronous time-division multiplexing


                     If
                          T       Jlf
                                         T      Jil
                                                         T

                          A3            A2            Al


                          B3            B2            Bl

                                                                            Each frame is 3 time slots.
                                                                          Each time slot duration is Tf3 s.
                          C3            C2            Cl

                              Data are taken from each
                                   line every T s.


                  In synchronous TDM, a round of data units from each input connection is collected
             into a frame (we will see the reason for this shortly). If we have n connections, a frame
             is divided into n time slots and one slot is allocated for each unit, one for each input
             line. If the duration of the input unit is T, the duration of each slot is Tin and the dura-
             tion of each frame is T (unless a frame carries some other information, as we will see
             shortly).
                  The data rate of the output link must be n times the data rate of a connection to
             guarantee the flow of data. In Figure 6.13, the data rate of the link is 3 times the data
             rate of a connection; likewise, the duration of a unit on a connection is 3 times that of
             the time slot (duration of a unit on the link). In the figure we represent the data prior to
             multiplexing as 3 times the size of the data after multiplexing. This is just to convey the
             idea that each unit is 3 times longer in duration before multiplexing than after.

                                In synchronous TDM, the data rate of the link is n times faster,
                                           and the unit duration is n times shorter.

                  Time slots are grouped into frames. A frame consists of one complete cycle of
             time slots, with one slot dedicated to each sending device. In a system with n input
             lines, each frame has n slots, with each slot allocated to carrying data from a specific
             input line.

              Example 6.5
              In Figure 6.13, the data rate for each input connection is 3 kbps. If 1 bit at a time is multiplexed (a
              unit is 1 bit), what is the duration of (a) each input slot, (b) each output slot, and (c) each frame?

              Solution
             We can answer the questions as follows:
              a. The data rate of each input connection is 1 kbps. This means that the bit duration is 111000 s
                 or 1 ms. The duration of the input time slot is 1 ms (same as bit duration).
              b. The duration of each output time slot is one-third of the input time slot. This means that the
                 duration of the output time slot is 1/3 ms.
              c. Each frame carries three output time slots. So the duration of a frame is 3 x 113 ms, or 1 ms.
                 The duration of a frame is the same as the duration of an input unit.

## SECTION 6.1      MULTIPLEXING            171


Example 6.6
Figure 6.14 shows synchronous TOM with a data stream for each input and one data stream for
the output. The unit of data is 1 bit. Find (a) the input bit duration, (b) the output bit duration,
(c) the output bit rate, and (d) the output frame rate.


Figure 6.14 Example 6.6

                    • •• 1
           I Mbps
                                                                     Frames
                    • •• 0   0   0   0    o
           1 Mbps                                   ••• ffilQI!] [Q]QJQliJ1III[Q[QJQli]"
                    • •• 1   0       0
           1 Mbps
                    • •• 0   0       0    o
           1 Mbps


Solution
We can answer the questions as follows:
 a. The input bit duration is the inverse of the bit rate: 1/1 Mbps = 1 lls.
 b. The output bit duration is one-fourth of the input bit duration, or 1/411s.
 c. The output bit rate is the inverse of the output bit duration or 1/4 lls, or 4 Mbps. This can also
    be deduced from the fact that the output rate is 4 times as fast as any input rate; so the output
    rate = 4 x 1 Mbps = 4 Mbps.
 d. The frame rate is always the same as any input rate. So the frame rate is 1,000,000 frames per
    second. Because we are sending 4 bits in each frame, we can verify the result of the previous
    question by multiplying the frame rate by the number of bits per frame.


Example 6.7
Four l-kbps connections are multiplexed together. A unit is I bit. Find (a) the duration of I bit
before multiplexing, (b) the transmission rate of the link, (c) the duration of a time slot, and
(d) the duration of a frame.

Solution
We can answer the questions as follows:
 a. The duration of 1 bit before multiplexing is 1/1 kbps, or 0.001 s (l ms).
 b. The rate of the link is 4 times the rate of a connection, or 4 kbps.
 c. The duration of each time slot is one-fourth of the duration of each bit before multiplexing,
    or 1/4 ms or 250 I.ls. Note that we can also calculate this from the data rate of the link, 4 kbps.
    The bit duration is the inverse of the data rate, or 1/4 kbps or 250 I.ls.
 d. The duration of a frame is always the same as the duration of a unit before multiplexing, or
    I ms. We can also calculate this in another way. Each frame in this case has fouf time slots.
    So the duration of a frame is 4 times 250 I.ls, or I ms.


Interleaving
TDM can be visualized as two fast-rotating switches, one on the multiplexing side and
the other on the demultiplexing side. The switches are synchronized and rotate at the
same speed, but in opposite directions. On the multiplexing side, as the switch opens

172   CHAPTER 6    BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             in front of a connection, that connection has the opportunity to send a unit onto the
             path. This process is called interleaving. On the demultiplexing side, as the switch
             opens in front of a connection, that connection has the opportunity to receive a unit
             from the path.
                  Figure 6.15 shows the interleaving process for the connection shown in Figure 6.13.
             In this figure, we assume that no switching is involved and that the data from the first
             connection at the multiplexer site go to the first connection at the demultiplexer. We
             discuss switching in Chapter 8.


             Figure 6.15      Interleaving


                                           r- - - - - - - - - -        Synchronization        - - - - - - - - - ,
                                           I
                                           I
                  A3   A2    Al            I
                                                                                                                        A3    A2   Al
                                           I
             c=J [==:J c::::::J            I                                                                          [==:J [==:J c:::J

                  B3   B2    Bl                                                                                          B3   B2     Bl
             ~~~                                                                                                      ~~~


                  C3   C2    CI                                                                                          C3   C2     Cl
             c=:::J [==:J c::::::J                                                                                    c:::J r:::::J c=:::J


             Example 6.8
             Four channels are multiplexed using TDM. If each channel sends 100 bytesis and we multiplex
             1 byte per channel, show the frame traveling on the link, the size of the frame, the duration of a
             frame, the frame rate, and the bit rate for the link.

             Solution
             The multiplexer is shown in Figure 6.16. Each frame carries 1 byte from each channel; the size of
             each frame, therefore, is 4 bytes, or 32 bits. Because each channel is sending 100 bytes/s and a
             frame carries 1 byte from each channel, the frame rate must be 100 frames per second. The dura-
             tion of a frame is therefore 11100 s. The link is carrying 100 frames per second, and since each
             frame contains 32 bits, the bit rate is 100 x 32, or 3200 bps. This is actually 4 times the bit rate of
             each channel, which is 100 x 8 = 800 bps.


             Figure 6.16 Example 6.8

                                                                       Frame 4 bytes                         Frame 4 bytes
                                                                          32 bits                               32 bits

                                                                  II          1,*"tiJ      'I ... II                g~ II


                            -
                                                                                             100 frames/s
                                                                                               3200 bps

                                                                                        Frame duration == 160s
                             100 bytes/s

## SECTION 6.1        MULTIPLEXING            173


Example 6.9
A multiplexer combines four 100-kbps channels using a time slot of 2 bits. Show the output with
four arbitrary inputs. What is the frame rate? What is the frame duration? What is the bit rate?
What is the bit duration?
Solution
Figure 6.17 shows the output for four arbitrary inputs. The link carries 50,000 frames per second
since each frame contains 2 bits per channel. The frame duration is therefore 1/50,000 s or 20 ~s.
The frame rate is 50,000 frames per second, and each frame carries 8 bits; the bit rate is 50,000 x
8 = 400,000 bits or 400 kbps. The bit duration is 1/400,000 s, or 2.5 IJ.s. Note that the frame dura-
tion is 8 times the bit duration because each frame is carrying 8 bits.


Figure 6.17        Example 6.9


                    ·..   110010
                                                        Frame duration = lI50,000 s = 20 Ils
        100 kbps

        100 kbps
                    ...   001010
                                            ... ~~~
                                                    Frame: 8 bits Frame: 8 bits    Frame: 8 bits


        100 kbps
                    ·..   101 101                                 50,000 frames/s

        100 kbps
                    ·..   000111
                                                                     400kbps


Empty Slots
Synchronous TDM is not as efficient as it could be. If a source does not have data to
send, the corresponding slot in the output frame is empty. Figure 6.18 shows a case in
which one of the input lines has no data to send and one slot in another input line has
discontinuous data.

Figure 6.18 Empty slots


                              II      II

                                                         I~ 0110           DII~       01


     The first output frame has three slots filled, the second frame has two slots filled,
and the third frame has three slots filled. No frame is full. We learn in the next section
that statistical TDM can improve the efficiency by removing the empty slots from the
frame.

Data Rate Management
One problem with TDM is how to handle a disparity in the input data rates. In all our
discussion so far, we assumed that the data rates of all input lines were the same. However,

174   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             if data rates are not the same, three strategies, or a combination of them, can be used.
             We call these three strategies multilevel multiplexing, multiple-slot allocation, and
             pulse stuffing.
             Multilevel Multiplexing Multilevel multiplexing is a technique used when the data
             rate of an input line is a multiple of others. For example, in Figure 6.19, we have two
             inputs of 20 kbps and three inputs of 40 kbps. The first two input lines can be multi-
             plexed together to provide a data rate equal to the last three. A second level of multi-
             plexing can create an output of 160 kbps.


              Figure 6.19 Multilevel multiplexing

                                     20 kbps - - - - ; " \
                                                             >------t
                                     20 kbps - - - - I
                                     40 kbps - - - - - - - - 1                        160 kbps

                                     40 kbps - - - - - - - - 1

                                     40 kbps - - - - - - - - 1


             Multiple-Slot Allocation Sometimes it is more efficient to allot more than one slot in
             a frame to a single input line. For example, we might have an input line that has a data
             rate that is a multiple of another input. In Figure 6.20, the input line with a SO-kbps data
             rate can be given two slots in the output. We insert a serial-to-parallel converter in the
             line to make two inputs out of one.


              Figure 6.20 Multiple-slot multiplexing


                           50 kbps


                           25 kbps -------1
                                                                            The input with a
                           25 kbps - - - - - - - 1                      50-kHz data rate has two
                                                                          slots in each frame.
                           25 kbps - - - - - - - 1 /


             Pulse Stuffing Sometimes the bit rates of sources are not multiple integers of each
             other. Therefore, neither of the above two techniques can be applied. One solution is to
             make the highest input data rate the dominant data rate and then add dummy bits to the
             input lines with lower rates. This will increase their rates. This technique is called pulse
             stuffing, bit padding, or bit stuffing. The idea is shown in Figure 6.21. The input with a
             data rate of 46 is pulse-stuffed to increase the rate to 50 kbps. Now multiplexing can
             take place.

## SECTION 6.1        MULTIPLEXING     175


Figure 6.21 Pulse stuffing


                      50 kbps - - - - - - - - - - 1
                                                                          150 kbps
                      50 kbps - - - - - - - - - - 1

                      46kbps - - - I


Frame Synchronizing
The implementation of TDM is not as simple as that of FDM. Synchronization between
the multiplexer and demultiplexer is a major issue. If the. multiplexer and the demulti-
plexer are not synchronized, a bit belonging to one channel may be received by the
wrong channel. For this reason, one or more synchronization bits are usually added to
the beginning of each frame. These bits, called framing bits, follow a pattern, frame to
frame, that allows the demultiplexer to synchronize with the incoming stream so that it
can separate the time slots accurately. In most cases, this synchronization information
consists of 1 bit per frame, alternating between 0 and I, as shown in Figure 6.22.

Figure 6.22      Framing bits


                                          I 1     0   1
                                                              ISynchronization
                                                               pattern

                          Frame 3               Frame 2                   Frame 1
                         C3 I B3 I A3             182 I A2               CI I           Al

                        .:11II:0                                                    :0
                                                                                    I
                                                  I       I                  I
                                           0
                                                  :11I:0                     I
                                                                             I


Example 6.10
We have four sources, each creating 250 characters per second. If the interleaved unit is a character
and 1 synchronizing bit is added to each frame, find (a) the data rate of each source, (b) the duration
of each character in each source, (c) the frame rate, (d) the duration of each frame, (e) the number of
bits in each frame, and (f) the data rate of the link.

Solution
We can answer the questions as follows:
 a. The data rate of each source is 250 x 8 = 2000 bps = 2 kbps.
 b. Each source sends 250 characters per second; therefore, the duration of a character is 1/250 s,
    or4 ms.
 c. Each frame has one character from each source, which means the link needs to send
    250 frames per second to keep the transmission rate of each source.
 d. The duration of each frame is 11250 s, or 4 ms. Note that the duration of each frame is the
    same as the duration of each character coming from each source.
 e. Each frame carries 4 characters and I extra synchronizing bit. This means that each frame is
    4 x 8 + 1 = 33 bits.

176   CHAPTER 6    BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


                  f. The link sends 250 frames per second, and each frame contains 33 bits. This means that the
                    data rate of the link is 250 x 33, or 8250 bps. Note that the bit rate of the link is greater than
                    the combined bit rates of the four channels. If we add the bit rates of four channels, we get
                    8000 bps. Because 250 frames are traveling per second and each contains 1 extra bit for
                    synchronizing, we need to add 250 to the sum to get 8250 bps.

             Example 6.11
             Two channels, one with a bit rate of 100 kbps and another with a bit rate of 200 kbps, are to be
             multiplexed. How this can be achieved? What is the frame rate? What is the frame duration?
             What is the bit rate of the link?

              Solution
             We can allocate one slot to the first channel and two slots to the second channel. Each frame car-
             ries 3 bits. The frame rate is 100,000 frames per second because it carries 1 bit from the first
             channel. The frame duration is 1/100,000 s, or 10 ms. The bit rate is 100,000 frames/s x 3 bits per
             frame, or 300 kbps. Note that because each frame carries 1 bit from the first channel, the bit rate
             for the first channel is preserved. The bit rate for the second channel is also preserved because
             each frame carries 2 bits from the second channel.

              Digital Signal Service
              Telephone companies implement TDM through a hierarchy of digital signals, called
              digital signal (DS) service or digital hierarchy. Figure 6.23 shows the data rates sup-
              ported by each level.

              Figure 6.23       Digital hierarchy


                            os-o                                6.312 Mbps
                                                                  405-1

                                            OS-1
                                                         T     OS-2
                                                         D
                                                         M                                       274.176 Mbps
                                                                                                    60S-3
                                                                         T       OS-3
                                                                         D : - - -......~
                                                               --~M
## 1.544 Mbps                                      T    OS-4
                                              24 DS-O                                       D
                                                                                            M
                                                                                                        •
                                                                                 --+-\


              o A DS-O service is a single digital channel of 64 kbps.
              ODS-I is a 1.544-Mbps service; 1.544 Mbps is 24 times 64 kbps plus 8 kbps of
                overhead. It can be used as a single service for 1.544-Mbps transmissions, or it can
                be used to multiplex 24 DS-O channels or to carry any other combination desired
                by the user that can fit within its 1.544-Mbps capacity.
              o DS-2 is a 6.312-Mbps service; 6.312 Mbps is 96 times 64 kbps plus 168 kbps of
                overhead. It can be used as a single service for 6.312-Mbps transmissions; or it can

## SECTION 6.1     MULTIPLEXING          177


    be used to multiplex 4 DS-l channels, 96 DS-O channels, or a combination of these
    service types.
o   DS-3 is a 44.376-Mbps service; 44.376 Mbps is 672 times 64 kbps plus 1.368 Mbps
    of overhead. It can be used as a single service for 44.376-Mbps transmissions; or it
    can be used to multiplex 7 DS-2 channels, 28 DS-l channels, 672 DS-O channels,
    or a combination of these service types.
o   DS-4 is a 274. 176-Mbps service; 274.176 is 4032 times 64 kbps plus 16.128 Mbps of
    overhead. It can be used to multiplex 6 DS-3 channels, 42 DS-2 channels, 168 DS-l
    channels, 4032 DS-O channels, or a combination of these service types.

T Lines
DS-O, DS-l, and so on are the names of services. To implement those services, the tele-
phone companies use T lines (T-l to T-4). These are lines with capacities precisely
matched to the data rates of the DS-l to DS-4 services (see Table 6.1). So far only T-l
and T-3 lines are commercially available.

Table 6.1 DS and T line rates

 Sen/ice                  Line                 Rate (Mbps)            Voice Channels
  DS-1                    T-1                     1.544                      24
  DS-2                    T-2                     6.312                      96
  DS-3                    T-3                    44.736                     672
  DS-4                    T-4                   274.176                   4032

     The T-l line is used to implement DS-l; T-2 is used to implement DS-2; and so on.
As you can see from Table 6.1, DS-O is not actually offered as a service, but it has been
defined as a basis for reference purposes.

T Lines for Analog Transmission
T lines are digital lines designed for the transmission of digital data, audio, or video.
However, they also can be used for analog transmission (regular telephone connec-
tions), provided the analog signals are first sampled, then time-division multiplexed.
     The possibility of using T lines as analog carriers opened up a new generation of
services for the telephone companies. Earlier, when an organization wanted 24 separate
telephone lines, it needed to run 24 twisted-pair cables from the company to the central
exchange. (Remember those old movies showing a busy executive with 10 telephones
lined up on his desk? Or the old office telephones with a big fat cable running from
them? Those cables contained a bundle of separate lines.) Today, that same organization
can combine the 24 lines into one T-l line and run only the T-l line to the exchange.
Figure 6.24 shows how 24 voice channels can be multiplexed onto one T-I line. (Refer
to Chapter 5 for PCM encoding.)
The T-1 Frame As noted above, DS-l requires 8 kbps of overhead. To understand how
this overhead is calculated, we must examine the format of a 24-voice-channel frame.
     The frame used on a T-l line is usually 193 bits divided into 24 slots of 8 bits each
plus 1 extra bit for synchronization (24 x 8 + 1 = 193); see Figure 6.25. In other words,

178   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Figure 6.24   T-l line for multiplexing telephone lines


                                      Sampling at 8000 sampJes/s
                                        Llsing 8 bits per sample


                                                                                                T-I line 1.544 Mbps
                                                                                 t        24 x 64 kbps + 8 kbps overhead
                                                                                I)
                                                                                M


             Figure 6.25 T-l frame structure

                               Samplen
                                  I


                                                                    I
                                                                    1 bit
                                                                            Channel
                                                                              24
                                                                             8 bits
                                                                                      I·· ·1    Channel
                                                                                                   2
                                                                                                 8 bits
                                                                                                          I   Channel
                                                                                                                 I
                                                                                                               8 bits
                                                                                                                        I
                                                                            1 frame= 193 bits


                                                                   ...      Frame
                                                                              n
                                                                                       ... I    Frame
                                                                                                   2
                                                                                                          II Frame
                                                                                                               1
                                                          T- I: 8000 frames/s = 8000 x 193 bps = 1.544 Mbps


             each slot contains one signal segment from each channel; 24 segments are interleaved
             in one frame. If a T-l line carries 8000 frames, the data rate is 1.544 Mbps (193 x 8000 =
## 1.544 Mbps)-the capacity of the line.

             E Lines
             Europeans use a version ofT lines called E lines. The two systems are conceptually iden-
             tical, but their capacities differ. Table 6.2 shows the E lines and their capacities.

## SECTION 6.1     MULTIPLEXING          179


                     Table 6.2 E line rates

                       Line         Rate (Mbps)      Voice Channels
                       E-1              2.048               30
                       E-2              8.448              120
                       E-3             34.368              480
                       E-4            139.264             1920


More Synchronous TDM Applications
Some second-generation cellular telephone companies use synchronous TDM. For
example, the digital version of cellular telephony divides the available bandwidth into
3D-kHz bands. For each band, TDM is applied so that six users can share the band. This
means that each 3D-kHz band is now made of six time slots, and the digitized voice sig-
nals of the users are inserted in the slots. Using TDM, the number of telephone users in
each area is now 6 times greater. We discuss second-generation cellular telephony in
## Chapter 16.

Statistical Time-Division Multiplexing
As we saw in the previous section, in synchronous TDM, each input has a reserved slot
in the output frame. This can be inefficient if some input lines have no data to send. In
statistical time-division multiplexing, slots are dynamically allocated to improve band-
width efficiency. Only when an input line has a slot's worth of data to send is it given a
slot in the output frame. In statistical multiplexing, the number of slots in each frame is
less than the number of input lines. The multiplexer checks each input line in round-
robin fashion; it allocates a slot for an input line if the line has data to send; otherwise,
it skips the line and checks the next line.
     Figure 6.26 shows a synchronous and a statistical TDM example. In the former,
some slots are empty because the corresponding line does not have data to send. In
the latter, however, no slot is left empty as long as there are data to be sent by any
input line.

Addressing
Figure 6.26 also shows a major difference between slots in synchronous TDM and
statistical TDM. An output slot in synchronous TDM is totally occupied by data; in
statistical TDM, a slot needs to carry data as well as the address of the destination.
In synchronous TDM, there is no need for addressing; synchronization and preassigned
relationships between the inputs and outputs serve as an address. We know, for exam-
ple, that input 1 always goes to input 2. If the multiplexer and the demultiplexer are
synchronized, this is guaranteed. In statistical multiplexing, there is no fixed relation-
ship between the inputs and outputs because there are no preassigned or reserved
slots. We need to include the address of the receiver inside each slot to show where it
is to be delivered. The addressing in its simplest form can be n bits to define N different
output lines with n = 10g2 N. For example, for eight different output lines, we need a
3-bit address.

180   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Figure 6.26       TDM slot comparison


                           Line A ----[:3:0
                           LineB
                          Line C - - - - - - - - {


                          Line 0
                          LineE
                                    --i.iI~=~
                         a. Synchronous TDM


                           Line A   -----[=:ACH
                           LineB
                           Line C - - - - - - - - i

                          Line 0    ---:~~
                          LineE     --I
                         b. Statistical TDM


             Slot Size
             Since a slot carries both data and an address in statistical TDM, the ratio of the data size
             to address size must be reasonable to make transmission efficient. For example, it
             would be inefficient to send 1 bit per slot as data when the address is 3 bits. This would
             mean an overhead of 300 percent. In statistical TDM, a block of data is usually many
             bytes while the address is just a few bytes.

             No Synchronization Bit
             There is another difference between synchronous and statistical TDM, but this time it is
             at the frame level. The frames in statistical TDM need not be synchronized, so we do not
             need synchronization bits.

             Bandwidth
             In statistical TDM, the capacity of the link is normally less than the sum of the capaci-
             ties of each channel. The designers of statistical TDM define the capacity of the link
             based on the statistics of the load for each channel. If on average only x percent of the
             input slots are filled, the capacity of the link reflects this. Of course, during peak times,
             some slots need to wait.


## 6.2     SPREAD SPECTRUM
             Multiplexing combines signals from several sources to achieve bandwidth efficiency; the
             available bandwidth of a link is divided between the sources. In spread spectrum (88), we
             also combine signals from different sources to fit into a larger bandwidth, but our goals

## SECTION 6.2   SPREAD SPECTRUM        181


are somewhat different. Spread spectrum is designed to be used in wireless applications
(LANs and WANs). In these types of applications, we have some concerns that outweigh
bandwidth efficiency. In wireless applications, all stations use air (or a vacuum) as the
medium for communication. Stations must be able to share this medium without intercep-
tion by an eavesdropper and without being subject to jamming from a malicious intruder
(in military operations, for example).
     To achieve these goals, spread spectrum techniques add redundancy; they spread
the original spectrum needed for each station. If the required bandwidth for each station
is B, spread spectrum expands it to Bss ' such that Bss » B. The expanded bandwidth
allows the source to wrap its message in a protective envelope for a more secure trans-
mission. An analogy is the sending of a delicate, expensive gift. We can insert the gift in
a special box to prevent it from being damaged during transportation, and we can use a
superior delivery service to guarantee the safety of the package.
     Figure 6.27 shows the idea of spread spectrum. Spread spectrum achieves its goals
through two principles:
 1. The bandwidth allocated to each station needs to be, by far, larger than what is
    needed. This allows redundancy.
 2. The expanding of the original bandwidth B to the bandwidth Bss must be done by a
    process that is independent of the original signal. In other words, the spreading
    process occurs after the signal is created by the source.


Figure 6.27    Spread spectrum

                                                                B SS
                                                          I'           >   I

                                      Spreading
                                       process


                                         i
                                      Spreading
                                         code


     After the signal is created by the source, the spreading process uses a spreading
code and spreads the bandwidth. The figure shows the original bandwidth B and the
spreaded bandwidth B ss . The spreading code is a series of numbers that look random,
but are actually a pattern.
     There are two techniques to spread the bandwidth: frequency hopping spread spec-
trum (FHSS) and direct sequence spread spectrum (DSSS).

Frequency Hopping Spread Spectrum (FHSS)
The frequency hopping spread spectrum (FHSS) technique uses M different carrier
frequencies that are modulated by the source signal. At one moment, the signal modu-
lates one carrier frequency; at the next moment, the signal modulates another carrier

182   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             frequency. Although the modulation is done using one carrier frequency at a time,
             M frequencies are used in the long run. The bandwidth occupied by a source after
             spreading is B pHSS »B.
                  Figure 6.28 shows the general layout for FHSS. A pseudorandom code generator,
             called pseudorandom noise (PN), creates a k-bit pattern for every hopping period Th •
             The frequency table uses the pattern to find the frequency to be used for this hopping
             period and passes it to the frequency synthesizer. The frequency synthesizer creates a
             carrier signal of that frequency, and the source signal modulates the carrier signal.


             Figure 6.28 Frequency hopping spread spectrum (FHSS)

                                                                    Modulator

                        Original --I----------'l~                           t-                  --lt-~Spread
                          signal                                                                           signal


                                                              Frequency table


                  Suppose we have decided to have eight hopping frequencies. This is extremely low
             for real applications and is just for illustration. In this case, Mis 8 and k is 3. The pseudo-
             random code generator will create eight different 3-bit patterns. These are mapped to
             eight different frequencies in the frequency table (see Figure 6.29).


              Figure 6.29 Frequency selection in FHSS

                                                                                 First-hop frequency


                                                                                 k-bit
                                                                                          t
                                                                                         Frequency

                                 k-bil patterns
                                                                                 000     200kHz
                                                                                 001     300kHz

                                 1
                                     101 111 001 000 010 110 011 100        I 010
                                                                              011
                                                                                         400kHz
                                                                                         500kHz
                                      I           First selection                100
                                                                                 101
                                                                                         600kHz
                                                                                         700kHz-       -
                                                                                 UQ      800kHz
                                                                                 III     900kHz
                                                                                  Frequency table

## SECTION 6.2      SPREAD SPECTRUM          183


     The pattern for this station is 101, 111, 001, 000, 010, all, 100. Note that the pat-
tern is pseudorandom it is repeated after eight hoppings. This means that at hopping
period 1, the pattern is 101. The frequency selected is 700 kHz; the source signal mod-
ulates this carrier frequency. The second k-bit pattern selected is 111, which selects the
900-kHz carrier; the eighth pattern is 100, the frequency is 600 kHz. After eight hop-
pings, the pattern repeats, starting from 101 again. Figure 6.30 shows how the signal hops
around from carrier to carrier. We assume the required bandwidth of the original signal
is 100 kHz.


Figure 6.30 FHSS cycles

              Carrier
            frequencies
              (kHz)


                       • •
                                  Cycle 1                          Cycle 2
             900                                            D
             800
             700
                                                                             D
             600
                                                                                  cP
             500
             400
             300
             200
                         ••
                        ..
                   1      2   3   4   5     6   7   8   9    10 11 12 13     14   l5   16    Hop
                                                                                            periods


    It can be shown that this scheme can accomplish the previously mentioned goals.
If there are many k-bit patterns and the hopping period is short, a sender and receiver
can have privacy. If an intruder tries to intercept the transmitted signal, she can only
access a small piece of data because she does not know the spreading sequence to
quickly adapt herself to the next hop. The scheme has also an antijamming effect. A
malicious sender may be able to send noise to jam the signal for one hopping period
(randomly), but not for the whole period.

Bandwidth Sharing
If the number of hopping frequencies is M, we can multiplex M channels into one by using
the same Bss bandwidth. This is possible because a station uses just one frequency in each
hopping period; M - 1 other frequencies can be used by other M - 1 stations. In other
words, M different stations can use the same Bss if an appropriate modulation technique
such as multiple FSK (MFSK) is used. FHSS is similar to FDM, as shown in Figure 6.31.
      Figure 6.31 shows an example of four channels using FDM and four channels
using FHSS. In FDM, each station uses 11M of the bandwidth, but the allocation is
fixed; in FHSS, each station uses 11M of the bandwidth, but the allocation changes hop
to hop.

184   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             Figure 6.31     Bandwidth sharing


                        Frequency                               Frequency


                                                                14
                                                                    h


                                                                    f1

                                                    Time                                  Time
                       a.FDM                                  b.FHSS


             Direct Sequence Spread Spectrum
             The direct sequence spread spectrum (nSSS) technique also expands the bandwidth
             of the original signal, but the process is different. In DSSS, we replace each data bit
             with 11 bits using a spreading code. In other words, each bit is assigned a code of 11 bits,
             called chips, where the chip rate is 11 times that of the data bit. Figure 6.32 shows the
             concept of DSSS.


             Figure 6.32 DSSS


                                                        Modulator

                           Original - + - - - - - - - + i       r--------ll-~ Spread
                             signal                                                    signal


                  As an example, let us consider the sequence used in a wireless LAN, the famous
             Barker sequence where 11 is 11. We assume that the original signal and the chips in the
             chip generator use polar NRZ encoding. Figure 6.33 shows the chips and the result of
             multiplying the original data by the chips to get the spread signal.
                  In Figure 6.33, the spreading code is 11 chips having the pattern 10110111000 (in
             this case). If the original signal rate is N, the rate of the spread signal is lIN. This
             means that the required bandwidth for the spread signal is 11 times larger than the
             bandwidth of the original signal. The spread signal can provide privacy if the intruder
             does not know the code. It can also provide immunity against interference if each sta-
             tion uses a different code.

## SECTION 6.4    KEY TERMS        185


Figure 6.33 DSSS example


      Original 1--              _
        signal


   Spreading 1---+--+--1-+--1---
        code


       Spread f----t-+-+-i--+---
        signal


Bandwidth Sharing
Can we share a bandwidth in DSSS as we did in FHSS? The answer is no and yes. If we
use a spreading code that spreads signals (from different stations) that cannot be combined
and separated, we cannot share a bandwidth. For example, as we will see in Chapter 14,
some wireless LANs use DSSS and the spread bandwidth cannot be shared. However, if
we use a special type of sequence code that allows the combining and separating of spread
signals, we can share the bandwidth. As we will see in Chapter 16, a special spreading code
allows us to use DSSS in cellular telephony and share a bandwidth between several users.


## 6.3       RECOMMENDED READING
For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [...] refer to the reference list at the end of the text.

Books                                                                      ,   '-

Multiplexing is elegantly discussed in Chapters 19 of [Pea92]. [CouOI] gives excellent
coverage of TDM and FDM in Sections 3.9 to 3.11. More advanced materials can be
found in [Ber96]. Multiplexing is discussed in Chapter 8 of [Sta04]. A good coverage of
spread spectrum can be found in Section 5.13 of [CouOl] and Chapter 9 of [Sta04].


## 6.4       KEY TERMS
analog hierarchy                                digital signal (DS) service
Barker sequence                                 direct sequence spread spectrum (DSSS)
channel                                         Eline
chip                                            framing bit
demultiplexer (DEMUX)                           frequency hopping spread spectrum
dense WDM (DWDM)                                   (FSSS)

186   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


             frequency-division multiplexing (FDM)            multiplexing
             group                                            pseudorandom code generator
             guard band                                       pseudorandom noise (PN)
             hopping period                                   pulse stuffing
             interleaving                                     spread spectrum (SS)
             jumbo group                                      statistical TDM
             link                                             supergroup
             master group                                     synchronous TDM
             multilevel multiplexing                          T line
             multiple-slot multiplexing                       time-division multiplexing (TDM)
             multiplexer (MUX)                                wavelength-division multiplexing (WDM)


## 6.5      SUMMARY
             o Bandwidth utilization is the use of available bandwidth to achieve specific goals.
                   Efficiency can be achieved by using multiplexing; privacy and antijamming can be
                   achieved by using spreading.
             o     Multiplexing is the set of techniques that allows the simultaneous transmission of
                   multiple signals across a single data link. In a multiplexed system, n lines share the
                   bandwidth of one link. The word link refers to the physical path. The word channel
                   refers to the portion of a link that carries a transmission.
             o     There are three basic multiplexing techniques: frequency-division multiplexing,
                   wavelength-division multiplexing, and time-division multiplexing. The first two are
                   techniques designed for analog signals, the third, for digital signals
             o     Frequency-division multiplexing (FDM) is an analog technique that can be applied
                   when the bandwidth of a link (in hertz) is greater than the combined bandwidths of
                   the signals to be transmitted.
             o     Wavelength-division multiplexing (WDM) is designed to use the high bandwidth
                   capability of fiber-optic cable. WDM is an analog multiplexing technique to com-
                   bine optical signals.
             o     Time-division multiplexing (TDM) is a digital process that allows several connec-
                   tions to share the high bandwidth of a link. TDM is a digital multiplexing technique
                   for combining several low-rate channels into one high-rate one.
             o     We can divide TDM into two different schemes: synchronous or statistical. In syn-
                   chronous TDM, each input connection has an allotment in the output even if it is
                   not sending data. In statistical TDM, slots are dynamically allocated to improve
                   bandwidth efficiency.
             o     In spread spectrum (SS), we combine signals from different sources to fit into a
                   larger bandwidth. Spread spectrum is designed to be used in wireless applications
                   in which stations must be able to share the medium without interception by an
                   eavesdropper and without being subject to jamming from a malicious intruder.
             o     The frequency hopping spread spectrum (FHSS) technique uses M different carrier
                   frequencies that are modulated by the source signal. At one moment, the signal

## SECTION 6.6     PRACTICE SET        187


      modulates one carrier frequency; at the next moment, the signal modulates another
      carrier frequency.
o     The direct sequence spread spectrum (DSSS) technique expands the bandwidth of
      a signal by replacing each data bit with n bits using a spreading code. In other words,
      each bit is assigned a code of n bits, called chips.


## 6.6      PRACTICE SET
Review Questions
 1. Describe the goals of multiplexing.
 2. List three main multiplexing techniques mentioned in this chapter.
 3. Distinguish between a link and a channel in multiplexing.
 4. Which of the three multiplexing techniques is (are) used to combine analog signals?
    Which of the three multiplexing techniques is (are) used to combine digital signals?
 5. Define the analog hierarchy used by telephone companies and list different levels
    of the hierarchy.
 6. Define the digital hierarchy used by telephone companies and list different levels
    of the hierarchy.
 7. Which of the three multiplexing techniques is common for fiber optic links?
    Explain the reason.
 8. Distinguish between multilevel TDM, multiple slot TDM, and pulse-stuffed TDM.
 9. Distinguish between synchronous and statistical TDM.
10. Define spread spectrum and its goal. List the two spread spectrum techniques dis-
    cussed in this chapter.
11. Define FHSS and explain how it achieves bandwidth spreading.
12. Define DSSS and explain how it achieves bandwidth spreading.

Exercises
13. Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex
    10 voice channels with guard bands of 500 Hz using FDM. Calculate the required
    bandwidth.
14. We need to transmit 100 digitized voice channels using a pass-band channel of
    20 KHz. What should be the ratio of bits/Hz if we use no guard band?
15. In the analog hierarchy of Figure 6.9, find the overhead (extra bandwidth for guard
    band or control) in each hierarchy level (group, supergroup, master group, and
    jumbo group).
16. We need to use synchronous TDM and combine 20 digital sources, each of 100 Kbps.
    Each output slot carries 1 bit from each digital source, but one extra bit is added to
    each frame for synchronization. Answer the following questions:
    a. What is the size of an output frame in bits?
    b. What is the output frame rate?

188   CHAPTER 6   BANDWIDTH UTIUZATION: MULTIPLEXING AND SPREADING


                  c. What is the duration of an output frame?
                  d. What is the output data rate?
                  e. What is the efficiency of the system (ratio of useful bits to the total bits).
              17. Repeat Exercise 16 if each output slot carries 2 bits from each source.
              18. We have 14 sources, each creating 500 8-bit characters per second. Since only some
                  of these sources are active at any moment, we use statistical TDM to combine these
                  sources using character interleaving. Each frame carries 6 slots at a time, but we need
                  to add four-bit addresses to each slot. Answer the following questions:
                  a. What is the size of an output frame in bits?
                  b. What is the output frame rate?
                  c. What is the duration of an output frame?
                  d. What is the output data rate?
              19. Ten sources, six with a bit rate of 200 kbps and four with a bit rate of 400 kbps are
                  to be combined using multilevel TDM with no synchronizing bits. Answer the fol-
                  lowing questions about the final stage of the multiplexing:
                  a. What is the size of a frame in bits?
                  b. What is the frame rate?
                  c. What is the duration of a frame?
                  d. What is the data rate?
              20. Four channels, two with a bit rate of 200 kbps and two with a bit rate of 150 kbps, are
                  to be multiplexed using multiple slot TDM with no synchronization bits. Answer
                  the following questions:
                  a. What is the size of a frame in bits?
                  b. What is the frame rate?
                  c. What is the duration of a frame?
                  d. What is the data rate?
              21. Two channels, one with a bit rate of 190 kbps and another with a bit rate of 180 kbps,
                  are to be multiplexed using pulse stuffing TDM with no synchronization bits. Answer
                  the following questions:
                  a. What is the size of a frame in bits?
                  b. What is the frame rate?
                  c. What is the duration of a frame?
                  d. What is the data rate?
              22. Answer the following questions about a T-1 line:
                  a. What is the duration of a frame?
                  b. What is the overhead (number of extra bits per second)?
              23. Show the contents of the five output frames for a synchronous TDM multiplexer
                  that combines four sources sending the following characters. Note that the characters
                  are sent in the same order that they are typed. The third source is silent.
                  a. Source 1 message: HELLO
                  b. Source 2 message: HI

## SECTION 6.6       PRACTICE SET      189


    c. Source 3 message:
    d. Source 4 message: BYE
24. Figure 6.34 shows a multiplexer in a synchronous TDM system. Each output slot is
    only 10 bits long (3 bits taken from each input plus 1 framing bit). What is the output
    stream? The bits arrive at the multiplexer as shown by the arrows.


Figure 6.34    Exercise 24


               101110111101~
                                                            IFrame of 10 bits I
                 11111110000~


              1010000001111~


25. Figure 6.35 shows a demultiplexer in a synchronous TDM. If the input slot is 16 bits
    long (no framing bits), what is the bit stream in each output? The bits arrive at the
    demultiplexer as shown by the arrows.


Figure 6.35   Exercise 25


              101000001110101010101000011101110000011110001

                                               •


26. Answer the following questions about the digital hierarchy in Figure 6.23:
    a. What is the overhead (number of extra bits) in the DS-l service?
    b. What is the overhead (number of extra bits) in the DS-2 service?
    c. What is the overhead (number of extra bits) in the DS-3 service?
    d. What is the overhead (number of extra bits) in the DS-4 service?
27. What is the minimum number of bits in a PN sequence if we use FHSS with a
    channel bandwidth of B = 4 KHz and B ss = 100 KHz?
28. An FHSS system uses a 4-bit PN sequence. If the bit rate of the PN is 64 bits per
    second, answer the following questions:
    a. What is the total number of possible hops?
    b. What is the time needed to finish a complete cycle of PN?

190   CHAPTER 6   BANDWIDTH UTILIZATION: MULTIPLEXING AND SPREADING


              29. A pseudorandom number generator uses the following formula to create a random
                  series:

                                           N i +1 = (5 + 7Ni ) mod 17-1

                  In which N j defines the current random number and Nj + 1 defines the next random
                  number. The term mod means the value of the remainder when dividing (5 + 7N j )
                  by 17.
              30. We have a digital medium with a data rate of 10 Mbps. How many 64-kbps voice
                  channels can be carried by this medium if we use DSSS with the Barker sequence?

## CHAPTER 7

      Transmission Media


      We discussed many issues related to the physical layer in Chapters 3 through 6. In this
## chapter, we discuss transmission media. Transmission media are actually located below
      the physical layer and are directly controlled by the physical layer. You could say that
      transmission media belong to layer zero. Figure 7.1 shows the position of transmission
      media in relation to the physical layer.


      Figure 7.1       Transmission medium and physical layer


              Sender   I Physical layer   I                         I   Physical layer   I
                                                                                         Receiver


                                L...          Transmission medium


                                                  Cable or air
                                                                    .....J
           A transmission medium can be broadly defined as anything that can carry infor-
      mation from a source to a destination. For example, the transmission medium for two
      people having a dinner conversation is the air. The air can also be used to convey the
      message in a smoke signal or semaphore. For a written message, the transmission
      medium might be a mail carrier, a truck, or an airplane.
           In data communications the definition of the information and the transmission
      medium is more specific. The transmission medium is usually free space, metallic cable,
      or fiber-optic cable. The information is usually a signal that is the result of a conversion
      of data from another form.
           The use of long-distance communication using electric signals started with the
      invention of the telegraph by Morse in the 19th century. Communication by telegraph
      was slow and dependent on a metallic medium.
           Extending the range of the human voice became possible when the telephone was
      invented in 1869. Telephone communication at that time also needed a metallic medium
      to carry the electric signals that were the result of a conversion from the human voice.


                                                                                                    191

192   CHAPTER 7   1RANSMISSION MEDIA


             The communication was, however, unreliable due to the poor quality of the wires. The
             lines were often noisy and the technology was unsophisticated.
                  Wireless communication started in 1895 when Hertz was able to send high-
             frequency signals. Later, Marconi devised a method to send telegraph-type messages
             over the Atlantic Ocean.
                  We have come a long way. Better metallic media have been invented (twisted-
             pair and coaxial cables, for example). The use of optical fibers has increased the data
             rate incredibly. Free space (air, vacuum, and water) is used more efficiently, in part
             due to the technologies (such as modulation and multiplexing) discussed in the previous
             chapters.
                  As discussed in Chapter 3, computers and other telecommunication devices use
             signals to represent data. These signals are transmitted from one device to another in the
             form of electromagnetic energy, which is propagated through transmission media.
                  Electromagnetic energy, a combination of electric and magnetic fields vibrating in
             relation to each other, includes power, radio waves, infrared light, visible light, ultraviolet
             light, and X, gamma, and cosmic rays. Each of these constitutes a portion of the electro-
             magnetic spectrum. Not all portions of the spectrum are currently usable for telecommu-
             nications, however. The media to harness those that are usable are also limited to a few
             types.
                   In telecommunications, transmission media can be divided into two broad catego-
             ries: guided and unguided. Guided media include twisted-pair cable, coaxial cable, and
             fiber-optic cable. Unguided medium is free space. Figure 7.2 shows this taxonomy.


              Figure 7.2   Classes of transmission media


## 7.1     GUIDED MEDIA
             Guided media, which are those that provide a conduit from one device to another,
             include twisted-pair cable, coaxial cable, and fiber-optic cable. A signal traveling
             along any of these media is directed and contained by the physical limits of the
             medium. Twisted-pair and coaxial cable use metallic (copper) conductors that accept
             and transport signals in the form of electric current. Optical fiber is a cable that accepts
             and transports signals in the form of light.

## SECTION 7.1     GUIDED MEDIA           193


Twisted-Pair Cable
A twisted pair consists of two conductors (normally copper), each with its own plastic
insulation, twisted together, as shown in Figure 7.3.

Figure 7.3      Twisted-pair cable


     '""il""'   <
      One of the wires is used to carry signals to the receiver, and the other is used only
as a ground reference. The receiver uses the difference between the two.
      In addition to the signal sent by the sender on one of the wires, interference (noise)
and crosstalk may affect both wires and create unwanted signals.
     If the two wires are parallel, the effect of these unwanted signals is not the same in
both wires because they are at different locations relative to the noise or crosstalk sources
(e,g., one is closer and the other is farther). This results in a difference at the receiver. By
twist,ing the pairs, a balance is maintained. For example, suppose in one twist, one wire
is closer to the noise source and the other is farther; in the next twist, the reverse is true.
Twisting makes it probable that both wires are equally affected by external influences
(noise or crosstalk). This means that the receiver, which calculates the difference between
the two, receives no unwanted signals. The unwanted signals are mostly canceled out.
From the above discussion, it is clear that the number of twists per unit of length
(e.g., inch) has some effect on the quality of the cable.

Unshielded Versus Shielded Twisted-Pair Cable
The most common twisted-pair cable used in communications is referred to as
unshielded twisted-pair (UTP). IBM has also produced a version of twisted-pair cable
for its use called shielded twisted-pair (STP). STP cable has a metal foil or braided-
mesh covering that encases each pair of insulated conductors. Although metal casing
improves the quality of cable by preventing the penetration of noise or crosstalk, it is
bulkier and more expensive. Figure 7.4 shows the difference between UTP and STP.
Our discussion focuses primarily on UTP because STP is seldom used outside of IBM.

Categories
The Electronic Industries Association (EIA) has developed standards to classify
unshielded twisted-pair cable into seven categories. Categories are determined by cable
quality, with 1 as the lowest and 7 as the highest. Each EIA category is suitable for
specific uses. Table 7. I shows these categories.

Connectors
The most common UTP connector is RJ45 (RJ stands for registered jack), as shown
in Figure 7.5. The RJ45 is a keyed connector, meaning the connector can be inserted in
only one way.

194   CHAPTER 7    TRANSMISSION MEDIA


             Figure 7.4           UTP and STP cables


                                                                                        Metal shield


                         Plastic cover                                        Plastic cover

              a.UTP                                                   b.STP


             Table 7.1          Categories of unshielded twisted-pair cables

                                                                                              Data Rate
                  Category                          Specification                              (Mbps)        Use
                     I             Unshielded twisted-pair used in telephone                     < 0.1    Telephone
                     2            Unshielded twisted-pair originally used in                       2      T-llines
                                  T-lines
                     3             Improved CAT 2 used in LANs                                    10      LANs
                     4            Improved CAT 3 used in Token Ring networks                      20      LANs
                     5             Cable wire is normally 24 AWG with a jacket                   100      LANs
                                   and outside sheath
                     SE            An extension to category 5 that includes                      125      LANs
                                   extra features to minimize the crosstalk and
                                   electromagnetic interference
                     6            A new category with matched components                         200      LANs
                                  coming from the same manufacturer. The
                                  cable must be tested at a 200-Mbps data rate.
                     7             Sometimes called SSTP (shielded screen                       600       LANs
                                   twisted-pair). Each pair is individually
                                   wrapped in a helical metallic foil followed by
                                   a metallic foil shield in addition to the outside
                                   sheath. The shield decreases the effect of
                                   crosstalk: and increases the data rate.

             Performance
             One way to measure the performance of twisted-pair cable is to compare attenuation
             versus frequency and distance. A twisted-pair cable can pass a wide range of frequencies.
             However, Figure 7.6 shows that with increasing frequency, the attenuation, measured in
             decibels per kilometer (dB/km), sharply increases with frequencies above 100 kHz. Note
             that gauge is a measure of the thickness of the wire.

## SECTION 7.1      GUIDED MEDIA     195


Figure 7.5         UTP connector


                            nrnl n
                            12345678


                                                               RJ-45 Male


Figure 7.6         UTP performance


                          Gauge   Diameter (inches)                            26 gauge
                   20
                           18         0.0403
                   18      22         0.02320
                           24         0.02010
                   16
                           26         0.0159
          ]' 14
          iIi
          ::3- 12
             <::                                                                  18 gauge
          .g
             '"
             :I    10
             <::

          ~"        8
                    6

                    4


                    2   E::::::::..------
                                           10                  100               1000
                                                      !(kHz)


Applications
Twisted-pair cables are used in telephone lines to provide voice and data channels. The
local loop-the line that connects subscribers to the central telephone office---commonly
consists of unshielded twisted-pair cables. We discuss telephone networks in Chapter 9.
     The DSL lines that are used by the telephone companies to provide high-data-rate
connections also use the high-bandwidth capability of unshielded twisted-pair cables.
We discuss DSL technology in Chapter 9.
     Local-area networks, such as lOBase-T and lOOBase-T, also use twisted-pair cables.
We discuss these networks in Chapter 13.

Coaxial Cable
Coaxial cable (or coax) carries signals of higher frequency ranges than those in twisted-
pair cable, in part because the two media are constructed quite differently. Instead of

196   CHAPTER 7   TRANSMISSION MEDIA


             having two wires, coax has a central core conductor of solid or stranded wire (usually
             copper) enclosed in an insulating sheath, which is, in turn, encased in an outer conductor
             of metal foil, braid, or a combination of the two. The outer metallic wrapping serves
             both as a shield against noise and as the second conductor, which completes the circuit.
             This outer conductor is also enclosed in an insulating sheath, and the whole cable is
             protected by a plastic cover (see Figure 7.7).


             Figure 7.7   Coaxial cable


                                                         Insulator


                                                     Outer conductor
                                                        (shield)


             Coaxial Cable Standards
             Coaxial cables are categorized by their radio government (RG) ratings. Each RG num-
             ber denotes a unique set of physical specifications, including the wire gauge of the
             inner conductor, the thickness and type of the inner insulator, the construction of the
             shield, and the size and type of the outer casing. Each cable defined by an RG rating is
             adapted for a specialized function, as shown in Table 7.2.

                                  Table 7.2     Categories of coaxial cables

                                     Category         Impedance             Use
                                   RG-59                 75 n          Cable TV
                                   RG-58                 50n           Thin Ethernet
                                   RG-ll                 50n           Thick Ethernet


             Coaxial Cable Connectors
             To connect coaxial cable to devices, we need coaxial connectors. The most common
             type of connector used today is the Bayone-Neill-Concelman (BNe), connector.
             Figure 7.8 shows three popular types of these connectors: the BNC connector, the
             BNC T connector, and the BNC terminator.
                  The BNC connector is used to connect the end of the cable to a device, such as a
             TV set. The BNC T connector is used in Ethernet networks (see Chapter 13) to branch
             out to a connection to a computer or other device. The BNC terminator is used at the
             end of the cable to prevent the reflection of the signal.

## SECTION 7.1                GUIDED MEDIA           11)7


- - - - - - - - - - - - - - - - - - - - - - - - - - - - _ . ------
Figure 7.8 BNC connectors

                                                 BNCT
         Cable

                 t

                              BNC connector                                       50-a           Ground
                                                                          BNe terminator          wire

---------------------------~-                                                              --

Performance
As we did with twisted-pair cables, we can measure the performance of a coaxial cable.
We notice in Figure 7.9 that the attenuation is much higher in coaxial cables than in
twisted-pair cable. In other words, although coaxial cable has a much higher bandwidth,
the signal weakens rapidly and requires the frequent use of repeaters.


Figure 7.9           Coaxial cable peiformance


## 0.712.9 mm
                     35                                                    !

                     30
                                                                              /
                                                                          I
          a
          ~
          a:l
          :2-
                     25

                                                                  !
                                                                      /       1.2/4.4 mm

             .:      20                                         /
             0


                                                            /
          .~
             ;::l
             .:
             ~       15
          ~

                     10


                      5


## 0.01           0.1          1.0                 IO                   100
                                                   j(kHz)


Applications
Coaxial cable was widely used in analog telephone networks where a single coaxial net-
work could carry 10,000 voice signals. Later it was used in digital telephone networks
where a single coaxial cable could carry digital data up to 600 Mbps. However, coaxial
cable in telephone networks has largely been replaced today with fiber-optic cable.
    Cable TV networks (see Chapter 9) also use coaxial cables. In the traditional cable
TV network, the entire network used coaxial cable. Later, however, cable TV providers

198   CHAPTER 7   TRANSMISSION MEDIA


             replaced most of the media with fiber-optic cable; hybrid networks use coaxial cable
             only at the network boundaries, near the consumer premises. Cable TV uses RG-59
             coaxial cable.
                  Another common application of coaxial cable is in traditional Ethernet LANs (see
## Chapter 13). Because of its high bandwidth, and consequently high data rate, coaxial
             cable was chosen for digital transmission in early Ethernet LANs. The 10Base-2, or Thin
             Ethernet, uses RG-58 coaxial cable with BNe connectors to transmit data at 10 Mbps
             with a range of 185 m. The lOBase5, or Thick Ethernet, uses RG-11 (thick coaxial cable)
             to transmit 10 Mbps with a range of 5000 m. Thick Ethernet has specialized connectors.

             Fiber-Optic Cable
             A fiber-optic cable is made of glass or plastic and transmits signals in the form of light.
             To understand optical fiber, we first need to explore several aspects of the nature of light.
                  Light travels in a straight line as long as it is moving through a single uniform sub-
             stance. If a ray of light traveling through one substance suddenly enters another substance
             (of a different density), the ray changes direction. Figure 7.10 shows how a ray of light
             changes direction when going from a more dense to a less dense substance.


             Figure 7.10        Bending of light ray


                     Less
                     dense
                                     /                 Less
                                                       dense
                                                                        I
                                                                                    Less
                                                                                    dense
                                                                                                   I


                                                                 r
                                                                        I                          I
                                                                                                   I

                     More                              More                         More,     A
                                A                                                                       ~
                     dense                             dense
                                                                                    densezj.

                                                                    I   I                     [    I
                                     I                                  I                          I

                            I < critical angle,               I = critical angle,          I> critical angle,
                               refraction                        refraction                   reflection


                  As the figure shows, if the angle of incidence I (the arIgle the ray makes with the
             line perpendicular to the interface between the two substances) is less than the critical
             angle, the ray refracts and moves closer to the surface. If the angle of incidence is
             equal to the critical angle, the light bends along the interface. If the angle is greater than
             the critical angle, the ray reflects (makes a turn) and travels again in the denser sub-
             stance. Note that the critical angle is a property of the substance, and its value differs
             from one substance to another.
                  Optical fibers use reflection to guide light through a channel. A glass or plastic core
             is surrounded by a cladding of less dense glass or plastic. The difference in density of the
             two materials must be such that a beam of light moving through the core is reflected off
             the cladding instead of being refracted into it. See Figure 7.11.

             Propagation Modes
             Current technology supports two modes (multimode and single mode) for propagating light
             along optical channels, each requiring fiber with different physical characteristics. Multi-
             mode can be implemented in two forms: step-index or graded-index (see Figure 7.12).

## SECTION 7.1   GUlDED MEDIA                199


Figure 7.11    Opticaljiber


                                         Cladding

      Sender                                                           L.-_....J
                                                                                   Receiver

                                         Cladding


Figure 7.12    Propagation modes


Multimode Multimode is so named because multiple beams from a light source
move through the core in different paths. How these beams move within the cable
depends on the structure ofthe core, as shown in Figure 7.13.
     In multimode step-index fiber, the density of the core remains constant from the
center to the edges. A beam of light moves through this constant density in a straight
line until it reaches the interface of the core and the cladding. At the interface, there is
an abrupt change due to a lower density; this alters the angle of the beam's motion. The
term step index refers to the suddenness of this change, which contributes to the distor-
tion of the signal as it passes through the fiber.
     A second type of fiber, called multimode graded-index fiber, decreases this distor-
tion of the signal through the cable. The word index here refers to the index of refraction.
As we saw above, the index of refraction is related to density. A graded-index fiber,
therefore, is one with varying densities. Density is highest at the center of the core and
decreases gradually to its lowest at the edge. Figure 7.13 shows the impact of this vari-
able density on the propagation of light beams.

Single-Mode Single-mode uses step-index fiber and a highly focused source of light
that limits beams to a small range of angles, all close to the horizontal. The single-
mode fiber itself is manufactured with a much smaller diameter than that of multimode
fiber, and with substantiallY lower density (index of refraction). The decrease in density
results in a critical angle that is close enough to 90° to make the propagation of beams
almost horizontal. In this case, propagation of different beams is almost identical, and
delays are negligible. All the beams arrive at the destination "together" and can be
recombined with little distortion to the signal (see Figure 7.13).

200   CHAPTER 7   TRANSMISSION MEDIA


             Figure 7.13       Modes


                           JlJ1
                             Source                                                   Destination


                       a. Multimode, step index


                           JlJ1
                             Source                                                   Destination


                       b. Multimode, graded index


                           JlJ1
                             Source                                                   Destination


                       c. Single mode


             Fiber Sizes
             Optical fibers are defined by the ratio of the diameter of their core to the diameter of
             their cladding, both expressed in micrometers. The common sizes are shown in Table 7.3.
             Note that the last size listed is for single-mode only.

             Table 7.3 Fiber types
                    Type                Core(~)            Cladding (Jlm)                    Mode
                  501125                   50.0                  125             Multimode, graded index
## 62.51125                 62.5                  125             Multimode, graded index
                  100/125                 100.0                  125             Multimode, graded index
                   7/125                     7.0                 125             Single mode

             Cable Composition
             Figure 7.14 shows the composition of a typical fiber-optic cable. The outer jacket is made
             of either PVC or Teflon. Inside the jacket are Kevlar strands to strengthen the cable. Kevlar
             is a strong material used in the fabrication of bulletproof vests. Below the Kevlar is another
             plastic coating to cushion the fiber. The fiber is at the center of the cable, and it consists of
             cladding and core.

             Fiber-Optic Cable Connectors
             There are three types of connectors for fiber-optic cables, as shown in Figure 7.15.

## SECTION 7.1          GUIDED MEDIA   201


Figure 7.14 Fiber construction

                                                    Du Pont Kevlar
                                              /     for strength


                                                           Glass or
                                                          plastic core


Figure 7.15    Fiber-optic cable connectors


                  SC connector                                   ST connector


                           RX

                           TX

                                       MT-RJ connector


    The subscriber channel (SC) connector is used for cable TV. It uses a push/pull
locking system. The straight-tip (ST) connector is used for connecting cable to
networking devices. It uses a bayonet locking system and is more reliable than SC.
MT-RJ is a connector that is the same size as RJ45.

Performance
The plot of attenuation versus wavelength in Figure 7.16 shows a very interesting
phenomenon in fiber-optic cable. Attenuation is flatter than in the case of twisted-pair
cable and coaxial cable. The performance is such that we need fewer (actually 10 times
less) repeaters when we use fiber-optic cable.

Applications
Fiber-optic cable is often found in backbone networks because its wide bandwidth is
cost-effective. Today, with wavelength-division multiplexing (WDM), we can transfer

202   CHAPTER 7   IRANSMISSION MEDIA


             Figure 7.16       Optical fiber performance


                                 100
                                  50


                                   IO
                                    5
                           ~
                           ~
                           ~
                           00
                           00
                           0
                                   1
                           ..l
## 0.5


## 0.1
## 0.05


## 0.01
                                        800      1000      1200       1400    1600   1800
                                                           Wavelength (urn)


             data at a rate of 1600 Gbps. The SONET network that we discuss in Chapter 17 provides
             such a backbone.
                  Some cable TV companies use a combination of optical fiber and coaxial cable,
             thus creating a hybrid network. Optical fiber provides the backbone structure while
             coaxial cable provides the connection to the user premises. This is a cost-effective con-
             figuration since the narrow bandwidth requirement at the user end does not justify the
             use of optical fiber.
                  Local-area networks such as 100Base-FX network (Fast Ethernet) and 1000Base-X
             also use fiber-optic cable.

             Advantages and Disadvantages of Optical Fiber
             Advantages Fiber-optic cable has several advantages over metallic cable (twisted-
             pair or coaxial).
             D Higher bandwidth. Fiber-optic cable can support dramatically higher bandwidths
               (and hence data rates) than either twisted-pair or coaxial cable. Currently, data rates
               and bandwidth utilization over fiber-optic cable are limited not by the medium but
               by the signal generation and reception technology available.
             D Less signal attenuation. Fiber-optic transmission distance is significantly greater
               than that of other guided media. A signal can run for 50 km without requiring
               regeneration. We need repeaters every 5 km for coaxial or twisted-pair cable.
             D Immunity to electromagnetic interference. Electromagnetic noise cannot affect
               fiber-optic cables.
             o Resistance to corrosive materials. Glass is more resistant to corrosive materials
               than copper.

## SECTION 7.2      UNGUIDED MEDIA: WIRELESS          203


o Light weight. Fiber-optic cables are much lighter than copper cables.
o Greater immunity to tapping. Fiber-optic cables are more immune to tapping than
      copper cables. Copper cables create antenna effects that can easily be tapped.

Disadvantages There are some disadvantages in the use of optical fiber.
o   Installation and maintenance. Fiber-optic cable is a relatively new technology. Its
    installation and maintenance require expertise that is not yet available everywhere.
o Unidirectional light propagation. Propagation of light is unidirectional. If we
    need bidirectional communication, two fibers are needed.
o Cost. The cable and the interfaces are relatively more expensive than those of other
    guided media. If the demand for bandwidth is not high, often the use of optical fiber
    cannot be justified.


## 7.2      UNGUIDED MEDIA: WIRELESS
Unguided media transport electromagnetic waves without using a physical conductor.
This type of communication is often referred to as wireless communication. Signals
are normally broadcast through free space and thus are available to anyone who has a
device capable of receiving them.
     Figure 7.17 shows the part of the electromagnetic spectrum, ranging from 3 kHz to
900 THz, used for wireless communication.


Figure 7.17     Electromagnetic spectrumfor wireless communication


                           Radio wave and microwave

        3                                                       300         400   900
       kHz                                                      GHz         THz THz


     Unguided signals can travel from the source to destination in several ways: ground
propagation, sky propagation, and line-of-sight propagation, as shown in Figure 7.18.
     In ground propagation, radio waves travel through the lowest portion of the
atmosphere, hugging the earth. These low-frequency signals emanate in all directions
from the transmitting antenna and follow the curvature of the planet. Distance depends
on the amount of power in the signal: The greater the power, the greater the distance. In
sky propagation, higher-frequency radio waves radiate upward into the ionosphere
(the layer of atmosphere where particles exist as ions) where they are reflected back to
earth. This type of transmission allows for greater distances with lower output power.
In line-or-sight propagation, very high-frequency signals are transmitted in straight
lines directly from antenna to antenna. Antennas must be directional, facing each other,

204   CHAPTER 7   TRANSMISSION MEDIA


             Figure 7.18      Propagation methods

                               Ionosphere                   Ionosphere                      Ionosphere


                           Ground propagation          Sky propagation               Line-af-sight propagation
                             (below 2 MHz)               (2-30 MHz)                      (above 30 MHz)


             and either tall enough or close enough together not to be affected by the curvature of
             the earth. Line-of-sight propagation is tricky because radio transmissions cannot be
             completely focused.
                  The section of the electromagnetic spectrum defined as radio waves and microwaves
             is divided into eight ranges, called bands, each regulated by government authorities.
             These bands are rated from very low frequency (VLF) to extremely highfrequency (EHF).
             Table 7.4 lists these bands, their ranges, propagation methods, and some applications.


             Table 7.4     Bands

                         Band                       Range                Propagation               Application
              VLF (very low frequency)            3-30 kHz               Ground           Long-range radio
                                                                                          navigation
              LF (low frequency)                 30-300 kHz          Ground               Radio beacons and
                                                                                          navigational locators
              MF (middle frequency)             300 kHz-3 MHz            Sky              AM radio
              HF (high frequency)                 3-30 MHz               Sky              Citizens band (CB),
                                                                                          shipiaircraft
                                                                                          communication
              VHF (very high frequency)          30-300 MHz          Sky and              VHF TV, FM radio
                                                                     line-of-sight
              UHF (ultrahigh frequency)         300 MHz-3 GHz        Line-of-sight        UHF TV, cellular phones,
                                                                                          paging, satellite
              SHF (superhigh frequency)           3-30 GHz               Line-of-sight    Satellite communication
              EHF (extremely high                30-300 GHz          Line-of-sight        Radar, satellite
              frequency)


                We can divide wireless transmission into three broad groups: radio waves, micro-
             waves, and infrared waves. See Figure 7.19.

## SECTION 7.2    UNGUIDED MEDIA: WIRELESS            205


Figure 7.19    Wireless transmission waves


Radio Waves
Although there is no clear-cut demarcation between radio waves and microwaves, elec-
tromagnetic waves ranging in frequencies between 3 kHz and 1 GHz are normally called
radio waves; waves ranging in frequencies between 1 and 300 GHz are called micro-
waves. However, the behavior of the waves, rather than the frequencies, is a better
criterion for classification.
     Radio waves, for the most part, are omnidirectional. When an antenna transmits
radio waves, they are propagated in all directions. This means that the sending and
receiving antennas do not have to be aligned. A sending antenna sends waves that can
be received by any receiving antenna. The omnidirectional property has a disadvantage,
too. The radio waves transmitted by one antenna are susceptible to interference by
another antenna that may send signals using the same frequency or band.
     Radio waves, particularly those waves that propagate in the sky mode, can travel
long distances. This makes radio waves a good candidate for long-distance broadcast-
ing such as AM radio.
     Radio waves, particularly those of low and medium frequencies, can penetrate walls.
This characteristic can be both an advantage and a disadvantage. It is an advantage
because, for example, an AM radio can receive signals inside a building. It is a disadvan-
tage because we cannot isolate a communication to just inside or outside a building. The
radio wave band is relatively narrow, just under 1 GHz, compared to the microwave
band. When this band is divided into subbands, the subbands are also narrow, leading to a
low data rate for digital communications.
     Almost the entire band is regulated by authorities (e.g., the FCC in the United
States). Using any part of the band requires permission from the authorities.


Omnidirectional Antenna
Radio waves use omnidirectional antennas that send out signals in all directions.
Based on the wavelength, strength, and the purpose of transmission, we can have sev-
eral types of antennas. Figure 7.20 shows an omnidirectional antenna.


Applications
The omnidirectional characteristics of radio waves make them useful for multicasting,
in which there is one sender but many receivers. AM and FM radio, television, mari-
time radio, cordless phones, and paging are examples of multicasting.

206   CHAPTER 7   TRANSMISSION MEDIA


             Figure 7.20    Omnidirectional antenna


                                Radio waves are used for multicast communications,
                                 such as radio and television, and paging systems.


             Microwaves
             Electromagnetic waves having frequencies between I and 300 GHz are called micro-
             waves.
                 Microwaves are unidirectional. When an antenna transmits microwave waves, they
             can be narrowly focused. This means that the sending and receiving antennas need to
             be aligned. The unidirectional property has an obvious advantage. A pair of antennas
             can be aligned without interfering with another pair of aligned antennas. The following
             describes some characteristics of microwave propagation:
             o Microwave propagation is line-of-sight. Since the towers with the mounted antennas
                  need to be in direct sight of each other, towers that are far apart need to be very tall.
                  The curvature of the earth as well as other blocking obstacles do not allow two short
                  towers to communicate by using microwaves. Repeaters are often needed for long-
                  distance communication.
             o    Very high-frequency microwaves cannot penetrate walls. This characteristic can be
                  a disadvantage if receivers are inside buildings.
             o    The microwave band is relatively wide, almost 299 GHz. Therefore wider subbands
                  can be assigned, and a high data rate is possible
              o   Use of certain portions of the band requires permission from authorities.

              Unidirectional Antenna
             Microwaves need unidirectional antennas that send out signals in one direction. Two
             types of antennas are used for microwave communications: the parabolic dish and the
             hom (see Figure 7.21).
                   A parabolic dish antenna is based on the geometry of a parabola: Every line
             parallel to the line of symmetry (line of sight) reflects off the curve at angles such that
             all the lines intersect in a common point called the focus. The parabolic dish works as a

## SECTION 7.2   UNGUIDED MEDIA: WIRELESS       207


Figure 7.21    Unidirectional antennas


                       Focus ~,,*=:::I


          a. Dish antenna                       b. Horn antenna


funnel, catching a wide range of waves and directing them to a common point. In
this way, more of the signal is recovered than would be possible with a single-point
receiver.
     Outgoing transmissions are broadcast through a horn aimed at the dish. The micro-
waves hit the dish and are deflected outward in a reversal of the receipt path.
     A horn antenna looks like a gigantic scoop. Outgoing transmissions are broadcast
up a stem (resembling a handle) and deflected outward in a series of narrow parallel
beams by the curved head. Received transmissions are collected by the scooped shape of
the horn, in a manner similar to the parabolic dish, and are deflected down into the stem.

Applications
Microwaves, due to their unidirectional properties, are very useful when unicast
(one-to-one) communication is needed between the sender and the receiver. They are
used in cellular phones (Chapter 16), satellite networks (Chapter 16), and wireless LANs
(Chapter 14).


       Microwaves are used for unicast communication such as cellular telephones,
                        satellite networks, and wireless LANs.


Infrared
Infrared waves, with frequencies from 300 GHz to 400 THz (wavelengths from 1 mm
to 770 nm), can be used for short-range communication. Infrared waves, having high
frequencies, cannot penetrate walls. This advantageous characteristic prevents interfer-
ence between one system and another; a short-range communication system in one room
cannot be affected by another system in the next room. When we use our infrared remote
control, we do not interfere with the use of the remote by our neighbors. However, this
same characteristic makes infrared signals useless for long-range communication. In
addition, we cannot use infrared waves outside a building because the sun's rays contain
infrared waves that can interfere with the communication.

208   CHAPTER 7   TRANSMISSION MEDIA


             Applications
             The infrared band, almost 400 THz, has an excellent potential for data transmission.
             Such a wide bandwidth can be used to transmit digital data with a very high data rate.
             The Infrared Data Association (IrDA), an association for sponsoring the use of infrared
             waves, has established standards for using these signals for communication between
             devices such as keyboards, mice, PCs, and printers. For example, some manufacturers
             provide a special port called the IrDA port that allows a wireless keyboard to commu-
             nicate with a PC. The standard originally defined a data rate of 75 kbps for a distance
             up to 8 m. The recent standard defines a data rate of 4 Mbps.
                  Infrared signals defined by IrDA transmit through line of sight; the IrDA port on
             the keyboard needs to point to the PC for transmission to occur.


                             Infrared signals can be used for short-range communication
                                   in a closed area using line-of-sight propagation.


## 7.3     RECOMMENDED READING
             For more details about subjects discussed in this chapter, we recommend the following
             books. The items in brackets [...] refer to the reference list at the end of the text.

             Books
             Transmission media is discussed in Section 3.8 of [GW04], Chapter 4 of [Sta04], Sec-
             tion 2.2 and 2.3 of [Tan03]. [SSS05] gives a full coverage of transmission media.


## 7.4     KEY TERMS
             angle of incidence                              IrDA port
             Bayone-Neil-Concelman (BNC)                     line-of-sight propagation
               connector                                     microwave
             cladding                                        MT-RJ
             coaxial cable                                   multimode graded-index fiber
             core                                            multimode step-index fiber
             critical angle                                  omnidirectional antenna
             electromagnetic spectrum                        optical fiber
             fiber-optic cable                               parabolic dish antenna
             gauge                                           Radio Government (RG) number
             ground propagation                              radio wave
             guided media                                    reflection
             horn antenna                                    refraction
             infrared wave                                   RJ45

## SECTION 7.6   PRACTICE SET        209


shielded twisted-pair (STP)                   twisted-pair cable
single-mode fiber                             unguided medium
sky propagation                               unidirectional antenna
straight-tip (ST) connector                   unshielded twisted-pair
subscriber channel (SC) connector               (UTP)
transmission medium                           wireless communication


## 7.5     SUMMARY
o Transmission media lie below the physical layer.
D A guided medium provides a physical conduit from one device to another. Twisted-
  pair cable, coaxial cable, and optical fiber are the most popular types of guided
  media.
D Twisted-pair cable consists of two insulated copper wires twisted together. Twisted-
  pair cable is used for voice and data communications.
D Coaxial cable consists of a central conductor and a shield. Coaxial cable can carry
  signals of higher frequency ranges than twisted-pair cable. Coaxial cable is used in
  cable TV networks and traditional Ethernet LANs.
o Fiber-optic cables are composed of a glass or plastic inner core surrounded by
  cladding, all encased in an outside jacket. Fiber-optic cables carry data signals in
  the form of light. The signal is propagated along the inner core by reflection. Fiber-
  optic transmission is becoming increasingly popular due to its noise resistance, low
  attenuation, and high-bandwidth capabilities. Fiber-optic cable is used in backbone
  networks, cable TV networks, and Fast Ethernet networks.
D Unguided media (free space) transport electromagnetic waves without the use of a
  physical conductor.
o Wireless data are transmitted through ground propagation, sky propagation, and line-
  of-sight propagation.Wireless waves can be classified as radio waves, microwaves, or
  infrared waves. Radio waves are omnidirectional; microwaves are unidirectional.
  Microwaves are used for cellular phone, satellite, and wireless LAN communications.
D Infrared waves are used for short-range communications such as those between a
  PC and a peripheral device. It can also be used for indoor LANs.


## 7.6     PRACTICE SET
Review Questions
 1. What is the position of the transmission media in the OSI or the Internet model?
 2. Name the two major categories of transmission media.
 3. How do guided media differ from unguided media?
 4. What are the three major classes of guided media?
 5. What is the significance of the twisting in twisted-pair cable?

210   CHAPTER 7   TRANSMISSION MEDIA


               6. What is refraction? What is reflection?
               7. What is the purpose of cladding in an optical fiber?
               8. Name the advantages of optical fiber over twisted-pair and coaxial cable.
               9. How does sky propagation differ from line-of-sight propagation?
              10. What is the difference between omnidirectional waves and unidirectional waves?

             Exercises
              11. Using Figure 7.6, tabulate the attenuation (in dB) of a 18-gauge UTP for the indicated
                  frequencies and distances.

                        Table 7.5 Attenuation/or I8-gauge UTP

                          Distance      dB at 1 KHz       dRat 10KHz        dB at 100 KHz
                          1 Krn
                          lOKm
                          15 Krn
                          20Km


              12. Use the result of Exercise 11 to infer that the bandwidth of a UTP cable decreases
                  with an increase in distance.
              13. If the power at the beginning of a 1 KIn 18-gauge UTP is 200 mw, what is the
                  power at the end for frequencies 1 KHz, 10 KHz, and 100 KHz? Use the result of
                  Exercise 11.
              14. Using Figure 7.9, tabulate the attenuation (in dB) of a 2.6/9.5 mm coaxial cable for
                  the indicated frequencies and distances.

                        Table 7.6 Attenuation/or 2.6/9.5 mm coaxial cable

                          Distance      dB at 1 KHz       dB at 10 KHz      dB at 100KHz
                          1 Km
                          lOKrn
                          15Km
                          20Km


              15. Use the result of Exercise 14 to infer that the bandwidth of a coaxial cable
                  decreases with the increase in distance.
              16. If the power at the beginning of a 1 KIn 2.6/9.5 mm coaxial cable is 200 mw, what
                  is the power at the end for frequencies 1 KHz, 10KHz, and 100 KHz? Use the
                  result of Exercise 14.
              17. Calculate the bandwidth of the light for the following wavelength ranges (assume a
                  propagation speed of 2 x 108 m):
                  a. 1000 to 1200 nm
                  b. 1000 to 1400 nm

## SECTION 7.6   PRACTICE SET       211


18. The horizontal axes in Figure 7.6 and 7.9 represent frequencies. The horizontal
    axis in Figure 7.16 represents wavelength. Can you explain the reason? lfthe prop-
    agation speed in an optical fiber is 2 x 108 ill, can you change the units in the hori-
    zontal axis to frequency? Should the vertical-axis units be changed too? Should the
    curve be changed too?
19. Using Figure 7.16, tabulate the attenuation (in dB) of an optical fiber for the indicated
    wavelength and distances.

              Table 7.7 Attenuation for optical fiber

               Distance      dB at 800 nm       dB at 1000 nm    dB at 1200nm
               1 Km
               lOKm
               15Km
               20Km


20. A light signal is travelling through a fiber. What is the delay in the signal if the
    length of the fiber-optic cable is 10 m, 100 m, and 1 Km (assume a propagation
    speed of 2 x 108 ill)?
21. A beam oflight moves from one medium to another medium with less density. The
    critical angle is 60°. Do we have refraction or reflection for each of the following
    incident angles? Show the bending of the light ray in each case.
    a. 40°
    b. 60°
          0
    c. 80


## CHAPTER 8

      Switching


      A network is a set of connected devices. Whenever we have multiple devices, we have
      the problem of how to connect them to make one-to-one communication possible. One
      solution is to make a point-to-point connection between each pair of devices (a mesh
      topology) or between a central device and every other device (a star topology). These
      methods, however, are impractical and wasteful when applied to very large networks.
      The number and length of the links require too much infrastructure to be cost-efficient,
      and the majority of those links would be idle most of the time. Other topologies
      employing multipoint connections, such as a bus, are ruled out because the distances
      between devices and the total number of devices increase beyond the capacities of the
      media and equipment.
           A better solution is switching. A switched network consists of a series of interlinked
      nodes, called switches. Switches are devices capable of creating temporary connections
      between two or more devices linked to the switch. In a switched network, some of these
      nodes are connected to the end systems (computers or telephones, for example). Others
      are used only for routing. Figure 8.1 shows a switched network.


      Figure 8.1 Switched network


          The end systems (communicating devices) are labeled A, B, C, D, and so on, and the
      switches are labeled I, II, III, IV, and V. Each switch is connected to multiple links.

                                                                                             213

214   CHAPTER 8   SWITCHING


                  Traditionally, three methods of switching have been important: circuit switching,
             packet switching, and message switching. The first two are commonly used today. The
             third has been phased out in general communications but still has networking applications.
             We can then divide today's networks into three broad categories: circuit-switched networks,
             packet-switched networks, and message-switched. Packet-switched networks can funher
             be divided into two subcategories-virtual-circuit networks and datagram networks-
             as shown in Figure 8.2.


             Figure 8.2 Taxonomy of switched networks


                   We can say that the virtual-circuit networks have some common characteristics
              with circuit-switched and datagram networks. Thus, we first discuss circuit-switched
              networks, then datagram networks, and finally virtual-circuit networks.
                   Today the tendency in packet switching is to combine datagram networks and virtual-
              circuit networks. Networks route the first packet based on the datagram addressing idea,
              but then create a virtual-circuit network for the rest of the packets coming from the same
              source and going to the same destination. We will see some of these networks in future
              chapters.
                   In message switching, each switch stores the whole message and forwards it to the
              next switch. Although, we don't see message switching at lower layers, it is still used in
              some applications like electronic mail (e-mail). We will not discuss this topic in this book.


## 8.1     CIRCUIT-SWITCHED NETWORKS
              A circuit-switched network consists of a set of switches connected by physical links.
              A connection between two stations is a dedicated path made of one or more links. How-
              ever, each connection uses only one dedicated channel on each link. Each link is nor-
              mally divided into n channels by using FDM or TDM as discussed in Chapter 6.

                  A circuit-switched network is made of a set of switches connected by physical links,
                                     in which each link is divided into n channels.

                   Figure 8.3 shows a trivial circuit-switched network with four switches and four
              links. Each link is divided into n (n is 3 in the figure) channels by using FDM or TDM.

## SECTION 8.1        CIRCUIT-SWITCHED NETWORKS           215


Figure 8.3 A trivial circuit-switched network


                                     One link, II channels


                                             Path


We have explicitly shown the multiplexing symbols to emphasize the division of the
link into channels even though multiplexing can be implicitly included in the switch
fabric.
     The end systems, such as computers or telephones, are directly connected to a
switch. We have shown only two end systems for simplicity. When end system A needs
to communicate with end system M, system A needs to request a connection to M that
must be accepted by all switches as well as by M itself. This is called the setup phase;
a circuit (channel) is reserved on each link, and the combination of circuits or channels
defines the dedicated path. After the dedicated path made of connected circuits (channels)
is established, data transfer can take place. After all data have been transferred, the
circuits are tom down.
     We need to emphasize several points here:
D   Circuit switching takes place at the physical layer.
D   Before starting communication, the stations must make a reservation for the resources
    to be used during the communication. These resources, such as channels (bandwidth
    in FDM and time slots in TDM), switch buffers, switch processing time, and switch
    input/output ports, must remain dedicated during the entire duration of data transfer
    until the teardown phase.
D   Data transferred between the two stations are not packetized (physical layer transfer
    of the signal). The data are a continuous flow sent by the source station and received
    by the destination station, although there may be periods of silence.
D   There is no addressing involved during data transfer. The switches route the data
    based on their occupied band (FDM) or time slot (TDM). Of course, there is end-to-
    end addressing used during the setup phase, as we will see shortly.


      In circuit switching, the resources need to be reserved during the setup phase;
                   the resources remain dedicated for the entire duration
                          of data transfer until the teardown phase.

216   CHAPTER 8   SWITCHING


             Example 8.1
             As a trivial example, let us use a circuit-switched network to connect eight telephones in a small
             area. Communication is through 4-kHz voice channels. We assume that each link uses FDM to
             connect a maximum of two voice channels. The bandwidth of each link is then 8 kHz. Figure 8.4
             shows the situation. Telephone 1 is connected to telephone 7; 2 to 5; 3 to 8; and 4 to 6. Of course
             the situation may change when new connections are made. The switch controls the connections.


             Figure 8.4 Circuit-switched network used in Example 8.1

                                   Circuit-switched network


             Example 8.2
             As another example, consider a circuit-switched network that connects computers in two remote
             offices of a private company. The offices are connected using a T-l line leased from a communi-
             cation service provider. There are two 4 X 8 (4 inputs and 8 outputs) switches in this network. For
             each switch, four output ports are folded into the input ports to allow communication between
             computers in the same office. Four other output ports allow communication between the two
             offices. Figure 8.5 shows the situation.


             Figure 8.5    Circuit-switched network used in Example 8.2

                       Circuit-switched network


                                       4x8                                        4x8
                                      swItch                  T-l line with       switch
## 1.544 Mbps

## SECTION 8.1      CIRCUIT-SWITCHED NEIWORKS               217


Three Phases
The actual communication in a circuit-switched network requires three phases: connec-
tion setup, data transfer, and connection teardown.

Setup Phase
Before the two parties (or multiple parties in a conference call) can communicate, a
dedicated circuit (combination of channels in links) needs to be established. The end sys-
tems are normally connected through dedicated lines to the switches, so connection setup
means creating dedicated channels between the switches. For example, in Figure 8.3,
when system A needs to connect to system M, it sends a setup request that includes the
address of system M, to switch I. Switch I finds a channel between itself and switch IV
that can be dedicated for this purpose. Switch I then sends the request to switch IV,
which finds a dedicated channel between itself and switch III. Switch III informs sys-
tem M of system A's intention at this time.
     In the next step to making a connection, an acknowledgment from system M needs
to be sent in the opposite direction to system A. Only after system A receives this
acknowledgment is the connection established.
     Note that end-to-end addressing is required for creating a connection between the
two end systems. These can be, for example, the addresses of the computers assigned
by the administrator in a TDM network, or telephone numbers in an FDM network.

Data Transfer Phase
After the establishment of the dedicated circuit (channels), the two parties can transfer data.

Teardown Phase
When one of the parties needs to disconnect, a signal is sent to each switch to release
the resources.

Efficiency
It can be argued that circuit-switched networks are not as efficient as the other two
types of networks because resources are allocated during the entire duration of the con-
nection. These resources are unavailable to other connections. In a telephone network,
people normally terminate the communication when they have finished their conversation.
However, in computer networks, a computer can be connected to another computer
even if there is no activity for a long time. In this case, allowing resources to be dedicated
means that other connections are deprived.

Delay
Although a circuit-switched network normally has low efficiency, the delay in this type
of network is minimal. During data transfer the data are not delayed at each switch; the
resources are allocated for the duration of the connection. Figure 8.6 shows the idea of
delay in a circuit-switched network when only two switches are involved.
     As Figure 8.6 shows, there is no waiting time at each switch. The total delay is due
to the time needed to create the connection, transfer data, and disconnect the circuit. The

218   CHAPTER 8   SWITCHING


             Figure 8.6 Delay in a circuit-switched network

                                   1I-------1.}\. f - - - - - - l


                                                         Data transfer


                            i[------------------
                            u


                            Q
                                Time              Time                   Time                Time


             delay caused by the setup is the sum of four parts: the propagation time of the source
             computer request (slope of the first gray box), the request signal transfer time (height of
             the first gray box), the propagation time of the acknowledgment from the destination
             computer (slope of the second gray box), and the signal transfer time of the acknowledg-
             ment (height of the second gray box). The delay due to data transfer is the sum of two
             parts: the propagation time (slope of the colored box) and data transfer time (height of
             the colored box), which can be very long. The third box shows the time needed to tear
             down the circuit. We have shown the case in which the receiver requests disconnection,
             which creates the maximum delay.

              Circuit-Switched Technology in Telephone Networks
             As we will see in Chapter 9, the telephone companies have previously chosen the circuit-
             switched approach to switching in the physical layer; today the tendency is moving
             toward other switching techniques. For example, the telephone number is used as the
             global address, and a signaling system (called SS7) is used for the setup and teardown
             phases.

                              Switching at the physical layer in the traditional telephone
                                    network uses the circuit-switching approach.


## 8.2    DATAGRAM NETWORKS
             In data communications, we need to send messages from one end system to another. If
             the message is going to pass through a packet-switched network, it needs to be divided
             into packets of fixed or variable size. The size of the packet is determined by the net-
             work and the governing protocol.
                  In packet switching, there is no resource allocation for a packet. This means that
             there is no reserved bandwidth on the links, and there is no scheduled processing time

## SECTION 8.2    DATAGRAM NETWORKS             219


for each packet. Resources are allocated on demand. The allocation is done on a first-
come, first-served basis. When a switch receives a packet, no matter what is the source
or destination, the packet must wait if there are other packets being processed. As with
other systems in our daily life, this lack of reservation may create delay. For example, if
we do not have a reservation at a restaurant, we might have to wait.

              In a packet-switched network, there is no resource reservation;
                            resources are allocated on demand.


     In a datagram network, each packet is treated independently of all others. Even if
a packet is part of a multipacket transmission, the network treats it as though it existed
alone. Packets in this approach are referred to as datagrams.
     Datagram switching is normally done at the network layer. We briefly discuss
datagram networks here as a comparison with circuit-switched and virtual-circuit-
switched networks. In Part 4 of this text, we go into greater detail.
     Figure 8.7 shows how the datagram approach is used to deliver four packets from
station A to station X. The switches in a datagram network are traditionally referred to
as routers. That is why we use a different symbol for the switches in the figure.


Figure 8.7 A datagram network with four switches (routers)

                        Datagram network
    A


     In this example, all four packets (or datagrams) belong to the same message, but
may travel different paths to reach their destination. This is so because the links may be
involved in carrying packets from other sources and do not have the necessary bandwidth
available to carry all the packets from A to X. This approach can cause the datagrams of
a transmission to arrive at their destination out of order with different delays between the
packets. Packets may also be lost or dropped because of a lack of resources. In most
protocols, it is the responsibility of an upper-layer protocol to reorder the datagrams or
ask for lost datagrams before passing them on to the application.
     The datagram networks are sometimes referred to as connectionless networks. The
term connectionless here means that the switch (packet switch) does not keep information
about the connection state. There are no setup or teardown phases. Each packet is treated
the same by a switch regardless of its source or destination.

220   CHAPTER 8     SWITCHING


             Routing Table
             If there are no setup or teardown phases, how are the packets routed to their destinations
             in a datagram network? In this type of network, each switch (or packet switch) has a rout-
             ing table which is based on the destination address. The routing tables are dynamic and
             are updated periodically. The destination addresses and the corresponding forwarding
             output ports are recorded in the tables. This is different from the table of a circuit-
             switched network in which each entry is created when the setup phase is completed and
             deleted when the teardown phase is over. Figure 8.8 shows the routing table for a
             switch.


             Figure 8.8 Routing table in a datagram network

                                                       Destination                Output
                                                        address                    port
                                                           1232                     I
                                                           4150                     2
                                                            .                       .
                                                           9130                     3
                                                             -......;..,: 7


                                                      -1
                                                            --
                                                            21                3
                                                                                        -4


                  A switch in a datagram network uses a routing table that is based on the destination address.


             Destination Address
             Every packet in a datagram network carries a header that contains, among other infor-
             mation, the destination address of the packet. When the switch receives the packet, this
             destination address is examined; the routing table is consulted to find the corresponding
             port through which the packet should be forwarded. This address, unlike the address
             in a virtual-circuit-switched network, remains the same during the entire journey of the
             packet.

                         The destination address in the header of a packet in a datagram network
                                remains the same during the entire journey of the packet.


              Efficiency
              The efficiency of a datagram network is better than that of a circuit-switched network;
              resources are allocated only when there are packets to be transferred. If a source sends
              a packet and there is a delay of a few minutes before another packet can be sent, the
              resources can be reallocated during these minutes for other packets from other sources.

## SECTION 8.3    VIRTUAL-CIRCUIT NETWORKS        221


Delay
There may be greater delay in a datagram network than in a virtual-circuit network.
Although there are no setup and teardown phases, each packet may experience a wait at a
switch before it is forwarded. In addition, since not all packets in a message necessarily
travel through the same switches, the delay is not uniform for the packets of a message.
Figure 8.9 gives an example of delay in a datagram network for one single packet.


Figure 8.9 Delay in a datagram network

                      Am---------tl~I_----_~_----_____1
                                                      B
      Transmis~ion[
             lime      r----=:--,-,---J
                                  Waiting [
                                     time     ,------1
                                                      Wai~ing[
                                                        time
                                                                 i------J


                    Time                    Time               Time             Time


     The packet travels through two switches. There are three transmission times (3T),
three propagation delays (slopes 3't of the lines), and two waiting times (WI + w2)' We
ignore the processing time in each switch. The total delay is

                                  Total delay = 3T + 3t + WI + W2


Datagram Networks in the Internet
As we will see in future chapters, the Internet has chosen the datagram approach to
switching at the network layer. It uses the universal addresses defined in the network
layer to route packets from the source to the destination.


                      Switching in the Internet is done by using the datagram
                        approach to packet switching at the network layer.


## 8.3     VIRTUAL-CIRCUIT NETWORKS
A virtual-circuit network is a cross between a circuit-switched network and a datagram
network. It has some characteristics of both.
  1. As in a circuit-switched network, there are setup and teardown phases in addition
     to the data transfer phase.

222   CHAPTER 8     SWITCHING


                  2. Resources can be allocated during the setup phase, as in a circuit-switched network,
                     or on demand, as in a datagram network.
                  3. As in a datagram network, data are packetized and each packet carries an address in
                     the header. However, the address in the header has local jurisdiction (it defines what
                     should be the next switch and the channel on which the packet is being canied), not
                     end-to-end jurisdiction. The reader may ask how the intermediate switches know
                     where to send the packet if there is no final destination address carried by a packet.
                     The answer will be clear when we discuss virtual-circuit identifiers in the next section.
                  4. As in a circuit-switched network, all packets follow the same path established during
                     the connection.
                  5. A virtual-circuit network is normally implemented in the data link layer, while a
                     circuit-switched network is implemented in the physical layer and a datagram net-
                     work in the network layer. But this may change in the future.
             Figure 8.10 is an example of a virtual-circuit network. The network has switches that
             allow traffic from sources to destinations. A source or destination can be a computer,
             packet switch, bridge, or any other device that connects other networks.


             Figure 8.10        Virtual-circuit network


             Addressing
             In a virtual-circuit network, two types of addressing are involved: global and local
             (virtual-circuit identifier).

              Global Addressing
             A source or a destination needs to have a global address-an address that can be unique
             in the scope of the network or internationally if the network is part of an international
             network. However, we will see that a global address in virtual-circuit networks is used
             only to create a virtual-circuit identifier, as discussed next.

              Virtual-Circuit Identifier
             The identifier that is actually used for data transfer is called the virtual-circuit identifier
             (Vel). A vel, unlike a global address, is a small number that has only switch scope; it

## SECTION 8.3   VIRTUAL-CIRCUIT NETWORKS            223


is used by a frame between two switches. When a frame arrives at a switch, it has a
VCI; when it leaves, it has a different VCl. Figure 8.11 shows how the VCI in a data
frame changes from one switch to another. Note that a VCI does not need to be a large
number since each switch can use its own unique set of VCls.


Figure 8.11    Virtual-circuit identifier


                                VCI           I               VCI

                      I Data tEJ ~                   I Data I~ ~
                   -----===::::=------~..I'..~ =====----


Three Phases
As in a circuit-switched network, a source and destination need to go through three
phases in a virtual-circuit network: setup, data transfer, and teardown. In the setup
phase, the source and destination use their global addresses to help switches make table
entries for the connection. In the teardown phase, the source and destination inform the
switches to delete the corresponding entry. Data transfer occurs between these two
phases. We first discuss the data transfer phase, which is more straightforward; we then
talk about the setup and teardown phases.

Data Transfer Phase
To transfer a frame from a source to its destination, all switches need to have a table
entry for this virtual circuit. The table, in its simplest form, has four columns. This
means that the switch holds four pieces of information for each virtual circuit that is
already set up. We show later how the switches make their table entries, but for the
moment we assume that each switch has a table with entries for all active virtual cir-
cuits. Figure 8.12 shows such a switch and its corresponding table.
     Figure 8.12 shows a frame arriving at port 1 with a VCI of 14. When the frame
arrives, the switch looks in its table to find port 1 and a VCI of 14. When it is found, the
switch knows to change the VCI to 22 and send out the frame from port 3.
     Figure 8.13 shows how a frame from source A reaches destination B and how its
VCI changes during the trip. Each switch changes the VCI and routes the frame.
     The data transfer phase is active until the source sends all its frames to the destina-
tion. The procedure at the switch is the same for each frame of a message. The process
creates a virtual circuit, not a real circuit, between the source and destination.

Setup Phase
In the setup phase, a switch creates an entry for a virtual circuit. For example, suppose
source A needs to create a virtual circuit to B. Two steps are required: the setup request
and the acknowledgment.

224   CHAPTER 8    SWITCHING


             Figure 8.12      Switch and tables in a virtual-circuit network


                                                              Incoming        Outgoing
                                                              Port
                                                               1
                                                               1
                                                                     VCl
                                                                      14
                                                                     77
                                                                               3
                                                                              Port

                                                                               2
                                                                                     VCl
                                                                                      22
                                                                                      41

                                                                     ~'~


                              I   Data    ~I     Data   [EJ-+                        I Data @]-+
                                                                     lA3
                                                                         2


                                                                             ~t
              Figure 8.13     Source-to-destination data transfer in a virtual-circuit network


                                         Incoming Outgoing                   Incoming Outgoing
                                         Port VCl Port VCl                   Port VCl Port VCI
                                          I    14  3    66                    2    22  3    77


                                                         Incoming Outgoing
                                                         Port VCI Port VCl
                                                          1    66  2    22


              Setup Request A setup request frame is sent from the source to the destination.
              Figure 8.14 shows the process.
                  a. Source A sends a setup frame to switch 1.
                  b. Switch 1 receives the setup request frame. It knows that a frame going from A to B
                     goes out through port 3. How the switch has obtained this information is a point
                     covered in future chapters. The switch, in the setup phase, acts as a packet switch;
                     it has a routing table which is different from the switching table. For the moment,
                     assume that it knows the output port. The switch creates an entry in its table for

## SECTION 8.3      VIRTUAL-CIRCUIT NETWORKS            225


Figure 8.14   Setup request in a virtual-circuit network


                  Incoming Outgoing                           Incoming Outgoing
                  Port IvcI Port IVCI                         Port IVCI Port IVCI
                   1 I 14    3 I                               2 122     3 I
                                                                                    VCI=77


                                        Incoming Outgoing
                                        Port IVCI Port IVCI
                                         I I 66    2 I


    this virtual circuit, but it is only able to fill three of the four columns. The switch
    assigns the incoming port (1) and chooses an available incoming VCI (14) and the
    outgoing port (3). It does not yet know the outgoing VCI, which will be found dur-
    ing the acknowledgment step. The switch then forwards the frame through port 3
    to switch 2.
 c. Switch 2 receives the setup request frame. The same events happen here as at
    switch 1; three columns of the table are completed: in this case, incoming port (l),
    incoming VCI (66), and outgoing port (2).
 d. Switch 3 receives the setup request frame. Again, three columns are completed:
    incoming port (2), incoming VCI (22), and outgoing port (3).
 e. Destination B receives the setup frame, and if it is ready to receive frames from A,
    it assigns a VCI to the incoming frames that come from A, in this case 77. This
    VCI lets the destination know that the frames come from A, and not other sources.
Acknowledgment A special frame, called the acknowledgment frame, completes
the entries in the switching tables. Figure 8.15 shows the process.
 a. The destination sends an acknowledgment to switch 3. The acknowledgment carries
    the global source and destination addresses so the switch knows which entry in the
    table is to be completed. The frame also carries VCI 77, chosen by the destination as
    the incoming VCI for frames from A. Switch 3 uses this VCI to complete the outgoing
    VCI column for this entry. Note that 77 is the incoming VCI for destination B, but
    the outgoing VCI for switch 3.
 b. Switch 3 sends an acknowledgment to switch 2 that contains its incoming VCI in the
    table, chosen in the previous step. Switch 2 uses this as the outgoing VCI in the table.
 c. Switch 2 sends an acknowledgment to switch 1 that contains its incoming VCI in the
    table, chosen in the previous step. Switch 1 uses this as the outgoing VCI in the table.
 d. Finally switch 1 sends an acknowledgment to source A that contains its incoming
    VCI in the table, chosen in the previous step.
 e. The source uses this as the outgoing VCI for the data frames to be sent to destination B.

226   CHAPTER 8   SWITCHING


              Figure 8.15        Setup acknowledgment in a virtual-circuit network


                                      Incoming Outgoing                           Incoming Outgoing
                                      Port IVCI Port IVCI                         Port IVCI Port IVCI
                                       I I 14    3 166                             2 122     3 I 77
                     VCI == 14                                                                          VCI == 77
                        A 1--==--;                                                                         B
                                 ~
                       o            @


                                                            Incoming Outgoing
                                                            Port IVCI Port IVCI
                                                             I I 66    2 122


              Teardowil Phase
              In this phase, source A, after sending all frames to B, sends a special frame called a
              teardown request. Destination B responds with a teardown confirmation frame. All
              switches delete the corresponding entry from their tables.

              Efficiency
              As we said before, resource reservation in a virtual-circuit network can be made during
              the setup or can be on demand during the data transfer phase. In the first case, the delay
              for each packet is the same; in the second case, each packet may encounter different
              delays. There is one big advantage in a virtual-circuit network even if resource allocation
              is on demand. The source can check the availability of the resources, without actually
              reserving it. Consider a family that wants to dine at a restaurant. Although the restaurant
              may not accept reservations (allocation of the tables is on demand), the family can call
              and find out the waiting time. This can save the family time and effort.


                  In virtual-circuit switching, all packets belonging to the same source and destination
                           travel the same path; but the packets may arrive at the destination
                                 with different delays if resource allocation is on demand.


              Delay in Virtual-Circuit Networks
              In a virtual-circuit network, there is a one-time delay for setup and a one-time delay for
              teardown. If resources are allocated during the setup phase, there is no wait time for
              individual packets. Figure 8.16 shows the delay for a packet traveling through two
              switches in a virtual-circuit network.
                   The packet is traveling through two switches (routers). There are three transmis-
              sion times (3T), three propagation times (3't), data transfer depicted by the sloping
              lines, a setup delay (which includes transmission and propagation in two directions),

## SECTION 8.4              STRUCTURE OF A SWITCH   227


Figure 8.16 Delay in a virtual-circuit network


                                                            I ~I


                                           1;'ransmission
                                         ] tIme


               ~" [--~---------------
               ~          ,

               ~
                   Time                Time                        Time           Time


and a teardown delay (which includes transmission and propagation in one direction).
We ignore the processing time in each switch. The total delay time is

                      Total delay = 3T + 3't + setup delay + teardown delay


Circuit-Switched Technology in WANs
As we will see in Chapter 18, virtual-circuit networks are used in switched WANs such
as Frame Relay and ATM networks. The data link layer of these technologies is well
suited to the virtual-circuit technology.

              Switching at the data link layer in a switched WAN is normally
                    implemented by using virtual-circuit techniques.


## 8.4     STRUCTURE OF A SWITCH
We use switches in circuit-switched and packet-switched networks. In this section, we
discuss the structures of the switches used in each type of network.

Structure of Circuit Switches
Circuit switching today can use either of two technologies: the space-division switch or
the time-division switch.

Space-Division Switch
In space-division switching, the paths in the circuit are separated from one another
spatially. This technology was originally designed for use in analog networks but is
used currently in both analog and digital networks. It has evolved through a long history
of many designs.

228   CHAPTER 8   SWITCHING


             Crossbar Switch A crossbar switch connects n inputs to m outputs in a grid, using
             electronic microswitches (transistors) at each crosspoint (see Figure 8.17). The major
             limitation of this design is the number of crosspoints required. To connect n inputs to
             m outputs using a crossbar switch requires n x m crosspoints. For example, to connect
             1000 inputs to 1000 outputs requires a switch with 1,000,000 crosspoints. A crossbar
             with this number of crosspoints is impractical. Such a switch is also inefficient because
             statistics show that, in practice, fewer than 25 percent of the crosspoints are in use at
             any given time. The rest are idle.


             Figure 8.17   Crossbar switch with three inputs and four outputs


                              2


                              30-+-·.....--4.---.--.
                                               II   III   IV


             Multistage Switch The solution to the limitations of the crossbar switch is the
             multistage switch, which combines crossbar switches in several (normally three)
             stages, as shown in Figure 8.18. In a single crossbar switch, only one row or column
             (one path) is active for any connection. So we need N x N crosspoints. If we can allow
             multiple paths inside the switch, we can decrease the number of crosspoints. Each
             crosspoint in the middle stage can be accessed by multiple crosspoints in the first or
             third stage.


             Figure 8.18   Multistage switch


                                      Nln                          k            Nln
                                   Crossbars                   Crossbars   Crossbars

                     n[                                                                   In
                  N n[                                                                    In N

                     n[                                                                   In
                                     Stage 1                    Stage 2     Stage 3

## SECTION 8.4     STRUCTURE OF A SWITCH              229


    To design a three-stage switch, we follow these steps:
 1. We divide the N input lines into groups, each of n lines. For each group, we use
    one crossbar of size n x k, where k is the number of crossbars in the middle stage.
    In other words, the first stage has N/n crossbars of n x k crosspoints.
 2. We use k crossbars, each of size (N/n) x (N/n) in the middle stage.
 3. We use N/n crossbars, each of size k x n at the third stage.
We can calculate the total number of crosspoints as follows:


                      N
                      -en
                      n
                          x k) + k (N
                                    - x N)
                                    n
                                        - + -N(k x n) = 2kN + k (N)2
                                        n    n
                                                                 -
                                                                 n


                  In a three-stage switch, the total number of crosspoints is

                                        2kN +k(~Y
    which is much smaller than the number of crosspoints in a single-stage switch (N2 ).


Example 8.3
Design a three-stage, 200 x 200 switch (N = 200) with k = 4 and n = 20.

Solution
In the first stage we have N/n or 10 crossbars, each of size 20 x 4. In the second stage, we have
4 crossbars, each of size 10 x 10. In the third stage, we have 10 crossbars, each of size 4 x 20.
The total number of crosspoints is 2kN + k(N/n)2, or 2000 crosspoints. This is 5 percent of the
number of crosspoints in a single-stage switch (200 x 200 = 40,000).

     The multistage switch in Example 8.3 has one drawback-blocking during periods
of heavy traffic: The whole idea of multistage switching is to share the crosspoints in
the middle-stage crossbars. Sharing can cause a lack of availability if the resources are
limited and all users want a connection at the same time. Blocking refers to times when
one input cannot be connected to an output because there is no path available between
them-all the possible intermediate switches are occupied.
     In a single-stage switch, blocking does not occur because every combination of
input and output has its own crosspoint; there is always a path. (Cases in which two
inputs are trying to contact the same output do not count. That path is not blocked; the
output is merely busy.) In the multistage switch described in Example 8.3, however,
only 4 of the first 20 inputs can use the switch at a time, only 4 of the second 20 inputs
can use the switch at a time, and so on. The small number of crossbars at the middle
stage creates blocking.
     In large systems, such as those having 10,000 inputs and outputs, the number of
stages can be increased to cut down on the number of crosspoints required. As the num-
ber of stages increases, however, possible blocking increases as well. Many people have
experienced blocking on public telephone systems in the wake of a natural disaster
when the calls being made to check on or reassure relatives far outnumber the regular
load of the system.

230   CHAPTER 8     SWITCHING


                  Clos investigated the condition of nonblocking in multistage switches and came up
             with the following formula. In a nonblocking switch, the number of middle-stage
             switches must be at least 2n - 1. In other words, we need to have k 2 2n - 1.
                  Note that the number of crosspoints is still smaller than that in a single-stage
             switch. Now we need to minimize the number of crosspoints with a fixed N by using
             the Clos criteria. We can take the derivative of the equation with respect to n (the only
             variable) and find the value of n that makes the result zero. This n must be equal to or
             greater than (N/2)1/2. In this case, the total number of crosspoints is greater than or equal
             to 4N [(2N) 112 -1]. In other words, the minimum number of crosspoints according to the
             Clos criteria is proportional to N 3/2.

                  According to Clos criterion:
                  n =(NI2)1/2
                  k>2n-1
                  Total number of crosspoints 2 4N [(2N)1/2 -1]


             Example 8.4
             Redesign the previous three-stage, 200 x 200 switch, using the Clos criteria with a minimum
             number of crosspoints.

             Solution
             We let n = (200/2) 1/2, or n = 10. We calculate k = 2n - 1 = 19. In the first stage, we have 200/10,
             or 20, crossbars, each with lOX 19 crosspoints. In the second stage, we have 19 crossbars,
             each with 10 X 10 crosspoints. In the third stage, we have 20 crossbars each with 19 X 10
             crosspoints. The total number of crosspoints is 20(10 X 19) + 19(10 X 10) + 20(19 XlO) =
             9500. If we use a single-stage switch, we need 200 X 200 = 40,000 crosspoints. The number
             of crosspoints in this three-stage switch is 24 percent that of a single-stage switch. More
             points are needed than in Example 8.3 (5 percent). The extra crosspoints are needed to prevent
             blocking.

                   A multistage switch that uses the Clos criteria and a minimum number of crosspoints
             still requires a huge number of crosspoints. For example, to have a 100,000 input/output
             switch, we need something close to 200 million crosspoints (instead of 10 billion). This
             means that if a telephone company needs to provide a switch to connect 100,000 tele-
             phones in a city, it needs 200 million crosspoints. The number can be reduced if we
             accept blocking. Today, telephone companies use time-division switching or a combina-
             tion of space- and time-division switches, as we will see shortly.

              Time-Division Switch
             Time-division switching uses time-division multiplexing (TDM) inside a switch. The
             most popular technology is called the time-slot interchange (TSI).
             Time-Slot Interchange Figure 8.19 shows a system connecting four input lines to
             four output lines. Imagine that each input line wants to send data to an output line
             according to the following pattern:

## SECTION 8.4      STRUCTURE OF A SWITCH          231


Figure 8.19    Time-slot interchange

           Time-division switch

                                  TSI   ,C{Jnt!ol unit
                                            1~3
                                           2~4
                                           3~1
                                           4~2


     The figure combines a TDM multiplexer, a TDM demultiplexer, and a TSI consist-
ing of random access memory (RAM) with several memory locations. The size of each
location is the same as the size of a single time slot. The number oflocations is the same
as the number of inputs (in most cases, the numbers of inputs and outputs are equal).
The RAM fills up with incoming data from time slots in the order received. Slots are
then sent out in an order based on the decisions of a control unit.


Time- and Space-Division Switch Combinations
When we compare space-division and time-division switching, some interesting facts
emerge. The advantage of space-division switching is that it is instantaneous. Its disadvan-
tage is the number of crosspoints required to make space-division switching acceptable in
terms of blocking.
     The advantage of time-division switching is that it needs no crosspoints. Its disad-
vantage, in the case of TSI, is that processing each connection creates delays. Each time
slot must be stored by the RAM, then retrieved and passed on.
     In a third option, we combine space-division and time-division technologies to
take advantage of the best of both. Combining the two results in switches that are
optimized both physically (the number of crosspoints) and temporally (the amount
of delay). Multistage switches of this sort can be designed as time-space-time (TST)
switch.
     Figure 8.20 shows a simple TST switch that consists of two time stages and one
space stage and has 12 inputs and 12 outputs. Instead of one time-division switch, it
divides the inputs into three groups (of four inputs each) and directs them to three time-
slot interchanges. The result is that the average delay is one-third of what would result
from using one time-slot interchange to handle all 12 inputs.
     The last stage is a mirror image of the first stage. The middle stage is a space-
division switch (crossbar) that connects the TSI groups to allow connectivity between
all possible input and output pairs (e.g., to connect input 3 of the first group to output 7
of the second group).

232   CHAPTER 8   SWITCHING


             Figure 8.20    Time-space-time switch


                                                            TST


                                                            Space


              Structure of Packet Switches
             A switch used in a packet-switched network has a different structure from a switch used
             in a circuit-switched network.We can say that a packet switch has four components:
             input ports, output ports, the routing processor, and the switching fabric, as shown
             in Figure 8.21.


              Figure 8.21   Packet switch components

                             --------------------------------------1

                                                 Routing
                                                processor
                                Input ports                                 Output ports


                                                     Switching fabric


                             1'--_ _----'
                             IL                                                            _


              Input Ports
              An input port performs the physical and data link functions of the packet switch. The
              bits are constructed from the received signal. The packet is decapsulated from the frame.
              Errors are detected and corrected. The packet is now ready to be routed by the network
              layer. In addition to a physical layer processor and a data link processor, the input port
              has buffers (queues) to hold the packet before it is directed to the switching fabric.
              Figure 8.22 shows a schematic diagram of an input port.

## SECTION 8.4         STRUCTURE OF A SWITCH    233


Figure 8.22   Input port

                 Input port


                        Physical layer     Data link layer
                          processor          processor


Output Port
The output port performs the same functions as the input port, but in the reverse order.
First the outgoing packets are queued, then the packet is encapsulated in a frame, and
finally the physical layer functions are applied to the frame to create the signal to be
sent on the line. Figure 8.23 shows a schematic diagram of an output port.


Figure 8.23    Output port

                 Output port


                                         Data link layer       Physical layer
                                           processor             processor


ROllting Processor
The routing processor performs the functions of the network layer. The destination
address is used to find the address of the next hop and, at the same time, the output port
number from which the packet is sent out. This activity is sometimes referred to as
table lookup because the routing processor searches the routing table. In the newer
packet switches, this function of the routing processor is being moved to the input ports
to facilitate and expedite the process.

Switching "Fabrics
The most difficult task in a packet switch is to move the packet from the input queue to
the output queue. The speed with which this is done affects the size of the input/output
queue and the overall delay in packet delivery. In the past, when a packet switch was
actually a dedicated computer, the memory of the computer or a bus was used as the
switching fabric. The input port stored the packet in memory; the output port retrieved
the packet from memory. Today, packet switches are specialized mechanisms that use a
variety of switching fabrics. We briefly discuss some of these fabrics here.

Crossbar Switch The simplest type of switching fabric is the crossbar switch, dis-
cussed in the previous section.

Banyan Switch A more realistic approach than the crossbar switch is the banyan
switch (named after the banyan tree). A banyan switch is a multistage switch with

234   CHAPTER 8     SWITCHING


             microswitches at each stage that route the packets based on the output port represented as
             a binary string. For n inputs and n outputs, we have log2 n stages with nl2 microswitches
             at each stage. The first stage routes the packet based on the high-order bit of the binary
             string. The second stage routes the packet based on the second high-order bit, and so on.
             Figure 8.24 shows a banyan switch with eight inputs and eight outputs. The number of
             stages is Iog2(8) = 3.


             Figure 8.24 A banyan switch

                                                          Left bit       Middle bit        Right bit


                                          O~

                                          l~


                                                                                                       ~6

                                                                                                       ~7


                 Figure 8.25 shows the operation. In part a, a packet has arrived at input port 1 and
             must go to output port 6 (110 in binary). The first microswitch (A-2) routes the packet
             based on the first bit (1), the second microswitch (B-4) routes the packet based on the
             second bit (1), and the third microswitch (C-4) routes the packet based on the third bit (0).
             In part b, a packet has arrived at input port 5 and must go to output port 2 (010 in
             binary). The first microswitch (A-2) routes the packet based on the first bit (0), the sec-
             ond microswitch (B-2) routes the packet based on the second bit (l), and the third
             microswitch (C-2) routes the packet based on the third bit (0).


              Figure 8.25           Examples of routing in a banyan switch


                     0                                               0         0                                         0
                      1                                              1         1                                         I

                     2                                               2         2                                         2
                     3                                               3         3                                         3

                     4                                               4         4                                         4
                     5                                               5         5                                         5

                     6                                               6         6                                         6
                     7                                               7         7                                         7


                  a. Input 1 sending a cell to output 6 (110)              b. Input 5 sending a cell to output 2 (010)

## SECTION 8.6     KEY TERMS    235


Figure 8.26   Batcher-banyan switch

                                      Banyan switch

      O~

      l~


                                                                            ~2

              Batcher                                                       ~3
                            Trap
              switch       module
                                                             ~--+ro ~"'lr-r ~ 4
                                                                            ~5


      6~                                                                    ~6
      7~                                                                    ~7


Batcher-Banyan Switch The problem with the banyan switch is the possibility of
internal collision even when two packets are not heading for the same output port. We
can solve this problem by sorting the arriving packets based on their destination port.
     K. E. Batcher designed a switch that comes before the banyan switch and sorts the
incoming packets according to their final destinations. The combination is called the
Batcher-banyan switch. The sorting switch uses hardware merging techniques, but we
do not discuss the details here. Normally, another hardware module called a trap is
added between the Batcher switch and the banyan switch (see Figure 8.26) The trap
## module prevents duplicate packets (packets with the same output destination) from
passing to the banyan switch simultaneously. Only one packet for each destination is
allowed at each tick; if there is more than one, they wait for the next tick.


## 8.5     RECOMMENDED READING
For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [...] refer to the reference list at the end of the text.

Books
Switching is discussed in Chapter 10 of [Sta04] and Chapters 4 and 7 of [GW04]. Circuit-
switching is fully discussed in [BELOO].


## 8.6     KEY TERMS
banyan switch                                    crosspoint
Batcher-banyan switch                            data transfer phase
blocking                                         datagram
circuit switching                                datagram network
circuit-switched network                         end system
crossbar switch                                  input port

236   CHAPTER 8    SWITCHING


             multistage switch                                 table lookup
             output port                                       teardown phase
             packet-switched network                           time-division switching
             routing processor                                 time-slot interchange (TSI)
             setup phase                                       time-space-time (TST)
             space-division switching                             switch
             switch                                            trap
             switching                                         virtual-circuit identifier (VCI)
             switching fabric                                  virtual-circuit network


## 8.7        SUMMARY
             o A switched network consists of a series of interlinked nodes, called switches. Tradi-
                    tionally' three methods of switching have been important: circuit switching, packet
                    switching, and message switching.
             o      We can divide today's networks into three broad categories: circuit-switched networks,
                    packet-switched networks, and message-switched. Packet-switched networks can also
                    be divided into two subcategories: virtual-circuit networks and datagram networks
             o A circuit-switched network is made of a set of switches connected by physical links,
                    in which each link is divided into n channels. Circuit switching takes place at the
                    physical layer. In circuit switching, the resources need to be reserved during the
                    setup phase; the resources remain dedicated for the entire duration of data transfer
                    phase until the teardown phase.
             o      In packet switching, there is no resource allocation for a packet. This means that
                    there is no reserved bandwidth on the links, and there is no scheduled processing
                    time for each packet. Resources are allocated on demand.
             o      In a datagram network, each packet is treated independently of all others. Packets in
                    this approach are referred to as datagrams. There are no setup or teardown phases.
             o      A virtual-circuit network is a cross between a circuit-switched network and a data-
                    gram network. It has some characteristics of both.
             o      Circuit switching uses either of two technologies: the space-division switch or the
                    time-division switch.
             o      A switch in a packet-switched network has a different structure from a switch used in
                    a circuit-switched network.We can say that a packet switch has four types of compo-
                    nents: input ports, output ports, a routing processor, and switching fabric.


## 8.8       PRACTICE SET
              Review Questions
                  I. Describe the need for switching and define a switch.
                  2. List the three traditional switching methods. What are the most common today?

## SECTION 8.8    PRACTICE SET        237


 3. What are the two approaches to packet-switching?
 4. Compare and contrast a circuit-switched network and a packet-switched network.
 5. What is the role of the address field in a packet traveling through a datagram
    network?
 6. What is the role of the address field in a packet traveling through a virtual-circuit
    network?
 7. Compare space-division and time-division switches.
 8. What is TSI and its role in a time-division switching?
 9. Define blocking in a switched network.
10. List four major components of a packet switch and their functions.


Exercises
11. A path in a digital circuit-switched network has a data rate of I Mbps. The exchange
    of 1000 bits is required for the setup and teardown phases. The distance between
    two parties is 5000 km. Answer the following questions if the propagataion speed is
    2 X 108 m:
    a. What is the total delay if 1000 bits of data are exchanged during the data transfer
       phase?
    b. What is the total delay if 100,000 bits of data are exchanged during the data
       transfer phase?
    c. What is the total delay if 1,000,000 bits of data are exchanged during the data
       transfer phase?
    d. Find the delay per 1000 bits of data for each of the above cases and compare
       them. What can you infer?
12. Five equal-size datagrams belonging to the same message leave for the destina-
    tion one after another. However, they travel through different paths as shown in
    Table 8.1.


          Table 8.1   Exercise 12

             Datagram      Path Length              Visited Switches
                 1           3200Km                      1,3,5
                 2          11,700 Km                    1,2,5
                 3          12,200 Km                   1,2,3,5
                 4          10,200 Km                    1,4,5
                 5          10,700 Km                   1,4,3,5


    We assume that the delay for each switch (including waiting and processing) is 3,
    10, 20, 7, and 20 ms respectively. Assuming that the propagation speed is 2 x 108 m,
    find the order the datagrams arrive at the destination and the delay for each. Ignore
    any other delays in transmission.

238   CHAPTER 8   SWITCHING


              13. Transmission of information in any network involves end-to-end addressing and
                  sometimes local addressing (such as YCI). Table 8.2 shows the types of networks
                  and the addressing mechanism used in each of them.


              Table 8.2 Exercise 13

                     Network                   Setup             Data Transfer           Teardown
                  Circuit-switched          End-ta-end                                  End-ta-end
                     Datagram                                     End-ta-end
                   Virtual-circuit          End-to-end               Local              End-to-end


                  Answer the following questions:
                  a. Why does a circuit-switched network need end-to-end addressing during the setup
                     and teardown phases? Why are no addresses needed during the data transfer phase
                     for this type of network?
                  b. Why does a datagram network need only end-to-end addressing during the data
                     transfer phase, but no addressing during the setup and teardown phases?
                  c. Why does a virtual-circuit network need addresses during all three phases?
              14. We mentioned that two types of networks, datagram and virtual-circuit, need a
                  routing or switching table to find the output port from which the information
                  belonging to a destination should be sent out, but a circuit-switched network has
                  no need for such a table. Give the reason for this difference.
              15. An entry in the switching table of a virtual-circuit network is normally created
                  during the setup phase and deleted during the teardown phase. In other words, the
                  entries in this type of network reflect the current connections, the activity in the
                  network. In contrast, the entries in a routing table of a datagram network do not
                  depend on the current connections; they show the configuration of the network and
                  how any packet should be routed to a final destination. The entries may remain
                  the same even if there is no activity in the network. The routing tables, however, are
                  updated if there are changes in the network. Can you explain the reason for these
                  two different characteristics? Can we say that a virtual-circuit is a connection-
                  oriented network and a datagram network is a connectionLess network because of the
                  above characteristics?
              16. The minimum number of columns in a datagram network is two; the minimum num-
                  ber of columns in a virtual-circuit network is four. Can you explain the reason? Is the
                  difference related to the type of addresses carried in the packets of each network?
              17. Figure 8.27 shows a switch (router) in a datagram network.
                  Find the output port for packets with the following destination addresses:
                  Packet 1: 7176
                  Packet 2: 1233
                  Packet 3: 8766
                  Packet 4: 9144
              18. Figure 8.28 shows a switch in a virtual circuit network.

## SECTION 8.8       PRACTICE SET   239


Figure 8.27   Exercise 17


                           Destination    Output
                            address        port
                              1233              3
                              1456              2
                              3255              1                       4
                              4470              4
                              7176              2          2       3
                              8766              3
                              9144              2


Figure 8.28 Exercise 18

                       Incoming           Outgoing
                     Port       VCI      Port       VCI
                       1         14       3         22
                       2         71       4         41                      4
                       2         92       1         45
                       3         58       2         43
                       3         78       2         70         2
                       4         56       3         11


    Find the output port and the output VCI for packets with the following input port
    and input VCI addresses:
    Packet 1: 3, 78
    Packet 2: 2, 92
    Packet 3: 4, 56
    Packet 4: 2, 71
19. Answer the following questions:
    a. Can a routing table in a datagram network have two entries with the same destina-
        tion address? Explain.
    b. Can a switching table in a virtual-circuit network have two entries with the same
        input port number? With the same output port number? With the same incoming
        VCls? With the same outgoing VCls? With the same incoming values (port, VCI)?
        With the same outgoing values (port, VCI)?
20. It is obvious that a router or a switch needs to do searching to find information in
    the corresponding table. The searching in a routing table for a datagram network is
    based on the destination address; the searching in a switching table in a virtual-
    circuit network is based on the combination of incoming port and incoming VCI.
    Explain the reason and define how these tables must be ordered (sorted) based on
    these values.
2]. Consider an n X k crossbar switch with n inputs and k outputs.
    a. Can we say that switch acts as a multiplexer if n > k?
    b. Can we say that switch acts as a demultiplexer if n < k?

240   CHAPTER 8   SWITCHING


              22. We need a three-stage space-division switch with N = 100. We use 10 crossbars at
                  the first and third stages and 4 crossbars at the middle stage.
                  a. Draw the configuration diagram.
                  b. Calculate the total number of crosspoints.
                  c. Find the possible number of simultaneous connections.
                  d. Find the possible number of simultaneous connections if we use one single cross-
                      bar (100 x 100).
                  e. Find the blocking factor, the ratio of the number of connections in c and in d.
              23. Repeat Exercise 22 if we use 6 crossbars at the middle stage.
              24. Redesign the configuration of Exercise 22 using the Clos criteria.
              25. We need to have a space-division switch with 1000 inputs and outputs. What is the
                  total number of crosspoints in each of the following cases?
                  a. Using one single crossbar.
                  b. Using a multi-stage switch based on the Clos criteria
              26. We need a three-stage time-space-time switch with N = 100. We use 10 TSIs at the
                  first and third stages and 4 crossbars at the middle stage.
                  a. Draw the configuration diagram.
                  b. Calculate the total number of crosspoints.
                  c. Calculate the total number of memory locations we need for the TSIs.

## CHAPTER 9

       Using Telephone and Cable Networks
      for Data Transmission
      Telephone networks were originally created to provide voice communication. The need
      to communicate digital data resulted in the invention of the dial-up modem. With the
      advent of the Internet came the need for high-speed downloading and uploading; the
      modem was just too slow. The telephone companies added a new technology, the digital
      subscriber line (DSL). Although dial-up modems still exist in many places all over the
      world, DSL provides much faster access to the Internet through the telephone network.
      In this chapter, we first discuss the basic structure of the telephone network. We then see
      how dial-up modems and DSL technology use these networks to access the Internet.
           Cable networks were originally created to provide access to TV programs for those
      subscribers who had no reception because of natural obstructions such as mountains.
      Later the cable network became popular with people who just wanted a better signal. In
      addition, cable networks enabled access to remote broadcasting stations via microwave
      connections. Cable TV also found a good market in Internet access provision using
      some of the channels originally designed for video. After discussing the basic structure
      of cable networks, we discuss how cable modems can provide a high-speed connection
      to the Internet.


## 9.1     TELEPHONE NETWORK
      Telephone networks use circuit switching. The telephone network had its beginnings
      in the late 1800s. The entire network, which is referred to as the plain old telephone
      system (POTS), was originally an analog system using analog signals to transmit voice.
      With the advent of the computer era, the network, in the 1980s, began to carry data in
      addition to voice. During the last decade, the telephone network has undergone many
      technical changes. The network is now digital as well as analog.

      Major Components
      The telephone network, as shown in Figure 9.1, is made of three major components:
      local loops, trunks, and switching offices. The telephone network has several levels of
      switching offices such as end offices, tandem offices, and regional offices.

                                                                                             241

242   CHAPTER 9   USING 1ELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             Figure 9.1    A telephone system


                                                         Trunk               Trunk

                                                                  Tandem
                                                                   offices           Regional offices


             Local Loops
             One component of the telephone network is the local loop, a twisted-pair cable that con-
             nects the subscriber telephone to the nearest end office or local central office. The local
             loop, when used for voice, has a bandwidth of 4000 Hz (4 kHz). It is interesting to examine
             the telephone number associated with each local loop. The first three digits of a local tele-
             phone number define the office, and the next four digits define the local loop number.

              Trunks
             Trunks are transmission media that handle the communication between offices. A
             trunk normally handles hundreds or thousands of connections through multiplexing.
             Transmission is usually through optical fibers or satellite links.

             Switching Offices
             To avoid having a permanent physical link between any two subscribers, the telephone
             company has switches located in a switching office. A switch connects several local
             loops or trunks and allows a connection between different subscribers.

              LATAs
             After the divestiture of 1984 (see Appendix E), the United States was divided into more
             than 200 local-access transport areas (LATAs). The number of LATAs has increased
             since then. A LATA can be a small or large metropolitan area. A small state may have one
             single LATA; a large state may have several LATAs. A LATA boundary may overlap the
             boundary of a state; part of a LATA can be in one state, part in another state.

             Intra-LATA Services
             The services offered by the common carriers (telephone companies) inside a LATA are
             called intra-LATA services. The carrier that handles these services is called a local
             exchange carrier (LEC). Before the Telecommunications Act of 1996 (see Appendix E),
             intra-LATA services were granted to one single carrier. This was a monopoly. After 1996,
             more than one carrier could provide services inside a LATA. The carrier that provided ser-
             vices before 1996 owns the cabling system (local loops) and is called the incumbent local
             exchange carrier (ILEC). The new carriers that can provide services are called
             competitive local exchange carriers (CLECs). To avoid the costs of new cabling, it

## SECTION 9.1    TELEPHONE NETWORK            243


was agreed that the ILECs would continue to provide the main services, and the CLECs
would provide other services such as mobile telephone service, toll calls inside a LATA,
and so on. Figure 9.2 shows a LATA and switching offices.

   Intra-LATA services are provided by local exchange carriers. Since 1996, there are two
 types ofLECs: incumbent local exchange carriers and competitive local exchange carriers.


Figure 9.2   Switching offices in a LATA


                                                  Tandem (toll) offices


     Communication inside a LATA is handled by end switches and tandem switches. A
call that can be completed by using only end offices is considered toll-free. A call that
has to go through a tandem office (intra-LATA toll office) is charged.

Inter-LATA Services
The services between LATAs are handled by interexchange carriers (IXCs). These
carriers, sometimes called long-distance companies, provide communication services
between two customers in different LATAs. After the act of 1996 (see Appendix E),
these services can be provided by any carrier, including those involved in intra-LATA
services. The field is wide open. Carriers providing inter-LATA services include AT&T,
MCI, WorldCom, Sprint, and Verizon.
     The IXCs are long-distance carriers that provide general data communications ser-
vices including telephone service. A telephone call going through an IXC is normally
digitized, with the carriers using several types of networks to provide service.

Points of Presence
As we discussed, intra-LATA services can be provided by several LECs (one ILEC and
possibly more than one CLEC). We also said that inter-LATA services can be provided
by several IXCs. How do these carriers interact with one another? The answer is, via a
switching office called a point of presence (POP). Each IXC that wants to provide inter-
LATA services in a LATA must have a POP in that LATA. The LECs that provide services
inside the LATA must provide connections so that every subscriber can have access to all
POPs. Figure 9.3 illustrates the concept.
      A subscriber who needs to make a connection with another subscriber is connected
first to an end switch and then, either directly or through a tandem switch, to a POP. The

244   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             Figure 9.3   Point ofpresences (POPs)


                                                                              LATA


             call now goes from the POP of an IXC (the one the subscriber has chosen) in the source
             LATA to the POP of the same IXC in the destination LATA. The call is passed through
             the toll office of the IXC and is carried through the network provided by the IXC.

             Signaling
             The telephone network, at its beginning, used a circuit-switched network with dedicated
             links (multiplexing had not yet been invented) to transfer voice communication. As we
             saw in Chapter 8, a circuit-switched network needs the setup and teardown phases to
             establish and terminate paths between the two communicating parties. In the beginning,
             this task was performed by human operators. The operator room was a center to which
             all subscribers were connected. A subscriber who wished to talk to another subscriber
             picked up the receiver (off-hook) and rang the operator. The operator, after listening to
             the caller and getting the identifier of the called party, connected the two by using a wire
             with two plugs inserted into the corresponding two jacks. A dedicated circuit was created
             in this way. One of the parties, after the conversation ended, informed the operator to
             disconnect the circuit. This type of signaling is called in-band signaling because the same
             circuit can be used for both signaling and voice communication.
                  Later, the signaling system became automatic. Rotary telephones were invented that
             sent a digital signal defining each digit in a multidigit telephone number. The switches in
             the telephone companies used the digital signals to create a connection between the caller
             and the called parties. Both in-band and out-of-band signaling were used. In in-band
             signaling, the 4-kHz voice channel was also used to provide signaling. In out-of-band
             signaling, a portion of the voice channel bandwidth was used for signaling; the voice
             bandwidth and the signaling bandwidth were separate.

## SECTION 9.1     TELEPHONE NETWORK             245


     As telephone networks evolved into a complex network, the functionality of the sig-
naling system increased. The signaling system was required to perform other tasks such as
 1. Providing dial tone, ring tone, and busy tone
 2. Transferring telephone numbers between offices
 3. Maintaining and monitoring the call
 4. Keeping billing information
 5. Maintaining and monitoring the status of the telephone network equipment
 6. Providing other functions such as caller ID, voice mail, and so on
These complex tasks resulted in the provision of a separate network for signaling. This
means that a telephone network today can be thought of as two networks: a signaling
network and a data transfer network.

  The tasks of data transfer and signaling are separated in modern telephone networks:
                data transfer is done by one network, signaling by another.

     However, we need to emphasize a point here. Although the two networks are separate,
this does not mean that there are separate physical links everywhere; the two networks
may use separate channels of the same link in parts of the system.

Data Transfer Network
The data transfer network that can carry multimedia information today is, for the most
part, a circuit-switched network, although it can also be a packet-switched network. This
network follows the same type of protocols and model as other networks discussed in
this book.

Signaling Network
The signaling network, which is our main concern in this section, is a packet-switched
network involving the layers similar to those in the OSI model or Internet model, dis-
cussed in Chapter 2. The nature of signaling makes it more suited to a packet-switching
network with different layers. For example, the information needed to convey a telephone
address can easily be encapsulated in a packet with all the error control and addressing
information. Figure 9.4 shows a simplified situation of a telephone network in which the
two networks are separated.
     The user telephone or computer is connected to the signal points (SPs). The link
between the telephone set and SP is common for the two networks. The signaling net-
work uses nodes called signal transport ports (STPs) that receive and forward signaling
messages. The signaling network also includes a service control point (SCP) that con-
trols the whole operation of the network. Other systems such as a database center may
be included to provide stored information about the entire signaling network.

Signaling System Seven (5S7)
The protocol that is used in the signaling network is called Signaling System Seven (SS7).
It is very similar to the five-layer Internet model we saw in Chapter 2, but the layers have
different names, as shown in Figure 9.5.

246   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             Figure 9.4 Data transfer and signaling networks

                      SP: Signal point
                                                                     Database
                      STP: Signal transfer point


                                                                  Signaling network


                                                                 Data transfer network


             Figure 9.5 Layers in SS7

                                                                                  MTP: Message transfer part
                                                                                  SCCP: Signaling connection control point
                                                      TUP                         TeAP: Transaction capabilities application port
                    Upper layers ,', T(;~ __                        ~SNP    ,I,
                                                                                  TUP: Telephone user port
                                                                                  ISUP: ISDN user port
                                                                      r,;   ~
                                                                          ": -


                                                     SCCP


                   Network layer                   MTP level 3


                   Data link layer                 MTPIevel2


                   Physical layer                  MTPlevell


             Physical Layer: MTP Level 1 The physical layer in SS7 called message transport
             part (MTP) level I uses several physical layer specifications such as T-l (1.544 Mbps)
             and DCa (64 kbps).
             Data Link Layer: MTP Level 2 The MTP level 2 layer provides typical data link
             layer services such as packetizing, using source and destination address in the packet
             header, and CRC for error checking.
              Network Layer: MTP Level 3 The MTP level 3 layer provides end-to-end connectivity
              by using the datagram approach to switching. Routers and switches route the signal packets
              from the source to the destination.
              Transport Layer: SCCP The signaling connection control point (SCCP) is used
              for special services such as SaO-call processing.
              Upper Layers: TUP, TCAP, and ISUP There are three protocols at the upper layers.
              Telephone user port (TUP) is responsible for setting up voice calls. It receives the dialed

## SECTION 9.1      TELEPHONE NETWORK              247


digits and routes the calls. Transaction capabilities application port (TCAP) provides
remote calls that let an application program on a computer invoke a procedure on another
computer. ISDN user port (ISUP) can replace TUP to provide services similar to those
of an ISDN network.

Services Provided by Telephone Networks
Telephone companies provide two types of services: analog and digital.

Analog Services
In the beginning, telephone companies provided their subscribers with analog services.
These services still continue today. We can categorize these services as either analog
switched services or analog leased services.
Analog Switched Services This is the familiar dial-up service most often encountered
when a home telephone is used. The signal on a local loop is analog, and the bandwidth is
usually between 0 and 4000 Hz. A local call service is normally provided for a flat monthly
rate, although in some LATAs, the carrier charges for each call or a set of calls. The rationale
for a non flat-rate charge is to provide cheaper service for those customers who do not
make many calls. A toll call can be intra-LATA or inter-LATA. If the LATA is geographi-
cally large, a call may go through a tandem office (toll office) and the subscriber will pay a
fee for the call. The inter-LATA calls are long-distance calls and are charged as such.
      Another service is called 800 service. If a subscriber (normally an organization)
needs to provide free connections for other subscribers (normally customers), it can
request the 800 service. In this case, the call is free for the caller, but it is paid by the
callee. An organization uses this service to encourage customers to call. The rate is less
expensive than that for a normal long-distance call.
      The wide-area telephone service (WATS) is the opposite of the 800 service. The
latter are inbound calls paid by the organization; the former are outbound calls paid by
the organization. This service is a less expensive alternative to regular toll calls;
charges are based on the number of calls. The service can be specified as outbound
calls to the same state, to several states, or to the whole country, with rates charged
accordingly.
      The 900 services are like the 800 service, in that they are inbound calls to a sub-
scriber. However, unlike the 800 service, the call is paid by the caller and is normally
much more expensive than a normal long-distance call. The reason is that the carrier
charges two fees: the first is the long-distance toll, and the second is the fee paid to the
callee for each call.
Analog Leased Service An analog leased service offers customers the opportunity
to lease a line, sometimes called a dedicated line, that is permanently connected to
another customer. Although the connection still passes through the switches in the tele-
phone network, subscribers experience it as a single line because the switch is always
closed; no dialing is needed.

Digital Services
Recently telephone companies began offering digital services to their subscribers. Digital
services are less sensitive than analog services to noise and other forms of interference.

248   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             The two most common digital services are switched/56 service and digital data service
             (DDS). We already discussed high-speed digital services-the T lines-in Chapter 6. We
             discuss the other services in this chapter.
             Switched/56 Service Switched/56 service is the digital version of an analog switched
             line. It is a switched digital service that allows data rates of up to 56 kbps. To communi-
             cate through this service, both parties must subscribe. A caller with normal telephone
             service cannot connect to a telephone or computer with switched/56 service even if the
             caller is using a modem. On the whole, digital and analog services represent two com-
             pletely different domains for the telephone companies. Because the line in a switched!
             56 service is already digital, subscribers do not need modems to transmit digital data.
             However, they do need another device called a digital service unit (DSU).
             Digital Data Service Digital data service (DDS) is the digital version of an analog
             leased line; it is a digital leased line with a maximum data rate of 64 kbps.


## 9.2     DIAL~UP MODEMS
             Traditional telephone lines can carry frequencies between 300 and 3300 Hz, giving
             them a bandwidth of 3000 Hz. All this range is used for transmitting voice, where a
             great deal of interference and distortion can be accepted without loss of intelligibility.
             As we have seen, however, data signals require a higher degree of accuracy to ensure
             integrity. For safety's sake, therefore, the edges of this range are not used for data com-
             munications. In general, we can say that the signal bandwidth must be smaller than the
             cable bandwidth. The effective bandwidth of a telephone line being used for data trans-
             mission is 2400 Hz, covering the range from 600 to 3000 Hz. Note that today some
             telephone lines are capable of handling greater bandwidth than traditional lines. How-
             ever, modem design is still based on traditional capability (see Figure 9.6).

              Figure 9.6   Telephone line bandwidth


                                                  Used for voice


                                300    600                                   3300
                                 I      I         2400 Hz for data              I
                                 I      I"                                      I
                                 I               3000 Hz for voice              I
                                 I.                                           .. I
                                 I                                              I


                 The term modem is a composite word that refers to the two functional entities that
             make up the device: a signal modulator and a signal demodulator. A modulator creates
             a bandpass analog signal from binary data. A demodulator recovers the binary data
             from the modulated signal.

                                      Modem stands for modulator/demodulator.

## SECTION 9.2     DIAL-UP MODEMS           249


     Figure 9.7 shows the relationship of modems to a communications linle The computer
on the left sends a digital signal to the modulator portion of the modem; the data are sent as
an analog signal on the telephone lines. The modem on the right receives the analog signal,
demodulates it through its demodulator, and delivers data to the computer on the right. The
communication can be bidirectional, which means the computer on the right can simulta-
neously send data to the computer on the left, using the same modulation/demodulation
processes.


Figure 9.7    Modulation/demodulation

   TELCO: Telephone company

              A                                                                 B
                                                                              r<
                                                                             .........
                                          c=J n


Modem Standards
Today, many of the most popular modems available are based on the V-series standards
published by the ITU-T. We discuss just the most recent series.

V.32 and V.32bis
The V.32 modem uses a combined modulation and encoding technique called trellis-
coded modulation. Trellis is essentially QAM plus a redundant bit. The data stream is
divided into 4-bit sections. Instead of a quadbit (4-bit pattern), however, a pentabit (5-bit
pattern) is transmitted. The value of the extra bit is calculated from the values of the
data bits. The extra bit is used for error detection.
     The Y.32 calls for 32-QAM with a baud rate of 2400. Because only 4 bits of each
pentabit represent data, the resulting data rate is 4 x 2400 = 9600 bps. The constellation
diagram and bandwidth are shown in Figure 9.8.
     The V.32bis modem was the first of the ITU-T standards to support 14,400-bps
transmission. The Y.32bis uses 128-QAM transmission (7 bits/baud with I bit for error
control) at a rate of 2400 baud (2400 x 6 = 14,400 bps).
     An additional enhancement provided by Y.32bis is the inclusion of an automatic
fall-back and fall-forward feature that enables the modem to adjust its speed upward or
downward depending on the quality of the line or signal. The constellation diagram and
bandwidth are also shown in Figure 9.8.

V. 34bis
The V.34bis modem provides a bit rate of 28,800 with a 960-point constellation and a
bit rate of 33,600 bps with a 1664-point constellation.

250   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             Figure 9.8    The V.32 and V.32bis constellation and bandwidth


                                          90
                                                            Full-duplex 2400-baud
                                  •
                                • • • •
                                        01'
                                        •                   9600-bps 2-wire


                               • •      • •
                            180 •
                               • •      ·i ·
                                          • 0
                                        • •
                                                                    600              1800   3000

                                •
                                  •
                                    •I•
                                        •1•
                                        •
                                          •
                                         270
                          a. Constellation and bandwidth for V.32


                                           90
                                                            Full-duplex. 2400-baud
                                       •••l •••
                                             •• •    14,400-bps 4-wire
                                   • •••
                                       • • •••••
                                      ••      •••
                                  • • • • •••••
                               •••••••••      ••••
                                       • • •••••
                                      ••
                            180 • • • •      • ••• 0       600                       1800   3000
                               ••••••• • • •••••
                                              ••••
                                  •••••••••••
                                       • • ••••
                                     •••      ••
                                       ••• •••
                                             ••
                                         270
                          b. Constellation and bandwidth for V.32bis


              1--:90
              Traditional modems have a data rate limitation of 33.6 kbps, as determined by the
              Shannon capacity (see Chapter 3). However, V.90 modems with a bit rate of 56,000 bps
              are available; these are called 56K modems. These modems may be used only if one
              party is using digital signaling (such as through an Internet provider). They are asym-
              metric in that the downloading rate (flow of data from the Internet service provider to
              the PC) is a maximum of 56 kbps, while the uploading rate (flow of data from the PC to
              the Internet provider) can be a maximum of 33.6 kbps. Do these modems violate the
              Shannon capacity principle? No, in the downstream direction, the SNR ratio is higher
              because there is no quantization error (see Figure 9.9).
                   In uploading, the analog signal must still be sampled at the switching station. In
              this direction, quantization noise (as we saw in Chapter 4) is introduced into the signal,
              which reduces the SNR ratio and limits the rate to 33.6 kbps.
                   However, there is no sampling in the downloading. The signal is not affected by
              quantization noise and not subject to the Shannon capacity limitation. The maximum data
              rate in the uploading direction is still 33.6 kbps, but the data rate in the downloading
              direction is now 56 kbps.
                   One may wonder how we arrive at the 56-kbps figure. The telephone companies
              sample 8000 times per second with 8 bits per sample. One of the bits in each sample is
              used for control purposes, which means each sample is 7 bits. The rate is therefore
              8000 x 7, or 56,000 bps or 56 kbps.

## SECTION 9.3      DIGITAL SUBSCRIBER LINE      251


Figure 9.9    Uploading and downloading in 56K modems

          Quantization noise limits
                the data rate


                                   -=tP-~
             1--------1
             1     PCM         I
             1     --.-        I
             1                 I
                                     ~                                   ISP
                                                                        server
                                              Uploading,
                                           quantization noise


                                   -=tP- ~ -=tP- ~
             1--------1
             1     Inverse     I


                                        "'--~~                          ~
             1      PCM        I
             1                 I

                                                                         ISP
                                                                        server
                                             Downloading,
                                          no quantization noise


1':92
The standard above V90 is called ~92. These modems can adjust their speed, and if
the noise allows, they can upload data at the rate of 48 kbps. The downloading rate is
still 56 kbps. The modem has additional features. For example, the modem can inter-
rupt the Internet connection when there is an incoming call if the line has call-waiting
service.


## 9.3     DIGITAL SUBSCRIBER LINE
After traditional modems reached their peak data rate, telephone companies developed
another technology, DSL, to provide higher-speed access to the Internet. Digital sub-
scriber line (DSL) technology is one of the most promising for supporting high-speed
digital communication over the existing local loops. DSL technology is a set of tech-
nologies, each differing in the first letter (ADSL, VDSL, HDSL, and SDSL). The set is
often referred to as xDSL, where x can be replaced by A, V, H, or S.

252   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             ADSL
             The first technology in the set is asymmetric DSL (ADSL). ADSL, like a 56K modem,
             provides higher speed (bit rate) in the downstream direction (from the Internet to the
             resident) than in the upstream direction (from the resident to the Internet). That is the
             reason it is called asymmetric. Unlike the asymmetry in 56K modems, the designers of
             ADSL specifically divided the available bandwidth of the local loop unevenly for the
             residential customer. The service is not suitable for business customers who need a
             large bandwidth in both directions.

                  ADSL is an asymmetric communication technology designed for residential users;
                                         it is not suitable for businesses.


              Using Existing Local Loops
             One interesting point is that ADSL uses the existing local loops. But how does ADSL
             reach a data rate that was never achieved with traditional modems? The answer is that the
             twisted-pair local loop is actually capable of handling bandwidths up to 1.1 MHz, but the
             filter installed at the end office of the telephone company where each local loop termi-
             nates limits the bandwidth to 4 kHz (sufficient for voice communication). If the filter is
             removed, however, the entire 1.1 MHz is available for data and voice communications.

                           The existing local loops can handle bandwidths up to 1.1 MHz.


             Adaptive Technology
             Unfortunately, 1.1 MHz is just the theoretical bandwidth of the local loop. Factors such
             as the distance between the residence and the switching office, the size of the cable, the
             signaling used, and so on affect the bandwidth. The designers of ADSL technology
             were aware of this problem and used an adaptive technology that tests the condition and
             bandwidth availability of the line before settling on a data rate. The data rate of ADSL
             is not fixed; it changes based on the condition and type of the local loop cable.

                            ADSL is an adaptive technology. The system uses a data rate
                                   based on the condition of the local loop line.


             Discrete Multitone Technique
              The modulation technique that has become standard for ADSL is called the discrete
              multitone technique (DMT) which combines QAM and FDM. There is no set way
              that the bandwidth of a system is divided. Each system can decide on its bandwidth
              division. Typically, an available bandwidth of 1.104 MHz is divided into 256 channels.
              Each channel uses a bandwidth of 4.312 kHz, as shown in Figure 9.10. Figure 9.11 shows
              how the bandwidth can be divided into the following:
              o Voice. Channel 0 is reserved for voice communication.
              o Idle. Channels 1 to 5 are not used and provide a gap between voice and data
                  communication.

## SECTION 9.3   DIGITAL SUBSCRIBER LINE           253


Figure 9.10      Discrete multitone technique


                                                                                      Upstream
                                                                                      bits


                                                                                      Downstream
                                                                                      bits


Figure 9.11      Bandwidth division in ADSL


              Voice             Upstream               Downstream
              ""'\          /              I'
              ,;d
                     Not
                                                                         '"
               "-

                     used


           o     4      26             108 138                           1104   kHz


o Upstream data and control. Channels 6 to 30 (25 channels) are used for upstream
    data transfer and control. One channel is for control, and 24 channels are for data
    transfer. If there are 24 channels, each using 4 kHz (out of 4.312 kHz available)
    with QAM modulation, we have 24 x 4000 x 15, or a 1.44-Mbps bandwidth, in
    the upstream direction. However, the data rate is normally below 500 kbps because
    some of the carriers are deleted at frequencies where the noise level is large. In other
    words, some of channels may be unused.
o   Downstream data and control. Channels 31 to 255 (225 channels) are used for
    downstream data transfer and control. One channel is for control, and 224 channels
    are for data. If there are 224 channels, we can achieve up to 224 x 4000 x 15, or
## 13.4 Mbps. However, the data rate is normally below 8 Mbps because some of the
    carriers are deleted at frequencies where the noise level is large. In other words,
    some of channels may be unused.

Customer Site: ADSL Modem
Figure 9.12 shows an ADSL modem installed at a customer's site. The local loop
connects to a splitter which separates voice and data communications. The ADSL

254   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             modem modulates and demodulates the data, using DMT, and creates downstream
             and upstream channels.


             Figure 9.12    ADSL modem

                                      Splitter

                                                               Voice

                         Local loop

                                                                Data

                                                                          ADSLmodem


             Note that the splitter needs to be installed at the customer's premises, normally by a
             technician from the telephone company. The voice line can use the existing telephone
             wiring in the house, but the data line needs to be installed by a professional. All this
             makes the ADSL line expensive. We will see that there is an alternative technology,
             Universal ADSL (or ADSL Lite).

             Telephone Company Site: DSLAM
             At the telephone company site, the situation is different. Instead of an ADSL modem, a
             device called a digital subscriber line access multiplexer (DSLAM) is installed that
             functions similarly. In addition, it packetizes the data to be sent to the Internet (ISP
             server). Figure 9.13 shows the configuration.


             Figure 9.13    DSLAM

                                                               Splitter

                    To telephone ~                 V_o_ic_e_ _-+--i       Low-pass
                         network                                            filter
                                                                                        Local loop
                                      Packetized
                         To the ~_ _~d~at~a_---i~d~             High-pass
                        Internet                 UIIM---I--""     filter
                                                             ",_,",!"",,_..u.


             ADSL Lite
             The installation of splitters at the border of the premises and the new wiring for the data
             line can be expensive and impractical enough to dissuade most subscribers. A new ver-
             sion of ADSL technology called ADSL Lite (or Universal ADSL or splitterless ADSL) is
             available for these subscribers. This technology allows an ASDL Lite modem to be
             plugged directly into a telephone jack and connected to the computer. The splitting is
             done at the telephone company. ADSL Lite uses 256 DMT carriers with 8-bit modulation

## SECTION 9.3   DIGITAL SUBSCRIBER LINE          255


(instead of 15-bit). However, some of the carriers may not be available because errors
created by the voice signal might mingle with them. It can provide a maximum down-
stream data rate of 1.5 Mbps and an upstream data rate of 512 kbps.

HDSL
The high-bit-rate digital subscriber line (HDSL) was designed as an alternative to
the T-lline (1.544 Mbps). The T-1line uses alternate mark inversion (AMI) encoding,
which is very susceptible to attenuation at high frequencies. This limits the length of
a T-l line to 3200 ft (1 km). For longer distances, a repeater is necessary, which means
increased costs.
     HDSL uses 2B1Q encoding (see Chapter 4), which is less susceptible to attenuation.
A data rate of 1.544 Mbps (sometimes up to 2 Mbps) can be achieved without repeaters
up to a distance of 12,000 ft (3.86 km). HDSL uses two twisted pairs (one pair for each
direction) to achieve full-duplex transmission.

SDSL
The symmetric digital subscriber line (SDSL) is a one twisted-pair version ofHDSL.
It provides full-duplex symmetric communication supporting up to 768 kbps in each
direction. SDSL, which provides symmetric communication, can be considered an
alternative to ADSL. ADSL provides asymmetric communication, with a downstream
bit rate that is much higher than the upstream bit rate. Although this feature meets the
needs of most residential subscribers, it is not suitable for businesses that send and
receive data in large volumes in both directions.

VDSL
The very high-bit-rate digital subscriber line (VDSL), an alternative approach that is
similar to ADSL, uses coaxial, fiber-optic, or twisted-pair cable for short distances. The
modulating technique is DMT. It provides a range of bit rates (25 to 55 Mbps) for
upstream communication at distances of 3000 to 10,000 ft. The downstream rate is nor-
mally 3.2 Mbps.

Summary
Table 9.1 shows a summary of DSL technologies. Note that the data rate and distances
are approximations and can vary from one implementation to another.

  Table 9.1      Summary of DSL technologies

                    Downstream       Upstream        Distance     Twisted     Line
    Technology         Rate            Rate            (jt)        Pairs      Code
    ADSL            1.5-6.1 Mbps   16-640 kbps        12,000         1        DMT
    ADSL Lite       1.5 Mbps       500 kbps           18,000         1        DMT
    HDSL            1.5-2.0 Mbps   1.5-2.0 Mbps       12,000         2        2B1Q
    SDSL            768 kbps       768 kbps           12,000         1        2B1Q
    VDSL            25-55 Mbps     3.2 Mbps       3000-10,000        1        DMT

256   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


## 9.4     CABLE TV NETWORKS
             The cable TV network started as a video service provider, but it has moved to the business
             of Internet access. In this section, we discuss cable TV networks per se; in Section 9.5 we
             discuss how this network can be used to provide high-speed access to the Internet.

             Traditional Cable Networks
             Cable TV started to distribute broadcast video signals to locations with poor or no
             reception in the late 1940s. It was called community antenna TV (CATV) because an
             antenna at the top of a tall hill or building received the signals from the TV stations and
             distributed them, via coaxial cables, to the community. Figure 9.14 shows a schematic
             diagram of a traditional cable TV network.

             Figure 9.14    Traditional cable TV network


                                                                              Splitter


                                                                                               Tap


                  The cable TV office, called the head end, receives video signals from broadcasting
             stations and feeds the signals into coaxial cables. The signals became weaker and
             weaker with distance, so amplifiers were installed through the network to renew the
             signals. There could be up to 35 amplifiers between the head end and the subscriber
             premises. At the other end, splitters split the cable, and taps and drop cables make the
             connections to the subscriber premises.
                  The traditional cable TV system used coaxial cable end to end. Due to attenuation of
             the signals and the use of a large number of amplifiers, communication in the traditional
             network was unidirectional (one-way). Video signals were transmitted downstream, from
             the head end to the subscriber premises.

                       Communication in the traditional cable TV network is unidirectional.


              Hybrid Fiber-Coaxial (HFC) Network
             The second generation of cable networks is called a hybrid fiber-coaxial (HFC) net-
             work. The network uses a combination of fiber-optic and coaxial cable. The transmission

## SECTION 9.5     CABLE TV FOR DATA TRANSFER             257


medium from the cable TV office to a box, called the fiber node, is optical fiber; from the
fiber node through the neighborhood and into the house is still coaxial cable. Figure 9.15
shows a schematic diagram of an HFC network.

Figure 9.15    Hybridfiber-coaxial (HFC) network


                              High-bandwidth
                                   fiber


      RCH


     The regional cable head (RCH) normally serves up to 400,000 subscribers. The
RCHs feed the distribution hubs, each of which serves up to 40,000 subscribers. The
distribution hub plays an important role in the new infrastructure. Modulation and dis-
tribution of signals are done here; the signals are then fed to the fiber nodes through
fiber-optic cables. The fiber node splits the analog signals so that the same signal is sent
to each coaxial cable. Each coaxial cable serves up to 1000 subscribers. The use of
fiber-optic cable reduces the need for amplifiers down to eight or less.
     One reason for moving from traditional to hybrid infrastructure is to make the cable
network bidirectional (two-way).

            Communication in an HFC cable TV network can be bidirectional.


## 9.5     CABLE TV FOR DATA TRANSFER
Cable companies are now competing with telephone companies for the residential
customer who wants high-speed data transfer. DSL technology provides high-data-rate
connections for residential subscribers over the local loop. However, DSL uses the
existing unshielded twisted-pair cable, which is very susceptible to interference. This
imposes an upper limit on the data rate. Another solution is the use of the cable TV net-
work. In this section, we briefly discuss this technology.

Bandwidth
Even in an HFC system, the last part of the network, from the fiber node to the sub-
scriber premises, is still a coaxial cable. This coaxial cable has a bandwidth that ranges

258   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             from 5 to 750 MHz (approximately). To provide Internet access, the cable company has
             divided this bandwidth into three bands: video, downstream data, and upstream data, as
             shown in Figure 9.16.


             Figure 9.16     Division of coaxial cable band by CATV


                                            . ~::2i
                                             Data:~          Video                  Data
                                            l1PStf~~~         bapd               downstream


                       Frequency, MHz   5          4254                    550                750


             Downstream Video Band
             The downstream video band occupies frequencies from 54 to 550 MHz. Since each
             TV channel occupies 6 MHz, this can accommodate more than 80 channels.

             Downstream Data Band
             The downstream data (from the Internet to the subscriber premises) occupies the upper
             band, from 550 to 750 MHz. This band is also divided into 6-MHz channels.
             Modulation      Downstream data band uses the 64-QAM (or possibly 256-QAM)
             modulation technique.

                     Downstream data are modulated using the 64-QAM modulation technique.


             Data Rate There is 6 bits/baud in 64-QAM. One bit is used for forward error correction;
             this leaves 5 bits of data per baud. The standard specifies I Hz for each baud; this means that,
             theoretically, downstream data can be received at 30 Mbps (5 bitslHz x 6 MHz). The stan-
             dard specifies only 27 Mbps. However, since the cable modem is normally connected to the
             computer through a lOBase-T cable (see Chapter 13), this limits the data rate to 10 Mbps.

                                   The theoretical downstream data rate is 30 Mbps.


              Upstream Data Band
             The upstream data (from the subscriber premises to the Internet) occupies the lower
             band, from 5 to 42 MHz. This band is also divided into 6-MHz channels.
              Modulation The upstream data band uses lower frequencies that are more suscepti-
              ble to noise and interference. For this reason, the QAM technique is not suitable for this
              band. A better solution is QPSK.

                        Upstream data are modulated using the QPSK modulation technique.

## SECTION 9.5     CABLE TV FOR DATA TRANSFER              259


Data Rate There are 2 bitslbaud in QPSK. The standard specifies 1 Hz for each baud;
this means that, theoretically, upstream data can be sent at 12 Mbps (2 bitslHz x 6 MHz).
However, the data rate is usually less than 12 Mbps.

                      The theoretical upstream data rate is 12 Mbps.


Sharing
Both upstream and downstream bands are shared by the subscribers.

Upstream Sharing
The upstream data bandwidth is 37 MHz. This means that there are only six 6-MHz
channels available in the upstream direction. A subscriber needs to use one channel to
send data in the upstream direction. The question is, "How can six channels be shared in
an area with 1000,2000, or even 100,000 subscribers?" The solution is timesharing. The
band is divided into channels using FDM; these channels must be shared between sub-
scribers in the same neighborhood. The cable provider allocates one channel, statically
or dynamically, for a group of subscribers. If one subscriber wants to send data, she or
he contends for the channel with others who want access; the subscriber must wait until
the channel is available.

Downstream Sharing
We have a similar situation in the downstream direction. The downstream band has
33 channels of 6 MHz. A cable provider probably has more than 33 subscribers; therefore,
each channel must be shared between a group of subscribers. However, the situation is dif-
ferent for the downstream direction; here we have a multicasting situation. If there are data
for any of the subscribers in the group, the data are sent to that channel. Each subscriber is
sent the data. But since each subscriber also has an address registered with the provider; the
cable modem for the group matches the address carried with the data to the address assigned
by the provider. If the address matches, the data are kept; otherwise, they are discarded.

CMandCMTS
To use a cable network for data transmission, we need two key devices: a cable modem
(CM) and a cable modem transmission system (CMTS).

CM
The cable modem (CM) is installed on the subscriber premises. It is similar to an ADSL
modem. Figure 9.17 shows its location.

CMTS
The cable modem transmission system (CMTS) is installed inside the distribution
hub by the cable company. It receives data from the Internet and passes them to the
combiner, which sends them to the subscriber. The CMTS also receives data from the
subscriber and passes them to the Internet. Figure 9.18 shows the location of the CMTS.

260   CHAPTER 9     USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             Figure 9.17      Cable modem (CM)

                                        Cable

                                                Customer residence
                                                r------------------------I
                                                I                                                    I
                                                I                     V~OO                           I
                                     Thp"~~                                                          I
                                                                                                     I
                                                                                                     1

                                                                                                     1

                                                                                                     1

                                                                                             r-

                                                                                             =-
                                                                                                     1

                                                                                 Data                1
                                                                                                     1
                                                                                                     1
                                                1
                                                1
                                                               Cable modem                         ..J1


             Figure 9.18      Cable modem transmission system (CMTS)

                                                 Distribution hub
                                                -------------------
                                                I
                                                I Video   I                  I                    Fiber
                              From head end     I         I   Combiner       I          ~,",,"-,,<.-::-.-'-_~
                                                I                                        I
                                                I                                        I
                                                I                                        I
                                                I                                        I
                                To and from     : Data         '     - c',               :

                                 the Internet   I                                        I
                                                I
                                                L
                                                               CMTS                     ~
                                                                                         I


             Data Transmission Schemes: DOeSIS
             During the last few decades, several schemes have been designed to create a standard for
             data transmission over an HFC network. Prevalent is the one devised by Multimedia
             Cable Network Systems (MCNS), called Data Over Cable System Interface Specifi-
             cation (DOCSIS). DOCSIS defines all the protocols necessary to transport data from a
             CMTS to aCM.

              Upstream Communication
             The following is a very simplified version of the protocol defined by DOCSIS for
             upstream communication. It describes the steps that must be followed by a CM:
                  1. The CM checks the downstream channels for a specific packet periodically sent by
                     the CMTS. The packet asks any new CM to announce itself on a specific upstream
                     channel.
                  2. The CMTS sends a packet to the CM, defining its allocated downstream and
                     upstream channels.
                  3. The CM then starts a process, called ranging, which determines the distance
                     between the CM and CMTS. This process is required for synchronization between all

## SECTION 9. 7   KEY TERMS        261


    CMs and CMTSs for the minislots used for timesharing of the upstream channels.
    We will learn about this timesharing when we discuss contention protocols in
## Chapter 12.
 4. The CM sends a packet to the ISP, asking for the Internet address.
 5. The CM and CMTS then exchange some packets to establish security parameters,
    which are needed for a public network such as cable TV.
 6. The CM sends its unique identifier to the CMTS.
 7. Upstream communication can start in the allocated upstream channel; the CM can
    contend for the minislots to send data.

Downstream Communication
In the downstream direction, the communication is much simpler. There is no conten-
tion because there is only one sender. The CMTS sends the packet with the address of
the receiving eM, using the allocated downstream channel.


## 9.6     RECOMMENDED READING
For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [...] refer to the reference list at the end of the text.

Books
[CouOl] gives an interesting discussion about telephone systems, DSL technology,
and CATV in Chapter 8. [Tan03] discusses telephone systems and DSL technology in
## Section 2.5 and CATV in Section 2.7. [GW04] discusses telephone systems in Sec-
tion 1.1.1 and standard modems in Section 3.7.3. A complete coverage of residential
broadband (DSL and CATV) can be found in [Max99].


## 9.7     KEY TERMS
56Kmodem                                      community antenna TV (CATV)
800 service                                   competitive local exchange carrier
900 service                                      (CLEC)
ADSL Lite                                     Data Over Cable System Interface
ADSLmodem                                        Specification (DOCSIS)
analog leased service                         demodulator
analog switched service                       digital data service (DDS)
asymmetric DSL (ADSL)                         digital service
cable modem (CM)                              digital subscriber line (DSL)
cable modem transmission system               digital subscriber line access multiplexer
  (CMTS)                                         (DSLAM)
cable TV network                              discrete multitone technique (DMT)
common carrier                                distribution hub

262   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


             downloading                                     server control point (SCP)
             downstream data band                            signal point (SP)
             end office                                      signal transport port (STP)
             fiber node                                      signaling connection control point
             head end                                           (SCep)
             high-bit-rate DSL (HDSL)                        Signaling System Seven (SS7)
             hybrid fiber-coaxial (HFC) network              switched/56 service
             in-band signaling                               switching office
             incumbent local exchange carrier                symmetric DSL (SDSL)
                (ILEC)                                       tandem office
             interexchange carrier (IXC)                     telephone user port (TUP)
             ISDN user port (ISUP)                           transaction capabilities application port
             local access transport area (LATA)                 (TCAP)
             local exchange carrier (LEC)                    trunk
             local loop                                      uploading
             long distance company                           upstream data band
             message transport port (MTP) level              Y.32
             modem                                           Y.32bis
             modulator                                       Y.34bis
             out-of-band signaling                           Y.90
             plain old telephone system (POTS)               Y.92
             point of presence (POP)                         very-high-bit-rate DSL (VDSL)
             ranging                                         video band
             regional cable head (RCH)                       V-series
             regional office                                 wide-area telephone service (WATS)


## 9.8     SUMMARY
             o The telephone, which is referred to as the plain old telephone system (POTS),
                  was originally an analog system. During the last decade, the telephone network
                  has undergone many technical changes. The network is now digital as well as
                  analog.
              o   The telephone network is made of three major components: local loops, trunks,
                  and switching offices. It has several levels of switching offices such as end offices,
                  tandem offices, and regional offices.
              o   The United States is divided into many local access transport areas (LATAs). The
                  services offered inside a LATA are called intra-LATA services. The carrier that
                  handles these services is called a local exchange carrier (LEC). The services
                  between LATAs are handled by interexchange carriers (lXCs).
              o   In in-band signaling, the same circuit is used for both signaling and data. In out-of-
                  band signaling, a portion of the bandwidth is used for signaling and another portion

## SECTION 9.9    PRACTICE SET         263


    for data. The protocol that is used for signaling in the telephone network is called
    Signaling System Seven (SS7).
o   Telephone companies provide two types of services: analog and digital. We can
    categorize analog services as either analog switched services or analog leased ser-
    vices. The two most common digital services are switched/56 service and digital
    data service (DDS).
o   Data transfer using the telephone local loop was traditionally done using a dial-up
    modem. The term modem is a composite word that refers to the two functional
    entities that make up the device: a signal modulator and a signal demodulator.
o   Most popular modems available are based on the V-series standards. The V.32 modem
    has a data rate of 9600 bps. The V32bis modem supports 14,400-bps transmission.
    V90 modems, called 56K modems, with a downloading rate of 56 kbps and upload-
    ing rate of 33.6 kbps are very common. The standard above V90 is called V92. These
    modems can adjust their speed, and if the noise allows, they can upload data at the rate
    of 48 kbps.
o   Telephone companies developed another technology, digital subscriber line (DSL), to
    provide higher-speed access to the Internet. DSL technology is a set of technologies,
    each differing in the first letter (ADSL, VDSL, HDSL, and SDSL. ADSL provides
    higher speed in the downstream direction than in the upstream direction. The high-bit-
    rate digital subscriber line (HDSL) was designed as an alternative to the T-l line
    (1.544 Mbps). The symmetric digital subscriber line (SDSL) is a one twisted-pair ver-
    sion of HDSL. The very high-bit-rate digital subscriber line (VDSL) is an alternative
    approach that is similar to ADSL.
o   Community antenna TV (CATV) was originally designed to provide video services
    for the community. The traditional cable TV system used coaxial cable end to end.
    The second generation of cable networks is called a hybrid fiber-coaxial (HFC)
    network. The network uses a combination of fiber-optic and coaxial cable.
o   Cable companies are now competing with telephone companies for the residential
    customer who wants high-speed access to the Internet. To use a cable network for
    data transmission, we need two key devices: a cable modem (CM) and a cable modem
    transmission system (CMTS).


## 9.9     PRACTICE SET
Review Questions
 1. What are the three major components of a telephone network?
 2. Give some hierarchical switching levels of a telephone network.
 3. What is LATA? What are intra-LATA and inter-LATA services?
 4. Describe the SS7 service and its relation to the telephone network.
 S. What are the two major services provided by telephone companies in the United
    States?
 6. What is dial-up modem technology? List some of the common modem standards
    discussed in this chapter and give their data rates.

264   CHAPTER 9   USING TELEPHONE AND CABLE NETWORKS FOR DATA TRANSMISSION


               7. What is DSL technology? What are the services provided by the telephone companies
                  using DSL? Distinguish between a DSL modem and a DSLAM.
               8. Compare and contrast a traditional cable network with a hybrid fiber-coaxial network.
               9. How is data transfer achieved using CATV channels?
              10. Distinguish between CM and CMTS.

             Exercises
              11. Using the discussion of circuit-switching in Chapter 8, explain why this type of
                  switching was chosen for telephone networks.
              12. In Chapter 8, we discussed the three communication phases involved in a circuit-
                  switched network. Match these phases with the phases in a telephone call between
                  two parties.
              13. In Chapter 8, we learned that a circuit-switched network needs end-to-end addressing
                  during the setup and teardown phases. Define end-to-end addressing in a telephone
                  network when two parties communicate.
              14. When we have an overseas telephone conversation, we sometimes experience a
                  delay. Can you explain the reason?
              15. Draw a barchart to compare the different downloading data rates of common modems.
              16. Draw a barchart to compare the different downloading data rates of common DSL
                  technology implementations (use minimum data rates).
              17. Calculate the minimum time required to download one million bytes of information
                  using each of the following technologies:
                  a. V32 modem
                  b. V32bis modem
                  c. V90 modem
              18. Repeat Exercise 17 using different DSL implementations (consider the minimum
                  rates).
              19. Repeat Exercise 17 using a cable modem (consider the minimum rates).
              20. What type of topology is used when customers in an area use DSL modems for
                  data transfer purposes? Explain.
              21. What type of topology is used when customers in an area use cable modems for
                  data transfer purposes? Explain.

Data Link Layer


Objectives
The data link layer transforms the physical layer, a raw transmission facility, to a link
responsible for node-to-node (hop-to-hop) communication. Specific responsibilities of
the data link layer include framing, addressing, flow control, error control, and media
access control. The data link layer divides the stream of bits received from the network
layer into manageable data units called frames. The data link layer adds a header to the
frame to define the addresses of the sender and receiver of the frame. If the rate at
which the data are absorbed by the receiver is less than the rate at which data are pro-
duced in the sender, the data link layer imposes a flow control mechanism to avoid
overwhelming the receiver. The data link layer also adds reliability to the physical layer
by adding mechanisms to detect and retransmit damaged, duplicate, or lost frames.
When two or more devices are connected to the same link, data link layer protocols are
necessary to determine which device has control over the link at any given time.
     In Part 3 of the book, we first discuss services provided by the data link layer. We
then discuss the implementation of these services in local area networks (LANs). Finally
we discuss how wide area networks (WANs) use these services.


                  Part 3 of the book is devoted to the data link layer and
                             the services provided by this layer.


Chapters
This part consists of nine chapters: Chapters 10 to 18.

## Chapter 10
## Chapter 10 discusses error detection and correction. Although the quality of devices and
media have been improved during the last decade, we still need to check for errors and
correct them in most applications.

## Chapter 11
## Chapter 11 is named data link control, which involves flow and error control. It dis-
cusses some protocols that are designed to handle the services required from the data
link layer in relation to the network layer.

## Chapter 12
## Chapter 12 is devoted to access control, the duties of the data link layer that are related
to the use of the physical layer.

## Chapter 13
This chapter introduces wired local area networks. A wired LAN, viewed as a link, is
mostly involved in the physical and data link layers. We have devoted the chapter to the
discussion of Ethernet and its evolution, a dominant technology today.

## Chapter 14
This chapter introduces wireless local area networks. The wireless LAN is a growing
technology in the Internet. We devote one chapter to this topic.

## Chapter 15
After discussing wired and wireless LANs, we show how they can be connected together
using connecting devices.

## Chapter 16
This is the first chapter on wide area networks (WANs). We start with wireless WANs
and then move on to satellite networks and mobile telephone networks.

## Chapter 17
To demonstrate the operation of a high-speed wide area network that can be used as a
backbone for other WANs or for the Internet, we have chosen to devote all of Chapter 17
to SONET, a wide area network that uses fiber-optic technology.

## Chapter 18
This chapter concludes our discussion on wide area networks. Two switched WANs,
Frame Relay and ATM, are discussed here.

## CHAPTER 10

      Error Detection and Correction


      Networks must be able to transfer data from one device to another with acceptable accu-
      racy. For most applications, a system must guarantee that the data received are identical to
      the data transmitted. Any time data are transmitted from one node to the next, they can
      become corrupted in passage. Many factors can alter one or more bits of a message. Some
      applications require a mechanism for detecting and correcting errors.


                            Data can be corrupted during transmission.
                   Some applications require that errors be detected and corrected.


           Some applications can tolerate a small level of error. For example, random errors
      in audio or video transmissions may be tolerable, but when we transfer text, we expect
      a very high level of accuracy.


## 10.1      INTRODUCTION
      Let us first discuss some issues related, directly or indirectly, to error detection and
      correcion.

      Types of Errors
      Whenever bits flow from one point to another, they are subject to unpredictable
      changes because of interference. This interference can change the shape of the signal.
      In a single-bit error, a 0 is changed to a 1 or a 1 to a O. In a burst error, multiple bits are
      changed. For example, a 11100 s burst of impulse noise on a transmission with a data
      rate of 1200 bps might change all or some of the 12 bits of information.

      Single-Bit Error
      The term single-bit error means that only 1 bit of a given data unit (such as a byte,
      character, or packet) is changed from 1 to 0 or from 0 to 1.

                                                                                                 267

268   CHAPTER 10   ERROR DETECTION AND CORRECTION


                              In a single-bit error, only 1 bit in the data unit has changed.

                    Figure 10.1 shows the effect of a single-bit error on a data unit. To understand the
              impact of the change, imagine that each group of 8 bits is an ASCII character with a 0 bit
              added to the left. In Figure 10.1,00000010 (ASCII STX) was sent, meaning start of
              text, but 00001010 (ASCII LF) was received, meaning line feed. (For more information
              about ASCII code, see Appendix A.)


              :Figure 10.1   Single-bit error

                                                             o changed to I


                                                Sent                          Received


                   Single-bit errors are the least likely type of error in serial data transmission. To under-
              stand why, imagine data sent at 1 Mbps. This means that each bit lasts only 1/1,000,000 s,
              or 1 )ls. For a single-bit error to occur, the noise must have a duration of only 1 )ls, which
              is very rare; noise normally lasts much longer than this.

              Burst Error
              The term burst error means that 2 or more bits in the data unit have changed from 1 to 0
              or from 0 to 1.


                        A burst error means that 2 or more bits in the data unit have changed.


                   Figure 10.2 shows the effect of a burst error on a data unit. In this case,
              0100010001000011 was sent, but 0101110101100011 was received. Note that a burst
              error does not necessarily mean that the errors occur in consecutive bits. The length of
              the burst is measured from the first corrupted bit to the last corrupted bit. Some bits in
              between may not have been corrupted.


              Figure 10.2     Burst error of length 8

                                                        Length of burst
                                                         error (8 bits)

## SECTION 10.1     INTRODUCTION          269


     A burst error is more likely to occur than a single-bit error. The duration of noise is
normally longer than the duration of 1 bit, which means that when noise affects data, it
affects a set of bits. The number of bits affected depends on the data rate and duration
of noise. For example, if we are sending data at I kbps, a noise of 11100 s can affect
10 bits; if we are sending data at I Mbps, the same noise can affect 10,000 bits.

Redundancy
The central concept in detecting or correcting errors is redundancy. To be able to
detect or correct errors, we need to send some extra bits with our data. These redundant
bits are added by the sender and removed by the receiver. Their presence allows the
receiver to detect or correct corrupted bits.

       To detect or correct errors, we need to send extra (redundant) bits with data.


Detection Versus Correction
The correction of errors is more difficult than the detection. In error detection, we are
looking only to see if any error has occurred. The answer is a simple yes or no. We are
not even interested in the number of errors. A single-bit error is the same for us as a
burst error.
     In error correction, we need to know the exact number of bits that are corrupted and
more importantly, their location in the message. The number of the errors and the size of
the message are important factors. If we need to correct one single error in an 8-bit data
unit, we need to consider eight possible error locations; if we need to correct two errors
in a data unit of the same size, we need to consider 28 possibilities. You can imagine the
receiver's difficulty in finding 10 errors in a data unit of 1000 bits.

Forward Error Correction Versus Retransmission
There are two main methods of error correction. Forward error correction is the pro-
cess in which the receiver tries to guess the message by using redundant bits. This is
possible, as we see later, if the number of errors is small. Correction by retransmission
is a technique in which the receiver detects the occurrence of an error and asks the sender
to resend the message. Resending is repeated until a message arrives that the receiver
believes is error-free (usually, not all errors can be detected).

Coding
Redundancy is achieved through various coding schemes. The sender adds redundant
bits through a process that creates a relationship between the redundant bits and the
actual data bits. The receiver checks the relationships between the two sets of bits to
detect or correct the errors. The ratio of redundant bits to the data bits and the robust-
ness of the process are important factors in any coding scheme. Figure 10.3 shows the
general idea of coding.
     We can divide coding schemes into two broad categories: block coding and convo-
lution coding. In this book, we concentrate on block coding; convolution coding is
more complex and beyond the scope of this book.

270   CHAPTER 10   ERROR DETECTION AND CORRECTION


              Figure 10.3 The structure ofencoder and decoder

                                       Sender                                                                         Receiver
                                                      Encoder                                         Decoder

                                                                                                              I                         I
                              ~
                                         e8sage                                                                       Message


                                                                                                                          t  correct or
                                                                                                                             discard
                              l I    Generator                                                                    I Checker I
                                           ~                                                                              t
                          [~es~~~~u~~y<;lHl-u.::..:n:.;;.re:.;;.li;,:;ab:.:le:..t::.:ra:.;;.ns:.::Iill.::..:·s;;;;'si;;;;on~~:~:~~~~~~f~~o,~=l


               In this book, we concentrate on block codes; we leave convolution codes to advanced texts.


              Modular Arithmetic
             Before we finish this section, let us briefly discuss a concept basic to computer science
             in general and to error detection and correction in particular: modular arithmetic. Our
             intent here is not to delve deeply into the mathematics of this topic; we present just
             enough information to provide a background to materials discussed in this chapter.
                  In modular arithmetic, we use only a limited range of integers. We define an upper
             limit, called a modulus N. We then use only the integers 0 to N - I, inclusive. This is
             modulo-N arithmetic. For example, if the modulus is 12, we use only the integers 0 to
             11, inclusive. An example of modulo arithmetic is our clock system. It is based on
             modulo-12 arithmetic, substituting the number 12 for O. In a modulo-N system, if a
             number is greater than N, it is divided by N and the remainder is the result. If it is neg-
             ative, as many Ns as needed are added to make it positive. Consider our clock system
             again. If we start a job at 11 A.M. and the job takes 5 h, we can say that the job is to be
             finished at 16:00 if we are in the military, or we can say that it will be finished at 4 P.M.
             (the remainder of 16/12 is 4).

                   In modulo-N arithmetic, we use only the integers in the range 0 to N - 1, inclusive.

                 Addition and subtraction in modulo arithmetic are simple. There is no carry when
             you add two digits in a column. There is no carry when you subtract one digit from
             another in a column.

             Modulo-2 Arithmetic
             Of particular interest is modulo-2 arithmetic. In this arithmetic, the modulus N is 2. We
             can use only 0 and 1. Operations in this arithmetic are very simple. The following
             shows how we can add or subtract 2 bits.

                           Adding:                        0+0=0                  0+1=1                   1+0=1                  1+1=0
                           Subtracting:                   0-0=0                  0-1=1                   1-0=1                  1-1=0

## SECTION 10.2           BLOCK CODING     271


     Notice particularly that addition and subtraction give the same results. In this arith-
metic we use the XOR (exclusive OR) operation for both addition and subtraction. The
result of an XOR operation is 0 if two bits are the same; the result is I if two bits are
different. Figure 10.4 shows this operation.


Figure 10.4 XORing of two single bits or two words


                                                               o
                                                                                      o    I    I   0
          a. Two bits are the same, the result is O.
                                                                            eB             I    0   °
          loeB1=1                                 leBO                           °         °        °
          b. Two bits are different, the result is 1.                   c. Result of XORing two patterns


Other Modulo Arithmetic
We also use, modulo-N arithmetic through the book. The principle is the same; we use
numbers between 0 and N - 1. If the modulus is not 2, addition and subtraction are distinct.
If we get a negative result, we add enough multiples of N to make it positive.


## 10.2      BLOCK CODING
In block coding, we divide our message into blocks, each of k bits, called datawords. We
add r redundant bits to each block to make the length n = k + r. The resulting n-bit blocks
are called codewords. How the extra r bits is chosen or calculated is something we will
discuss later. For the moment, it is important to know that we have a set of datawords,
each of size k, and a set of codewords, each of size of n. With k bits, we can create a com-
bination of 2k datawords; with n bits, we can create a combination of 2n codewords.
Since n > k, the number of possible codewords is larger than the number of possible data-
words. The block coding process is one-to-one; the same dataword is always encoded as
the same codeword. This means that we have 2n - 2k codewords that are not used. We
call these codewords invalid or illegal. Figure 10.5 shows the situation.


Figure 10.5 Datawords and codewords in block coding


                                 II      Hits    II Hits I •       eo     I Hits I   I
                                                2k Datawords, each of k bits


                       II      II bits     II       II bits                       nbits    II
                              2n Codewords, each of n bits (only 2k of them are valid)

272   CHAPTER 10   ERROR DETECTION AND CORRECTION


             Example 10.1
             The 4B/5B block coding discussed in Chapter 4 is a good example of this type of coding. In this
             coding scheme, k = 4 and n = 5. As we saw, we have 2k = 16 datawords and 2n = 32 codewords.
             We saw that 16 out of 32 codewords are used for message transfer and the rest are either used for
             other purposes or unused.

             Error Detection
             How can errors be detected by using block coding? If the following two conditions are
             met, the receiver can detect a change in the original codeword.
               1. The receiver has (or can find) a list of valid codewords.
               2. The original codeword has changed to an invalid one.
             Figure 10.6 shows the role of block coding in error detection.

             Figure 10.6 Process of error detection in block coding

                                       Sender                                                       Receiver
                                                    Encoder                             Decoder

                            k bits I D,at:aword 1                                                 I Dat~~ord·1 bits
                                                                                                                k


                                         I                                                             t   Extract

                                    I Generator I                                                 I Checker         Discard


                         n bits I
                                         +
                                     Codeword
                                                              Unreliable transmission
                                                                                                       i
                                                                                               r· Codeword           In bits
                                                    I                                          r


                   The sender creates codewords out of datawords by using a generator that applies the
              rules and procedures of encoding (discussed later). Each codeword sent to the receiver may
              change during transmission. If the received codeword is the same as one of the valid code-
              words, the word is accepted; the corresponding dataword is extracted for use. If the received
              codeword is not valid, it is discarded. However, if the codeword is corrupted during trans-
              mission but the received word still matches a valid codeword, the error remains undetected.
              This type of coding can detect only single errors. Two or more errors may remain undetected.

             Example 10.2
              Let us assume that k = 2 and n = 3. Table 10.1 shows the list of datawords and codewords. Later,
              we will see how to derive a codeword from a dataword.
                                     Table 10.1 A code for error detection (Example 10.2)

                                                Datawords                           Codewords
                                                        00                               000
                                                        01                               011
                                                        10                               101
                                                        11                               110

## SECTION 10.2           BLOCK CODING          273


     Assume the sender encodes the dataword 01 as 011 and sends it to the receiver. Consider the
following cases:
  1. The receiver receives OIl. It is a valid codeword. The receiver extracts the dataword 01
     from it.
 2. The codeword is corrupted during transmission, and 111 is received (the leftmost bit is cor-
    rupted). This is not a valid codeword and is discarded.
 3. The codeword is corrupted during transmission, and 000 is received (the right two bits are
    corrupted). This is a valid codeword. The receiver incorrectly extracts the dataword 00. Two
    corrupted bits have made the error undetectable.