#! python3
import twitter, datetime

""" psuedo code
-search for contetst tweets
--retweet to win
--follow original poster
---make sure not to retweet a contest entry but the original poster
-obey the rate limites
--dont tweet too often
--dont retweet to agressively
--dont create following churn
---only follow the most recent 2000 people
"""

# Load the configuration from the JSON file.
## Open config.json and load it to a dictionary

# Assign the variables loaded in the dictionary to idividual variables

# Set up global variables
## assign twitter API to an object with the consumer/access keys and tokens variables assigned previously.
## create empty list called post_list
## create empty list called ignore_list
## create list called ratelimit
## create list called ratelimit_search

# conditional if statement checking if there is a an ignore list
## if true loads the ignore list file and exports it to the ignore_list list

# function definition for LogAndPrint taking 'text' as a parameter
## creates str called tmp loading the str method with text as a aurgument
## modifies the str tmp with replace method changing newlines to blank ("").
## prints the str tmp variable
## creates a file object called f_log which opens (creates) a file called 'log' as append)
## writes to the log file the str variable tmp with a newline appened after the variable.
## closes the file object

# function definition for CheckError taking 'r' as a parameter
## Converts 'r' to a JSON object.
## Conditional if statement checking for the string 'errors' in the r json object.
### If true calls the function LogAndPrint with string and error codes

# function definition for CheckRateLimit with no paramter
## 