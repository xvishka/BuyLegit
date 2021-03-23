class BuyLegitService:
    
    # Declare an empty list to store unique products
    unique_product_list=[]

    #Declare an empty dictionary to store duplicate products 
    duplicat_product = dict(duplicateName:str , productList : list)

    def addProduct(product:Product):
        if not product.hasDuplicate:
            unique_product_list.append(product)
        else:
            if dict.has_key(duplicateName):
               temList =  duplicat_product.get(duplicateName)
               temList.append(product)
               duplicat_product[duplicateName] = temList
            else:
                duplicateName[duplicateName] = productList.append(product)


    #Sort product list according to price in ascending oreder
    def sortAlgorithmForPrice(productList:list):
        if not len(productList==0):
            listLength = len(productList)
            for i in range(listLength-1):
                for j in range(0,listLength-i-1):
                    if productList[j].price > productList[j+1].price :
                        productList[j],productList[j+1] = productList[j+1],productList[j]            

        else:
            print("Empty List !")       

    #Sort product list according to feedbackScore, positiveFeedbackPercent and soldItem in descending oreder
     def sortAlgorithm(productList:list):
        if not len(productList==0):
            listLength = len(productList)
            for i in range(listLength-1):
                for j in range(0,listLength-i-1):
                    if productList[j].feedbackScore < productList[j+1].feedbackScore :
                        productList[j],productList[j+1] = productList[j+1],productList[j]

            for i in range(listLength-1):
                for j in range(0,listLength-i-1):
                    if productList[j].positiveFeedbackPercent < productList[j+1].positiveFeedbackPercent :
                        productList[j],productList[j+1] = productList[j+1],productList[j]

            for i in range(listLength-1):
                for j in range(0,listLength-i-1):
                    if productList[j].soldItem < productList[j+1].soldItem :
                        productList[j],productList[j+1] = productList[j+1],productList[j]

        else:
            print("Empty List !")       


    