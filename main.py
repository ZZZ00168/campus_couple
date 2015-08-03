#!/usr/bin/python
# -*- coding: utf8 -*-
import web
import route
import cgi
import sites

if __name__ == "__main__":
    cgi.maxlen = 10 * 1024 * 1024
    app = web.application(route.getURLs(), globals())
    app.run()
