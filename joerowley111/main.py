#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import csv
import os
import re
import random
from google.appengine.api import users

from collections import defaultdict

import webapp2
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World')


class Dashboard(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/dashboard.html')
        self.response.write(template.render(path, {}))

class Homepage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/home.html')
        self.response.write(template.render(path, {}))

class Aboutpage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/about.html')
        self.response.write(template.render(path, {}))

class Contactpage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/contact.html')
        self.response.write(template.render(path, {}))



class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        self.error(404)
        dognum = random.randint(0, 4)
        #self.response.out.write('Your 404 error html page')
        output = {
            'dognum': dognum,
            }
        path = os.path.join(os.path.dirname(__file__), 'templates/404.html')
        self.response.write(template.render(path, output))



app = webapp2.WSGIApplication([
                                  ('/', Homepage),
                                  ('/dashboard', Dashboard),
                                  ('/about', Aboutpage),
                                  ('/contact', Contactpage),
                                  ('/.*', NotFoundPageHandler),
                                  ], debug=True)
