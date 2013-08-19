# Overview Tips & Tools

This outlines some materials which can be useful to astronomy research.


-------------------------------------------------------


## Coding and Computation


### Editing Text and Writing Code

You want a text editor which will highlight your syntax, assist you with the code syntax, tell you what row/column you're on, give you hints

* [Emacs](www.gnu.org/s/emacs/) - Basic text editor. Can be run from the command line as well as has GUI. Good for quick editing of files

* [Spider](code.google.com/p/spyderlib/) - Python Integrated Development Environment (IDE). Allows you to write and run code you're developing. Will tell you when there are errors before running and will give help with functions. IDEs are useful for projects. 

* [Eclipse](www.eclipse.org) - The most widely used IDE. It's written for java but has an extension call [PyDev](pydev.org) for python. Like Spider this provides syntax highlighting, pre compile error checking, code outlines, and much more!

### Code Languages

A good language to code in should allow you to write it quickly (because your time is valuable), and give you the power of many pre-compile libraries.  
Using high-level languages such as Python or IDL is preferred over low-level because they are quicker to code and easier to debug.  

Object Oriented Programming (OOP) is a very powerful way to organize your code. 

* C/C++ - A low level language above the operating system which is lightning fast to run but takes times to write. C++ supports using objects

* Fortan - Avoid using fortran. It is a low-level language which is fast to run but slow to write. 

* [Python](http://www.continuum.io/downloads) - Our preferred choice. Python is a high-level language based on C. It's a widely used language so there's much support both in and out of astronomy. 

	* Some key [standard libraries](docs.python.org/2/library/):
	
		* PDB - python debugging tool. Which is very quick for finding and fixing errors

		* os - operating system python library
	

	* The key extensions to python are:
		
		* numpy - for lightning fast and versitile vector manipulation
	
		* scipy - extensive library for science related mathematic operations

		* matplotlib - a plotting utility package
	
	* Other useful extensions:
		
		* Astropy - an library of code developed for astronomy

		* Pyraf - Python wrapper for IRAF

	* You can check out the [pip-library](pypi.python.org/pypi?%3Aaction=index) for other useful code. Pip allows you to easily install more python packages by running:
	
		pip install <package-name>
	
* IDL - This is a high-level language based roughly on Fortan. It's supported by the US military for doing visualization. It costs money but astronomers adopted it in the late 80's so there are mature libraries. NOTE: many of the previous supporters of IDL (such as NOAO and NASA) are switching to python)
	
	* Key exstensions for IDL:
		
		* [NASA Library](idlastro.gsfc.nasa.gov/ftp/) - This is a common location for astronomy related IDL code

	
* [R](www.r-project.org/) - A statistical computing language. Similar to python but has been developed specifically for data statisitics and visualization. 

### File Versioning

File versioning allows you to track and undo changes to documents and code. This is very useful, not only for writing code but for also for any file which you expect to change and evolve.


* [git](git-scm.com) Easy version control. A few commands allows you to track changes and recover previous versions

	* Online repository cites - There are 'free' sites which host git type repositories. Both given here are useful for their own strengths. I have repositories on both to fit the needs of my project.

		* [GitHub](github.com) - Its model is that all repositories are public and you can have many collaborators. You must pay for private repositories

		* [BitBucket](bitbucket.org) - Its model is that all repositories are private and you pay for more than 5 collaborators. Comes with built-in Wiki page
	

* [SVN](subversion.tigris.org) - The one of the earlier version control systems. 


--------------------------------------------------------


## Data Analysis

These are tools for analyzing your data.

* [TopCat](http://www.star.bris.ac.uk/~mbt/topcat/) - This tool allows you to quickly view and analyse your data. It supports reading in many file types and also connections to online resources such as SIMBAD and ALADIN. It does rapid list comparison for finding RA and Dec matches between these large databases. It allows you to create subsests of data and then view them in many different phase spaces


--------------------------------------------------------


## Work Flow

These are tools which help you with your daily work flow

* [Mendeley](www.mendeley.com) - Like iTunes for scientific papers. Allows you to import PDFs, organize and rapidly search out needed information

* [Docear](www.docear.org) - Allows you to create flow charts and organize information

* [Evernote](evernote.com) - A note portfolio which allows you to collaboratively share information and also store your own info.


--------------------------------------------------------


## Online Tools

The internet has many useful tools

### References

* [Astrobetter](www.astrobetter.com) - Tips and tricks for astronomers. This online reference has many things for astronomers.

* [AstroBabel](http://www.astrobabel.com) - A place for computational questions in astronomy


### Papers

* [Astro-ph](http://arxiv.org/list/astro-ph/new) - The Arxiv is a source of cutting edge knowledge. It's a pre-publication database, where papers are put up before finishing referee process.

* [ADS](http://adsabs.harvard.edu/abstract_service.html) - A common database for many papers. 

### Data

* [SIMBAD](http://simbad.u-strasbg.fr/simbad/sim-fid) - A database of astronomical objects. There is compiled information and references for many thousands of objects.

* [VizieR](http://vizier.u-strasbg.fr/viz-bin/VizieR) - Has online catelogs and many sources of data

* [Aladin](http://aladin.u-strasbg.fr/aladin.gml) - Software that links up with SIMBAD and others to provide visualizations of data


## Podcasts

* [AstronomyCast](http://www.astronomycast.com/) - Fairly basic but quality presentation about astronomy knowledge

* [StarStuff](http://www.learnoutloud.com/Podcast-Directory/Science/Astronomy/StarStuff-with-Stuart-Gary-Podcast/30502) - Has in-depth information about the most interesting stuff going on in astronomy. 







