from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from PIL import Image
import os
from datetime import datetime

fileName = 'gallery.pdf'
images = ['images/' + str(i) + '.jpeg' for i in range(1, 51)]
backgroundColor = colors.lightpink
page_width, page_height = letter
inch /= 2
left_margin = inch
right_margin = page_width - inch
top_margin = page_height - inch
bottom_margin = inch
image_spacing = inch
available_width = right_margin - left_margin
available_height = top_margin - bottom_margin
num_images_per_row = 2
num_images_per_col = 2
image_width = (available_width - (num_images_per_row - 1) * image_spacing) / num_images_per_row
image_height = (available_height - (num_images_per_col - 1) * image_spacing) / num_images_per_col
current_x = left_margin
current_y = top_margin

pdf = canvas.Canvas(fileName)
pdf.setFillColor(backgroundColor)
pdf.rect(0, 0, letter[0], letter[1] * 2, fill=True)

for idx, image_path in enumerate(images):
    if current_y - image_height < bottom_margin:
        pdf.showPage()
        pdf.setFillColor(backgroundColor)
        pdf.rect(0, 0, letter[0], letter[1] * 2, fill=True)
        current_x = left_margin
        current_y = top_margin
    pdf.drawImage(image_path, current_x, current_y - image_height, width=image_width, height=image_height)
    
    # Getting image metadata
    image = Image.open(image_path)
    image_date = datetime.fromtimestamp(os.path.getmtime(image_path)).strftime('%Y-%m-%d')
    
    # Drawing metadata under the image
    pdf.setFont("Helvetica", 10)
    pdf.setFillColorRGB(0, 0, 0)  # Setting text color to black
    pdf.drawString(current_x, current_y - image_height - 20, f"Date: {image_date}")
    
    current_x += image_width + image_spacing
    if current_x > right_margin:
        current_x = left_margin
        current_y -= image_height + image_spacing

pdf.save()
print("Gallery PDF generated successfully.")
