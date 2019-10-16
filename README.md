# Code-test
# Instructions

# To build the image using the dockerfile
  docker build <image_name> .

# To find the image_id
  docker images
  
# To tag the image
  docker tag <image_id> <image_name>:<tag> 
 
# To run the image
  docker run <image_name>:<tag> [3,5,6] [2,7,8]
  
