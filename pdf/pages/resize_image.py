import cv2
from PIL import Image
import numpy as np
import streamlit as st


def seam_carve(img, new_width, new_height):
	img = img.astype(np.float64)
	for i in range(int(img.shape[1] - new_width)):
		energy_map = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2GRAY)
		energy_map = cv2.Sobel(energy_map, cv2.CV_64F, 1, 0) ** 2 + \
			cv2.Sobel(energy_map, cv2.CV_64F, 0, 1) ** 2
		min_energy_map = np.zeros_like(energy_map)
		min_energy_map[0] = energy_map[0]
		for row in range(1, energy_map.shape[0]):
			for col in range(energy_map.shape[1]):
				if col == 0:
					min_energy_map[row, col] = energy_map[row, col] + \
						min(min_energy_map[row - 1, col],
							min_energy_map[row - 1, col + 1])
				elif col == energy_map.shape[1] - 1:
					min_energy_map[row, col] = energy_map[row, col] + min(
					min_energy_map[row - 1, col - 1],
					min_energy_map[row - 1, col])
				else:
					min_energy_map[row, col] = energy_map[row, col] + min(
					min_energy_map[row - 1, col - 1],
					min_energy_map[row - 1, col],
					min_energy_map[row - 1, col + 1])
		seam_mask = np.ones_like(img[:, :, 0])
		col = np.argmin(min_energy_map[-1])
		for row in reversed(range(img.shape[0])):
			seam_mask[row, col] = 0
			if col == 0:
				col = np.argmin(min_energy_map[row - 1, col:col + 2])
			elif col == img.shape[1] - 1:
				col = np.argmin(
					min_energy_map[row - 1, col - 1:col + 1]) + col - 1
			else:
				col = np.argmin(
					min_energy_map[row - 1, col - 1:col + 2]) + col - 1
		img = cv2.resize(img, (new_width, new_height))
		seam_mask = cv2.resize(seam_mask, (new_width, new_height))
		for channel in range(img.shape[2]):
			img[:, :, channel] = np.multiply(img[:, :, channel], seam_mask)
		img = img.astype(np.uint8)
	return img


st.title("Seam Carving Image Resizing")

# uploaded_file = st.file_uploader(
# 	"Choose an image...", type=["jpg", "jpeg", "png"])
# if uploaded_file is not None:
# 	img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
# 	st.write(img.shape)
# 	st.image(img, clamp=True, channels="RGB")
# 	new_width = st.slider("New Width", 100, img.shape[1], img.shape[1])
# 	new_height = st.slider("New Height", 100, img.shape[0], img.shape[0])
# 	if st.button("Resize?"):
# 		with st.spinner("Please Wait ... "):
# 			new_img = seam_carve(img, new_width, new_height)
# 			st.write(new_img.shape, new_width,new_height )
# 			st.image(new_img,clamp=True, channels="RGB")
		




bottom_image = st.file_uploader('', type=["jpg", "jpeg", "png"], key=6)

if bottom_image is not None:
	
	img_shape= Image.open(bottom_image)
	st.write(img_shape.height, img_shape.width)
	img = Image.open(bottom_image)
	st.image(img, clamp=True, channels="RGB")
	
	new_width = st.slider("New Width",  min_value=img_shape.width, max_value=2*img_shape.width, value=img_shape.width)
	new_height = st.slider("New Height", img_shape.height, img_shape.height*2, img_shape.height)
	
	if st.button("Resize?"):
		new_image = img.resize((new_width, new_height))
		st.image(new_image, clamp=True, channels="RGB")
		# st.write(new_image.shape)