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

def load_img(path):

  img = tf.io.read_file(path)
  img = tf.io.decode_jpeg(img, channels=3)
  img = tf.image.resize_with_pad(img, 224, 224)
  img  = tf.image.convert_image_dtype(img, tf.float32)[tf.newaxis, ...]

  return img
def cluster():

  start_time = time.time()
  
  # Defining data structures as empty dict
  file_index_to_file_name = {}
  file_index_to_file_vector = {}
  #file_index_to_product_id = {}

  # Configuring annoy parameters
  dims = 1792
  n_nearest_neighbors = 20
  trees = 10000

  # Reads all file names which stores feature vectors 
  allfiles = glob.glob('images/*.npz')

  t = AnnoyIndex(dims, metric='angular')

  for file_index, i in enumerate(allfiles):
    
    # Reads feature vectors and assigns them into the file_vector 
    file_vector = np.loadtxt(i)

    # Assigns file_name, feature_vectors and corresponding product_id
    file_name = os.path.basename(i).split('.')[0]
    file_index_to_file_name[file_index] = file_name
    file_index_to_file_vector[file_index] = file_vector
    

    # Adds image feature vectors into annoy index   
    t.add_item(file_index, file_vector)

  # Builds annoy index
  t.build(trees)
  
  named_nearest_neighbors = []

  # Loops through all indexed items
  for i in file_index_to_file_name.keys():

    # Assigns master file_name, image feature vectors and product id values
    master_file_name = file_index_to_file_name[i]
    master_vector = file_index_to_file_vector[i]

    # Calculates the nearest neighbors of the master item
    nearest_neighbors = t.get_nns_by_item(i, n_nearest_neighbors)

    # Loops through the nearest neighbors of the master item
    for j in nearest_neighbors:

      # Assigns file_name, image feature vectors and product id values of the similar item
      neighbor_file_name = file_index_to_file_name[j]
      neighbor_file_vector = file_index_to_file_vector[j]

      # Calculates the similarity score of the similar item
      similarity = 1 - spatial.distance.cosine(master_vector, neighbor_file_vector)
      rounded_similarity = int((similarity * 10000)) / 10000.0

      # Appends master product id with the similarity score 
      # and the product id of the similar items
      if(rounded_similarity>0.9 and master_file_name != neighbor_file_name):
        named_nearest_neighbors.append({
          'similarity': rounded_similarity,
          'master_pi': master_file_name,
          'similar_pi':neighbor_file_name})
        
  print ("Similarity score calculation - Finished ") 

  # Writes the 'named_nearest_neighbors' to a json file
  with open('similarity.json', 'w') as out:
    json.dump(named_nearest_neighbors, out)

  print ("Data stored in 'nearest_neighbors.json' file ") 
  print("--- Prosess completed in %.2f minutes ---------" % ((time.time() - start_time)/60))

def main():

  i = 0

  start_time = time.time()

  # Definition of module with using tfhub.dev handle
  module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4" 
  
  # Load the module
  module = hub.load(module_handle)

  # Loops through all images in a local folder
  for filename in glob.glob('images/*.jpg'): #assuming gif
    i = i + 1

    # Loads and pre-process the image
    img = load_img(filename)

    # Calculate the image feature vector of the img
    features = module(img)   
  
    # Remove single-dimensional entries from the 'features' array
    feature_set = np.squeeze(features)  

    # Saves the image feature vectors into a file for later use

    outfile_name = os.path.basename(filename).split('.')[0] + ".npz"
    out_path = os.path.join('images/', outfile_name)

    # Saves the 'feature_set' to a text file
    np.savetxt(out_path, feature_set, delimiter=',')

  print("---------------------------------")
  print ("Generating Feature Vectors - Completed at %s" %time.ctime())
  print("--- %.2f minutes passed ---------" % ((time.time() - start_time)/60))
  print("--- %s images processed ---------" %i)
  print("---------------------------------\n")
  cluster()

main()