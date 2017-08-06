# TASK 1 (Check Primality Functions)
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). Take this opportunity to practice using functions, described below.
### Discussion  
#### Concepts for this week:

* Functions
* Reusable functions
* Default arguments
* Functions

One of the tools programming gives us is the ability to break down problems into easier (or perhaps previously solved) or reusable subproblems. It is good practice to have a function have a single purpose, and the name of that function should hint at it’s purpose in some way.

Most programming languages have this idea of a function, subroutine, or subprogram. In Python, a function is a programming construct that allows exactly that.

**Let’s look at a simple example:**
```python
  def get_integer():
    return int(input("Give me a number: "))
 ```
In this small example, we used the same code that asks a user for input as a tabbed line underneath this def statement. The def means that everything tabbed underneath is a function. The name get_integer() is just a name that I (the programmer) made up. If I just include this code inside a Python file and run it, nothing will happen - all I have done so far is wrapped my code inside of a function; I never told my program to actually RUN my function.

```python
  def get_integer():
    return int(input("Give me a number: "))
  age = get_integer()
  school_year = get_integer()
  if age > 15:
    print("You are over the age of 15")
  print("You are in grade " + str(school_year))
```

What I have done here is called the function (told it to run) by writing age = get_integer(). When this line of code runs, what happens is the program will execute (run) the function by asking me for a number, then returning it (giving it back to me) by saving it inside the variable age. Now when I want to ask the user for another number (this time representing the school year), I do the same thing with the variable school_year.

#### Reusable functions

This is all well and good, but I can make my function do much more for me. Right now, my function will always ask the user for a number by printing the string "Give me a number: ". What if I want to print a different string every time I ask the user for a number, but otherwise use the same idea for the function? In other words, I want a variable parameter in my function that changes every time I call the function based on something I (the programmer) want to be different.

I can do this by passing (giving) my function a variable. Like this:
```python
  def get_integer(help_text):
    return int(input(help_text))
```
Now what I can do when I call the function is something like this:
```python
  def get_integer(help_text):
    return int(input(help_text))

  age = get_integer("Tell me your age: ")
  school_year = get_integer("What grade are you in? ")
  if age > 15:
    print("You are over the age of 15")
  print("You are in grade " + str(school_year))
```
Now it is easier for a user to use the program, because the help text is different.

These variables you pass to functions are called variables, parameters, or arguments.

#### Default arguments

In the example above, once I have added an argument to my function, I always have to give an argument when I call the function. I can’t forget to give the get_integer() function from above a string to print to the screen. In some cases, I want there to be a “default” behavior for my function that happens when I create an argument for it but don’t give it any.

In the example above, if I don’t give a custom string (which may be 95% of the time I use this function), I just want the input() line to say "Give me a number: " and I want to save myself the trouble of writing this every single time I call the function. So what I can do is give my function default arguments. Like so:
```python
  def get_integer(help_text="Give me a number: "):
    return int(input(help_text))
```
What happens now is I can use the function in two ways: by giving it an argument and by NOT giving it an argument.
```python
  def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

  age = get_integer("Tell me your age: ")
  school_year = get_integer()
  if age > 15:
    print("You are over the age of 15")
  print("You are in grade " + str(school_year))
```
The first time I call the function, it will print "Tell me your age: ", but the second time, it will print "Give me a number: ", because I did not give it a string and it will execute the default behavior.

#### Recap

What a function does is wrap a piece of code that we want to reuse, labels it, and allows us to use it again relatively easily. You can add variables to the functions to make your code even MORE reusable, and you can add default arguments to these variables.

Functions are a bit strange to deal with at first, but once you master them, they will be your savior in programming. Besides, the whole point of learning programming is abstraction, problem solving, breaking down problems, and that’s exactly what functions are all about.



# TASK 2 (Reverse Word Order)

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.

#### Discussion

**Concepts for this week:**

* More string things

Python has a lot of interesting things you can do with strings. I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string format.

Remember that strings are lists.

#### Splitting strings

