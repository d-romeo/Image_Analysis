import numpy as np
import matplotlib.pyplot as plt
import cv2
def remove_blue_borders(image_path, output_path):
	# Caricare l'immagine
	image = cv2.imread(image_path)

	# Convertire l'immagine in scala di grigi
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Applicare un filtro gaussiano per ridurre il rumore
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)

	# Applicare una soglia per creare una maschera binaria
	_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	# Trovare i contorni
	contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Trovare il contorno con l'area maggiore che dovrebbe essere la targa
	max_contour = max(contours, key=cv2.contourArea)

	# Ottenere il rettangolo di delimitazione per il contorno maggiore
	x, y, w, h = cv2.boundingRect(max_contour)

	# Ritagliare l'immagine per rimuovere i bordi blu
	cropped_image = image[y:y + h, x:x + w]

	# Salvare l'immagine ritagliata
	cv2.imwrite(output_path, cropped_image)

	# Visualizzare l'immagine originale e l'immagine ritagliata
	plt.subplot(1, 2, 1)
	plt.title('Original Image')
	plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

	plt.subplot(1, 2, 2)
	plt.title('Cropped Image')
	plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

	plt.show()