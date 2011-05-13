# TwitPYc
## About
This script was started due to the controvercy over the licensing of your images on TwitPic. I had a look for something that would easily scrape my images off TwitPic, but the only one I found then stuck it in Posterous:
http://posterous.com/switch/twitpic/

Which doesn't nessecarily improve the situation. So I had a bit of a look around the TwitPic site and found the RSS feed looked fairly easy to use so I'm using that.

## Running
You need Python, anything recent will do, and you need BeautifulSoup.
 * http://www.python.org/download/
 * http://www.crummy.com/software/BeautifulSoup/#Download

I've coded it so that it should run equally well on Windows and Linux.

Run the following command from your command line:
    python grab.py [username]

Obviously where [username] is your username on Twitter. Your RSS feed has to be publically accessible.

It will then tell you it's progress with lots of screen messages and then exit. Check you do have all your images, and now you can delete your TwitPic account.

You can modify the Python script in Notepad or whatever to change a few settings, but only if you know what you are doing. The most useful one is probably the 'delay' option which sets how long it waits between requests to TwitPic so as not to flood their network.

You will end up with a directory containing another directory with your username which contains your original images along with the meta-data associated with them from the RSS feed.

## Problems?
Do let me know if you have any problems or patches. My RSS feed isn't big, and I expect it'll only have the most recent 25 or something so I may have to do some work there. Let me know.

## License
Copyright (C) 2011 by Matthew Copperwaite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
