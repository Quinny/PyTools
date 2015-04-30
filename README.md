PyTools
=======

One day I got sick of all the added bloat that accompanied some of the tools I used on a semi-regular basis.  I decided that instead of just putting up with it, I would write my own command line versions without the bloat.


Dependancies
--------------------
Although most of the modules used come pre-installed with python, I will still list them here

* optparse
* BeautifulSoup4
* python-nmap
* Image
* pygeoip
* pyPdf
* zipfile
* datetime

Most (if not all) of these should be available using 

```
easy_install <module>
```

Usages
=======

First of all, clone the repo and add it to your PATH variable

cb
------------

Copies entire files to the clipboard

```
cb <filename>
```

checkport
-------------

Checks the status of the given port(s) on the host machine.

```
checkport <host address>:<port>[-<endport>]
```

eulerq
---------

Grabs the name and a creates a file for a given project euler problem number

```
eulerq <problem number> [extension]
```

fitsin
----------

Checks if a given number (or python friendly expression) will fit in the builtin integral types (int or long).

```
fitsin <number | expression>
```

grabimages
-----------

Downloads all images found within ```<img>``` tags on a given web page

```
grabimages <url>
```

The images will be downloaded into the current working directory



imageanalyze
-------------------

Reads the exif data from the given image file

```
imageanalyze <image file>
```

I woud suggest redirecting the ouput of this one to a text file as the output can get long/wonky depending on the file

```
imageanalyze <image file> > output.txt
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

jpost
--------

Automatically creates properly formated jekyll post markdown files in the current working directory

```
jpost "Hello World"
```

lines
-------

Counts the number of lines of code of given extensions

```
lines extension[ extension]*
```

myip
-----

Displays both your local and public IP address

```
myip
```

pdfanalyze
--------------
Reads the meta data from the given PDF file

```
pdfanalyze <filename>
```

prime
--------------

Checks the primality of a given number

```
prime <number>
```

serve
------------------

Creates a local, light weight web server that serves out of your current working directory on port 8000.

```
serve
```

textemp
---------------
Creates a latex template file based on the contents of resources/textemplate.tex.  The contents will be copied into the specified file.

```
textemp -o <output file>
```

OR with an option for an editor command to be run immediately after the template is generated

```
textemp -o <output file> -e <editor command>
```

For example:

```
textemp -o thesis -e vi
```

Will create thesis.tex in the current working directory and then open that file with vi

timer
-------------------------------

Puts a time limit on process execution

```
timer real_time arg[ args]*
```

real_time is a time in seconds represented by a real number (can be fractional)

arg[ args]* is the command which spawns the process to be timed

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

