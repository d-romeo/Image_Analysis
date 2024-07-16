import imutils
import numpy as np
import matplotlib.pyplot as plt
import cv2
from imutils.perspective import four_point_transform


def remove_blue_borders(image_path, output_path):
	image = cv2.imread(image_path)

	# Convertire l'immagine in scala di grigi
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Visualizzare l'immagine in scala di grigi
	plt.figure(figsize=(12, 6))
	plt.subplot(2, 3, 1)
	plt.title('Grayscale Image')
	plt.imshow(gray, cmap='gray')

	# Applicare un filtro gaussiano per ridurre il rumore
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(blurred, 50, 200, 255)


	# Visualizzare l'immagine sfocata
	plt.subplot(2, 3, 2)
	plt.title('Edged Image')
	plt.imshow(edged, cmap='gray')

	# Applicare una soglia per creare una maschera binaria
	_, binary = cv2.threshold(edged, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	# Trovare i contorni
	contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Creare una copia dell'immagine per disegnare i contorni
	contour_image = image.copy()
	cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

	# Visualizzare i contorni trovati
	plt.subplot(2, 3, 4)
	plt.title('Contours')
	plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))

	# Trovare il contorno con l'area maggiore che dovrebbe essere la targa
	max_contour = max(contours, key=cv2.contourArea)

	# Ottenere il rettangolo di delimitazione per il contorno maggiore
	x, y, w, h = cv2.boundingRect(max_contour)

	# Disegnare il rettangolo di delimitazione sull'immagine originale
	rect_image = image.copy()
	cv2.rectangle(rect_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

	# Visualizzare il rettangolo di delimitazione
	plt.subplot(2, 3, 5)
	plt.title('Bounding Rect')
	plt.imshow(cv2.cvtColor(rect_image, cv2.COLOR_BGR2RGB))

	# Ritagliare l'immagine per rimuovere lo sfondo
	cropped_image = image[y:y + h, x:x + w]

	# Salvare l'immagine ritagliata senza sfondo
	cv2.imwrite(output_path, cropped_image)
	cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

	# Visualizzare l'immagine ritagliata senza sfondo
	plt.subplot(2, 3, 6)
	plt.title('Cropped Image')
	plt.imshow(cropped_image)

	# Rimuovere i bordi blu dalla targa
	height, width, _ = cropped_image.shape
	blue_border_width = int(width * 0.1)  # Assumiamo che i bordi blu occupino il 10% della larghezza totale
	cropped_image_no_blue = cropped_image[:, blue_border_width:width - blue_border_width]

	# Convertire l'immagine ritagliata in scala di grigi
	plate_gray = cv2.cvtColor(cropped_image_no_blue, cv2.COLOR_BGR2GRAY)

	# Applicare una soglia binaria per isolare le lettere
	_, binary_plate = cv2.threshold(plate_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

	# Salvare l'immagine con solo le lettere in evidenza
	cv2.imwrite(output_path, binary_plate)

	# Visualizzare e salvare l'immagine ritagliata senza bordi blu
	plt.figure(figsize=(12, 6))
	plt.subplot(1, 2, 1)
	plt.title('Original Cropped Image')
	plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
	plt.axis('off')

	plt.subplot(1, 2, 2)
	plt.title('Cropped Image without Blue Borders')
	plt.imshow(cv2.cvtColor(binary_plate, cv2.COLOR_BGR2RGB))
	plt.axis('off')

	# Salvare l'immagine ritagliata senza bordi blu
	cv2.imwrite(output_path, binary_plate)

	plt.tight_layout()
	plt.show()