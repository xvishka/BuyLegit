import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import time
import glob
import os.path
import numpy as np
import json
from annoy import AnnoyIndex
from scipy import spatial


def clusterImages(category):

  # Staring a timer to get the time to process the Feature Vectors.
  startTimer = time.time()
  
  # Data Structures to store output results 
  fileNames = {}
  fileVectors = {}

  # Annoy parameters
  dimensions = 1792
  nearestNeighborsNodes = 20
  trees = 10000

  # Reads all files names which stores feature vectors from the directory. 
  directory = category.rstrip("\n")
  directoryPath = os.path.basename(directory).split('.')[0] + "/*.npz"
  allfiles = glob.glob(directoryPath)

  # Index that's read-write and stores vector of 1792 dimensions.
  indexAnnoy = AnnoyIndex(dimensions, metric='angular')

  for fileIndex, i in enumerate(allfiles):
    
    # Reads feature vectors and assigns them into the file_vector
    # Loads and assigns the feature vectors to the 'vector' Variable.
    vector = np.loadtxt(i)

    # Assigns the .npz file name which is the itemId of a product.
    itemId = os.path.basename(i).split('.')[0]
    
    # Appending the File Names to the python data structure. 
    fileNames[fileIndex] = itemId
    
    # Appending the Feature Vectors to the python data structure. 
    fileVectors[fileIndex] = vector
    
    #Assigns item index (any nonnegative integer) with image feature vectors.
    indexAnnoy.add_item(fileIndex, vector)

  # Builds annoy index
  # After calling build method, no more items can be added. 
  indexAnnoy.build(trees)
  
  processedSimilarImageList = [] # List which contains all the Similar Images


  # Loops within all the indexed items within the data structure.
  for i in fileNames.keys():

    # Assigns 'masterName' to the main file to be compared with the rest.
    masterName = fileNames[i]
    # Assigns 'masterVector' the feature vector of the 'masterName'.
    masterVector = fileVectors[i]

    # Calculates the nearest neighbors to the main item.
    # Returns a list of all nearest neighbors.
    nearestNeighbors = indexAnnoy.get_nns_by_item(i, nearestNeighborsNodes)

    # Loops through the nearest neighbors of the main item.
    for j in nearestNeighbors:
      
      # Assigns 'neighborName' with nearest neighbor to the main item.
      neighborName = fileNames[j]
      # Assigns 'neighborVector' the feature vector of the 'neighborName'.
      neighborVector = fileVectors[j]

      # Calculates the similarity score of the nearest neighbor item.
      # 'spatial.distance.cosine': Computes the Cosine distance between 1-D arrays
      similarity = 1 - spatial.distance.cosine(masterVector, neighborVector)

      #Rouding off the Similarity Score
      roundedSimilarity = int((similarity * 10000)) / 10000.0

      # Checks if the rounded similarity score is greater than '0.91'
      # Checks if the rounded similarity score is not equal to the main item.
      if(roundedSimilarity>0.91 and masterName != neighborName):
        # Appends master product id with the rounded similarity score 
        # and the product id of the similar items
        processedSimilarImageList.append({
          'similarity': roundedSimilarity,
          'master_pi': masterName,
          'similar_pi':neighborName})

  # Writes only the similarity indexes to a json file.
  jsonFile = os.path.basename(directory).split('.')[0] + "Similarity.json"
  with open(jsonFile, 'w') as out:
    json.dump(processedSimilarImageList, out)
  noOfSimilarImages = int(len(processedSimilarImageList)/2)
  print ("-------------Image Similarity ore Calculation ------------\n")
  print( "Time Completed at %s" %time.ctime())
  print("Proceesed Time   : %.2f minutes" % ((time.time() - startTimer)/60))
  print("No of Similar Images  : %d "% noOfSimilarImages)

def runDatabase(category):

  #Staring a timer to get the time to process the Feature Vectors.
  startTimer = time.time()

  #TF2 Saved Model to get feature vectors from images.
  handler = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"

  #Resolving a handle and loads the module results.
  moduleLoader = hub.load(handler)

  #Setting the Directory Path of a category
  directory = category.rstrip("\n")
  directoryPath = os.path.basename(directory).split('.')[0] + "/*.jpg"

  filecounter = 0
  # Getting all the images on the directory
  for file in glob.glob(directoryPath): 
    filecounter = filecounter + 1

    # Loads the image and pre-process the image using tensor.
    image = imageLoader(file)

    # Calculates the image feature vector from the tf module.
    features = moduleLoader(image)   
  
    # Removing 1-dimensional entries from the 'features' array
    featureSet = np.squeeze(features)  

    # Saving the feature vectors to the same directory as a npz file.
    # "npz" is a file format in numpy to store array data.
    directoryFile = os.path.basename(directory).split('.')[0] + "/"
    outputFile = os.path.basename(file).split('.')[0] + ".npz"
    path = os.path.join(directoryFile, outputFile)

    # Saves the 'featureSet' npz file
    np.savetxt(path, featureSet, delimiter=',')

  print ("----------------Feature Vectors Generated-----------------\n")
  print( "Time Completed at %s" %time.ctime())
  print("Proceesed Time   : %.2f minutes" % ((time.time() - startTimer)/60))
  print("Images Processed : %s \n" %filecounter)
  clusterImages(category)


def imageLoader(path):
  
  # Reads and Output file content
  image = tf.io.read_file(path)
  # Converting a jpeg image to a uint8 tensor
  # channels(How many color channels for decoded image)
  image = tf.io.decode_jpeg(image, channels=3)
  # Resize the image to 224px * 224px
  image = tf.image.resize_with_pad(image, 224, 224)
  # Converting image into data type object.
  image  = tf.image.convert_image_dtype(image, tf.float32)[tf.newaxis, ...]
  return image

def loopDirectory():
  directory = open('Directory.txt', 'r')
  row = directory.readlines()
  for line in row:
      print("\n       Processing Image Comparison for "+ line)
      runDatabase(line)
      
loopDirectory()
