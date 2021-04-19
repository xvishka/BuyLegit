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

# ALGO : Inserting it to the database for Category.
def insertingCategory(cateId,Category):
    cursor = database.cursor()
    cursor.execute("""INSERT INTO Category (CategoryId ,Category )
                    VALUES (%s,%s);""",(cateId,Category))
    database.commit()

# ALGO : getting data from the list and inserting it to the database for Unique Products.
def insertingUniqueProducts(itemId,rank,title,categoryId,url,selName,feedS,posFeed,topRate,price,img,hasDupli):
    cursor = database.cursor()
    cursor.execute("""INSERT INTO UniqueProducts (ItemId,ProductRank ,Title,CategoryId,
                    Url,SellerUserName,FeedbackScore,
                    PostiveFeedbackPercent,TopRatedSeller,Price,Image,HasDuplicate)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );""",(itemId,rank,title,categoryId,url,selName,feedS,posFeed,topRate,price,img,hasDupli))
    database.commit()

# ALGO : getting data from the list and inserting it to the database for Duplicate Products.
def insertingDuplicateProducts(itemId,title,categoryId,url,selName,feedS,posFeed,topRate,price,img,masterId):
    cursor = database.cursor()
    cursor.execute("""INSERT INTO DuplicateProducts (ItemId,Title,CategoryId,
                    Url,SellerUserName,FeedbackScore,
                    PostiveFeedbackPercent,TopRatedSeller,Price,Image,masterId)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );""",(itemId,title,categoryId,url,selName,feedS,posFeed,topRate,price,img,masterId))
    database.commit()

# all product list from the json
productList = []
similarityList = []

try:
    f = open('ApicemData.json',)
    data = json.load(f)

    for q in data['products']:
        productList.append(q)

    f.close()

except:
    print("'ApicemData.json' File not Found")

try:
    # Load Unique data and duplicate dat separately
    ml = open('similarity.json',)
    mlData = json.load(ml)

    for k in mlData:
        similarityList.append(k)
    ml.close()
except:
    print("'similarity.json' File not Found")

listItems = []
listItems2 = []

if(len(similarityList) != 0):
    for r in similarityList:
        master = r['master_pi']
        if master not in listItems:
            items = []
            listItems.append(master)
            items.append(master)
            for l in similarityList:
                if(master == l['similar_pi']):
                    listItems.append(l['master_pi'])
                    items.append(l['master_pi'])
            listItems2.append(items)  
        
print(listItems2)

# get product category details
if(len(productList) != 0):
    findCategoryProduct = productList[0]
    findCategoryId = findCategoryProduct['categoryId']
    findCategoryName = findCategoryProduct['category']

# INSERT CATEGORY DETAILS TO CATEGORY TABLE
try:
    insertingCategory(findCategoryId, findCategoryName)
except:
    print("This category: " , findCategoryName, " already exists!")

# before adding duplicated recommended products
print("Length before adding duplicated Recommended Products ", len(productList))
       
# sort product list according to the product price
def sortPrice(dataList:list):
    listLength = len(dataList)
    
    if listLength != 0:
        for i in range(listLength-1):
            for j in range(0,listLength-i-1):

                product_j = dataList[j]
                product_k = dataList[j+1]

                price_j =product_j["price"]
                price_k =product_k["price"]
                
            
                if(float(price_j) > float(price_k)):
                    dataList[j],dataList[j+1] = dataList[j+1],dataList[j]

# sort product list according to the positive feedback score
def sortPositiveFeedbackScore(dataList:list):
    
    listLength = len(dataList)
    if listLength != 0:
        for i in range(listLength-1):
            for j in range(0,listLength-i-1):

                product_j = dataList[j]
                product_k = dataList[j+1]

                sellerData_j = product_j["seller"]
                sellerData_k = product_k["seller"]
                feedbackScore_j = sellerData_j["feedbackScore"]
                feedbackScore_k = sellerData_k["feedbackScore"]

                if(int(feedbackScore_j[0]) < int(feedbackScore_k[0])):
                    dataList[j],dataList[j+1] = dataList[j+1],dataList[j]

