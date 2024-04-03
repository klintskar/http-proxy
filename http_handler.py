import http.server

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    blocked_sites = ["example.com", "blocked.com"]  # List of blocked websites

    def parse_request(self):
        try:
            # Parse the incoming request and extract information
            self.request_method = self.command
            self.request_url = self.path
            self.request_headers = self.headers
            self.request_body = None
        
            # Check if the requested URL is in the list of blocked sites
            if self.request_url in self.blocked_sites:
                self.block_request()

            # If the request is a POST request, read the body
            elif self.request_method == 'POST':
                content_length = int(self.headers.get('Content-Length', 0))
                self.request_body = self.rfile.read(content_length).decode('utf-8')

        except Exception as e:
            # Handle any exceptions that occur during request parsing
            print("Error parsing request:", e)
            # Optionally, you can log the error or send an appropriate response to the client


    def block_request(self):
        # Send a forbidden response for blocked requests
        self.send_response(403)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Access to this website is blocked.")
        
    def do_GET(self):
        # Handle GET requests
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_POST(self):
        try:
            # Handle POST requests
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"POST request received with body: " + body)
        except Exception as e:
            # Handle any exceptions that occur during POST request handling
            print("Error handling POST request:", e)
            # Optionally, you can log the error or send an appropriate response to the client

