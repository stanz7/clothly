from flask import Flask, request, jsonify, Response, json
from flask import render_template, redirect
import pymysql.cursors
import datetime
import os

app = Flask(__name__)
connection = pymysql.connect(host="clothly.cxk0kbqodnhw.us-east-1.rds.amazonaws.com", port=3306, db="clothly", user="admin", password="hackerman123")

# route index page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about_us.html")


@app.route("/contact")
def contact():
    return render_template("contact_us.html")


@app.route("/donations")
def donations():
    return render_template("donations.html")

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
        data = []
        query = 'SELECT * FROM donor WHERE emailAddress = "%s"' % (email)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            connection.commit()
        responseData = {
            "data": data
        }
        js = json.dumps(responseData)
        resp = Response(js, status=200, mimetype='application/json')
        return resp
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

@app.route("/api/getDonors", methods=['GET', 'POST'])
def getAllDonors():
    content = request.json
    orgId = content["orgId"]
    query = 'SELECT * FROM donation WHERE orgId = %d AND pickedUp = 0;' % (orgId)
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

@app.route("/api/getPastDonors", methods=['GET', 'POST'])
def getAllPastDonors():
    content = request.json
    orgId = content["orgId"]
    query = 'SELECT * FROM donation WHERE orgId = %d AND pickedUp = 1;' % (orgId)
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

@app.route("/api/getOrganizations", methods=['GET'])
def getAllOrganizations():
    query = 'SELECT * FROM organization;'
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            connection.commit()
    except:
        return Response('Unable to retrieve organizations', status=500)
    responseData = {
        "data": data,
        "count": len(data)
    }
    js = json.dumps(responseData)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/api/getPendingDonations", methods=['GET', 'POST'])
def getPendingDonations():
    content = request.json
    donorId = content["donorId"]
    query = 'SELECT * FROM donation WHERE donorId = %d AND pickedUp = 0' % (donorId)
    data = {}
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


@app.route("/api/getPastDonations", methods=['GET', 'POST'])
def getPastDonations():
    content = request.json
    donorId = content["donorId"]
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
    instructions = content["instructions"]
    quantity = content["quantity"]
    pickUpDate = content["pickUpDate"]
    donationId = content["donationId"]

    query = 'UPDATE donation SET type = "%s", instructions = "%s", quantity = %d, pickUpDate ="%s" WHERE donationId = %d' % (donationType, instructions, quantity, pickUpDate, donationId)
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
    query = 'SELECT pointValue, donorId FROM donation WHERE donationId = %d' % (donationId)
    pointValue = 0
    donorId = 0
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchone()
        pointValue = data[0]
        donorId = data[1]
        connection.commit()
    query = 'UPDATE donor SET points = points + %d WHERE donorId = %d' % (pointValue, donorId)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Unable to mark as picked up', status=500)
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
    instructions = content["instructions"]
    orgId = content["orgId"]
    quantity = content["quantity"]
    pickUpDate = content["pickUpDate"]
    donorId = content["donorId"]
    pointValue = 5 * quantity
    orgName = content["orgName"] 

    query = 'SELECT address, city, state, zip FROM donor WHERE donorId = "%s"' % (donorId)
    address = ""
    with connection.cursor() as cursor:
        cursor.execute(query)
        addressData = cursor.fetchone()
        address = " ".join(str(x) for x in addressData)
        connection.commit()
    
    query = 'SELECT firstName, lastName FROM donor WHERE donorId = "%s"' % (
        donorId)
    name = ""
    with connection.cursor() as cursor:
        cursor.execute(query)
        nameData = cursor.fetchone()
        name = " ".join(nameData)
        connection.commit()

    query = 'INSERT INTO donation (type, instructions, orgId, quantity, pickUpDate, donorId, pointValue, orgName, address, name) VALUES ("%s", "%s", %d, %d, "%s", %d, %d, "%s", "%s", "%s");' % (donationType, instructions, orgId, quantity, pickUpDate, donorId, pointValue, orgName, address, name)
    print(query)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return Response('Error', status=500)
    return Response('Success', status=200)


@app.route("/api/getDonorInfo", methods=['POST'])
def getDonorInfo():
    content = request.json
    donorId = content["donorId"]
    query = 'SELECT COUNT(*) FROM donation WHERE donorId = %d' % (donorId)
    totalDonations = 0
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            totalDonations = cursor.fetchone()[0]
    except:
        return Response('Unable to retrieve data', status=500)
    query = 'SELECT points FROM donor WHERE donorId = %d;' % (donorId)
    points = 0
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            points = cursor.fetchone()[0]
    except:
        return Response('Unable to retrieve data', status=500)
    responseData = {
        "totalDonations": totalDonations,
        "points": points
    }
    js = json.dumps(responseData)
    return Response(js, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(
    host=os.getenv('LISTEN', '0.0.0.0'),
    port=int(os.getenv('PORT', '80')))
