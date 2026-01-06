# Network Forensics: Meerkat Lab Analysis
An investigation into an IDS alert log to identify and document a web server compromise.

## 📌 Executive Summary
During this analysis, I investigated a series of Suricata alerts originating from a suspicious external IP. The investigation confirmed an exploitation attempt against a Bonitasoft instance using **CVE-2022-25237**. By correlating flow IDs and analyzing User-Agent strings, I successfully mapped the attacker's path from initial scanning to successful authorization bypass.

## 🛠️ Technical Workflow
1. **Identification**: Used `jq` to filter for Severity 1 alerts.
2. **Analysis**: Identified `python-requests` as the primary User-Agent for the attack delivery.
3. **Correlation**: Pivot-searched the `flow_id` to see the full HTTP request and response cycle.
4. **Conclusion**: Confirmed the exploit was successful based on the HTTP response codes and subsequent outbound traffic.

## 📊 Skills Demonstrated
* **Log Analysis**: Deep parsing of Suricata EVE JSON format.
* **Traffic Forensics**: Identifying malicious User-Agents and suspicious POST requests.
* **Tooling**: Mastery of `jq` for data reduction and evidence extraction.
