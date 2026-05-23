import os
import random
import shutil
import imagehash
import numpy as np
from PIL import Image       

def shuffled_images(input_folder):
    if not os.path.exists("data_shuffled"):
        os.mkdir("data_shuffled")

    image_files = [f for f in os.listdir("data") if f.endswith(".jpg")]
    random.shuffle(image_files)
    for i, img in enumerate(image_files):
        src = os.path.join(input_folder, img)
        dst = os.path.join('data_shuffled', f"img_{i}.jpg")

        shutil.copy(src, dst)

def find_and_remove_duplicates(folder_path):
   # Dictionary to store image hashes
   hash_dict = {}
   duplicates = []
   # Iterate through all files in the folder
   for filename in os.listdir(folder_path):
       file_path = os.path.join(folder_path, filename)
       # Skip if not an image file
       if not os.path.isfile(file_path) or not filename.lower().endswith('.jpg'):
           continue
       try:
           # Compute hash of the image
           img_hash = imagehash.phash(Image.open(file_path))
           # Check if hash already exists
           if img_hash in hash_dict:
               duplicates.append(file_path) # Mark as duplicate
           else:
               hash_dict[img_hash] = file_path # Store unique hash
       except Exception as e:
           print(f"Error processing {file_path}: {e}")
   # Delete duplicate images
   for duplicate in duplicates:
       os.remove(duplicate)
       print(f"Deleted: {duplicate}")

