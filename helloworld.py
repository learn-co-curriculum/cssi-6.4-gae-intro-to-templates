import webapp2 #webapp2 is a module that you import

class HelloHandler(webapp2.RequestHandler):#This is the handler class
  def get(self):
    self.response.out.write('Hello webapp2 world!')#replacing your print statements

routes = [  #a list of tuples mapping paths to handlers

    ('/.*', HelloHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
#creates a WSGIApplication and assigns it to the variable app.
#app.yaml is pointed to this object
