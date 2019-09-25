# Server script for Portfolio Website 
# Includes server side functions such as handling get and push requests 

import http.server
import socketserver



PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("serving at port", PORT)
	httpd.serve_forever()