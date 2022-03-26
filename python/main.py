import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands = 2)

while True:
	success, img = cap.read()
	hands, img = detector.findHands(img)


	if hands:
		hand1 = hands[0]
		lmList1 = hand1['lmList'] # 21 landmark points
		bbox1 = hand1['bbox'] # bounding box info x, y, w, h
		centerPoint = hand1['center'] # center of hand
		handType1 = hand1['type'] # left or right

		print(lmList1[0])
		print()
		# print(bbox1)
		# print(centerPoint)


	cv2.imshow("Image", img)
	cv2.waitKey(1)
