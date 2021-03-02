class Seller:

    def __init__(self,sellerUserName,sellerId,feedbackScore,positiveFeedbackPercent,topRatedSeller):
        self.__sellerUserName=sellerUserName
        self.sellerId=sellerId
        self.feeedbackScore=feedbackScore
        self.positiveFeedbackPercent=positiveFeedbackPercent
        self.topRatedSeller=topRatedSeller

    def getSellerUserName(self):
        return self.sellerUserName

    def getSellerId(self):
        return self.sellerId

    def getFeedbackScore(self):
        return self.feeedbackScore

    def getPositiveFeedbackPercent(self):
        return self.positiveFeedbackPercent

    def getTopRatedSeller(self):
        return self.topRatedSeller

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