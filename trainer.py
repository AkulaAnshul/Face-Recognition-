import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "D:/Coding/Python/Face Recognition/dataset"

def get_images_with_id(path):
    images_path = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for single_image_path in images_path:
        faceImg = Image.open(single_image_path).convert('L')
        faceNp = np.array(faceImg, np.uint8)
        id = int(os.path.split(single_image_path)[-1].split(".")[1])
        print(f"ID: {id}")
        
        # Resize all images to a fixed size (e.g., 200x200)
        faceNp = cv2.resize(faceNp, (200, 200))
        
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)

    return np.array(ids), faces

ids, faces = get_images_with_id(path)

# Convert faces list to a NumPy array after ensuring consistent dimensions
faces = np.array(faces)

recognizer.train(faces, ids)
recognizer.save("D:/Coding/Python/Face Recognition/recognizer/trainingdata.yml")
cv2.destroyAllWindows()
