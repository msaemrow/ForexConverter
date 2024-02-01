### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    1. javascript is traditionally a front end language and Python is traditionally a back end language (though could be used for frontend if wanted)
    1. python can be easier to learn syntax vs javascript
    1. variable declaration in python doesn't require a let/const/var declaration
    1. javascript runs in browser and python runs on a server
    1. python has a very clean syntax. javascript can get a bit messy


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    1. you could use a try/except block to catch possible error handling
    1. you could use a if/else condition to check if the key is present. If it is do something, else report key not found

- What is a unit test?
    1. A unit test focuses on an individual component of an application, often times a single function/class. A successful unit test does not guarantee a successful start to finish application

- What is an integration test?
    1. An integration test checks to see if the various functions/classs work together.

- What is the role of web application framework, like Flask?
    1. Allows developers to create web apps faster. Has a bunch of logic to logic that runs behind the scenes to complete requests while having to write less code. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  1.  using a query param can give more flexibility and options when selecting parameters, can be easier to change params, and can be easier to share a link with specific params. 
  1. using a param in a route URL can give a clear URL, help when building and API, and be better for identifying specific routes such as for a user ID. 

- How do you collect data from a URL placeholder parameter using Flask?
    1. Add <> around the paramter to make it a variable

- How do you collect data from the query string using Flask?
  1. use request.args to get all data from a query string
    1. can specify which piece of data wtih request.args["param"]

- How do you collect data from the body of the request using Flask?
  1. use request.form["param"] to get data

- What is a cookie and what kinds of things are they commonly used for?
  1. cookies store small bits of info for the browser i.e. pages viewed, shopping cart, clicks, etc

- What is the session object in Flask?
  1. sessions stores info for the current browser. Sessions preserve the type (lists stay lists) and they are "signed" so the data can't be modified. 


- What does Flask's `jsonify()` do?
  1. it converts the output of a function to a JSON object