class Product:

    def __init__(self,productId,productTitle,productDesciption,productUrl,price,condition,currencyType,shipping,seller):
       
        self.productId=productId
        self.productTitle=productTitle
        self.productDesciption=productDesciption
        self.productUrl=productUrl
        self.price=price
        self.condition=condition
        self.currencyType=currencyType
        self.shipping=shipping
        self.seller=seller

 """   product1 = Product("P001p","Black Watch","AAAAAAAAABBBBBBB","prouduct1.url",254.25,"YES","Dollar","Free",Seller("Thiran","101125",12,75.24,True)
    """
     def getProductId(self):
        return self.productId

    def getProductTitle(self):
        return self.productTitle

    def getProductDesciption(self):
        return self.productDesciption

    def getProductUrl(self):
        return self.productUrl

    def getPrice(self):
        return self.price

    def getCondition(self):
        return self.condition

    def getCurrencyType(self):
        return self.currencyType

    def getShipping(self):
        return self.shipping

    def getSellerUserName(self):
        return self.sellerUserName

    def setProductId(self, productId):
        self.productId = productId

    def setProductTitle(self, productTitle):
        self.productTitle = productTitle

    def setProductDesciption(self, productDesciption):
        self.productDesciption = productDesciption

    def setProductUrl(self, productUrl):
        self.productUrl = productUrl

    def setPrice(self, price):
        self.price = price

    def setCondition(self, condition):
        self.condition = condition

    def setCurrencyType(self, currencyType):
        self.currencyType = currencyType

    def setShipping(self, shipping):
        self.shipping = shipping

    def setSellerUserName(self, sellerUserName):
        self.sellerUserName = sellerUserName