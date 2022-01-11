# externalDNS
solution (alternative) for MindMeld Palo Alto

This wil resolve FQDN and save the result to a txt file. Use savedir parameter for saving the file to webserver folder.
For multple DNS entry`s create a new dns line.

Example multple DNS conf:
```
dns=www.google.com
dns=www.nu.nl
savedir=/path/to/folder
```

Use crontab for schedule
```crontab
*/5 * * * * root python /etc/tooling/externalDns.py > /dev/stdout
```

Exmaple result:
```bash
# cat /path/to/folder/www.google.com.txt
142.250.179.132
```
