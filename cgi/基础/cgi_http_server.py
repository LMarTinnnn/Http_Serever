from http.server import CGIHTTPRequestHandler, HTTPServer


def main():
    try:
        # CGI可以自动处理不同类型的文件 如：
        # html 则 Content-Type 为 text/html
        # jgp 则 为 image／jpg

        server = HTTPServer(('', 8000), CGIHTTPRequestHandler)
        print('HttpServer serves at port 8000')
        print('Press ^c to stop the server machine')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down the server')
        server.socket.close()

if __name__ == '__main__':
    main()
