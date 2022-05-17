# Ping Sample App

Files:
- Dockerfile: Installs requires packages and copies files into container image
- init.sh: Starts the telnet daemon and runs ping.py
- ping.py: Periodically sends pings to a hard-coded IP address

Setup instructions:
1. Upload container image to UI (Apps -> Container Applications -> Images)
2. Create container application (Apps -> Container Applications -> Status)
   with uploaded container image and volume, command /init.sh,
   and make sure auto assignment is enabled

Note: If another bridge other than Default-LAN is desired, change the container's bridge
in Hardware Interfaces -> General -> Configuration. The container IP address can be found
in Networking -> General -> DHCP Reservation (Fixed IP Assignments).
