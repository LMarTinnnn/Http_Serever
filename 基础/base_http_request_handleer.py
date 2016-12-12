from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if not (self.path[1:].endswith('jpg') or self.path.endswith('jpeg')):
                with open(self.path[1:], 'r') as f:
                    self.send_response(200)

                    # set the Content-Type depend on the type of the file
                    if self.path[1:].endswith('html'):
                        self.send_header('Content-type', 'text/html')

                    elif self.path[1:].endwith('txt'):
                        self.send_header('Content-Type', 'text/plain')

                    self.end_headers()
                    self.wfile.write(f.read().encode())

            else:
                with open(self.path[1:], 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-Type', 'image/jpeg')  # !![jpeg]
                    self.end_headers()
                    self.wfile.write(f.read())
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        server = HTTPServer(('', 8000), MyHandler)
        print('Welcome to the base http server machine...')
        print('Press ^c to stop the server')
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()
