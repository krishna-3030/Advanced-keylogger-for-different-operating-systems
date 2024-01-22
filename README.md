# Advanced-keylogger-for-different-operating-systems
ABSTRACT
In the dynamic landscape of the digital era, marked by scarcity of time and resources, the significance of efficient management has surged. With technology ingrained in all aspects of our lives, optimizing productivity and comprehending our digital conduct have emerged as paramount concerns. This project seeks to address this imperative through the introduction of an inconspicuous key-logger—a discreet software solution engineered to capture keyboard inputs on specified systems. This innovation holds the potential to provide personalized typing insights, elevate productivity, and offer comprehensive activity analysis, catering to both personal and professional spheres. Amidst today's demand for heightened efficiency, the concept of the unobtrusive key-logger takes root, offering a subtle data collection approach. It silently captures keyboard interactions on designated systems, aspiring to empower users with personalized insights that extend beyond data collection. The goal is to enhance productivity and refine workflow management. This project's objective is to delve comprehensively into the features and ramifications of the unobtrusive key-logger. In an era where digital connectivity blurs the boundaries between work and personal life, optimizing digital behavior becomes a potent tool. This software facilitates pattern identification, task streamlining, and effective time allocation, contributing to a balanced work-life equilibrium.
Functioning discreetly, the unobtrusive key-logger preserves ongoing tasks by capturing keyboard inputs subtly, imperative in the fast-paced digital realm. Central to its functionality is meticulous data compilation, analyzing typing patterns to offer insights into speed, common keystrokes, and avenues for improvement. These insights empower users to identify time-saving methods, optimize shortcuts, and refine task efficiency. Moreover, ethical considerations inherent in such technology are recognized within this project. Responsible usage mandates transparency and user consent, ensuring that the captured data serves self-improvement rather than invasive surveillance. This report embarks on exploring the potential of the unobtrusive key-logger to enhance productivity and activity analysis. Through an evaluation of its attributes, applications, and ethical dimensions, it seeks to illuminate the intricate interaction between technology and human behaviour. By grasping the capabilities and limitations of this software, the goal is to contribute to a nuanced discussion on its responsible integration in an efficiency-driven digital era characterized by effective resource management.

CHAPTER 1
INTRODUCTION
In the rapidly evolving landscape of the digital age, where time and resources are at a premium, the importance of effective management has never been greater. With technology permeating every facet of our lives, the need to optimize our productivity and better understand our digital behavior has become a central concern. This project endeavors to address this imperative by introducing an unobtrusive key-logger, a discreet software solution designed to capture keyboard inputs on targeted systems. This innovation holds the promise of delivering personalized typing insights, enhancing productivity, and providing comprehensive activity analysis for users across personal and professional domains.
The contemporary world demands a new level of efficiency and effectiveness, and it is within this context that the concept of the unobtrusive key-logger takes root. This software offers a subtle approach to data collection, allowing for the silent capture of keyboard interactions on designated systems. Its primary goal is to furnish users with insights that transcend mere data collection; rather, it seeks to empower users with personalized insights, thus contributing to heightened productivity and improved workflow management.
The objective of this project is to delve deeper into the features and implications of the unobtrusive key-logger. In an era where the lines between work and personal life are increasingly blurred by digital connectivity, the ability to harness one's digital behavior for optimization emerges as a potent tool. Through this software, users can uncover patterns, streamline tasks, and achieve a balanced allocation of time, ultimately leading to an improved work-life equilibrium.
The unobtrusive key-logger holds multifaceted potential. It operates discreetly, ensuring minimal intrusion into the user's system, thereby preserving the integrity of ongoing tasks. By capturing keyboard inputs subtly, it facilitates uninterrupted activities, a feature crucial in the fast-paced digital landscape.
At the core of this software lies its capacity for meticulous data compilation. By analyzing users' typing patterns, it provides insights into typing speed, common keystrokes.

