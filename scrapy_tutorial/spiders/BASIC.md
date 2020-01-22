# Some Basics on the web scraping with scrapy.

### With scrapy, there are more than one way to get the data from a web page. The two most commonly used are the `xpath` and `css` selectors to specify parts on the html code and get the texts from them. The selectors works with the html structure, the `css` ones uses styles and css classes to be more specific, the `xpath` is based on the html tags structures and the classes this tags have.

### To create the structure of a selector, it is necessary to know the code of the page. So to get it, you need to "inspect" the web page itself, almost all web browsers have tools that allows the users to inspect the html code of the pages they are visiting, usually it is just necessary a "right click" to access this tools.

### Scrapy makes things easier, by providing some commands on its tools, that allows you to test the selectors

`scrapy shell <url>`

### This commands simply downloads the html associated to the provided url, and returns a response object, that contains the body of that html downloaded. Over that response, can be tested the selectors, just like if it was the spider itself.

### There are cases where it is very difficult to specify a part on a page through its html, usually due to bad practices applied on the code, for this cases Google Chrome Browser has an extension named *'SelectorGadget'* that helps on the creation of `xpath` and `css` selectors, it is really intuitive and useful.

### Scrapy also provides a command to take a better look at the html you are working on

`scrapy view <url>` 

### This downloads temporarily the page from the provided url, and opens the downloaded file in the default browser. This usually helps you to know when a web can be scraped with a basic approach or if it is necessary to use a more advanced one (explanation for this on the SELENIUM.md and SPLASH.md files).

### Every spider has a basic code structure when it is created with the `genspider` command. The scrapy tool creates a class, which is the spider itself, and inside it adds properties `name`, `allowed_domains`, `start_urls` and also creates a function named `parse`

## name

### The name of the spider, is the identifier of that class inside the scrapy project, so, when you want to start a spider's run, just type `scrapy crawl <spider_name>` and it will start its lifecicle.

## allowes_domains

### It is a list that tells the spider wich is the main domains where it can stract data from, at some cases web pages have outside links and if for some case the spider is taken an outside page whose domain does not match with any of the specified in `allowed_domains` then it will be ignored.

## start_urls

### This is a list of urls that tells the spider what is/are the main url(s) it will get on the main parse function.

## parse function

### This function receives the html form the main urls, the ones that are inside `start_urls`, so here it is where your spider's logic will begin.