from flask import Flask, request, jsonify, Response, json
import pymysql.cursors
import datetime

app = Flask(__name__)
connection = pymysql.connect(host="clothly.cxk0kbqodnhw.us-east-1.rds.amazonaws.com", port=3306, db="clothly", user="admin", password="hackerman123")

@app.route("/")
def home():
    return Response('No Content', status=204)

@app.route("/api/createDonor", methods=['GET', 'POST'])
def donorRegister():
    content = request.json
    firstName = content["firstName"]
    lastName = content["lastName"]
    password = content["password"]
    address = content["address"]
    city = content["city"]
    state = content["state"]
    zipcode = content["zip"]
    email = content["emailAddress"]
    phoneNumber = content["phoneNumber"]

    query = 'INSERT INTO donor (firstName, lastName, password, address, city, state, zip, emailAddress, phoneNumber) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", "%s");' % (
        firstName, lastName, password, address, city, state, zipcode, email, phoneNumber)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Error', status=500)
    return Response('Success', status=200)


@app.route("/api/createOrganization", methods=['GET', 'POST'])
def organizationRegister():
    content = request.json
    firstName = content["firstName"]
    lastName = content["lastName"]
    orgType = content["orgType"]
    password = content["password"]
    address = content["address"]
    city = content["city"]
    state = content["state"]
    zipcode = content["zip"]
    email = content["emailAddress"]
    phoneNumber = content["phoneNumber"]

    query = 'INSERT INTO organization (firstName, lastName, password, address, city, state, zip, emailAddress, phoneNumber, orgType) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", "%s", "%s");' % (
        firstName, lastName, password, address, city, state, zipcode, email, phoneNumber, orgType)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Error', status=500)
    return Response('Success', status=200)

@app.route("/api/donorLogin", methods=['GET', 'POST'])
def donorLogin():
    content = request.json
    email = content["emailAddress"]
    password = content["password"]
    correctPassword = ""
    query = 'SELECT password FROM donor WHERE emailAddress = "%s";' % (email)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            correctPassword = cursor.fetchone()[0]
    except:
        return Response('Error', status=500)
    if password == correctPassword:
        return Response('Success', status=200)
    return Response('Wrong password', status=400)


@app.route("/api/organizationLogin", methods=['GET', 'POST'])
def organizationLogin():
    content = request.json
    email = content["emailAddress"]
    password = content["password"]
    correctPassword = ""
    query = 'SELECT password FROM organization WHERE emailAddress = "%s";' % (email)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            correctPassword = cursor.fetchone()[0]
    except:
        return Response('Error', status=500)
    if password == correctPassword:
        return Response('Success', status=200)
    return Response('Wrong password', status=400)

@app.route("/api/getDonors", methods=['GET'])
def getAllDonors():
    query = 'SELECT * FROM donor;'
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            connection.commit()
    except:
        return Response('Unable to retrieve donors', status=500)
    responseData = {
        "data": data,
        "count": len(data)
    }
    js = json.dumps(responseData)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/api/getPendingDonations", methods=['GET'])
def getPendingDonations():
    donorId = 1
    query = 'SELECT * FROM donation WHERE donorId = %d AND pickedUp = 0' % (donorId)
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    except:
        return Response('Unable to retrieve donations', status=500)
    responseData = {
        "data": data,
        "count": len(data)
    }
    js = json.dumps(responseData)
    return Response(js, status=200, mimetype='application/json')


@app.route("/api/getPastDonations", methods=['GET'])
def getPastDonations():
    donorId = 1
    query = 'SELECT * FROM donation WHERE donorId = %d AND pickedUp = 1 ORDER BY pickUpDate DESC;' % (
        donorId)
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    except:
        return Response('Unable to retrieve donations', status=500)
    responseData = {
        "data": data,
        "count": len(data)
    }
    js = json.dumps(responseData)
    return Response(js, status=200, mimetype='application/json')

@app.route("/api/updateDonation", methods=['POST'])
def updateDonation():
    content = request.json
    donationType = content["type"]
    gender = content["gender"]
    ageGroup = content["ageGroup"]
    instructions = content["instructions"]
    quantity = content["quantity"]
    pickUpDate = content["pickUpDate"]
    donationId = content["donationId"]

    query = 'UPDATE donation SET type = "%s", gender = "%s", ageGroup = "%s", instructions = "%s", quantity = %d, pickUpDate ="%s" WHERE donationId = %d' % (donationType, gender, ageGroup, instructions, quantity, pickUpDate, donationId)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Unable to update donation', status=500)
    return Response('Success', status=200)


@app.route("/api/markPickedUp", methods=['POST'])
def markAsPickedUp():
    content = request.json
    donationId = content["donationId"]
    query = 'UPDATE donation SET pickedUp = 1 WHERE donationId = %d' % (donationId)
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    return Response('Success', status=200)

@app.route("/api/deleteDonation", methods=['POST'])
def deleteDonation():
    content = request.json
    donationId = content["donationId"]
    query = 'DELETE FROM donation WHERE donationId = %d' % (donationId)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Unable to delete donation', status=500)
    return Response('Success', status=200)

@app.route("/api/createDonation", methods=['GET', 'POST'])
def addDonation():
    content = request.json
    donationType = content["type"]
    gender = content["gender"]
    ageGroup = content["ageGroup"]
    instructions = content["instructions"]
    orgId = content["orgId"]
    quantity = content["quantity"]
    pickUpDate = content["pickUpDate"]
    donorId = content["donorId"]
    query = 'INSERT INTO donation (type, gender, agegroup, instructions, orgId, quantity, pickUpDate, donorId) VALUES ("%s", "%s", "%s", "%s", %d, %d, "%s", %d);' % (donationType, gender, ageGroup, instructions, orgId, quantity, pickUpDate, donorId)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Error', status=500)
    return Response('Success', status=200)


if __name__ == "__main__":
    app.run(
    host=os.getenv('LISTEN', '0.0.0.0'),
    port=int(os.getenv('PORT', '80')))
