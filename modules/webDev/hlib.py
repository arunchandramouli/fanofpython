
'''
	Aim :: Using httplib for connection

'''

import httplib,urllib


url = 'www.github.com'


conn = httplib.HTTPSConnection(url)

print conn , '\n\n' 


'''
  dir(conn)	

  ['_HTTPConnection__response', '_HTTPConnection__state', '__doc__', '__init__', '__module__', '_buffer', '_context', '_create_connection', '_get_hostport', '_http_vsn', '_http_vsn_str', 
  '_method', '_output', '_send_output', '_send_request', '_set_content_length', '_tunnel', '_tunnel_headers', '_tunnel_host', '_tunnel_port', 'auto_open', 'cert_file', 'close', 'connect', 
  'debuglevel', 'default_port', 'endheaders', 'getresponse', 'host', 'key_file', 'port', 'putheader', 'putrequest', 'request', 'response_class', 'send', 'set_debuglevel', 'set_tunnel', 
  'sock', 'source_address', 'strict', 'timeout']

'''

print conn.host , '\n\n', conn.port,'\n\n'#,conn.status,'\n\n',conn.reason

conn.request("GET","/")
resp = conn.getresponse()

print resp , '\n\n',resp.reason, '\n\n',resp.status, '\n\n',resp.msg, '\n\n',resp.length, '\n\n'
data = resp.read()

print 'Data - ',data

'''
dir(resp)

['__doc__', '__init__', '__module__', '_check_close', '_method', '_read_chunked', '_read_status', '_safe_read', 'begin', 'chunk_left', 'chunked', 'close', 'debuglevel', 
'fileno', 'fp', 'getheader', 'getheaders', 'isclosed', 'length', 'msg', 'read', 'reason', 'status', 'strict', 'version', 'will_close']

'''

print 'Posting Data!', '\n\n'



params = urllib.urlencode({'@number': 125240, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
          "Accept": "text/plain"}
conn = httplib.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
