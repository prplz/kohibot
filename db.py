from peewee import SqliteDatabase, Model, BigIntegerField, CharField

db = SqliteDatabase('kohibot.db')


class Tweet(Model):
    tweet_id = BigIntegerField(primary_key=True)
    text = CharField(max_length=250, null=False)
    user_id = BigIntegerField(null=False)
    user_name = CharField(max_length=32, null=False)

    @staticmethod
    def from_tweepy(tweet):
        return Tweet(
            tweet_id=tweet.id,
            text=tweet.full_text,
            user_id=tweet.user.id,
            user_name=tweet.user.screen_name)

    class Meta:
        database = db


db.create_tables([Tweet], True)