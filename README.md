# Twitter-API


## **Run commands:**

docker compose build <br/>
docker compose up

## **Test:**
docker compose exec python bash
python manage.py test

## **APIs:**

### **User Login and Registration**<br/>
Send a **POST** request to account/login to login<br/>
Send a **POST** request to account/signup to register<br/>

### **Message**<br/>
Send a **GET** request to messages/<:userID> to retrieve a list
of messages <br/>
Send a **POST** request to messages/<:userID> to send a message<br/>

### **Tweet**<br/>
Send **GET** request on mytweets/ endpoint to 
retrieve the list of tweets for the user <br/>
Send a **POST** request with body property on mytweets/ endpoint to 
create a tweet <br/>
Send a **PUT** request on mytweets/<:tweetID> endpoint with
updated tweet data to update the tweet <br/>
Send a **DELETE** request on mytweets/<:tweetID> endpoint to
delete a tweet<br/>

### **Retweet**<br/>
Send a **POST** request on retweet/<:tweetID>
to retweet a tweet<br/>

### **Like/Unlike**<br/>
Send a **POST** request on likes/<:tweetID> endpoint
to like a tweet <br/>
Send a **DELETE** request on likes/<:tweetID> endpoint
to delete a tweet<br/>

### **Thread**<br/>
Send a **POST** request on thread/ to create
a new thread.<br/>
Send a **GET** request on thread/ to retrieve the 
list of threads.<br/>

### **ThreadTweet**<br/>
 Send a **POST** request on thread/<:threadID> with 
 tweet property to create a new tweet on a thread.<br/>
 Send a **GET** request on thread/<:threadID> to
 retrieve the list of tweets on a thread.<br/>

### **Additional:**<br/>

### **Friends**<br/>
Send a **POST** request with UserID value against handle2 property
to add a friend on friends/ endpoint <br/>
Send a **DELETE** request on friends/<:userID> endpoint 
to remove a friend<br/>

### **Home**<br/>
Send a **GET** request on home/ endpoint
to get the list of tweets of user and his friends<br/>






    
