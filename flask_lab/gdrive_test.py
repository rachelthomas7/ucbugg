

from __future__ import print_function

# some imports might still be missing
import os
import httplib2

from oauth2client.file import Storage
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

# should point to flask lab test in auto labs in website admin
file_id = '1QMbV7A0iyms41ItPRGeYzjqnMAdmvkj0tGBGIWsY6tM'
request = drive_service.files().export_media(fileId=file_id, mimeType='text/plain')

fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print "Download %d%%." % int(status.progress() * 100)

# where is the file thing saved..?

