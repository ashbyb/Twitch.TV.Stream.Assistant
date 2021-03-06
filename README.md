Twitch.tv Stream Assistant
=============

<p align="center">
  <img src="http://i.imgur.com/Sz85eic.png" alt="Twitch.Tv IRC Bot Interface"/>
  <br> (As of May 31 2013)
  <br> A system that automates a number of tasks to aid in streaming and community involvment.
</p>

<p align="center">
  <img src="http://i.imgur.com/oLeYf8O.gif" alt="Twitch.Tv IRC Bot Interface Example 2"/>
  <br>(As of June 2 2013)
  <br> A quick look at the chat client in motion
</p>

A short feature list 
--------------------
>(All are WIP)

  * IRC Bot
    * View and talk in chat from the program
    * Track who is online (filter by mod, op, voice, subscriber)
    * Moderate chat (links, bans, spam, caps)
    * Numerous triggers (!command <arguments>)

  * Monitor Stream Statistics
    * Viewers
    * Unique views
    * Stream uptime
    * Chat room population

  * Update textural information (with OBS or Xsplit)
    * Read now playing information from foobar
    * Write out statistics
    * Write out other variables
    * Write images as well as text

Goal
-------

Increase community interation though an automated input to response system. Users can input through chat or offsite website. Output can be seen in chat, on stream, or on offsite website.

Getting Started
---------------

This program is written in Python. It was written against Python 2.7.3. It uses a pipy Python IRC library called irc 8.3. The GUI is written in PyQT4.

So you will need:

 * [Python 2.7](http://www.python.org/download/releases/2.7/)
 * [pipy IRC 8.3 Library](https://pypi.python.org/pypi/irc/)
 * [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download)
 
>You may need to install [setuptools](https://pypi.python.org/pypi/setuptools) before you can install the above dependancies.

Once you have everything installed, run:
    `> path\to\python main.py`

Drawbacks and Limitations
-------------------------

Moobot and other JTV bot systems exist already and work well. There is no reason to re-invent the wheel here. All features needs to be unique and useful. 

Moobot does drop out of a channel that is idle. Possible drawback to moobot. As features are added, need to be able to show they don't already exist out there.
