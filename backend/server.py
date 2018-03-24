from flask import Flask, request, jsonify
import pymysql.cursors
import datetime

app = Flask(__name__)
connection = pymysql.connect(host="clothly.cxk0kbqodnhw.us-east-1.rds.amazonaws.com", port=3306, db="clothly", user="admin", password="hackerman123")

@app.route("/")
def home():
    return "working 123"

@app.route("/api/createDonor", methods=['GET', 'POST'])
def donorRegister():
    myData = {"firstName": "Danny", "lastName": "Lin", "password": "hackerman123", "address": "6 Metrotech Center", "city": "Brooklyn", "state": "New York", "zip": 11201, "emailAddress": "danny.lin@nyu.edu", "phoneNumber": "19173990398"}
    firstName = myData["firstName"]
    lastName = myData["lastName"]
    password = myData["password"]
    address = myData["address"]
    city = myData["city"]
    state = myData["state"]
    zipcode = myData["zip"]
    email = myData["emailAddress"]
    phoneNumber = myData["phoneNumber"]

    query = 'INSERT INTO donor (firstName, lastName, password, address, city, state, zip, emailAddress, phoneNumber) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", "%s");' % (
        firstName, lastName, password, address, city, state, zipcode, email, phoneNumber)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        print("error")
    return "hello"

@app.route("/api/getDonors", methods=['GET'])
def getAllDonors():
    query = 'SELECT * FROM donor;'
    data = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            connection.commit()
    except:
        return "error"
    print(data)
    return "success"

@app.route("/api/getDonations", methods=['GET'])
def getDonations():
    orgId = 1
    query = 'SELECT * FROM donation WHERE orgId = %d AND pickedUp = 0' % (orgId)
    data = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    except:
        return "Error"
    print(data)
    return "success!"

@app.route("/api/markPickedUp", methods=['POST'])
def markAsPickedUp():
    donationId = 1
    query = 'UPDATE donation SET pickedUp = 1 WHERE donationId = %d' % (donationId)
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    return True

@app.route("/api/deleteDonation", methods=['POST'])
def deleteDonation():
    donationId = 1
    query = 'DELETE FROM donation WHERE donationId = %d' % (donationId)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return False
    return True

@app.route("/api/createDonation", methods=['GET', 'POST'])
def addDonation():
    now = datetime.datetime(2009, 5, 5)
    myData = {"type": "Clothing", "gender": "M", "ageGroup": "Adult", "instructions": "N/A", "orgId": 1, "quantity": 10, "pickUpDate": now, "donorId": 1}
    donationType = myData["type"]
    gender = myData["gender"]
    ageGroup = myData["ageGroup"]
    instructions = myData["instructions"]
    orgId = myData["orgId"]
    quantity = myData["quantity"]
    pickUpDate = myData["pickUpDate"]
    donorId = myData["donorId"]
    query = 'INSERT INTO donation (type, gender, agegroup, instructions, orgId, quantity, pickUpDate, donorId) VALUES ("%s", "%s", "%s", "%s", %d, %d, "%s", %d);' % (donationType, gender, ageGroup, instructions, orgId, quantity, pickUpDate, donorId)
    print(query)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        return "error"
    return "success"


if __name__ == "__main__":
    app.run()
