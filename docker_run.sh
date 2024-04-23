#!/bin/bash  

docker build  -t "college_project" .   

docker run -d  -p  8000:8000 --name project college_project 
