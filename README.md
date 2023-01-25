# cyberSecurityTool
Script to create sales-sounding description for some IT security tool.
Even the name of the repo has that whiff of what you would expect for 
a tool advert aimed at managers.

Impress your friends! Be the life of the party!

## Usage
For now its config filename, `data.json` is hardcoded into the script so
it require no arguments. That of course can be changed later.

### Sample output
I like to see a given tool in action.
Output sentences have been split for readability.

```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our disruptive tool implements a Data-driven design enabling you 
to amplify the positive impact of the visibility of your verticals 
by using our intent-driven interface.
user@desktop:~/cyberSecurityTool$ 
```
```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our trendsetting tool implements a Zero Trust deployment enabling 
you to increase the visibility of the ROI of your non-tangible 
assets by using our intent-driven interface.
user@desktop:~/cyberSecurityTool$ 
```
```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our disruptive tool implements a passwordless methodology enabling 
you to amplify the positive impact of the ROI of your verticals by 
using our continuous monitoring interface.
user@desktop:~/cyberSecurityTool$ 
```

## Requirements
- Python 3
- The 
[random](https://docs.python.org/3/library/random.html) 
and 
[json](https://docs.python.org/3/library/json.html) 
python libraries. Chances are they came in your python install, but I want
to make sure you are aware of them.

## History
Long time ago when I was in high school I found an old book or magazine
at the school library 
with a bunch of programming exercises in basic of all languages; this was
not a rich school. Amongst those programs, there was one I still (vaguely) 
remember. It picked 3 strings at random from 3 arrays (one string per array) 
and then would use them to craft a jargon-filled sentence in 
[economese](https://en.wiktionary.org/wiki/economese) on how to fix the
economy. Yes, that amused me to no end; I thought it was clever specially
because the author took the time to ensure the strings would seamless fit in
their respective places in the sentence.

Unfortunately I cannot name the book. I wish I had written it down. 

This script is my humble homage to that code. I wrote it aimed at the computer
security community because after reading a few articles and watching 
infomercials disguised as webinars, the original code poped back into my mind
screaming "it is the same thing with different buzzwords!" 

Its initial version was done in
October of 2022. At that time I thought it was not enough with it to make it publicly 
available, so I left it alone. 
Fast forward a bit, I cleaned up the code a bit (will not claim it
is full [PEP 8](https://peps.python.org/pep-0008/) compliant, but it sure is
much closer than what I had before), put its strings
in a JSON config file (still wondering if that was a good idea), and here it 
is.

If you know where the original economese version was published, please let
me know so I can properly acknowledge I got here by standing on the shoulders
of giants.

### Plot Twist 
Recently I found out the original idea was created by 
Philip Broughton, who 
proposed a more management-oriented version it in the article 
"How to Win at Wordsmanship", 
supposedly (I will remove that word as soon as I can
confirm the original source down to the issue number; too many online 
references just repeat each other) 
published in a 1968 issue of [Newsweek](https://www.newsweek.com/). 
This article described the "Systematic 
Buzz Phrase Projector," which works as follows:

1. Think of 3 numbers between 0 and 9.
1. For each column on the table below, pick the buzzword whose row matches the 
number you picked. So, if you picked `0`, `7`, and `5`, you end up with 
"integrated incremental concept."

   | |Column 1 | Column 2 | Column 3 |
   |-|---------|----------|----------|
   |0| integrated| management| options|
   |1| total | organizational | flexibility|
   |2| systematized | monitored | capability|
   |3| parallel | reciprocal | mobility|
   |4| functional | digital | programming|
   |5| responsive | logistical | concept|
   |6| optional | transitional | time-phase|
   |7| synchronized | incremental | projection|
   |8| compatible | third-generation | hardware|
   |9| balanced | policy | contingency|

3. Enjoy how this generated phase adds a ring of decisive, knowledgeable
authority to any report. 

## To be done
This may currently look like a very small script but I think it has a lot of
entertainment potential. If you want to contribute, please fork it! Some
of the items in the to-do list are

1. More acronyms. A lot of infomercials disguise themselves as webinars, 
articles, and whitepapers. And they, and their presenters, seem to love 'em 
acronyms. 
1. More buzzwords. You can't have too many buzzwords.
1. Rename the fields. Calling them patternN was done to get it working but
is not very helpful.
1. Add option to feed the config file from command line?
1. Con others to help improve this extremely useful script
