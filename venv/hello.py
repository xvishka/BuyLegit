import flask
from flask import request, jsonify
import json
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True

productList=[]
originalProductList_1=[]
originalProductList_2=[]

@app.route('/', methods=['GET'])
def home():
    return "<h1>!.!Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

f = open('ApicemData.json',)
#f = open('/Users/IIT/data.json',)

data = json.load(f)

for i in data['products']:
    productList.append(i)
f.close()

# Get copy list form original product list

print("Original list : ")
print(len(productList))

originalProductList_1 = productList.copy()
originalProductList_2 = productList.copy()

# return all products 
@app.route('/api/product/all', methods=['GET'])
def api_all():
    return jsonify(originalProductList_1)

# return selected item according to requested item ID

@app.route('/api/product', methods=['GET'])
def api_id():

    if 'itemId' in request.args:
        itemId = request.args['itemId']
        print(itemId)
       
    else:
        return "Error: No id field provided. Please specify an id."

    selectedProduct = []

    for product in originalProductList_1:
        print("product itemId: ", product['itemId'])
        print(itemId)
        if product['itemId'] == itemId:
            selectedProduct.append(product)
    print("selected product list: " , selectedProduct)

    return jsonify(selectedProduct)

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
                
# sort product list according to the product 
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

# sort product list according to the feedback score
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

#Sorted recommended products                  
recomendProducts = []     
                          
sortPrice(productList)

# Return all products sort according to the price
@app.route('/api/product/all/priceSort', methods=['GET'])
def api_all_priceSort():
    return jsonify(productList)

recomendProducts.append(productList[0])
# print(recomendProducts)
sortPositiveFeedbackScore(originalProductList_2)

# Return all products sort according to the feedback score
@app.route('/api/product/all/feedbackScoreSort', methods=['GET'])
def api_all_feedbackScoreSort():
    return jsonify(originalProductList_2)
    
recomendProducts.append(originalProductList_2[0])
print(recomendProducts)
print(len(recomendProducts))

length = len(productList)

totalPrice = 0
price_j = 0
for j in range(length):
    product_j = productList[j]
    price_j =product_j["price"]
    totalPrice = totalPrice + float(price_j) 

print("Total Price : ")
print(totalPrice)
# Find product price average
priceAverage = totalPrice / len(productList)
print("Price average  : ")
print(priceAverage)

priceRecommendedProduct = recomendProducts[0]
price =priceRecommendedProduct["price"]

priceAveragePercentage = ((priceAverage - float(price)) / priceAverage) * 100
print("Price percentage : ")
print(priceAveragePercentage)

totalFeedbackScore = 0
feedBackScoreIntValue = 0
feedbackScoreList = [] 

for j in range(length):
    product_j = originalProductList_2[j]
    seller_j = product_j["seller"]
    feedbackScoreList = seller_j["feedbackScore"]
    feedBackScoreIntValue = feedbackScoreList[0]
    totalFeedbackScore = totalFeedbackScore + int(feedBackScoreIntValue)

print("Total feedback score : ")
print(totalFeedbackScore)
# Find product price average
feedbackAverage = totalFeedbackScore / len(productList)
print("Feedback Score average  : ")
print(feedbackAverage)

recommendedFeedbackScoreProduct = recomendProducts[1]

seller = recommendedFeedbackScoreProduct["seller"]
feedbackScore = seller["feedbackScore"]

feedbackScoreAveragePercentage = ((feedbackAverage - float(feedbackScore[0])) / feedbackAverage) * 100
print("Feedback Score percentage : ")
print(feedbackScoreAveragePercentage)

#find final recommended product list
finalOutput =[]

if(priceAveragePercentage > feedbackScoreAveragePercentage):
    finalOutput = productList.copy() 
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
        finalOutput = productList.copy() 

print(finalOutput)
#sort final output lis according to the top rated seller
sortTopRatedSellers(finalOutput)

print(finalOutput)
print(len(productList))

#final output
@app.route('/api/product/all/finalProductList', methods=['GET'])
def api_all_finalProductList():

    return jsonify(finalOutput) 

app.run()
