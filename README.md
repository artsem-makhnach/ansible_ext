# ansible_ext

cache plugin with sending facts to mongodb

1. build image from Dockerfile:
    docker build -t my_mongo .
2. run container: 
    docker run --rm -d --name=my_mongo --entrypoint=mongod -p 27017:27017 my_mongo --bind_ip 0.0.0.0
3. run test playbook with ansible.cfg in its folder

unfortunately, not all functionality have been realized to make it real cache plugin... :-(
