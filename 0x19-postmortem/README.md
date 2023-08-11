## Postmortem: Server Breakdown due to Prolonged Garbage Cleanup Neglect
Date: 9th August, 2023

By the DevOps Team

### Issue Summary
From 7:00 PM to 8:00 PM WAT, all requests to our applcation and database server resulted in 500 error responses.
At its peak, the issue affected 100% of traffic to the website. Users continue to access static infos on the website.
The root cause is the prolonged accumulation of garbage on the server, leading to performance degradation and eventual system failure

### Timeline (all times West African Time)
* 7:00 PM: Performance degradation begins
* 7:28 PM: Outage begins
* 7:28 PM: Pager alerted teams
* 7:30 PM: Users report application timeouts
* 7:32 PM: Initial investigation reveals abnormally high memory usage
* 7:32 PM: Server restart attempted
* 7:35 PM: Server restart led to temporary relief but memory leak issue persisted
* 7:35 PM: Escalation to Senior engineers for more comprehensive analysis
* 7:55 PM: Patch for the memory leak was developed and tested in a controlled environment
* 7:57 PM: Patch was deployed and executed on the affected servers
* 7:59 PM: Patch executes successfully
* 8:00 PM: 100% traffic back online

### Root Cause
At 7:00 PM, a configuration change in the garbage cleanup tool was inadvertently release to our production environment without being tested first.The change exposed a bug in the cleanup tool causing the accumulation of unreclaimed memory blocks. Over time, this led to excessive memory fragmentation and increased consumption, ultimately leading to performance degradation and server failure

### Resolution and recovery
At 7:28 PM, the monitoring system alerted our engineers who investgated and quickly escalated the issue. By 7:45 PM, the incident response team identfied the bug in the cleanup tool and develop a patch to mitigate it.

At 7:55 PM, the patch was completely developed and succesfully tested in a controlled enviromment. At 7:57 PM, the patch was deployed and executed succesfully  on the affected servers solving the bug by 7:59 PM.

After a server restart, 100% traffic was restored by 8:00 PM.

### Corrective and Preventative Measures
in the last few hours, we've conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improved response times:
* Redesign of the garbage cleanup tool to improve it effectiveness and efficiency
* Implement a recurring garbage collection schedule to prevent memory leaks and fragementation
* Enhance monitoring and alerting systems to notify administrators of abnormal resource usage.
* Conduct thorough code reviews and testing to identify and address memory leak vulnerabilities.
* Develop and enforce best practices for memory management across the development team.
* Establish a knowledge sharing session to educate the team about the impact of neglecting garbage cleanup and the importance of regular maintenance.
The team is committed to ontinually and quickly improving our technology and operational processes to prevent outages. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support.

Sincerely,

The DevOps team
