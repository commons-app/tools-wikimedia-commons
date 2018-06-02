#!/usr/bin/env python

import os
import cgi
import sys
import toolforge

#Print header
print ('Content-type: text/html\n')

# Fetch params
if 'QUERY_STRING' in os.environ:
	QS = os.environ['QUERY_STRING']
	qs = cgi.parse_qs(QS)
	try:
		username = qs['user'][0].replace('_', ' ')
	except:
		print ('nouser')
		sys.exit(0)
else:
	print ('nouser')
	sys.exit(0)

##### PROGRAM ####

conn = toolforge.connect('commonswiki')
cur = conn.cursor()
with cur:
	sql = 'select count(*) from filearchive where fa_user=(select user_id from user where user_name="' + username + '");'
	cur.execute(sql)
	data = cur.fetchall()

result = data[0][0]
print (result)