CHAPTER 2
LITERATURE SURVEY
2.1 OVERVIEW
[1] “Stefano, Cristiano Giuffrida (2011) at el. KLIMAX: Profiling Memory Write Patterns to Detect Keystroke-Harvesting Malware”
The paper "KLIMAX: Profiling Memory Write Patterns to Detect Keystroke-Harvesting Malware" by Stefano et al. introduces an innovative technique for detecting keystroke-harvesting malware through analyzing memory write patterns. By monitoring memory write activities and training a machine learning model to distinguish between normal and malicious behaviors, the approach offers a promising solution to identify covert keystroke-harvesting attacks. The paper's contributions include the concept of memory write pattern profiling, the development of a machine learning model, successful experimental results with real-world malware samples, and implications for enhancing cybersecurity against such threats.
[2] “R Sreeram Sreenivas, Dr R Anitha. (2011). Detecting key-loggers based on traffic analysis with periodic Behaviour”
The study by Anith et al. (2011) proposes a method for detecting key-loggers through traffic analysis using periodic behavior. By analyzing network traffic patterns, the approach aims to identify the presence of key-loggers, which are malicious software designed to capture keystrokes. The authors' method involves detecting consistent periodic patterns in network traffic that might indicate the transmission of captured keystrokes. This technique provides a potential means of identifying key-loggers by focusing on the unique behavioral characteristics of their network communication.
[3] “J. Fu , Yiwen Liang , Chengyu Tanat el. (2010). Detecting Software Key-loggers with Dendrite Cell Algorithm”
In the paper "Detecting Software Keyloggers with Dendritic Cell Algorithm" by J. Fu et al. (2010), a novel approach using the Dendritic Cell Algorithm (DCA) is presented for the detection of software key-loggers, which are malicious programs that record users' keystrokes. The DCA, inspired by the immune system's behavior, is employed to distinguish between normal and anomalous keyboard input patterns, effectively identifying key-loggers. The paper's contribution lies in its utilization of the DCA's adaptive and pattern recognition capabilities, demonstrating its potential as a mechanism to enhance cybersecurity by accurately detecting software key-loggers through a unique immune-inspired approach.
[4] “Parth Mananbhai Patel, Prof. Vivek K.ShahParth (2015) Analysis and Implementation of Decipherments of KeyLogger.”
The research paper titled "Analysis and Implementation of Decipherments of KeyLogger" explores the detection of keyloggers, software tools used to monitor and record keystrokes, often for malicious purposes. The paper proposes a new detection technique that operates in an unprivileged environment, allowing it to identify keyloggers running in user space. This approach relies on a black-box model that correlates input (keystrokes) with output (I/O patterns) to detect keyloggers without needing to understand their internal workings. The methodology includes components like an injector, monitor, pattern translator, detector, and pattern generator. The evaluation of the technique demonstrates its effectiveness in detecting real-world keyloggers with no false positives or negatives. Overall, the research presents a practical and unprivileged approach to keylogger detection, offering potential solutions to safeguard against these privacy-breaching tools.
2.2 OBJECTIVE
•	Develop a sophisticated and discreet key-logger software with a strong focus on minimizing resource utilization. 
•	Design the software to operate covertly, capturing and recording keyboard inputs on a designated system without interrupting ongoing tasks.
•	Enable the software to compile and log data pertaining to keyboard inputs, enabling users to gain insights into their typing speed, commonly used keystrokes, and potential areas for improvement.
•	Implement a webhook system to enable real-time communication between different web services and applications. 

2.3 MOTIVATION
The driving force behind stems from the limitations encountered with conventional keyloggers that utilized SMTP for data transmission. Such approaches raised security concerns and triggered alerts, impeding their effectiveness. In response, to employ webhooks as an alternative, sidestepping these issues. By embracing webhooks, we aim to establish secure, real-time connections between systems, ensuring efficient and discreet data transmission without relying on email-based mechanisms. This motivation underscores our commitment to innovating a more secure and reliable approach to keylogging, addressing previous shortcomings head-on.
By transitioning away from SMTP-based methods, we are determined to overcome the hurdles that hindered previous keyloggers. The core objective is to develop a sophisticated solution that captures keyboard inputs seamlessly while prioritizing security and privacy. Embracing webhooks not only promises to enhance the keylogger's functionality but also positions us at the forefront of responsible and efficient data transmission in the realm of digital security.

