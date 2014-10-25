# -*- coding: UTF-8 -*-

import webapp2
import html

class Handler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(html.render('lab.html'))