You can “split” or tear apart strings based on a given set of characters. For example:
```python
  teststring = "this is a test"
  result = teststring.split("t")
```
And at the end, result will contain the list:
```python
  ['', 'his is a ', 'es', '']
```

Instead of "t", you can write any character you want. If you do not include any character, it means “split on all whitespace”:
```python
  teststring = "  this      has a lot    of   spaces and    tabs"
  result = testring.split()
```
Then result contains:
```python
  ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
```
#### Joining strings

You can also relatively easily “join” or “smush” strings together:
```python
  listofstrings = ['a', 'b', 'c']
  result = "**".join(listofstrings)
```
Then result will contain the string:
```python
  a**b**c
```
Take a look at the official Python documentation for more information.


# TASK 3(Password Generator)

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:
* Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# TASK 4(Decode A Web Page)

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the [New York Times homepage](https://www.nytimes.com).

### Discussion

#### Concepts for this week:

* Libraries
* requests
* BeautifulSoup

Many people have written libraries in Python that do not come with the standard distribution of Python (like the random library mentioned in a previous post). These libraries can do anything from machine learning to date and time formatting to meme generation. If you have a task you need done, most likely someone has written a library for it.

There are three main things to keep in mind when using a library:

You need to install it. Installation in GNU/Linux based systems will generally be easier than on Windows or OSX, but there will always be documentation for how to do it.
You need to import it. At the top of your program, make sure you write the line import requests, or whatever the name of your library is. Then you can use it to your heart’s content.
You need to read documentation. Someone else wrote it, so the rules might not be so obvious. Anyone (or any group) that writes a Python package writes documentation for it. Eventually, reading documentation will become second nature.
Requests

One of the most useful libraries written for Python recently, requests does “HTTP for humans.” What this means in laymen’s terms is that it asks the internet things from Python. When you type “facebook.com” into the browser, you are asking the internet to show you Facebook’s homepage.

In the same way, a program can ask the internet something. It might not be “show me Facebook”, but you can for example ask Github for a list of all the repositories that the user “mprat” has. You can do this with an API (Application Programming Interface). This exercise doesn’t use APIs, so we’ll talk more about those in a later post.

Back to showing the user a webpage. When I type “facebook.com” into the browser, Facebook sends my browser a bunch of HTML (basically, code for how the website looks). The browser then takes this HTML and shows it to me in a pretty way. (Fun fact: to see the HTML of any page in a browser, right click on the page and “Inspect Element” or “View Source” depending on your browser. In Chrome, “Inspect Element” will pop up a module at the bottom of your page where you can see the HTML from the page. This trick will come in handy when you’re doing the exercise. If you need to DO anything with this HTML, better to use a program. More posts about this coming later.) If I want to “see” a webpage with a program, all I need to do is ask it for it’s HTML and read it.

The ‘requests’ library does half of that job: it asks (requests, if you will) a server for information. This could be just data (through an API - more later) or in the case of this exercise, HTML.

Look at the documentation for all the details you need. In this particular latest version, all you need to do to ask a website for it’s HTML is:
```python
  import requests
  url = 'http://github.com'
  r = requests.get(url)
  r_html = r.text
```
Now inside the variable r_html, you have the HTML of the page as a string. Reading (otherwise called parsing) happens with a different Python package.

#### BeautifulSoup

To solve our problem of parsing (reading, understanding, interpreting) the string of HTML we got from requests, we use the BeautifulSoup library.

What it does is give a hierarchical (a pyramid structure) to the HTML in the document. If you don’t know anything about HTML, the Wikipedia article is a good summary. For the purposes of this exercise, you don’t need to know anything about HTML beyond being able to look at it quickly.

Because BeautifulSoup takes care of interpreting our HTML for us, we can ask it things like: “give me all the lines with <p> tags” or “find me the parent element to the <title> element”, etc.

Your code would look something like this:
```python
  from bs4 import BeautifulSoup

  # some requests code here for getting r_html 

  soup = BeautifulSoup(r_html)
  title = soup.find('span', 'articletitle').string
```
And you can do many more things in BeautifulSoup, but I will leave you to explore those by yourself or through other later exercises.
