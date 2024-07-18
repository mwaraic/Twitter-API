# Twitter API


## **Run commands:**

docker compose build <br/>
docker compose up<br/>

## **Test:** <br/>
docker compose exec python bash<br/>
python manage.py test<br/>


## **URL:**<br/>
127.0.0.1:8000 <br/>

## **APIs:**

### User Authentication

- **POST** `/account/login`
  - Login with credentials.

- **POST** `/account/signup`
  - Register a new user.

### Messages

- **GET** `/messages/<userID>`
  - Retrieve messages for a specific user.

- **POST** `/messages/<userID>`
  - Send a message to a user.

### Tweets

- **GET** `/mytweets/`
  - Retrieve tweets for the authenticated user.

- **POST** `/mytweets/`
  - Create a new tweet for the authenticated user.

- **PUT** `/mytweets/<tweetID>`
  - Update a specific tweet.

- **DELETE** `/mytweets/<tweetID>`
  - Delete a specific tweet.

### Retweet

- **POST** `/retweet/<tweetID>`
  - Retweet a specific tweet.

### Like/Unlike

- **GET** `/likes/`
  - Retrieve tweets liked by the authenticated user.

- **POST** `/likes/<tweetID>`
  - Like a specific tweet.

- **DELETE** `/likes/<tweetID>`
  - Unlike a specific tweet.

### Thread

- **POST** `/thread/`
  - Create a new thread.

- **GET** `/thread/`
  - Retrieve all threads.

### Thread Tweets

- **POST** `/thread/<threadID>`
  - Create a new tweet within a thread.

- **GET** `/thread/<threadID>`
  - Retrieve tweets within a specific thread.

### Additional APIs

#### Friends

- **POST** `/friends/`
  - Add a friend for the authenticated user.

- **DELETE** `/friends/<userID>`
  - Remove a friend.

#### Profile

- **GET** `/profile/<userID>`
  - Retrieve the tweet timeline of a specific user.

#### Home

- **GET** `/home/`
  - Retrieve tweets from the authenticated user and their friends.
