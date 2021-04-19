import flask
from flask import request, jsonify
import json
import csv
from flask_cors import CORS
import pymysql
import re

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

# Conneting Database
database = pymysql.connect(
    host='apicem-db.cud06hsz15em.us-east-2.rds.amazonaws.com',
    user='admin',
    port = 3306,
    password = "admin123",
    db='buylegit',
    )

# get category details
def getCategoryDetails():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Category")
    details = cursor.fetchall()
    return details

# load for home page
def getAllProducts():
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    ORDER BY  ProductRank """)
    allProducts = cursor.fetchall()
    return allProducts

# return sorted price list
def getAllProductsSortedByPrice():
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    ORDER BY  Price """)
    priceSortedProducts = cursor.fetchall()
    return priceSortedProducts

# return requeted duplicated product list 
def getRequestedProduct(requestedItemId:str):
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM DuplicateProducts
                    WHERE MasterId = %s ; """, (requestedItemId))
    requestedProduct = cursor.fetchall()
    return requestedProduct

# return sorted feedback score list
def getAllProductsSortedByFeedbackScore():
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    ORDER BY  FeedbackScore DESC""")
    FeedbackScoreSortedProducts = cursor.fetchall()
    return FeedbackScoreSortedProducts

def getSearchedProduct(requestedProductName:str):
    search = '%' + requestedProductName + '%'
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    WHERE Title LIKE %s ; """, (search))
    searchResult = cursor.fetchall()
    return searchResult

categoryList = getCategoryDetails()
allProductList = getAllProducts()
priceSortedProductList = getAllProductsSortedByPrice()
FeedbackScoreSortedProductList = getAllProductsSortedByFeedbackScore()

# Return all category details
@app.route('/category', methods=['GET'])
def api_category():
    return jsonify(categoryList)

# Return all original product list
@app.route('/product/all', methods=['GET'])
def api_all():
    return jsonify(allProductList)

# return selected item according to requested item ID
@app.route('/product', methods=['GET'])
def api_id():

    if 'itemId' in request.args:
        itemId = request.args['itemId']

    else:
        return "Error: No id field provided. Please specify an id."

    requestedDuplicateList = getRequestedProduct(itemId)

    print("PRINT " , requestedDuplicateList)
    return jsonify(requestedDuplicateList)

# Return all products sort according to the price
@app.route('/product/all/priceSort', methods=['GET'])
def api_all_priceSort():
    return jsonify(priceSortedProductList)

# Return all products sort according to the feedback score
@app.route('/product/all/feedbackScoreSort', methods=['GET'])
def api_all_feedbackScoreSort():
    return jsonify(FeedbackScoreSortedProductList)

# return selected item according to requested title
@app.route('/product/search', methods=['GET'])
def api_search():

    if 'title' in request.args:
        title = request.args['title']
        
    else:
        return "Error: No id field provided. Please specify an title."

    searchProductDetails = getSearchedProduct(title)
    return jsonify(searchProductDetails)

# with open('allProducts.json', 'w') as out:
#     json.dump(allProductList, out)

app.run()