CHAPTER 3
HIGH LEVEL DESIGN
3.1 EXISTING SYSTEM
 


The existing system as shown in Fig 3.0 of key-loggers refers to the range of software applications designed to secretly record and monitor keyboard inputs on a target system. These key-loggers can be broadly categorized into two types: hardware-based and software-based. Hardware key-loggers are physical devices attached to a computer's keyboard or USB port, while software key-loggers are programs installed on a system, either with or without the user's knowledge.
Software key-loggers can be further classified based on their installation methods: user-mode key-loggers and kernel-mode key-loggers. User-mode key-loggers operate within the application layer of an operating system and have limited access to sensitive system as shown in Fig 3.0 functions. Kernel-mode key-loggers, on the other hand, operate at a deeper level within the operating system's kernel, granting them more comprehensive access and making them harder to detect.
Keyloggers have diverse applications, including legitimate purposes like monitoring employee activity and parental control, but they are also employed maliciously for unauthorized data collection, identity theft, and cyber espionage. Detection methods for key-loggers range from antivirus software and intrusion detection systems to more advanced techniques like behavioural analysis and dynamic taint analysis.
The presence of key-loggers raises significant privacy and security concerns, as they can capture sensitive information like passwords, credit card details, and personal communications. As a result, the development of countermeasures and detection strategies is crucial to mitigate the risks posed by these tools and protect users from potential misuse.
3.2 PROPOSED SYSTEM 
 


The proposed system as shown in Fig 3.1 aims to create an advanced and covert key-logger software with minimal resource consumption, intended to silently record and log keyboard inputs on a designated system. This key-logger's primary focus is not on malicious intent, but rather on providing users with insights as shown in Fig 3.1 into their own typing behaviors to enhance personal productivity. The key-logger is designed to operate undetectable, capturing keyboard input patterns without causing noticeable system performance issues or alerting the user. By offering a detailed analysis of users' typing activities, the proposed system as shown in Fig 3.1 aims to empower individuals to identify typing patterns, improve efficiency, and enhance their overall productivity while maintaining a non-intrusive approach.


3.3 SYSTEM REQUIREMENTS
These are the following Hardware and software requirements for the system 
3.3.1 HARDWARE REQUIREMENTS
•	Intel core or AMD systems.
3.3.2 SOFTWARE REQUIREMENTS
•	Windows 
•	Linux 
•	Mac Operating System 

3.4 SYSTEM ARCHITECTURE
                         


The system architecture as shown in Fig 3.2  of the proposed key-logger software comprises several interconnected components that work cohesively to achieve its objectives. At its core, the architecture as shown in Fig 3.2  includes a keyboard input capture module responsible for intercepting and logging user keystrokes in real-time. This module is designed to operate stealthily within the target system, ensuring minimal impact on system resources and user experience. The captured input is then directed to a data storage component, which organizes and stores the logged keystrokes securely. To enhance the user experience, an analysis module processes the collected data to provide insights into typing patterns and behaviours , enabling users to understand their productivity habits better. The as shown in Fig 3.2  architecture as shown in Fig 3.2  also incorporates an efficient communication module that facilitates data transfer, enabling users to access the recorded information remotely if desired. The system's layered and interconnected architecture as shown in Fig 3.2 ensures seamless operation, minimal resource consumption, and a user-friendly approach that prioritizes valuable insights into typing patterns for personal productivity enhancement.

