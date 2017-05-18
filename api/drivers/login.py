import dbConnect
import hashlib

def authenticate(login_data):
    db = dbConnect.connect()
    cursor = db.cursor()

    if not login_data['email'] and login_data['password']:
        return -1
    else:
        print "logging in..."
        print login_data
        email = login_data['email']
        password = login_data['password']
        passwordHash = hashlib.sha512(password).hexdigest()

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        result = cursor.fetchone()
        db.close()

        if result:
            user = {'id': result[0], 'email': result[1], 'firstname': result[2],
                    'lastname': result[3], 'passwordhash': result[4], 'salt': result[5],
                    'usertype': result[6]}
            if user['passwordhash'] == passwordHash:
                return 200, user
            else:
                return 401, {}
        else:
            return 404, {}

