# cyberSecurityTool
Script to create sales-sounding description for some IT security tool.
Even the name of the repo has that whiff of what you would expect for 
a tool advert aimed at managers.

## Usage
For now its config filename, `data.json` is hardcoded into the script so
it require no arguments. That of course can be changed later.

### Sample output

```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our disruptive tool implements a Data-driven design enabling you to amplify the positive impact of the visibility of your verticals by using our intent-driven interface.
```
```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our trendsetting tool implements a Zero Trust deployment enabling you to increase the visibility of the ROI of your non-tangible assets by using our intent-driven interface.
```
```bash
user@desktop:~/cyberSecurityTool$ ./cyberSecurityTool.py 
Our disruptive tool implements a passwordless methodology enabling you to amplify the positive impact of the ROI of your verticals by using our continuous monitoring interface.
user@desktop:~/cyberSecurityTool$ 
```

## History
I have had this script for a while (since October of 2022) but was never happy 
enough with it to make it publicly available.

## To be added
1. More acronyms. A lot of infomercials disguise themselves as webinars, 
articles, and whitepapers. And they, and their presenters, seem to love 'em 
acronyms. 
1. Rename the fields. Calling them patternN was done to get it working but
is not very helpful.
