# scrapy-tutorial

## This tutorial is ment to teach the members of KeyStoneLabs how to create and use a scrapy project for Python.

### In first place, we need to install Scrapy package for python, this can be done with command: 

`pip install Scrapy`

### This will install the package and let you use the Scrapy command line tools.

### Once the package is installed, then we must proceed to the project's creation. Scrapy makes this very easy, providing a command to its tools `startproject` initializes a scrapy project with a basic structure:

```
scrapy.cfg
<project_name>/
	__init__.py
	items.py
	pipelines.py
	settings.py
	spiders/
		__init__.py
```

### And the usage of the `startproject` command is:

`scrapy startproject <project_name>`

### Where `project_name` is substituted with the desired name for the main directory of the project, the project's name.

#### For more reference about this: [Click here](https://docs.scrapy.org/en/latest/topics/commands.html#std:command-startproject)

### In addition to that structure, we are adding one more file `middlewares.py` so the structure will look like: 

```
scrapy.cfg
<project_name>/
	__init__.py
	items.py
	middlewares.py
	pipelines.py
	settings.py
	spiders/
		__init__.py
```

### This file can be really useful in future, but first it is recommendable to make a few changes to `settings.py`, just find this lines and un-comment them and the content the variables have:
```
SPIDER_MIDDLEWARES
DOWNLOADER_MIDDLEWARES
ITEM_PIPELINES
```

### This will let you use the middlewares for scrapy, to see it just check the `middlewares.py` file in this project.

### Now, to finish the initial setup, we need spiders, which is the real target on creating this. To create a spider is necessary that you are inside the root folder of a scrapy project (root folder is where `scrapy.cfg` file will be) and run the command:

`scrapy genspider <spider_name> <url>`

### Where `<spider_name>` is the name the will have the .py file created and `<url>` is the main url where the spider will start scraping (For this project, we are using `basic`, `selenium`, and `splash` to make examples).

#### For more reference about this: [Click here](https://docs.scrapy.org/en/latest/topics/commands.html#std:command-genspider)

### This way, our project's new structure is: 

```
scrapy.cfg
<project_name>/
	__init__.py
	items.py
	middlewares.py
	pipelines.py
	settings.py
	spiders/
		__init__.py
		basic.py
		selenium.py
		splash.py
```

### Now lets talk about the content on each file and what are they for.

## scrapy.cfg

### This file is created by default, and contains some configurations for the settings inside the project, and indications for deployment.

## Items.py

### Inside this file it is possible to define the fields that the spider will have as its output, this output is usually a dictionary, containing the scraped data, to be processed later.

## middlewares.py

### Here are contained some standard classes from scrapy, whose code will execute in a determinate moment in the spider's life cicle. There is more information about this in the file itself.

## Pipelines.py

### After the spider's work is done, the information returned by it, goes somewhere, inside this file, it is possible to transform every item returned by the parse functions, after being crawled. That is why it is called pipelines.

## Settings.py

### This is basically the place where you switch some configurations for the entire project to work. You activate and deactivate middlewares, pipelines, proxy, etc in this place. It is very important and have a huge amount of different settings that can be used.


### Those are basically all the files in a basic project, the spiders files will have their explanation inside themselves. Like how they work.

# For a more detailed documentation go to scrapy's official [documentation.](https://docs.scrapy.org/en/latest/index.html)