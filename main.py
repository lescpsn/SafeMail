#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import tornado.httpserver
import tornado.web
import tornado.ioloop
import os.path
import webview
import asyncio
import sys


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('inbox.html')



class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)


def start_server():

    asyncio.set_event_loop(asyncio.new_event_loop())

    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), 'static'),

    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen("8888")
    tornado.ioloop.IOLoop.instance().start()


def safmail_main():
    t = threading.Thread(target=start_server)
    t.daemon=True
    t.start()
    webview.create_window("安全邮件", "http://127.0.0.1:8888/")
    sys.exit()


if __name__ == '__main__':
    safmail_main()