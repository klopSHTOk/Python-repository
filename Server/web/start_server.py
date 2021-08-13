from http.server import HTTPServer 
from http.server import CGIHTTPRequestHandler

addr = ("", 8000)                               # Here I've just created a new server address with port number 8000
httpd = HTTPServer(addr, CGIHTTPRequestHandler) # In this string I had identified CGI work
httpd.serve_forever()                           # And in the last string I made a forever server work