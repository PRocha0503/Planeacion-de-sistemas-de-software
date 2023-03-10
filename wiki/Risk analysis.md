# Risk analysis

Created: March 9, 2023 7:49 PM
Last edited time: March 9, 2023 8:53 PM
Tags: document

| Risk No. | Description | Mitigation Action | Owner | Probability | Impact |
| --- | --- | --- | --- | --- | --- |
| 1 | SQL Injection | By using AWS WAF be will reduce the possiblilty of SQL injection attacks by filtering traffic at the appliaction layer. |  | High | High |
| 2 | Access to unauthorized information.  |  |  |  |  |
| 3 | DoS Attack:
Malicious attempt to overwhelm a service by flooding it with traffic. | Use AWS WAF to block IPS that are flooding the system. |  | Low | Medium |
| 4 | Man-in-the-middle attacks |  |  |  |  |
| 5 | Web Scraping
It is considered a cyberattack when web scraping involves extracting data without permission. In the case of malicious intent, web scraping can put personal information and intellectual property at risk. | Adding reCaptcha en important places of the application. |  | Medium | Low |
| 7 | Due that the users are able to upload their documents, it could occur that an attacker could upload malware that could affect both the functionality and user privacy. |  |  |  |  |
| 8 | Brute Force
A brute-force attack is a continuous attempt to guess login credentials and gain access to the protected areas of the application. | Block an account after X amount of attempts to login. |  | Medium | High |
| 10 | Database corruption/loss | Daily Backup to recover up to date data. |  | Low | High |