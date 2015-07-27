---
tags: cssi, gae, python, templates
level: 2
languages: python
---

#Google App Engine: Intro to Templates

The **template** is the view of the MVC model. This is where our python is embedded into our HTML.  

There are many templating systems for Python: <a href="https://docs.djangoproject.com/en/dev/topics/templates/Django">Django</a>, and <a href="http://jinja.pocoo.org/">Jinja</a> are just a few. You can use your template engine of choice by bundling it with your application code.

Let's start with a simple page:

**Code Along: Templating**
+ Clone the repo into the development directory of your local machine, or you can use the Boilerplate Code below.

+ Copy and save this into main.py


```python
import webapp2 #webapp2 is a module that you import

class MainHandler(webapp2.RequestHandler):#This is the handler class
  def get(self):
    self.response.write('Hello webapp2 world!')#replacing your print statements

class CountHandler(webapp2.RequestHandler):
  def get(self):
    for i in range(1, 101):
      self.response.write(i)

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/count', CountHandler),
], debug=True) #creates a WSGIApplication and assigns it to the variable app. app.yaml is pointed to this object
```
+ Now we need to tell <kbd>app.yaml</kbd> where to find our app (<kbd>helloworld.app</kbd>) and the <kbd>webapp2</kbd> library.

```python
application: appengine-practice
version: 1
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /favicon\.ico
  static_files: favicon.ico
  upload: favicon\.ico

- url: /.*
  script: main.app

libraries:
- name: webapp2
  version: "2.5.2"
```

+ Run your app using the AppEngineLauncher by Adding and Existing Application, and then open your page in the browser.

#Templating

We can add elements and styling to our page by using **templates**.

**Template** - reusable code that provides a framework for embedding python into HTML. It lets us write an html page that will have similar structure and style, but different data depending on who visits a page and the state of the application.

Here is some html in a file called hello.html, in a directory called templates, saved in the same directory as your appengine-practice project. It gives us a webpage that contains two lines of text and an image.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <img height="100px" width="150px" src="https://blackgeoscientists.files.wordpress.com/2014/06/helloworld.jpg" alt="A cute Pic of a Dude on the World">
    <h2>How are ya?</h2>
  </body>
</html>
```
We can edit the app.yaml file to use the jinja library: jinja is a templating system for python.

+ If you modify the libraries section at the bottom of your app.yaml page to add jinja.

```python
application: appengine-practice #Unique application name
version: 1 # version 1 of this application’s code
runtime: python27 # running on python 2.7
api_version: 1 # API version 1
threadsafe: true # how AppEngine processes multiple requests simultaneously

handlers:
- url: /favicon\.ico
  static_files: favicon.ico
  upload: favicon\.ico

- url: .*
  script: main.app

 libraries:
- name: jinja2
  version: latest
- name: webapp2
  version: "2.5.2"
```
  + And Edit main.py to add jinja at the top of the page, plus add jinja to the handler in main.py

```python  
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/hello.html')
        self.response.out.write(template.render())
```
+   You can run the app and, Hooray we have styling!
