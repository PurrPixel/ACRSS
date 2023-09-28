# ACRSS
AC Repair and Services System 1.0 - Unauthenticated Admin Account Takeover &amp; Privilege Escalation

[exploit](/acrss.jpg)

1. This uses python to directly send a request on the server page classes/Users.php?f=save
2. The function in the applicaiton is not checking for the source cookie and any request without cookie can be sent to change the password for admin user.
3. The script by default sets the password as "hacker@123"
