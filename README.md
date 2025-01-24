# FortiGate Belsen Group leak IP enricher

On January 14, 2025 a new [threat actor named Belsen Group leaked a full dump](https://www.fortinet.com/blog/psirt-blogs/analysis-of-threat-actor-data-posting) containing more that 15K IP addresses exposing compromised Fortinet FortiGate administrative interfaces with credentials and configuration files. The campaign is suspected to be occurred a few years ago by exploiting [CVE-2022–40684](https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2022-40684).

This script uses https://ip-api.com/ (free tier with rate limit) to enrich the IPs with autonomous system number, location, etc. to help security researchers assessing potential impacts on their perimeter. Due to the high volume of impacted assets, expect between eight to nine hours to complete the task.

Thanks to https://github.com/arsolutioner for providing the `affected_IPs.txt` dump.
