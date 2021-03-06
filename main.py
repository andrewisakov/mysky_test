#!/usr/bin/python3
import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
from routes import routes_setup
import settings
import database


if __name__ == '__main__':
    database.init()
    tornado.options.define('log_file_max_size', default=10*1024*1024)
    tornado.options.define('log_file_prefix', default='mysky_test.log')
    tornado.options.parse_command_line()
    app = tornado.web.Application(routes_setup(), **settings.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port=settings.SERVICE['port'],
                       address=settings.SERVICE['host'])
    # http_server.listen(settings.SERVICE['port'])
    tornado.ioloop.IOLoop.current().start()
