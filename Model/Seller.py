class Seller:
    def __init__(self,sellerUserName,sellerId,feedbackScore,positiveFeedbackPercent,topRatedSeller,soldItem):
        self.__sellerUserName=sellerUserName
        self.__sellerId=sellerId
        self.__feeedbackScore=feedbackScore
        self.__positiveFeedbackPercent=positiveFeedbackPercent
        self.__topRatedSeller=topRatedSeller
        self._soldItem=soldItem


    def setSellerUserName(self,sellerUserName):
        self.__sellerUserName=sellerUserName

    def getSellerUserName(self):
        return self.__sellerUserName

    def getSellerId(self):
        return self.__sellerId

    def getFeedbackScore(self):
        return self.__feeedbackScore

    def getPositiveFeedbackPercent(self):
        return self.__positiveFeedbackPercent=positiveFeedbackPercent

    def getTopRatedSeller(self):
        return self.__topRatedSeller=topRatedSeller

     def setSellerUserName(self,sellerUserName):
        self.sellerUserName = sellerUserName

    def setSellerId(self, sellerId):
        self.sellerId = sellerId

    def setFeeedbackScore(self, feedbackScore):
        self.feeedbackScore = feedbackScore

    def setPositiveFeedbackPercent(self, positiveFeedbackPercent):
        self.positiveFeedbackPercent = positiveFeedbackPercent

    def setTopRatedSeller(self, topRatedSeller):
        self.topRatedSeller = topRatedSeller



