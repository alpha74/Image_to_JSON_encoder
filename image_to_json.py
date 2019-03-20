"""
	AIM:
		Takes image(jpeg) as input.
		Compresses image to resolution of (320*568)
		Creates a JSON file from image with Attributes: (image64, size, resolution)
"""
# Author: Aman Kumar, IIIT Nagpur


from PIL import Image
import base64
import os


# Function to encode image to base64
def encode_image_b64(image_file):
	with open( image_file, "rb" ) as image:
		str = base64.b64encode( image.read() )
	
	return str
		
# Function to get image resolution
def get_image_res(image_file):
	image = Image.open( image_file )
	return image.size

# Function to get image size in BYTES
def get_image_size(image_file):
	size = os.path.getsize( image_file )
	return size 
	
# Function to resize the image
def resize_image(image_file, new_image_file, width, height):
	image = Image.open( image_file )
	new_image = image.resize((width,height), Image.ANTIALIAS)
	new_image.save(new_image_file)
	

# Function to save in JSON format
def save_as_json( image_b64, image_size, image_res, json_name ):
	json_file = open( json_name, "w" )
	
	json_file.write( "{" ) 
	json_file.write( '\n' + '\t' + "\"image64\": \"" + image_b64 + "\"," )
	json_file.write( '\n' ) ;
	json_file.write( '\t' + "\"size\": \"" )
	json_file.write( image_size + "\"")
	json_file.write( "," )
	json_file.write( '\n' + '\t' + "\"resolution\": \"" + image_res + "\"" )
	json_file.write( '\n' + "}" ) 
	
	json_file.close()
	
	
# -------------  Main Code ---------------------------	

# Set filenames
image = "images/2.jpg"						# Input image filename	
new_image = "images/new_image.jpg" 			# New image filename
new_image_json = "images/new_image.json"	# Output json filename

res = get_image_res(image)					# res stores RESOLUTION OF IMAGE
resize_image( image, new_image, 320, 568 )	# Resize image and provide new resolution
size = get_image_size( new_image )			# size stores SIZE of image in BYTES

json_str = encode_image_b64( new_image )	# Encode to base64

save_as_json( str(json_str), str(size), str(res), new_image_json )



