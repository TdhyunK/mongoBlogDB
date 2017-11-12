import pymongo

client = pymongo.MongoClient("mongodb://Team08:9vPYcYlOdB8dmFBe@cluster0-shard-00-00-ppp7l.mongodb.net:27017,cluster0-shard-00-01-ppp7l.mongodb.net:27017,cluster0-shard-00-02-ppp7l.mongodb.net:27017/Team08DB?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.Team08DB
# db.blog.drop()
cursor = db.blog.find({})
for thing in cursor:
	print (thing)
# print("db: " + str(db))

post_counter = 0

# post blogName userName title postBody tags
def post(blog_name, user_name, title, post_body, tags):
	global post_counter
	result = db.blog.insert_one({
		"blog_name": blog_name,
		"user_name": user_name,
		"title": title,
		"post_body": post_body,
		"tags": tags,
		"comments": [],
		"entry_id": post_counter
		})
	post_counter += 1




# # comment blogname entryID userName commentBody
def comment(blog_name, entry_ID, user_name, comment_body):
	global post_counter
	found_id = db.blog.find_one({"entry_id": entry_ID, "blog_name": blog_name})
	comment_post = {"user_name" : user_name, "comment_body" : comment_body, "entry_id" : post_counter }
	if found_id:
		db.blog.update_one({"entry_id": entry_ID}, {'$push':{"comments": comment_post}})
	post_counter += 1




# # delete blogname entryID userName
# def delete(blog_name, entry_ID, user_name):


# # show blogName
# def show(blog_name):

def user_query():
	user_query = input("Welcome to the journal database. Please enter your query")
	user_query = user_query.strip().split(" ")
	if user_query[0] == "post" and (len(user_query) == 6 or len(user_query) == 5):
		blog_name = user_query[1]
		user_name = user_query[2]
		title = user_query[3]
		post_body = user_query[4]
		tags = user_query[5] if len(user_query) == 6 else None
		post(blog_name, user_name, title, post_body, tags)
	elif user_query[0] == "comment" and len(user_query) == 5:
		blog_name = user_query[1]
		entry_ID = user_query[2]
		user_name = user_query[3]
		comment_body = user_query[4]
		comment(blog_name, entry_ID, user_name, comment_body)
	elif user_query[0] == "delete" and len(user_query) == 4:
		blog_name = user_query[1]
		entry_ID = user_query[2]
		user_name = user_query[3]
		delete(blog_name, entry_ID, user_name)
	elif user_query[0] == "show" and len(user_query) == 2:
		blog_name = user_query[1]
		show(blog_name)
	else:
		print("Sorry, that is an invalid query. Please try another one.")


if __name__ == '__main__':
	while True:
		user_query()