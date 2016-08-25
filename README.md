# ClaireCut Server

## Run

2. Download project

		$ git clone https://github.com/clairecut/clairecut-backend.git
		$ cd clairecut-backend

2. This project uses [docker](https://github.com/docker/docker), so start the container by running

		$ docker-compose up

3. If you see a `{ hello: world }` response to a `GET` request to `$ <YOUR_DOCKER_IP>/api/v1` the server is running. 

4. Further test the back-end with a `POST` request to

		$ <YOUR_DOCKER_IP>/api/v1/submit
		
	and include a base64 encoded image as payload with parameter `image`.


## Test
Test with one word in the image:

        $ python test0.py

Test with six words on the image

        $python test1.py

## Future Tasks

1. Validation
	* Received string is base64-image string
	* Add JSON web token authentication
	    * New `\authenticate` endpoint

2. Create clean docker image and upload

3. Make algorithm robust

    * Detect whether image is suitable or not. (imageTropical.json gives several results for blue, but it is not a whiteboard)
    * Did not work with .gif image (do we need that?)

further tasks: see `Issues` of this repo.
 
## Tipps

To undestand the image processing algorithm, look at processor/README.md 

Delete `.pyc` files with:

    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf