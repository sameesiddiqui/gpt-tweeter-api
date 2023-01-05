import os
import tweepy
from fastapi import FastAPI
from fastapi import HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()
load_dotenv()

# Authenticate to Twitter
api = tweepy.Client(
  consumer_key=os.getenv("CONSUMER_KEY"),
  consumer_secret=os.getenv("CONSUMER_SECRET"),
  access_token=os.getenv("ACCESS_TOKEN"),
  access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

class Tweet(BaseModel):
    text: str

@app.post("/postTweet")
def post_tweet(tweet: Tweet):
    print("Posting tweet: ", tweet.text)
    try:
        api.create_tweet(text=tweet.text)
        return {"status": "success"}
    except tweepy.TweepyException as e:
        print (e)
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def read_root():
    return {"Hello": "World"}