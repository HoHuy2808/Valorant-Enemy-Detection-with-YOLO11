import os
from create_dataset import extract_images
from preprocess import find_and_remove_duplicates, shuffled_images

if __name__ == '__main__':
    os.makedirs("data", exist_ok=True)

    vid_path = "./video/VOD.mp4"
    data_path = "./data"

    # Extract data from video
    extract_images(vid_path, data_path)

    # Preprocessing
    find_and_remove_duplicates(data_path)

    shuffled_images(data_path)

    """ Optional """
    # Extract more data for roboflow
    os.makedirs("data_sub", exist_ok=True)
    vid_path_sub = "./video/VOD2.mp4"
    data_sub = "./data_sub"

    extract_images(vid_path_sub, data_sub)

    find_and_remove_duplicates(data_sub)