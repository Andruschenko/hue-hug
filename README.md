# ClaireCut Server

## Run

1. Install docker

2. Download project

		$ git clone ...
		$ cd ...

2. Start container

		$ docker-compose up

3. Test back-end with a `POST` request to

		$ <YOUR_DOCKER_IP>/api/v1/submit
		
	and include a base64 encoded image as payload with parameter `image`.

## Future Tasks

1. Validation
	* Received string is base64-image string
	* Add JSON web token authentication
	    * New `\authenticate` endpoint

2. Create clean docker image and upload

3. Make algorithm robust

    * Detect whether image is suitable or not. (imageTropical.json gives several results for blue, but it is not a whiteboard)
    * Did not work with .gif image (do we need that?)

## Tipps

Delete `.pyc` files with:

    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf