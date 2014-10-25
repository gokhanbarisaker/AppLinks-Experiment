# -*- coding: UTF-8 -*-

import webapp2

class Handler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Hellow")
