---
tags: cssi, gae, python, templates
level: 2
languages: python
---

#Google App Engine: Intro to Templates

#Objectives:

+ Understand and articulate the purpose of a template framework
+ Reference python templating libraries such as jinja2 or django
+ Understand why we use template variables in our views
+ Understand how to use python tags and template variables to display dynamic information in views

#Motivation
The advantage of templates is that you put the bulk of your html in another file, which then looks like html. You cleanly separate the file full of code from the file full of rich text - Separation of Concern

#Lesson: Template Introduction
The template is the view of the MVC model. This is where our python is embedded into our HTML. HTML embedded in code is difficult to maintain. It's better to use a templating system, where the HTML is kept in a separate file with special syntax to indicate where the data from the application appears. There are many templating systems for Python: <a href="https://docs.djangoproject.com/en/dev/topics/templates/Django">Django</a>, and <a href="http://jinja.pocoo.org/docs/dev/Jinja2">Jinja</a> are just a few. You can use your template engine of choice by bundling it with your application code.

**Code Along: Templating**

+ Boilerplate code: Copy and save into helloworld.py

```python
import webapp2 #webapp2 is a module that you import

class HelloHandler(webapp2.RequestHandler):#This is the handler class
  def get(self):
    self.response.out.write('Hello webapp2 world!')#replacing your print statements

routes = [  #a list of tuples mapping paths to handlers

    ('/.*', HelloHandler),
]

app = webapp2.WSGIApplication(routes, debug=True) #creates a WSGIApplication and assigns it to the variable app. app.yaml is pointed to this object
```
+ Now we need to tell <kbd>app.yaml</kbd> where to find our app (<kbd>helloworld.app</kbd>) and the <kbd>webapp2</kbd> library.

```python
application: helloworld
version: 1
runtime: python27
api_version: 1
threadsafe: false

handlers:
- url: /.*
  script: helloworld.app

libraries:
- name: webapp2
  version: latest
```

+ Run your app using the AppEngineLauncher - Click File>Add Existing Project, then navigate to folder that helloworld.py is in. Open the page in the browser. How would you describe it?

We can add elements and styling to our page by using **templates**.

A template is reusable code that provides a framework for embedding python into HTML. It lets us write an html page that will have similar structure and style, but different data depending on who visits a page and the state of the application.

+ Open up terminal:
 + cd development
 + mkdir templates
 + cd templates
 + touch hello.html
 + touch style.cssi
 + open hello.html

**Popcorn Coding**
+ Write some html in hello.html that gives us a webpage that contains two lines of text and an image. Something like:

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
Now Edit app.yaml to use jinja library: jinja is a templating system for python. Jinja is a templating ninja! Haha get it?

+ First modify the libraries section at the bottom of your app.yaml page.

```python
 libraries:
- name: jinja2
  version: latest
- name: webapp2
  version: "2.5.1"
```
  + Edit helloworld.py to add jinja at the top of the page

```python  
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py
```
+ Add jinja to helloworld.py handler (this way we can use our template instead of writing boring output)

```python
class HelloHandler(webapp2.RequestHandler):
def get(self):
template = jinja_environment.get_template('templates/hello.html')
self.response.out.write(template.render())
```
+  Run app: Hooray we have styling! This is an improvement and more exciting, we have styling now!

#Labs:
(to add)
