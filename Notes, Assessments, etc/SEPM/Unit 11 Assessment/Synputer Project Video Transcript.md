https://github.com/Wwaess/wwaess.github.io/tree/main/Notes%2C%20Assessments%2C%20etc/SEPM/Unit%2011%20Assessment for this transcript and the video presentation. 

To download the mp4 file to view, click on the mp4 file, then click on "View Raw" to download the video recording.

Synputer Progress Report

Hello. This presentation is a progress update on how far along development we are for the new Synputer, which should include responses to EDC's concerns regarding their feedback on the project. I'll briefly recap the original plan and show its current status, where EDC's specifications are and aren't met with this plan and with Colin Syn's February 1984 redesigned plan, and then walk through the revised timeline, costs and key trade-offs needed to keep the project as viable as possible. 

First here's a recap on where we are at the moment. To clarify: this first spiral from November last year to the end of January focused on checking for feasibility, so there's no physical build from that point until the end of January just to check that the components synergise well together. The second phase combines the hardware with the software development and identifying design issues if they arise before scaling up, and gives us the first integrated prototype towards late April. This last stage we're wrapping up since then is the one dedicated to iterative refinement of that prototype, including testing the full component stack, emulation software, EZ-Suite and configuring the ROMs so that they work.

Looking at this plan then, we're currently at the start of August '83 here, as per this purple line, and we've just moved beyond the early prototyping stages - which have been more or less finished by now - into the initial production-unit stage. So far, we've made a batch of 50 units for in-house operation and testing (which, if sales promise gratuitous results and we no longer have any need of them, we can sell as limited editions), we've sent 20 review units to EDC and a further set of 30 has been distributed to computer, electronics and business computing magazines. Incidentally, the marketing department has been rather effective at promoting those to the magazines, because we've attained 3000 preorders for the Synputer at a price of £400 each. 

It's believed that Syn's plan for a Synputer, including an evaluation model, was also sent to EDC at around this time, which is why we have the legal dispute with EDC here, which I'll address in a bit. 

Before addressing any revised design, firstly I'll briefly summarise the original plan as the baseline for comparison here. Here's the proposal that was initially agreed upon, following the transcript between Colin Syn and Will Burns, the CEO of EDC. 

This plan relies on an A83-S socketed board, with the idea being that this gives as much user-upgradeability as possible. For the CPU we're using the Motorola 68k. We have four 128 kB chips giving us 512 kB of RAM for the Synputer; for the ROM we've got an 8 kB one as the bootloader and a 32 kB one for the HB/OS operating system. All four ULA glues, as is standard for any computer; a mono-sound system; two serial ports; a joystick port; an SCSI expansion slot; a floppy-and-cartridge mix for the storage; and a desktop case combined with an external keyboard. 

As for software, this machine relies on the HyperBasic OS in the ROM and a HyperBasic interpreter, always available upon booting the machine up. Alongside we've added the EZ-Office Suite as a bundle to come with, which can create documents that can be exported into other formats such as MS-Word and WordStar and spreadsheets that can be exported into the Lotus 123 software. There are also some optional DOS-style tools for interoperability with IBM systems. 

Following on from this, starting from February 1984, Syn has updated the shipping specification — henceforth the "evaluation model" — as follows: 

For similarities, all four glue chips are there, we have the same desktop case idea here, we've got integrated sound, and one of the ROMs is a 32 kB one. It also uses the same operating system and software as the original does. For differences, there is quite a lot, for cost-saving reasons, I suspect - except for the other ROM slot, which houses another 32 kB. Beyond that, this uses a 68k8 chip instead of the 68k, four 32 kB RAM chips (and all of that is soldered on), and some differing IOP port selections. 

As can be seen, this redesign isn't really aimed at reducing the raw cost of materials, costing around 8 pounds more at £168.05, but instead it tries to optimise for manufacturing predictability by for instance using soldered RAM and using a 68k8 chip for simpler CPU integration. Though the material cost is more, I believe the aim here is to lower integration complexity and risk during early production stages; as we'll see later I'll have marked this other computer as needing to take less time, in part because of the shared amount of work done in the first spiral. 

However, EDC have threatened to sue after raising some concerns about the design, restating their requirements in order of importance: 
- an operating system that meets industry standards
- an external keyboard
- 512 kilobytes of RAM
- some industry-standard drive with removable media
- expansion options with SCSI
- at least a 68-thousand CPU
- at least 2 network serial ports
- and a board that can support a GUI and a mouse

They want some response to addressing these, so we'll go through the design specifications that currently exist and see whether these requirements have been met or if there are reasons why they may not be. 

The OS:
Both computers aim to use HyperBasic, our in-house operating system. It's a ROM-based operating system with an integrated BASIC environment, which ensures familiarity with the existing BASIC functions, and is largely industry-adjacent to the OSes used in the BBC Micro and the IBM microcomputers (BBC BASIC, n.d.; IBM, 2021). 

