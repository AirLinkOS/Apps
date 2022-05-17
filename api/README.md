# Rest API Sample App

Files:
- Dockerfile: Installs requires packages and copies files into container image
- init.sh: Runs api.py
- api.py: Reads a configuration file in volume and uses the REST API to get and set datastore values
- data.json: Configuration file read by api.py. Must be uploaded as volume with mount point /config

Setup instructions:
1. Upload container image to UI (Apps -> Container Applications -> Images)
2. Upload tar or tar.gz containing data.json as a container volume (Apps -> Container Applications -> Volumes)
   and make sure to use mount point /config
3. Create a user with credentials defined in api.py variables AOS_USER and AOS_PWD, required for REST API use
4. Create container application (Apps -> Container Applications -> Status)
   with uploaded container image and volume, command /init.sh,
   and make sure auto assignment is enabled

Note: If another bridge other than Default-LAN is desired, change the container's bridge
in Hardware Interfaces -> General -> Configuration. The container IP address can be found
in Networking -> General -> DHCP Reservation (Fixed IP Assignments).
