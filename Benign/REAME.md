## Benign
One of the client’s IDS indicated a potentially suspicious process execution indicating one of the hosts from the HR department was compromised. Some tools related to network information gathering / scheduled tasks were executed which confirmed the suspicion. Due to limited resources, we could only pull the process execution logs with Event ID: 4688 and ingested them into SPLUNK with the index win_eventlogs for further investigation.

About the Network Information

The network is divided into three logical segments. It will help in the investigation.

IT Department

* James
* Moin
* Katrina

HR department

* Haroon
* Chris
* Diana

Marketing department

* Bell
* Amelia
* Deepak  
Answer the questions below  
Q1:How many logs are ingested from the month of March, 2022?
```bash
13959
```
Filter the time range.
![image1](images/2026-06-30_16-50.png)
Q2:Imposter Alert: There seems to be an imposter account observed in the logs, what is the name of that user?
```bash
Amel1a
```
we will use this query to see all the users 
```bash
index= win_eventlogs 
| stats count by UserName
```
![image1](images/pic2.png)
Q3:Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host. 
```bash
Chris.fort
```
I used the following query
```bash
index= win_eventlogs schtasks 
|  stats count by UserName
```
and than we can see Chris.fort is the only user for HR department.
![image1](images/pic3.png)
Q4:Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host. 
```bash
haroon
```
LOLBIN is living off land binary that is used by attackers to avoid the external tools.Some famous are cmd.exe,Powershell.exe,certtuil.exe,Bitsadmin.exe.  
I just casully search for certutil.exe and there was only one log and that was accessing paste link from the website controlc.com and user was haroon.
![image1](images/pic4.png)

Q5:What was the date that this binary was executed by the infected host? format (YYYY-MM-DD)
```bash
2022-03-04
```
In the Same log we can see the date 
![image1](images/pic5.png)