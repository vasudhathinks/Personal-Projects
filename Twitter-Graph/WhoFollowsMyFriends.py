"""
This project requires Python 2.7. It maps users I follow on Twitter and their followers.
I used the Twitter API as implemented by Tweepy.
The corresponding write-up can be found at:
https://github.com/vasudhathinks/Personal-Projects/tree/master/Twitter-Graph
"""

# Set up environment
import csv
import json
import tweepy


# Function to load necessary keys needed to run the API
def loadKeys(key_file):
    with open(key_file) as json_data:
        keys_dict = json.load(json_data)
    return keys_dict['api_key'], keys_dict['api_secret'], keys_dict['token'], keys_dict['token_secret']


# Load keys from a separate file (not shared, and one should not share)
KEY_FILE = 'keys.json'
api_key, api_secret, token, token_secret = loadKeys(KEY_FILE)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)


# Get the root-user's friends (being followed by root-user): root-user -> friend
def getFriends(api, root_user):
    api.wait_on_rate_limit = True
    api.wait_on_rate_limit_notify = True
    api.retry_count = 2
    api.retry_delay = 10
    api.timeout = 120
    friends_tuple_list = []
    friends_ids = api.friends_ids(root_user)
    for i in friends_ids:
        friend_screen_name = str(api.get_user(i).screen_name)
        friend_tuple_entry = (root_user, friend_screen_name)
        friends_tuple_list.append(friend_tuple_entry)
    return friends_tuple_list


# Function to convert list of tuples to a csv
def writeToFile(data, output_file):
    b = open(output_file, 'wb')
    a = csv.writer(b)
    for i in data:
        a.writerow(i)
    b.close()
    pass


# Acquire my friends (users I follow)
vasudhathinks_friends_tuple_list = getFriends(api, 'vasudhathinks')
writeToFile(vasudhathinks_friends_tuple_list, 'vasudhathinks_primary_friends.csv')
print(len(vasudhathinks_friends_tuple_list))  # Output: 112

# Capturing followership of 112 users is going to be very tedious (b/c of API rate limits)
# and very difficult to plot (b/c of the sheer amount of nodes that will be captured)
# so I will capture information about every 5th user I began to follow from the start ~> 22 users
vthinks_every_5th_friend = []
for i in range(int(len(vasudhathinks_friends_tuple_list) / 5)):
    vthinks_every_5th_friend.append(vasudhathinks_friends_tuple_list[5 * i][1])
print(len(vthinks_every_5th_friend))  # Output: 22


# Function to capture the friends' followers: follower -> friend, with input as a list
def getNextLevelFollowers(api, friend_list, no_of_followers):
    api.wait_on_rate_limit = True
    api.wait_on_rate_limit_notify = True
    api.retry_count = 2
    api.retry_delay = 10
    api.timeout = 120
    friends_followers = []
    for primary_friend in friend_list:
        followers_ids_list = api.followers_ids(primary_friend, count=no_of_followers)
        for follower_id in followers_ids_list:
            # follower_screen_name = str(api.get_user(follower_id).screen_name) # too many API calls, not necessary
            follower_tuple_entry = (follower_id, primary_friend)
            friends_followers.append(follower_tuple_entry)
    return friends_followers


# Isolate the friends column for next step
vasudhathinks_friends_list = []
for i in range(len(vthinks_every_5th_friend)):
    vasudhathinks_friends_list.append(vthinks_every_5th_friend[i][1])

# Acquire the followers of my friends (only first 1,000 followers to have a reasonable number of nodes for Gephi)
vthinks_5th_friends_followers_tuple_list = getNextLevelFollowers(api, vasudhathinks_friends_list, 1000)
writeToFile(vthinks_5th_friends_followers_tuple_list, 'vthinks_5th_friends_followers.csv')

# Use the 2 csv outputs to graph on Gephi
