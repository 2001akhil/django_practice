import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('your_connection_string')
database = client['your_database_name']
users_collection = database['users']

# 1. Create (Insert) Operation:
# Insert a single document
user_data = {'username': 'john_doe', 'email': 'john@example.com'}
users_collection.insert_one(user_data)

# Insert multiple documents
additional_users = [
    {'username': 'jane_doe', 'email': 'jane@example.com'},
    {'username': 'bob_smith', 'email': 'bob@example.com'}
]
users_collection.insert_many(additional_users)

# 2. Read Operation:
# Find one document
result = users_collection.find_one({'username': 'john_doe'})
print(result)

# Find all documents
all_users = users_collection.find()
for user in all_users:
    print(user)

# 3. Update Operation:
# Update a document
users_collection.update_one({'username': 'john_doe'}, {'$set': {'email': 'new_email@example.com'}})

# Update multiple documents
users_collection.update_many({'email': {'$regex': 'example\.com'}}, {'$set': {'status': 'active'}})

# 4. Delete Operation:
# Delete a document
users_collection.delete_one({'username': 'john_doe'})

# Delete multiple documents
users_collection.delete_many({'status': 'inactive'})
