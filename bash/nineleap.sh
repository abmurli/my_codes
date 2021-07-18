docker run -d --name my-container -v /tmp:/tmp busybox:latest

docker exec <container_id> find /tmp -type f -name my-list +0

#echo "dummy" > /tmp/my-list

docker run -d --name my-container -p 80:8000 nginx:latest

wget -qO- http://localhost:8000