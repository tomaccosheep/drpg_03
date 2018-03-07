FROM mysql/mysql-server:latest
MAINTAINER Al Burns "al.burns.email@gmail.com"
RUN yum install -y vim
EXPOSE 3306
#COPY ["./sql_scripts", "/sql_scripts"]
ENV MYSQL_USER=mysql \
MYSQL_PASSWORD=Viapjor5 \
MYSQL_DATABASE=db
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld"]
