


# API design
* We use the basic authorization header to protect our API. Following algorithm shows how to protect our APIs. The `client_id` / `client_secret` is stored in the vault, and the load into envirnmenet variable as `CLIENT_ID` / `CLIENT_SECRET`.
  ```
  basic_token = base64(client_id):base64(client_secret)
  ```
## Server APIs
* List all nginx servers monitor by this project
  * URL: `[GET] /api/v1/servers`
  * Headers:
    ``` json
    {
        "Content-Type": "application/json",
        "Authorization": "Basic {basic_token}"
    }
    ```
  * Body:
    ``` json
    [[
        "id": 1,
        "name": "myserver1",
        "description" : "server1 desc",
        "ip" : "10.19.251.101",
        "hostname": "myserver1.tsmc.com"
    ]]
    ```
* Get server info
  * URL: `[GET] /api/v1/servers/{id}`
  * Headers:
    ``` json
    {
        "Content-Type": "application/json",
        "Authorization": "Basic {basic_token}"
    }
    ```
  * Body:
    ``` json
    {
        "id": 1,
        "name": "myserver1",
        "description": "server1 desc",
        "ip": "10.19.251.101",
        "hostname": "myserver1.tsmc.com",
        "username": "user"
    }
    ```
* Add a new server
  * URL: `[POST] /api/v1/servers`
  * Headers:
    ``` json

    ```
  * Request body
    ``` json
    {
        "name": "myserver2",
        "description": "myserver2 desc",
        "ip": "10.19.251.102",
        "hostname": "myserver2.tsmc.com",
        "username" : "user",
        "password": "mypassword",
        "nginx_config_location": "/var/nginx/nginx.cfg",
        "nginx_container_name": "nginx_proxy",
    }
    ```
  * Response:
    * `201 Created`
      ``` json
      {
        "id": 2,
        "name": "myserver2",
        "desciption": "mysrever2 desc",
        "ip": "10.19.251.102",
        "hostname": "myserver2.tsmc.com",
        "username" : "user"
      }
      ```
    * `400 Bad Request`
      ``` json
      {
        "errors": [{
          "code": "SERVER_CONNECT_FAILED",
          "message": "Can't connect to {ip}",
          "field_value": "10.19.251.102",
          "field_name": "ip"                
        },{
          "code": "SERVER_CREDENTIAL_FAILED",
          "message": "The credenital for the nginx server is incorrect or expired",
          "field_value": "user",
          "field_name": "username"
        },{
          "code": "SERVER_NGINGX_CFG_NOT_FOUND",
          "message": "The nginx config is not found",
          "field_value": "/var/nginx/nginx.cfg",
          "field_name": "nginx_config_location"
        },{
          "code": "SERVER_NGINX_CFG_INVALID",
          "message": "The nginx config is invalid",
          "field_value": "/var/nginx/nginx.cfg",
          "field_name": "nginx_config_location"
        }]
      }
      ```
    * `422 Data Invalid`
      ``` json
      {
        "errors": [{
          "code": "DATA_INVALID",
          "message": "The ip address is incorrect",
          "field_name": "ip",
          "field_value" : "1111.22.33.44"
        }]
      }
      ```
  * `Steps to add an nginx server`
    * Use `netmiko` to connect the nginx server with given `username` / `password`.
      * if connect failed, return `SERVER_CONNECT_FAILED` error.
      * if the credential failed, return `SERVER_CREDENTIAL_FAILED` error.
   * Check the file of `nginx`
    * connect to nginx server with given `ip` address.
      * if connect failed, return   
    * use `username` / `password` to login the nginx server
    * 


## Database tables
``` mermaid

```


## Need to discuss
1. how to store server's cdential: vault or database?
2. each server's username/password can be the same?
3. if not, how to store that in the vault


