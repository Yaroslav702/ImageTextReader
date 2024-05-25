import os
import easyocr
import cv2
from difflib import SequenceMatcher

reader = easyocr.Reader(['uk'])

def get_text_from_image(image_path):
    result = reader.readtext(image_path, detail=0)

    return ' '.join(result)

def get_similar_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_matching_images(question, folder_path, threshold=0.5):
    result = list()

    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            text = get_text_from_image(image_path)
            if get_similar_ratio(question, text) >= threshold:
                result.append(image_path)
    return result

def main():
    question = input("Enter your question: ")
    folder_path = 'questions'

    matching_images = find_matching_images(question, folder_path)
    
    if matching_images:
        print(f"Found images: {matching_images}")

        for img in matching_images:
            image = cv2.imread(img)
            cv2.imshow('Found answer:', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("The image was not found.")

if __name__ == "__main__":
    main()
