class ProductImage:

    def _init_(self,hasDuplicate,duplicateName,imageId,imageSize):
        self.hasDuplicate=hasDuplicate
        self.duplicateName=duplicateName
        self.imageId = imageId
        self.imageSize = imageSize
       

    def getImageId(self):
        return self.imageId

    def getImageSize(self):
        return self.imageSize

    def getHasDuplicat(self):
        return self.isDuplicate

    def setImageId(self, imageId):
        self.imageId = imageId

    def setImageSize(self, imageSize):
        self.imageSize = imageSize

    def setHasDuplicate(self, isDuplicate):
        self.isDuplicate = isDuplicate