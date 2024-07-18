import random
import os
import matplotlib.pyplot as plt
import cv2
import pytesseract

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
	blue_border_width = int(width * 0.117)  # Assumiamo che i bordi blu occupino il 10% della larghezza totale
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

	#plt.tight_layout()
	#plt.show()

def select_random_plates(folder_path, max_plates=3):
	# Lista dei file nella cartella 'plates'
	files = os.listdir(folder_path)
	# Filtrare solo i file che sono immagini (estensioni comuni come .jpg, .png)
	image_files = [file for file in files if file.endswith('.jpg') or file.endswith('.png')]

	# Selezionare casualmente fino a max_plates immagini
	selected_files = random.sample(image_files, min(max_plates, len(image_files)))

	# Creare i percorsi completi alle immagini selezionate
	selected_paths = [os.path.join(folder_path, file) for file in selected_files]
	image = selected_paths[random.randint(0, 2)]
	print(image)
	return image


def request_to_join(accepted_plates):
	pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\danie\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

	#seleziona una targa random in plates
	rand_plate = select_random_plates('plates/', max_plates=4)
	#rimuovi bordi
	remove_blue_borders(rand_plate, 'temp/borderless.png')

	img = cv2.imread('temp/borderless.png')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	pytesseract

	hImg, wImg, _ = img.shape
	boxes = pytesseract.image_to_boxes(img)
	plate = []
	count = 0

	for b in boxes.splitlines():
		print(b)
		b = b.split(' ')
		print(b)
		x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
		cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
		cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

		# evitare il 3 elemento (simbolo repubblica)
		if count != 2:
			plate.append(b[0])
		count = count + 1

	# to string
	plate = ''.join(map(str, plate))
	print(plate)
	cv2.imshow('img', img)
	cv2.waitKey(0)
	# check plate
	if plate in accepted_plates:
		return True