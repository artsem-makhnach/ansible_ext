FROM mongo
MAINTAINER Artsem Makhnach
COPY mongod.conf.orig /etc/mongod.conf.orig
RUN mongod --fork -logpath=/opt/1.log && \
mongo admin --eval "db.getSiblingDB('my_db').createUser({ user : 'my_user', pwd :  'my_pass', roles : [{ role: 'dbOwner', db: 'my_db'}]});" && \
mongod --shutdown
EXPOSE 27017
CMD ""
