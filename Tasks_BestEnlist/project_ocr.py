import cv2
import pytesseract
import img2pdf
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
img = cv2.imread("img1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
rect_Kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(18,18))
dilation = cv2.dilate(thresh1,rect_kernel,iteration = 1)
contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
inm = img.copy()
file  = open("recognized.txt","w++")
file.write("")
file.close()
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    rect = cv2rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2)
    cropped = im2[y:y + h, x:x + w]
    file = open("recognized.txt","a")
    text = pytesseract.image_to_string(cropped)
    file.write(text)
    file.close
pdfdata=img2pdf.convert('recognized.txt')
file = open("myreport3.pdf","wb")
file.write(pdfdata)
file.close()