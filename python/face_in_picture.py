from PIL import Image
import face_recognition

image = face_recognition.load_image_file("transcript.pdf")


face_locations in face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = IMage.fromarray(face_image)
    pil_image.show()
