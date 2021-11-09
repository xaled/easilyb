# easilyb
Frequently used functions library for Python By Khalid Grandi (github.com/xaled).

## Installation
pip3 install easilyb

## Changelog
**version 0.27.0:**
- Rsync helper class
- terminal.ctext (color text)

**version 0.26.0:**
- Revert fixes in serialization

**version 0.25.0:**
- Map class in serialization
- Install new version after upload to pypi

**version 0.24.1:**
- making most requirements optional

**version 0.24.0:**
- delete_index in elastic

**version 0.23.0:**
- easilyb.crypto
- hits_search in elastic

**version 0.22.0:**
- added contains, remove and clear methods to SimpleCache (easily.cache)
- ElasticSearch key validation
- added search method to ElasticDB class for paginated search 
- ElasticType class for type simplified type mapping in ElasticSearch
- Fix bug in docker container stopping
- added private attribute to easilyb.net.ip classes
- added whois_ex1 method to easily.net.whois (netname extraction + dict result instead of tuple)


**version 0.21.0:**
- elastic instance (easilyb.databases.elastic) & some mongo changes

**version 0.20.0:**
- mongodb instance (easilyb.databases.mongo & easilyb.docker)

**version 0.19.0:**
- prompt and cprint functions (easilyb.terminal)

**version 0.18.0:**
- EasyConfig config path generation, 3 types:
    - Application root
    - User Config dir, Ex: `~/.config`
    - System config dir, Ex: `/etc/xdg/config`
    
**version 0.17.1:**
- deadlock fix in json_min_db 

**version 0.17.0:**
- IP address and IP pool classes `easilyb.net.ip.IP` & `easilyb.net.ip.Pool`.
