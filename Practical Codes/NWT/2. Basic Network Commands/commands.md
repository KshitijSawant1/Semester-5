### **Basic Networking Commands: Windows vs macOS/Linux**

| **Purpose / Task**                  | **Windows Command**                      | **macOS / Linux Command**                                                                                       |
| ----------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Show IP configuration**           | `ipconfig`                               | `ifconfig` *(or)* `ip addr show`                                                                                |
| **Test connectivity to a host**     | `ping <hostname/IP>`                     | `ping <hostname/IP>`                                                                                            |
| **Trace route to a host**           | `tracert <hostname/IP>`                  | `traceroute <hostname/IP>`                                                                                      |
| **Display routing table**           | `route print`                            | `netstat -r` *(or)* `ip route show`                                                                             |
| **Check open ports & connections**  | `netstat -an`                            | `netstat -tuln` *(or)* `ss -tuln`                                                                               |
| **Check current hostname**          | `hostname`                               | `hostname`                                                                                                      |
| **Change hostname**                 | `hostname <newname>` *(temporary)*       | `sudo hostname <newname>` *(temporary)*                                                                         |
| **Test name resolution**            | `nslookup <domain>`                      | `nslookup <domain>` *(or)* `dig <domain>`                                                                       |
| **Check network statistics**        | `netstat -e`                             | `netstat -i`                                                                                                    |
| **Show ARP cache (MAC table)**      | `arp -a`                                 | `arp -a`                                                                                                        |
| **Show active users / sessions**    | `net session`                            | `who` *(or)* `w`                                                                                                |
| **Display Wi-Fi networks**          | `netsh wlan show networks`               | `airport -s` *(macOS)* / `nmcli dev wifi` *(Linux)*                                                             |
| **Verify domain name resolution**   | `nslookup google.com`                    | `dig google.com` *(or)* `host google.com`                                                                       |
| **Renew / Release IP (DHCP)**       | `ipconfig /release`<br>`ipconfig /renew` | `sudo dhclient -r`<br>`sudo dhclient`                                                                           |
| **Show default gateway & DNS**      | `ipconfig /all`                          | `cat /etc/resolv.conf`                                                                                          |
| **Display DNS cache**               | `ipconfig /displaydns`                   | `sudo killall -INFO mDNSResponder` *(macOS)*                                                                    |
| **Flush DNS cache**                 | `ipconfig /flushdns`                     | `sudo dscacheutil -flushcache` *(macOS)*                                                                        |
| **Show firewall status**            | `netsh advfirewall show allprofiles`     | `sudo ufw status` *(Linux)* / `sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate` *(macOS)* |
| **Check current route to internet** | `tracert 8.8.8.8`                        | `traceroute 8.8.8.8`                                                                                            |
| **View listening network services** | `netstat -ab`                            | `sudo lsof -i -P -n`                                                                                            |
