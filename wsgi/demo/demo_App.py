from wsgiref.simple_server import make_server, demo_app

srv = make_server('', 8000, demo_app)
print('Started app serving on port 8000...')
srv.serve_forever()

