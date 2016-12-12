from http.server import CGIHTTPRequestHandler, HTTPServer
import cgitb
cgitb.enable()

def main():
    try:
        srv = HTTPServer(('', 8080), CGIHTTPRequestHandler)
        print('Start serving at port [%s]' % 8080)
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.socket.close()

if __name__ == '__main__':
    main()
