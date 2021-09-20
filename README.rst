=======
Git CMS
=======
Git Based Content Management
----------------------------

**DEPRECATED**: This project is no longer maintained. There are a lot of good
alternatives nowadays. Use those.


This is a simple way to allow git to store information related to a website.

USAGE
-----

I assume that you know django. If not, check the django website.

Edit the files in example-website. The format of the files should be pretty
obvious. If not, check the corresponding load.py file (e.g., for
example-website/pages/ check gitcms/pages/load.py).

WHAT'S NEW
----------

**Version 0.3.6**
- Add RSS for blog app
- Add disqus integration for blog app

BACKGROUND
----------

I came to this after having spent a semester maintaining a simple course
website by using restructured text and sphinx to build a website. It was very
easy to use a text editor and reST and after a bit of setting up, I had written
a script so that, after each edit, I could publish by calling ``publish.sh``. I
almost converted my website to this system, but I hesitated because of the
limitations of only having text.

This is similar to the couple of gitwiki projects that are around the web, but
with the major difference that it can use *any time of content*. For example, I
want to maintain a list of upcoming conferences as a text file and have it
served on a webpage, as an online calendar, &c.

