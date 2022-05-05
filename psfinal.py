from passporteye import read_mrz
import cv2
import os



# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread("britishp.jpg")
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w] 
    print("[INFO] Object found. Saving locally.") 
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color) 
# Process image
mrz = read_mrz("britishp.jpg")

# Obtain image
mrz_data = mrz.to_dict()

print('Nationality :'+ mrz_data['nationality'])
print('Given Name :'+ mrz_data['names'])
print('Surname :'+ mrz_data['surname'])
print('Passport type :'+ mrz_data['type'])
print('Date of birth :'+ mrz_data['date_of_birth'])
print('ID Number :'+ mrz_data['personal_number'])
print('Gender :'+mrz_data['sex'])
print('Expiration date :'+ mrz_data['expiration_date'])
print(mrz_data,file=open('passportdata.csv',"a"))
print(mrz_data,file=open('passportdata.json',"a"))
nft_desc=('Nationality :'+ mrz_data['nationality'] + 'Given Name :'+ mrz_data['names'] + 'Surname :'+ mrz_data['surname'] + 'Passport type :'+ mrz_data['type'] + 'Date of birth :'+ mrz_data['date_of_birth'] + 'ID Number :'+ mrz_data['personal_number'] + 'Gender :'+mrz_data['sex'] + 'Expiration date :'+ mrz_data['expiration_date'])



os.system("arweave deploy /Users/aryankaushik/Downloads/pss/6565_faces.jpg --key-file /Users/aryankaushik/Downloads/arweave-key-xvDg99sDJZtQMK_WCWZk0h6IJqSBDPuNuzx8WipKnjQ.json")






