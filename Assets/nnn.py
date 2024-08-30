from PIL import Image, ImageDraw, ImageFont

# Load the image
image_path = '/mnt/data/712437.png'
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Define font and size
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update with your font path
font_size = 100
font = ImageFont.truetype(font_path, font_size)

# Text parameters
text_fv = "FV"
text_feel_vibes_editz = "FEEL VIBES EDITZ"
neon_color = (0, 255, 255)  # Neon blue color

# Stroke size
stroke_width = 5

# Position for "FV"
text_fv_position = (100, 50)  # Adjust the position based on your image
text_feel_vibes_editz_position = (100, 200)  # Adjust the position based on your image

# Draw the text with neon stroke
draw.text(text_fv_position, text_fv, font=font, fill=neon_color, stroke_width=stroke_width, stroke_fill=neon_color)
draw.text(text_feel_vibes_editz_position, text_feel_vibes_editz, font=font, fill=neon_color, stroke_width=stroke_width, stroke_fill=neon_color)

# Save the image
output_path = '/mnt/data/neon_text_image.png'
image.save(output_path)

# Display the image
image.show()
