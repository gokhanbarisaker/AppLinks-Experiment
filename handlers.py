# -*- coding: UTF-8 -*-

import webapp2
import lab

application = webapp2.WSGIApplication([
    ('/', lab.Handler)
], debug=True)
