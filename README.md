
==============
Yik Yak Command Line for College IT 
==============

Are students using YikYak to voice their concerns about broken printers and slow Wi-Fi?
Too underfunded to afford a full-time intern to browse YikYak?

Presenting: YikYakIT

Yik Yak Command Line + YakMining + CSV File Keyword search = Easy Life

YakMining adds a 'write to CSV' function to the Yik Yak Command Line. Then we can easily search the output file for key words such as "printer", "broken", "wifi", etc.

Run YikYak.py, enter your campus/location, and hit W to write Yaks to CSV file. Note: Make sure you have a valid User ID. 

Use the 'keywordsearch.py' script to search the CSV file for keywords. Edit the keywords as needed. 

Could be utilized to identify other types of issues on campus. 



To do: 


1. Figure out how to Chron this so it runs automatically every half-hour. 


Edit 1: March 2016
The geocoder broke, as warned, so the csv files with locations now point to the incorrect locations. 
Current workaround is to hardcode the latitude/longitude into the YikYak.py file. 

Also hid superfluous functions from showing up in the YikYakTerminal. 
These can be re-enabled by uncommenting the longer 'choice = ...' line, and commenting the shorter one below.


============

Forked from djtech42's Python Implementation of the pyak API by joseph346.
Check out https://github.com/djtech42/YikYakTerminal for instructions on how to install and use. 

See YakMining: http://duckpond.wesleyan.edu/2015/04/04/yakmining-part/ 
for how "Write to CSV" function was implemented
