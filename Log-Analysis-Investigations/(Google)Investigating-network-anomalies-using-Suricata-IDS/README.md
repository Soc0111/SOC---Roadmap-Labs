# Investigating network anomalies using Suricata IDS

### 🎯 Purpose of the work

## Configuring an intrusion detection system (IDS) to identify specific HTTP requests and analyze the resulting logs in Fast Log and EVE JSON formats.

🛠 Environment

Tool: Suricata IDS.

Data analysis: jq, awk, cat utilities.

Input data: sample.pcap network capture file.

📝 Description of custom rule

I analyzed the rule for searching HTTP GET requests:
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:“GET on wire”; content:“GET”; http_method; sid:12345;)

🚀 Execution process

Launching analysis: Traffic processing was performed using the suricata -r sample.pcap command.

Initial analysis: Fast.log confirmed that the rule was triggered on outgoing traffic.

Deep analysis (Forensics):

The jq utility was used to parse eve.json.

Filtering by flow_id was implemented, which allowed us to reconstruct the complete chain of actions of the attacked host.

📊 Results

Several suspicious sessions to IP 142.250.1.139 were detected. Thanks to flow_id analysis, we were able to link alerts to specific network flows, which is critical for further investigation (Incident Response).

✅ Conclusions

Working with EVE JSON via jq is a more effective method for SOC analysts than reading simple logs, as it allows them to automate the search for relationships between events.

Translated with DeepL.com (free version)
