import sys
import cv2
import os

def detect_faces(image_path):
    haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Не удалось загрузить изображение по пути: {image_path}")
        sys.exit(1)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5, minSize=(30, 30))
    
    print(f"Найдено лиц: {len(faces)}")
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    output_path = 'output.jpg'
    cv2.imwrite(output_path, image)
    print(f"Результат сохранён в {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = os.path.join(os.path.dirname(__file__), 'image.jpg')
    
    detect_faces(image_path)