# sort product list according to the feedback percentage
def sortPositiveFeedbackPercentage(dataList:list):
    listLength = len(dataList)
    
    if listLength != 0:
         for i in range(listLength-1):
             for j in range(0,listLength-i-1):

                product_j = dataList[j]
                product_k = dataList[j+1]

                sellerData_j = product_j["seller"]
                sellerData_k = product_k["seller"]
                feedbackScorePercent_j = sellerData_j["positiveFeedbackPercent"]
                feedbackScorePercent_k = sellerData_k["positiveFeedbackPercent"]
                product_j = dataList[j]
                product_k = dataList[j+1]

                if(float(feedbackScorePercent_j[0]) < float(feedbackScorePercent_k[0])):
                    dataList[j],dataList[j+1] = dataList[j+1],dataList[j]

#sort final output lis according to the top rated seller
def sortTopRatedSellers(dataList:list):
    listLength = len(dataList)

    if listLength != 0:
          for i in range(listLength-1):
              for j in range(0,listLength-i-1):

                product_j = dataList[j]
                product_k = dataList[j+1]

                sellerData_j = product_j["seller"]
                sellerData_k = product_k["seller"]
                topRatedValue_j = sellerData_j["topRatedSeller"]
                topRatedValue_k = sellerData_k["topRatedSeller"]

                if(topRatedValue_j[0] == "false" ) and (topRatedValue_k[0] == "true"):
                    dataList[j],dataList[j+1] = dataList[j+1],dataList[j]

def sortFinalOutput(dataList:list):

    originalProductList_2 = dataList.copy()
    length = len(dataList)

    recomendProducts = []
    sortPrice(dataList)

    recomendProducts.append(dataList[0])

    sortPositiveFeedbackScore(originalProductList_2)
    recomendProducts.append(originalProductList_2[0])

    totalPrice = 0
    price_j = 0

    for j in range(length):
        product_j = dataList[j]
        price_j =product_j["price"]
        totalPrice = totalPrice + float(price_j) 

    # Find product price average
    priceAverage = totalPrice / len(dataList)

    priceRecommendedProduct = recomendProducts[0]
    price = priceRecommendedProduct["price"]

    priceAveragePercentage = ((priceAverage - float(price)) / priceAverage) * 100

    totalFeedbackScore = 0
    feedBackScoreIntValue = 0
    feedbackScoreList = [] 

    for j in range(length):
        product_j = originalProductList_2[j]
        seller_j = product_j["seller"]
        feedbackScoreList = seller_j["feedbackScore"]
        feedBackScoreIntValue = feedbackScoreList[0]
        totalFeedbackScore = totalFeedbackScore + int(feedBackScoreIntValue)

    # Find product price average
    feedbackAverage = totalFeedbackScore / len(dataList)

    recommendedFeedbackScoreProduct = recomendProducts[1]

    seller = recommendedFeedbackScoreProduct["seller"]
    feedbackScore = seller["feedbackScore"]

    feedbackScoreAveragePercentage = ((feedbackAverage - float(feedbackScore[0])) / feedbackAverage) * 100

    finalOutput = []

    if(priceAveragePercentage > feedbackScoreAveragePercentage):
        finalOutput = dataList.copy() 
    elif(priceAveragePercentage < feedbackScoreAveragePercentage):
        finalOutput = originalProductList_2.copy()
    else:
        product_1 = recomendProducts[0]
        product_1_seller = product_1["seller"]
        feedbackPrecentage_1 = product_1_seller["positiveFeedbackPercent"]
        precentage_1_IntValue = float(feedbackPrecentage_1[0])

        product_2 = recomendProducts[1]
        product_2_seller = product_2["seller"]
        feedbackPrecentage_2 = product_2_seller["positiveFeedbackPercent"]
        precentage_2_IntValue = float(feedbackPrecentage_2[0])
        if(precentage_1_IntValue < precentage_2_IntValue):
            finalOutput = originalProductList_2.copy()
        else:
            finalOutput = dataList.copy() 

    # sort final output lis according to the top rated seller
    sortTopRatedSellers(finalOutput)

    return finalOutput

similarProductList = []

