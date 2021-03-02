class ProductImage:

    def __init__(self,imageId,imageSize,isDuplicate):
        self.imageId = imageId
        self.imageSize = imageSize
        self.isDuplicate = isDuplicate

    def getImageId(self):
        return self.imageId

    def getImageSize(self):
        return self.imageSize

    def getIsDuplicat(self):
        return self.isDuplicate

    def setImageId(self, imageId):
        self.imageId = imageId

    def setImageSize(self, imageSize):
        self.imageSize = imageSize

    def setIsDuplicate(self, isDuplicate):
        self.isDuplicate = isDuplicate
