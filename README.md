Twitch.tv Stream Assistant
=============

A system that automates a number of tasks to aid in streaming and community involvment.

A short feature list 
--------------------
>(All are WIP)

  * IRC Bot
    * View and talk in chat
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


Once you have everything installed, run:
    `> path\to\python main.py`
