# Who Follows My Friends? 

In this short exercise, I wanted to explore the popularity of the people/organizations (users) I follow on Twitter. 
Since I joined Twitter back in 2009, it has evolved tremendously and I imagine people use it differently--I know I do. 
When I first joined, I only followed friends and some famous names. Since then, however, Twitter for me has become less of a way to connect with friends, but more of an information channel where I follow more famous names than people I personally know. 

Along this vein, I wanted to explore how popular are the users that I follow? Are the majority of them companies or celebrities that have millions of followers? Have the people I know personally grown to have large followerships? 

I follow about 110 users on Twitter, but capturing the followership of all 110+ users would be tedious on the Twitter API (https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids; http://docs.tweepy.org/en/v3.5.0/) and cumbersome to plot on Gephi (https://gephi.org/). 

I learned the hardships of rate limits early (referring to the "tedious on the Twitter API" above) and decided to get information on every 5th user I follow on Twitter, which at the time equated to 22 users. For the 22 users, I used Tweepy to get all their followers. The Twitter API returns 5,000 followers at a time per user (per page), which I thought could be good testing ground. For the 22 users, this returned over 56,000 users, which when plotted on Gephi was difficult to discern and burdensome on its in-built network algorithms (referring the the "cumbersome to plot on Gephi" above). 

Here's an image of 56,000+ nodes and their edges (representing users and connections): 
![alt text](Personal-Projects/56000nodes.png)
