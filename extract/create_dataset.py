import cv2
import os

def extract_images(vid_path, data_path):
    """
    The number of frames can get from video:
        frames = second * FPS
    Examples with a 10 minutes video in 60 FPS we can get:
        600 * 60 = 36000 frames
    So if we want to extract every 10 frames per second:
        36000 / 10 = 3600 frames
    """

    video = cv2.VideoCapture(vid_path)

    current_frame = 0
    saved_count = 0

    while (True):

        success, frame = video.read()

        if not success:
            print("Finished video")
            break

        # Save every 10th frame
        if current_frame % 10 == 0:

            file_name = os.path.join(
                data_path,
                f'frame_{saved_count:06d}.jpg'
            )

            cv2.imwrite(file_name, frame)

            cv2.imshow('Output', frame)

            saved_count += 1

        current_frame += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    print("Saved:", saved_count)