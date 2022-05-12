#!/usr/bin/env python3

import base64
from datetime import datetime
import httplib
import io
import os
import time

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


wdir = "workdir"
stream_url = ''
username = ''
password = ''


def main():
    time_count = 2
    looper_stream(time_count)


def looper_stream(time_count):
    h = httplib.HTTP(stream_url)
    h.putrequest('GET', '/videostream.cgi')
    h.putheader('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (username, password))[:-1])
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    stream_file = h.getfile()
    start = time.time()
    end = start + time_count
    while time.time() <= end:
        now = datetime.now()
        dte = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        dte1 = str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) + "." + str(now.microsecond)
        cname = "Cam1-"
        dnow = """Date: %s """ % dte
        dnow1 = """Time: %s""" % dte1
        # your camera may have a different streaming format
        # but I think you can figure it out from the debug style below
        source_name = stream_file.readline()    # '--ipcamera'
        content_type = stream_file.readline()    # 'Content-Type: image/jpeg'
        content_length = stream_file.readline()   # 'Content-Length: 19565'
        print 'confirm/adjust content (source?): ' + source_name
        print 'confirm/adjust content (type?): ' + content_type
        print 'confirm/adjust content (length?): ' + content_length
        # find the beginning of the jpeg data BEFORE pulling the jpeg framesize
        # there must be a more efficient way, but hopefully this is not too bad
        b1 = b2 = b''
        while True:
            b1 = stream_file.read(1)
            while b1 != chr(0xff):
                b1 = stream_file.read(1)
            b2 = stream_file.read(1)
            if b2 == chr(0xd8):
                break
        # pull the jpeg data
        framesize = int(content_length[16:])
        jpeg_stripped = b''.join((b1, b2, stream_file.read(framesize - 2)))
        # throw away the remaining stream data. Sorry I have no idea what it is
        junk_for_now = stream_file.readline()
        # convert directly to an Image instead of saving / reopening
        # thanks to SO: http://stackoverflow.com/a/12020860/377366
        image_as_file = io.BytesIO(jpeg_stripped)
        image_as_pil = Image.open(image_as_file)
        draw = ImageDraw.Draw(image_as_pil)
        draw.text((0, 0), cname, fill="white")
        draw.text((0, 10), dnow, fill="white")
        draw.text((0, 20), dnow1, fill="white")
        img_name = "Cam1-" + dte + dte1 + ".jpg"
        img_path = os.path.join(wdir, img_name)
        image_as_pil.save(img_path)


if __name__ == '__main__':
    main()
