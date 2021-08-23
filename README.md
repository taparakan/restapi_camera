# restapi_camera
Dockerized webcam streaming with RESTful communication to rotate camera using Arduino servos and Raspberry Pi as a server

Running container:
```
cd docker
docker build -t myimage .
docker run -d --name mycontainer --device=/dev/ttyACM0 -p 80:80 myimage
```
