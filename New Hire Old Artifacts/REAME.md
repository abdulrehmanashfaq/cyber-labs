## New Hire Old Artifacts
Investigate the intrusion attack using Splunk.
![image1](images/task2.png)


__Scenario__: You are a SOC Analyst for an MSSP(managed Security Service Provider) company called TryNotHackMe.  
A newly acquired customer (Widget LLC) was recently onboarded with the managed Splunk service. The sensor is live, and all the endpoint events are now visible on TryNotHackMe's end. Widget LLC has some concerns with the endpoints in the Finance Dept, especially an endpoint for a recently hired Financial Analyst. The concern is that there was a period (December 2021) when the endpoint security product was turned off, but an official investigation was never conducted. 
Your manager has tasked you to sift through the events of Widget LLC's Splunks instance to see if there is anything that the customer needs to be alerted on.   

Happy Hunting!
### Answer the questions below
##### Q1:A Web Browser Password Viewer executed on the infected machine. What is the name of the binary? Enter the full path. 
```bash
C:\Users\FINANC~1\AppData\Local\Temp\11111.exe
```
For this i first look for ``EventId 1`` and check the count of images based on it.
So there was a binary ``11111.exe`` with most hit and its name was also very odd.So I started to analyze its activity.
![image1](images/pic2.png)
So For this we filter for Event id 1 again and look at this binary commandline ParentCommandline.
In the following image we can see this binary is steeling web cookies.
![image1](images/pic3.png)
##### Q2:What is listed as the company name?
```bash
NirSoft
```
For this i look for the events with keyword ``11111.exe`` and open the the first event and found the company name.
![image4](images/pic4.png)
##### Q3:Another suspicious binary running from the same folder was executed on the workstation. What was the name of the binary? What is listed as its original filename? (format: file.xyz,file.xyz)
```bash
IonicLarge.exe,PalitExplorer.exe
```
For this we need to need our current directory to be ``C:\\Users\\Finance01\\AppData\\Local\\Temp\\`` and look for Images.
![image5](images/pic5.png)
From this we can look that IonicLarge.exe is a supicious binary.
For orignal file name we go for raw events and on right side panel look for the orignal file name.
![image6](images/pic6.png)