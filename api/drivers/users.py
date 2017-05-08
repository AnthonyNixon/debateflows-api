import dbConnect

# Set up DB connection
db = dbConnect.connect()
cursor = db.cursor()

def get_users():
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    users = []

    for row in results:
        result = {'id': row[0], 'email': row[1], 'firstname': row[2],
                  'lastname': row[3], 'passwordhash': row[4], 'salt': row[5],
                  'usertype': row[6]}
        users.append(result)

    return users


def get_user(user_id):
    print "Getting user with ID: " + str(user_id)
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    result = cursor.fetchone()

    if result:
        user = {'id': result[0], 'email': result[1], 'firstname': result[2],
            'lastname': result[3], 'passwordhash': result[4], 'salt': result[5],
            'usertype': result[6]}

        return user
    else:
        return {}