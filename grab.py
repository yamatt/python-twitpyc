#!/usr/bin/python
"""
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
"""

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
from time import sleep
import sys
import os
import re

backup_dir = "twitpic-backup"
id_match = re.compile('^http:\/\/twitpic.com\/([a-zA-Z0-9]+)$')
img_extension_match = re.compile('^http:\/\/s3.amazonaws.com\/twitpic\/photos\/full\/[0-9]+\.(png|jpg|gif)',re.IGNORECASE)
feed_path = "feed.rss" # optional
delay = 5

if len(sys.argv) > 1:
     username = sys.argv[1]
     rss_url = "http://twitpic.com/photos/%s/feed.rss" % username
     user_backup_dir = os.path.join(backup_dir, username)
else:
     print "You need a username as an argument"
     raise

print ('Getting data')
if os.path.exists(feed_path):
    print ('Found file. Using that instead')
    data = open(feed_path, 'r')
else:
    data = urlopen(rss_url)

print ('Parsing data')
rss = data.read()
soup = BeautifulStoneSoup(rss)
items = soup.rss.channel.findAll('item')

if os.path.exists(user_backup_dir):
    print ('Using existing directory')
else:
    print ('Creating backup directory')
    os.makedirs(user_backup_dir)

print ('Processing data')
for item in items:
    img_url = item.guid.renderContents()
    id = id_match.match(img_url).group(1)
    print ("Working on %s" % img_url)
    meta_filename = id + ".xml"
    meta_filepath = os.path.join(user_backup_dir, meta_filename)
    meta_file = open(meta_filepath, 'w')
    meta_file.write(item.prettify())
    if delay > 0:
        print "Adding delay"
    sleep(delay)
    print ("Downloading image page")
    img_page = urlopen(img_url + "/full")
    img_soup = BeautifulSoup(img_page)
    images = img_soup.html.body.findAll('img')
    for image in images:
        img_url = image['src']
        if bool(img_extension_match.match(img_url)):
           img_extension = img_extension_match.match(img_url).group(1)
           img_filename = ".".join([id, img_extension])
           img_filepath = os.path.join(user_backup_dir, img_filename)
           print ("Downloading image")
           img_data = urlopen(img_url)
           img_file = open(img_filepath, 'w')
           image = img_data.read()
           img_file.write(image)
