# Postmortem: Load balance routing failure

####Issue Summary

Duration:

The issue was on July 15, 10:00 PM lasted for 2 hours until resolved by 12:00 AM (UTC).

Impact:

The site became relatively slow and the load routing was pointing to only one web server which causes a single point of failure(SPOF) vulnerability.


####Root Cause:
Misconfiguration on the DNS setting the main record was pointing to a non-existing IP address of a web server.

####Timeline:
10:00 PM - Issue was detected when testing site for traffic handling, the load balancer was redirecting all traffic to the secondary web server.

10:10 PM - Started to debug config files of the primary web server and the load balancer which was the main area of suspicion .

10:30 PM - A misleading path of resetting configuration files for all servers took place.


11:00 PM - After checking config files it turned out that both web servers configuration. was identical and they're both configured properly to the load balancer.

11:20 PM - The incident escalated to a teammate software engineer who found that it was a DNS record pointing to non-existing server IP.

11:45 PM - went to the DNS setting of the Hosting service and changed the record to point to the correct IP address of the primary web server.


12:00 AM - Issue resolved and the site was back to normality with load balancer distributing the traffic using round-robin technique.

####Root Cause and Resolution

The user noticed slightly slow rendering while the engineer was testing the site for traffic. In fact that didn't seem like a very abnormal condition due to the traffic applied to the site wasn't. serious enough to cause an outage. However after testing both web servers individually it turned out that the primary web server is not handling any load from the load balancer.

After a long misleading process of debugging configuration files of the servers the configuration for both web servers was identical and configured properly to the load balancer.

Hopefully after checking out the DNS setting of the host service it turned out that the root cause is the DNS record. was pointing to invalid IP address.

The issue was resolved instantly by visiting the Hosting provider site then clicking on "DNS setting" and changing the â"A" record to point to the IP address of the primary web server.

The load balancer returned to distribute load between the two servers using "round-robin" as the normal behavior.


####Corrective and Preventative measures

Things to improve:

A monitoring service must be added to the both web servers.
Automate the. load balancer and web server configuration and make sure it's up to date with the DNS records if a new web server is applied.
Write a good documentation.
Tasks List:

1- Add load balancer monitoring alerts, to monitor the load routing of the load balancing method us.

2- Patch load balancer configuration and make sure it's up to date with the web servers connected to the load balancer.

3- Make sure that all DNS records are pointing to the correct IP addresses.

4- Review in team the load balancing method used and change it if needed.
