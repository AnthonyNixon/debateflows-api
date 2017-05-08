import dbConnect
import MySQLdb

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


def new_user(user_data):
    print user_data
    if not user_data['firstname'] and user_data['lastname'] and user_data['email'] and user_data['passwordhash']:
        return -1
    else:
        firstname = user_data['firstname']
        lastname = user_data['lastname']
        email = user_data['email']
        passwordhash = user_data['passwordhash']
        try:
            # Execute the SQL command
            cursor.execute('''INSERT INTO users (firstname, lastname, email, password, status) VALUES (%s, %s, %s, %s, 'student')''', (firstname, lastname, email, passwordhash))
            # Commit your changes in the database
            db.commit()
            print "worked"
            return cursor.lastrowid
        except:
            print "didn't work"
            db.rollback()
            return -1