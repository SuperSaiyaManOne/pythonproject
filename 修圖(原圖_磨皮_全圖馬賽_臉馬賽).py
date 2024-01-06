import cv2
import os

def apply_mosaic(image, factor):# 馬賽克效果 方法
    height, width = image.shape[:2]# 獲取圖片大小
    small_img = cv2.resize(image, (width // factor, height // factor))# 縮小圖片
    result_img = cv2.resize(small_img, (width, height), interpolation=cv2.INTER_NEAREST)# 放大縮小後的圖片
    return result_img

def apply_mosaic_to_faces(image, factor):# 臉部馬賽克 方法
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')# 載入人臉識別器
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# 將圖片轉換為灰度
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))# 進行人臉檢測
    for (x, y, w, h) in faces:# 對每張臉應用馬賽克效果
        face_roi = image[y:y+h, x:x+w]
        face_mosaic = apply_mosaic(face_roi, factor)
        image[y:y+h, x:x+w] = face_mosaic
    return image

def replace_faces(image, replacement_image_path):  # 臉部換圖方法
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # 載入人臉識別器
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 將原圖轉換為灰度
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))  # 進行人臉檢測
    replacement_img = cv2.imread(replacement_image_path, -1)# 讀取替換圖片
    for (x, y, w, h) in faces:  # 遍歷每張臉，將臉部區域替換為替換圖片
        face_roi = image[y:y+h, x:x+w]
        replacement_img_resized = cv2.resize(replacement_img, (w, h))# 確保替換圖片和臉部區域大小相同
        image[y:y+h, x:x+w] = replacement_img_resized# 替換臉部區域

    return image


talk1 = input("請輸入要修改的圖片xxx.xxx ： \n")
# img1 = cv2.imread(r"C:\Users\a0930\Desktop\圖檔\pic\\"+talk1, -1)
img1 = cv2.imread(os.path.join(r"C:\Users\Jason\Downloads", talk1), -1)

factor = int(input("請輸入馬賽克的調整值（整數，例如5）：\n"))# 接收用戶輸入 factor 值

nr1, nc1 = img1.shape[:2]
nr2, nc2 = 300, int(300*nc1/nr1)

#-------------------------------------------
img01=cv2.resize(img1, (nc2, nr2), interpolation = cv2.INTER_LINEAR )# 原始圖片調整為新的大小
cv2.imshow("Original Image", img01)# 顯示圖片高度300像素寬度照比例

# img1 = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
img2 = cv2.bilateralFilter(img01, 11, 50, 50 )# 雙邊濾波器
cv2.imshow("Bilateral Filtering", img2)# 顯示圖片 紋理進行平滑(磨皮效果)

mosaic_img = apply_mosaic(img01, factor=factor)# 將整張圖片套用馬賽克
cv2.imshow("Mosaic Effect", mosaic_img)# 顯示圖片factor處理馬賽克大小

mosaic_img_faces = apply_mosaic_to_faces(img01, factor=factor)# 將馬賽克只套用臉部
cv2.imshow("Mosaic Effect on Faces", mosaic_img_faces)# 顯示圖片factor處理馬賽克大小
#-------------------------------------------

#-----------------還沒成功待修改-------------
# replacement_image_path = input("請輸入用於替換臉部的圖片文件名(xx.xxx)： \n")# 讀取替換臉部的圖片xx.xxx
# replacement_image_path = os.path.join(r"C:\Users\Jason\Downloads", replacement_image_path)# 讀取替換臉部的圖片路徑
# replacement_img = cv2.imread(replacement_image_path, -1)# 讀取替換圖片
# replaced_img = replace_faces(img01, replacement_image_path)# 將臉部區域替換為另一張圖片
# cv2.imshow("Replaced Faces", replaced_img)# 將臉部區域替換為另一張圖片
cv2.waitKey(0)# 任意按鍵，然後關閉顯示的窗口
#-------------------------------------------

# file_path = os.path.join(r"C:\Users\j2172\Downloads\PycharmProjects", talk1)
# img1 = cv2.imread(file_path, -1)
# print(file_path)
# if img1 is None:
#     print("Error: Unable to read the image")
# else:
#     nr1, nc1 = img1.shape[:2]
#     nr2, nc2 = 300, int(300 * nc1 / nr1)
#     img1 = cv2.resize(img1, (nc2, nr2), interpolation=cv2.INTER_LINEAR)
#     img2 = cv2.bilateralFilter(img1, 11, 50, 50)
#     cv2.imshow("Original Image", img1)
#     cv2.imshow("Bilateral Filtering", img2)
#     cv2.waitKey(10000)