CHAPTER 4
IMPLEMENTATION 
Keyboard Input Capture:
1.	Used Python libraries like `pynput` to capture keyboard input.
2.	Created a listener to intercept key presses and releases.
3.	Stored the captured keystrokes in memory for later processing.
Webhook Integration:
1.	Utilized the `requests` library to send captured data to a remote server via a webhook
2.	 Set up a webhook endpoint to receive data on the remote server.
Data Transmission:
1.	Converted the captured keystrokes to a suitable format (e.g., JSON) before sending.
2.	Sent the data to the remote server using HTTP POST requests with the `requests` library.
3.	Implemented error handling and retries for robust data transmission.
Security Measures:
1.	Implemented basic encryption for the data sent to the remote server.
2.	Used HTTPS to ensure secure communication between the keylogger and the server.
3.	Implemented server-side security measures to protect the received data.
Remote Access and Analysis:
1.	On the remote server, processed and stored received data in a secure manner.
2.	 Analysed the captured keystrokes to extract typing patterns and behaviors.
3.	Provided a web-based dashboard for users to visualize and analyze their typing patterns.
User Interface:
1.	Developed a simple command-line interface for users to start and stop the keylogger.
2.	 Allowed users to specify the remote server's webhook URL and other settings.


CHAPTER 5
EXPERIMENTAL RESULTS
5.1. Event Listener Approach:
In the experiment, a key-logger was designed to utilize event listeners to capture keyboard events. By registering itself with the operating system, the key-logger was able to receive notifications whenever a key was pressed or released. This approach, commonly found in legitimate productivity tools, allowed the key-logger to intercept keyboard input effectively. The event listener mechanism proved efficient in capturing keystrokes without significantly affecting system performance or causing noticeable delays.
5.2. Time-stamping for Typing Patterns:
As part of the experiment, the keylogger implemented a timestamping feature alongside key capturing. This additional layer recorded not only the keys pressed but also the timestamps of each event. This timestamp data was intended to facilitate the analysis of typing patterns, typing speed, and intervals between keystrokes. By associating time information with keystrokes, the keylogger aimed to provide insights into users' typing behaviours, potentially offering valuable information for enhancing personal productivity.
5.3. Webhook Integration for Real-Time Communication:
The experiment involved integrating web-hooks to establish real-time communication between the key-logger and an external system. Web-hooks enabled automatic data transfer through a predefined URL or endpoint. By utilizing web-hooks, the key-logger could securely transmit captured data to another application or server, facilitating remote data analysis and storage. This integration showcased the potential of web-hooks to enhance data exchange and enable seamless communication between different components.
5.4. Browser Data Retrieval:
The experimental setup also explored the retrieval of browser data as part of the keylogger's functionality. Specifically, the experiment aimed to determine the browser from which historical data, such as browsing history, would be retrieved. Different browsers store their history using distinct file formats or databases. This feature highlighted the keylogger's adaptability to various browser environments, potentially broadening its applicability and usability for users seeking comprehensive data insights.
Overall, the experiment successfully demonstrated the capabilities of the developed keylogger software. The utilization of event listeners, timestamping, webhook integration, and browser data retrieval collectively contributed to the software's potential for silently recording keyboard input, analysing typing patterns, and enhancing personal productivity through detailed activity analysis.

 
Fig 5.1 Discord Interface

Fig 5.3 Data on Discord server
CONCLUSION
The keylogger project has successfully demonstrated the creation of a powerful tool capable of discreetly recording keyboard input. Throughout the development process, we prioritized user privacy and ethical considerations, ensuring that the application is used responsibly and with explicit consent. The project showcases the importance of understanding potential risks and adhering to legal guidelines while exploring the capabilities of such software. Moving forward, this knowledge can be utilized to build more secure and privacy-conscious applications, fostering a positive impact on the field of cybersecurity and digital privacy.


REFERENCES
[1]. “Stefano, Cristiano Giuffrida (2011) at el. KLIMAX: Profiling Memory Write Patterns to Detect Keystroke-Harvesting Malware”
[2]. “R Sreeram Sreenivas, Dr R Anitha. (2011). Detecting key-loggers based on traffic analysis with periodic Behaviour”
[3]. “J. Fu , Yiwen Liang , Chengyu Tanat el. (2010). Detecting Software Key-loggers with Dendrite Cell Algorithm”
[4]. “Parth Mananbhai Patel, Prof. Vivek K.ShahParth (2015) Analysis and Implementation of Decipherments of KeyLogger.”