if(len(listItems2) != 0):
    for i in listItems2:
        duplicateList = i
        duplicateProductList = []

        for j in duplicateList:
            duplicateItem = j

            for k in productList:    
                idNumber = k["itemId"]
            
                if (idNumber == duplicateItem):
                    getProduct = k
                    duplicateProductList.append(getProduct)
                    productList.remove(getProduct)
                
        #sort duplicate product list
        tempList = []
        tempList = sortFinalOutput(duplicateProductList)

        masterId = tempList[0]

        for a in tempList:
            if(masterId != a):
                a["isDuplicate"] = masterId["itemId"]
                similarProductList.append(a)
            else:
                # print("master: " , a["itemId"])
                a["isDuplicate"] = "true"

        # print(tempList[0])
        productList.append(tempList[0])

# after adding duplicated recommended products
print("Length after adding duplicated Recommended Products ", len(productList)) 

recommendedUniqueProductList = []
recommendedUniqueProductList = sortFinalOutput(productList)

# define the product rank
for c in range(len(recommendedUniqueProductList)):
    product = recommendedUniqueProductList[c]      
    # Recommended product Rank start with 0
    product['productRank'] = c

#convert categoryId to int
categoryIdForDB = int(findCategoryId)

# WRITE UNIQUE RECOMMENDED PRODUCTS TO THE DATABASE
if(len(recommendedUniqueProductList) != 0):
    for x in recommendedUniqueProductList:
        uniqueProduct = x
        uniqueProductId = uniqueProduct['itemId']
        uniqueProductRank = uniqueProduct['productRank']
        uniqueProductTitle = uniqueProduct['title']
        uniqueProductUrl = uniqueProduct['url']

        uniqueProductSeller = uniqueProduct['seller']

        uniqueProductSellerUserName = uniqueProductSeller['sellerUserName'][0]
        uniqueProductFeedbackScore = uniqueProductSeller['feedbackScore'][0]
        uniqueProductPostiveFeedbackPercent = uniqueProductSeller['positiveFeedbackPercent'][0]
        uniqueProductTopRatedSeller = uniqueProductSeller['topRatedSeller'][0]

        uniqueProductPrice = uniqueProduct['price']
        uniqueProductImage = uniqueProduct['image']
        uniqueProductDuplicate = uniqueProduct['isDuplicate']

        # print(uniqueProductId)

        try:
            insertingUniqueProducts(uniqueProductId, uniqueProductRank, uniqueProductTitle, categoryIdForDB, uniqueProductUrl, 
                            uniqueProductSellerUserName, uniqueProductFeedbackScore, uniqueProductPostiveFeedbackPercent, uniqueProductTopRatedSeller,
                            uniqueProductPrice, uniqueProductImage, uniqueProductDuplicate)
        except:
            print("No more products to add to Unique product table!")
            break

# WRITE THE DUPLICATED NON-RECOMMENDED PRODUCTS TO THE DATABASE
if(len(similarProductList) != 0):
    for s in similarProductList:
        similarProduct = s
        similarProductId = similarProduct['itemId']
        similarProductTitle = similarProduct['title']
        similarProductUrl = similarProduct['url']

        similarProductSeller = similarProduct['seller']

        similarProductSellerUserName = similarProductSeller['sellerUserName'][0]
        similarProductFeedbackScore = similarProductSeller['feedbackScore'][0]
        similarProductPostiveFeedbackPercent = similarProductSeller['positiveFeedbackPercent'][0]
        similarProductTopRatedSeller = similarProductSeller['topRatedSeller'][0]

        similarProductPrice = similarProduct['price']
        similarProductImage = similarProduct['image']
        similarProductDuplicate = similarProduct['isDuplicate']
        # print(similarProduct)

        try:
            insertingDuplicateProducts(similarProductId, similarProductTitle, categoryIdForDB, similarProductUrl, similarProductSellerUserName,
                                        similarProductFeedbackScore, similarProductPostiveFeedbackPercent, similarProductTopRatedSeller, 
                                        similarProductPrice, similarProductImage, similarProductDuplicate)
        except:
            print("No more products to add to duplicate Products table!")
            break

app.run()

