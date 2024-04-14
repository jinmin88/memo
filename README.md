# 筆記

## Fast API notes

### Fast API Logging
https://github.com/tiangolo/fastapi/issues/1276

### Testing

### Run powsershell in a container

### Additional Response
https://fastapi.tiangolo.com/advanced/additional-responses/

### API-Key authroization
https://github.com/tiangolo/fastapi/issues/142

### Logging
https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/

### install fast api application as a windows service (nssm)
https://stackoverflow.com/questions/65591630/fastapi-as-a-windows-service

### 422 error remove it!
https://blog.csdn.net/weixin_36179862/article/details/110507491


### fastapi logging middleware ###
https://github.com/jeffsiver/fastapi-route-logger/blob/e52b5344e19de3e31cd70aee277fc7bc2355bd9a/fastapi_route_logger_middleware/__init__.py#L47
#### Loguru ####
https://github.com/Delgan/loguru
#### unify-logging-for-a-gunicorn-uvicorn-app ####
https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/
### loguru example ###

### sqlalchemy
https://www.youtube.com/watch?v=nt5sSr1A_qw
https://www.readfog.com/a/1640196300205035520
### Multiple module logging ###
https://stackoverflow.com/questions/52175730/python-question-on-logging-in-init-py

### docker copy file from container to host ###
https://stackoverflow.com/questions/22049212/docker-copying-files-from-docker-container-to-host

### wso2 api manager docker github ###
https://github.com/wso2/docker-apim/tree/master/dockerfiles/ubuntu/apim

### oauth 2 ###
https://blog.yorkxin.org/posts/oauth2-1-introduction.html


### invoke java library from python ###
https://github.com/jpype-project/jpype
https://www.twblogs.net/a/5be2419c2b717720b51d24fc

### wso2 api manager
https://github.com/wso2/docker-apim/blob/master/docker-compose/apim-with-mi/dockerfiles/apim/Dockerfile

### Promethues
https://github.com/udemy-course/telegraf-prometheus-grafana

### course
db theory: https://www.udemy.com/course/database-engines-crash-course/
db mysql: https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/
rabbomq: https://www.udemy.com/course/rabbitmq-in-practice/
oop: https://www.udemy.com/course/object-oriented-programming-with-modern-python/

### leetcode
* 1598 https://leetcode.com/problems/crawler-log-folder/description/


### sql
``` sql

CREATE TABLE mac_record (
    id uuid NOT NULL,
    bucket varchar(10) NOT NULL,
	user_mac varchar(17) NOT NULL,
	device_name varchar(64) NOT NULL,
	interface_name varchar(64) NOT NULL,
	dynamic_acl_number int NULL,
	dynamic_acl_name varchar(100) NULL,
	static_acl_number int NULL,
	static_acl_name varchar(100) NULL,
	effective_acl_number int NULL,
	effective_acl_name varchar(100) NULL,
	created timestamp,
	last_updated timestamp,
	PRIMARY KEY (id, bucket)
) PARTITION BY RANGE (bucket);

CREATE TABLE arp_record (
	id uuid NOT NULL,
	bucket varchar(10) NOT NULL,
	user_mac varchar(17) NOT NULL,
	user_ip varchar(39) NOT NULL,
	user_devicename varchar(64) NULL,
	router_name varchar(64) NOT NULL,
	router_ip varchar(39) NOT NULL,
	created timestamp,
	last_updated timestamp,
	PRIMARY KEY (id, bucket)
) PARTITION BY RANGE (bucket);

CREATE TABLE mac_record_20240412 PARTITION OF mac_record
	FOR VALUES FROM ('2024041200') TO ('2024041299');

CREATE TABLE arp_record_20240412 PARTITION OF arp_record
	FOR VALUES FROM ('2024041200') TO ('2024041299');

CREATE INDEX idx_mac_record_20240412_bucket_mac ON mac_record_20240412 (bucket DESC, user_mac ASC);
```
