# restapi_camera
Dockerized webcam streaming with RESTful communication to rotate camera using Arduino servos and Raspberry Pi as a server

Running container:
```
cd docker
docker build -t myimage .
>>>>>>> ad18a5b878d8fac7555b7d86dad7bd1a1b8089f7
docker run -d --name mycontainer --device=/dev/ttyACM0 -p 80:80 myimage
```
