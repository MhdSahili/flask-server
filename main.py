import twitter as twitterPremier
import pymongo


client = pymongo.MongoClient("localhost", 27017)
db = client.local
collection = db.PremierLeagueA
collection2 = db.hashtags
requesting = []


query = "#premierleague until:2021-10-03 since:2021-10-01 near:London within:4000km"
scraper1 = twitterPremier.TwitterSearchScraper(query)

Tweets = []
limit = 5000

for i, tweet in enumerate(scraper1.get_items()):
    if len(Tweets) == limit:
        break
    else:
        Tweets.append({"userName": tweet.user.username, "accountCreated": tweet.user.created,
                       "date": tweet.date, "dateString": f"{tweet.date.year}-{tweet.date.month}-{tweet.date.day}",
                       "day": tweet.date.day, "month": tweet.date.month, "year": tweet.date.year,
                       "hour": tweet.date.hour, "text": tweet.content, "userFollowers": tweet.user.followersCount,
                       "isVerified": tweet.user.verified, "profilePicture": tweet.user.profileImageUrl,
                       "mentionString": f"{tweet.mentionedUsers}", "email": tweet.user.linkUrl, "email1": tweet.user.linkTcourl,
                       "verified": "Verified" if tweet.user.verified == True else "Unverified",
                       "likes": tweet.likeCount, "accountCreatedYear": tweet.user.created.year,
                       "accountCreatedMonth": tweet.user.created.month, "link": tweet.url,
                       "retweets": tweet.retweetCount, "label": (tweet.sourceLabel).rpartition("Twitter for ")[2],
                       "reply": tweet.replyCount, "hashtags": tweet.hashtags, "userLink": tweet.user.url,
                       "location1": tweet.user.location, "coordinates": f"{tweet.coordinates}",
                       "longitude": tweet.coordinates.longitude, "latitude": tweet.coordinates.latitude})

x = collection.insert_many(Tweets)
