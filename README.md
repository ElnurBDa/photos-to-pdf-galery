# Gallery PDF Generator
This project demonstrates how to generate a PDF gallery using Python and ReportLab. It takes a list of images and arranges them into a PDF document with specified dimensions and margins.

## Features
- Generates a PDF gallery from a list of images.
- Configurable page size, margins, and image spacing.
- Adds metadata (creation date and size) under each image in the PDF.

## Requirements
- Python 3.x
- ReportLab

## Installation
1. Clone this repository:
2. Install the required dependencies:

```bash
pip install reportlab
```
## Usage
Place your images in the images/ directory.
Adjust the configuration variables in gallery_generator.py as needed.
Run the script to generate the PDF:

```bash
python gallery_generator.py
```
The generated PDF will be saved as gallery.pdf in the project directory.

## Configuration
You can adjust the following parameters in gallery_generator.py:

- images: List of image paths to include in the gallery.
- backgroundColor: Background color of the PDF.
- num_images_per_row: Number of images per row in the gallery.
- num_images_per_col: Number of images per column in the gallery.
- Other dimensions and margins for layout.

# Contribution
My contribution to the project is desire to create such app for personal purposes.
Another main Contributor to the project is ChatGPT :)
