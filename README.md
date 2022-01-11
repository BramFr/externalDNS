# externalDNS
solution (alternative) for MindMeld Palo Alto

This wil resolve FQDN and save the result to a txt file. 
Use crontab for schedule
```crontab
*/5 * * * * root python /etc/tooling/externalDns.py > /dev/stdout
```

Exmaple result:
```bash
# cat /path/to/folder/www.google.com.txt
142.250.179.132
```