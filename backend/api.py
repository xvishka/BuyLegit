import flask
from flask import request, jsonify
import json
import csv
from flask_cors import CORS
import pymysql

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
def getAllProducts(requestedCategoryId:str):

    categoryId = int(requestedCategoryId)

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    WHERE CategoryId = %s 
                    ORDER BY  ProductRank ;""", (categoryId))
    allProducts = cursor.fetchall()
    return allProducts

# return sorted price list
def getAllProductsSortedByPrice(requestedCategoryId:str):
    categoryId = int(requestedCategoryId)

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    WHERE CategoryId = %s 
                    ORDER BY  Price ;""", (categoryId))
    priceSortedProducts = cursor.fetchall()
    return priceSortedProducts

# return requeted Unique product list 
def getRequestedUniqueProduct(requestedUniqueItemId:str):
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    WHERE ItemId = %s ; """, (requestedUniqueItemId))
    requestedUniqueProduct = cursor.fetchall()
    return requestedUniqueProduct

# return requeted duplicated product list 
def getRequestedDuplicateProduct(requestedItemId:str):
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM DuplicateProducts
                    WHERE MasterId = %s ; """, (requestedItemId))
    requestedProduct = cursor.fetchall()
    return requestedProduct

# return sorted feedback score list
def getAllProductsSortedByFeedbackScore(requestedCategoryId:str):
    categoryId = int(requestedCategoryId)

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM UniqueProducts
                    WHERE CategoryId = %s 
                    ORDER BY  FeedbackScore DESC ;""", (categoryId))
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

@app.route('/', methods=['GET'])
def home():
    return "<h1> BuyLegit data set !</p>"

# Return all category details
@app.route('/category', methods=['GET'])
def api_category():
    return jsonify(categoryList)

# Return all original product list
@app.route('/product/all', methods=['GET'])
def api_all():

    if 'categoryId' in request.args:
        categoryId = request.args['categoryId']

    else:
        return "Error: No id field provided. Please specify an categoryId."

    allProductList = getAllProducts(categoryId)
    return jsonify(allProductList)

# return selected unique item according to requested item ID
@app.route('/product/unique', methods=['GET'])
def api_unique_id():

    if 'itemId' in request.args:
        itemId = request.args['itemId']

    else:
        return "Error: No id field provided. Please specify an id."

    requestedUniqueProduct = getRequestedUniqueProduct(itemId)

    print("PRINT " , requestedUniqueProduct)
    return jsonify(requestedUniqueProduct)


# return selected duplicate item list according to requested item ID
@app.route('/product/duplicate', methods=['GET'])
def api_duplicate_id():

    if 'itemId' in request.args:
        itemId = request.args['itemId']

    else:
        return "Error: No id field provided. Please specify an id."

    requestedDuplicateProductList = getRequestedDuplicateProduct(itemId)

    print("PRINT " , requestedDuplicateProductList)
    return jsonify(requestedDuplicateProductList)


# return selected duplicate item according to requested item ID
@app.route('/product/result', methods=['GET'])
def api_result_id():

    if 'itemId' in request.args:
        itemId = request.args['itemId']

    else:
        return "Error: No id field provided. Please specify an id."

    requestedDuplicateProduct = getRequestedDuplicateProduct(itemId)
    requestedUniqueProduct = getRequestedUniqueProduct(itemId)

    finalResult = []
    # append recommended duplicate product(s) to result List
    finalResult.append(requestedDuplicateProduct) 

    # append recommended unique product to result List
    # NOTE THAT THIS WILL APPEND AS THE LAST INDEX
    finalResult.append(requestedUniqueProduct)

    print(finalResult)
    return jsonify(finalResult)

# Return all products sort according to the price
@app.route('/product/all/priceSort', methods=['GET'])
def api_all_priceSort():

    if 'categoryId' in request.args:
        categoryId = request.args['categoryId']

    else:
        return "Error: No id field provided. Please specify an categoryId."

    priceSortedProductList = getAllProductsSortedByPrice(categoryId)

    return jsonify(priceSortedProductList)

# Return all products sort according to the feedback score
@app.route('/product/all/feedbackScoreSort', methods=['GET'])
def api_all_feedbackScoreSort():

    if 'categoryId' in request.args:
        categoryId = request.args['categoryId']
    else:
        return "Error: No id field provided. Please specify an categoryId."

    feedbackScoreSortedProductList = getAllProductsSortedByFeedbackScore(categoryId)

    return jsonify(feedbackScoreSortedProductList)

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

# app.run()