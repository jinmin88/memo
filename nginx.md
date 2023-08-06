


# API design
* We use basic authorization header to protect our API, we will use `username` / `password` to protect our APIs, following algorithm is show how to protect our APIs.
  ```
  basic_token = base64_encode(username):base64_encode(password)
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
        "hostname": "myserver1.tsmc.com"
    }
    ```



## Database tables
``` mermaid

```


## Need to discuss
1. how to store server's cdential: vault or database?
2. each server's username/password can be the same?
3. if not, how to store that in the vault


