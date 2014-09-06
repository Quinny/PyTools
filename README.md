PyTools
=======

One day I got sick of all the added bloat that accompanied some of the tools I used on a semi-regular basis.  I decided that instead of just putting up with it, I would write my own command line versions without the bloat.


Dependancies
--------------------
Although most of the modules used come pre-installed with python, I will still list them here

* optparse
* python-nmap
* Image
* pygeoip
* pyPdf
* zipfile

Most (if not all) of these should be available using 

```
pip-install <module>
```

Usages
=======

First of all, clone the repo and add it to your PATH variable

checkport
-------------

Checks the status of the given port(s) on the host machine.

```
checkport -H <host address> -p <port>
```

OR

```
checkport -H <host address> -p <start port>:<end port>
```

For checking a range of ports

imageanalyze
-------------------

Reads the exif data from the given image file

```
imageanalyze -f <image file>
```

I woud suggest redirecting the ouput of this one to a text file as the output can get long/wonky depending on the file

```
imageanalyze -f <image file> > output.txt
```

iplocate
----------

Finds an approximate location for the given IP Address or file of IP Addresses

```
iplocate -a <ip address>
```

OR 

```
iplocate -f <filename>
```

where ```<filename>``` contains a list of IP Addresses separated by newlines

pdfanalyze
--------------
Reads the meta data from the given PDF file

```
pdfanalyze -f <filename>
```

zipcrack
-----------
Attempts to open a password protected zip file using the top 10,000 most commonly used passwords found at [xato.net](https://xato.net/passwords/more-top-worst-passwords/#.VAomI2RdVyF)

```
zipcrack -f <zip file>
```

OR with an option passwordfile argument to overwrite the default one

```
zipcrack -f <zip file> --pf <password file>
```

More tools to come...
-----------------------------