The external keyboard:
This is important for our client, and we initially considered that, assuming we could design a bespoke case for this, we'd be able to use that for this computer. We hadn't done so, on account of not having the figures to hand on how much developing such a case would cost, so we'd initially built on the assumption that we would use a desktop with a separate external keyboard to sell. And to manage the connectivity to the desktop we'd use one of the two existing 16550 UART ports (and I'll address that serial port issue later), as far as this design goes, this is conformant. 
The evaluation plan however has ditched the external keyboard in favour of the internal keyboard the desktop casing comes with, since it's still operable with it and saves on cost. A good compromise is to ship two versions - one without the external keyboard as per the evaluation plan, which can be sold as a standard model; and the one with the external keyboard, which can be sold under the EDC name. This allows a good balance of meeting EDC's requirements and getting Syn's design on the market too, and when possible this will be the main idea going forward. 

The RAM:
The original plan had 4 lots of 128 kB sticks of RAM, which meets this criterion; the evaluation plan has a board with 4 slots to place RAM in, but only has 32 kB sticks in them. Despite our initial plan having this pinned as a low Syn-Stakeholder priority, considering the high priority here, it's in our best interests to keep this original configuration so as to meet this bullet point. As for the 4-times-32 kB configuration, this would be better fitted into the standard version i.e. the base version, as the next possible lower RAM configuration.  

The removable media issue:
The original design uses a combination of cartridges and floppy disks. While the evaluation doesn't rely on floppy disks, the original can support both, and seeing as floppy disks are a common form of removable storage (Cohen, 2017), this fits the criterion. 

The SCSI: 
Both versions have this, so this is a non-issue. 

The CPU:
The original specification already had a 68k CPU which is socketed, though the evaluation plan changed it out for the 68k8 and soldered it to save on cost, although it is easier to work with, with existing 8-bit hardware designs. The original spec already meets the CPU requirement and the option to upgrade it, should it be needed. 

The networking ports:
Although the evaluation design only has the one serial port, the original design does have two of them. The case study unfortunately does not specify whether these ports meet the RS-422/485 standard required by EDC for network compatibility. However, as the boards we have already have two existing ports, it would be a straightforward modification to verify whether the IOP designs support this requirement or upgrade the transceivers in the ports if needed. 

GUI and mouse support: 
Considering the low priority of this, we haven't endeavoured as much to consider adding a GUI as standard, although in response to an increasing expectation to transition from a terminal-based interface to a graphical-based one (Kavinda, 2021), we are aiming to delve into some more research into this. The DOS-tools addon that Synful already has would be a viable way to meet this requirement, however. 


So, in all, we can meet EDC's requirements and reduce costs by splitting the Synputer into two separate specs, selling the higher end one under EDC's name. As you can see here, this is a summary of those changes, and as noted here, regarding the professional model under EDC, this one certainly surpasses the 80-percent threshold that EDC was asking for with regards to the compliance of their requirements. I will point out the only main change would be the swapping of the ROMs, so that the professional model has two lots of 32 kB, while the standard one has the 8kB bootloader ROM. 


To note, EDC have asked for a troubleshooting guide for their evaluation model, due to some minor crashes, so I'll briefly go over this here: 

The HyperBasic operating system has been known to crash whenever it can't log any data. To mitigate, check whether the writable media has been installed into the computer correctly and/or limit how much load the memory is having to handle. If neither of those work, as a last resort, disconnect and reconnect the OS cartridges to reset the OS. 

There are issues with multitasking causing the memory to run out. We recommend disabling any background services that aren't in use, and bearing in mind how many applications are running at the same time. 

We have also noticed that cartridge drives generally interfere with each other electromagnetically, the long and short of which is there are occasions where the machine will reset itself randomly. We note that other companies are also having these EMI problems (TME, 2025), so while our engineers investigate further into the cause of this, we recommend not to swap drives in and out while the machine is turned on, and to check that any peripherals plugged into the machine are properly grounded to prevent electrical noise from interfering. 

Lastly there's the possibility of configurations being lost when restarting the machine. We're working on some persistent storage for production units; for the time being we'll advise to document configurations for repeat testing and reapply these when restarting. 


Now regarding the machines' development, how does this affect the timeline on our production? 
Well, at present we're at the prototyping stage for the standard model, and while the production itself should not be severely delayed, I should note that due to some late-stage personnel management being needed we may expect some weeks' delay. In an ideal scenario we predict the plan for the EDC Professional models to be completed by the end of this year; the standard models should be completed by mid-January. There will need to be some statements for Marketing to make to explain the delay and while that might have some cost to it, such an act should have negligible direct financial cost to this project, so it hasn't been included in this calculation. We might be impacted reputationally and potential extra pre-orders may slow down, so the marketing team should ensure to justify the delay carefully and frame it as a quality-and-compliance decision more than a failure of delivery. 


Thanks for watching; references are in the transcript attached with this recording, and apologies for any mistranscriptions if there are any. 
Thank you. 

References:

BBC BASIC (n.d.) The Website Dedicated to the BBC BASIC Programming Language. Available at: https://www.bbcbasic.co.uk/bbcbasic.html [Accessed: 19th January 2026]

Cohen, P (2017) A History of Removable Computer Storage. Available at: https://www.backblaze.com/blog/history-removable-computer-storage/ [Accessed: 19th January 2026]

IBM (2021) BASIC Language Reference. Available at: https://www.ibm.com/docs/en/iis/11.5.0?topic=reference-basic-language [Accessed: 19th January 2026]

TME (2025) Electromagnetic Interference (EMI): Identification and Prevention Methods in Electronics. Available at: https://www.tme.eu/gb/news/library-articles/page/68660/electromagnetic-interference-emi-identification-and-prevention-methods-in-electronics/ [Accessed: 19th January 2026]

Kavinda, L. (2021) Interfaces in the 80s: Creating GUIs before it was cool. Accessible at: https://uxdesign.cc/creating-guis-before-it-was-cool-57473c96cd6b [Accessed: 19th January 2026]

