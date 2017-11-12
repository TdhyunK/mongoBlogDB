import pymongo
# client = pymongo.MongoClient("mongodb://Team08:9vPYcYlOdB8dmFBe@mycluster0-shard-00-00-wpeiv.mongodb.net:27017,mycluster0-shard-00-01-wpeiv.mongodb.net:27017,mycluster0-shard-00-02-wpeiv.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")

client = pymongo.MongoClient("mongodb://Team08:9vPYcYlOdB8dmFBe@cluster0-shard-00-00-ppp7l.mongodb.net:27017,cluster0-shard-00-01-ppp7l.mongodb.net:27017,cluster0-shard-00-02-ppp7l.mongodb.net:27017/Team08DB?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.database_names()
print("db: " + str(db))

# # post blogName userName title postBody tags
# def post(blog_name, user_name, title, post_body, tags):



# # comment blogname entryID userName commentBody
# def comment(blog_name, entry_ID, user_name, comment_body):



# # delete blogname entryID userName
# def delete(blog_name, entry_ID, user_name):


# # show blogName
# def show(blog_name):

def user_query():
	user_query = input("Welcome to the journal database. Please enter your query")
	user_query = user_query.strip().split(" ")
	if user_query[0] == "post" and len(user_query) == 6:
		blog_name = user_query[1]
		user_name = user_query[2]
		title = user_query[3]
		post_body = user_query[4]
		tags = user_query[5]
		post(blog_name, user_name, title, post_body, tags)
	elif user_query[0] == "comment" and len(user_query) == 5:
		blog_name = user_query[1]
		entry_ID = user_query[2]
		user_name = user_query[3]
		comment_body = user_query[4]
	elif user_query[0] == "delete" and len(user_query) == 4:
		blog_name = user_query[1]
		entry_ID = user_query[2]
		user_name = user_query[3]
	elif user_query[0] == "show" and len(user_query) == 2:
		blog_name = user_query[1]
	else:
		print("Sorry, that is an invalid query. Please try another one.")


if __name__ == '__main__':
	while True:
		user_query()