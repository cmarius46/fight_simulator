import cv2
import mediapipe as mp

def detect_hands():

	mp_drawing = mp.solutions.drawing_utils
	mp_drawing_styles = mp.solutions.drawing_styles
	mp_hands = mp.solutions.hands

	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

	with mp_hands.Hands(
			model_complexity=0,
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as hands:
		
		# print('yes')

		while cap.isOpened():
			success, image = cap.read()

			if not success:
				print("ignoring empty cam frame")

				continue

			image.flags.writeable = False
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			results = hands.process(image)

			# print(results)
			# print()
			# print()

			if results.multi_hand_landmarks:
				for hand_landmarks in results.multi_hand_landmarks:
					mp_drawing.draw_landmarks(
					image,
					hand_landmarks,
					mp_hands.HAND_CONNECTIONS,
					mp_drawing_styles.get_default_hand_landmarks_style(),
					mp_drawing_styles.get_default_hand_connections_style())

			cv2.imshow("Image", image)

			if cv2.waitKey(5) & 0xFF == 27:
				break

	cap.release()