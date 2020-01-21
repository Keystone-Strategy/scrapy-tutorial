# Some Basics on the web scraping with scrapy.

### With scrapy, there are more than one way to get the data from a web page. The two most commonly used are the `xpath` and `css` selectors to specify parts on the html code and get the texts from them. The selectors works with the html structure, the `css` ones uses styles and css classes to be more specific, the `xpath` is based on the html tags structures and the classes this tags have. 

### To create the structure of a selector, it is necessary to know the code of the page. So to get it, you need to "inspect" the web page itself, almost all web browsers have tools that allows the users to inspect the html code of the pages they are visiting, usually it is just necessary a "right click" to access this tools.

### Scrapy makes things easier, by providing some commands on its tools, that allows you to test the selectors `scrapy shell <url>` this commands simply downloads the html associated to the provided url, and returns a response object, that contains the body of that html downloaded. Over that response, can be tested the selectors, just like if it was the spider itself.

### There are cases where it is very difficult to specify a part on a page through its html, usually due to bad practices applied on the code, for this cases Google Chrome Browser has an extension that helps on the creation of `xpath` and `css` selectors 