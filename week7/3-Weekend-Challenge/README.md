# A simple weekend challenge

Now, we know a lot of different things - HTTP, how to crawl websites, how to store data in `sqlite`.

Now, lets combine that into something more advanced.

We are going to upgrade the [1-Scan-Bg-Web problem](https://github.com/HackBulgaria/Programming101-3/tree/master/week7/1-Scan-Bg-Web) by adding few more things:

* We want to crawl more websites. Lets say, crawl the entire [start.bg](http://www.start.bg/). We want everything we can get out of there.
* Store the data in a `sqlite` database! **Crawl only websites that have not been crawled before!**. This will make our script more useful since if we crawl 10k sites and something breaks down at the 9999th, we are going to lose the entire information we have :( So add a database!
* Make the script crawl every day, lets say at 12:30PM. [Figure out how to make this.](https://help.ubuntu.com/community/CronHowto)
* Of course, have a script that exports the data in a histogram, using **matplotlib**

That's it.

Good luck!

