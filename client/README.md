## Client 

![Project Structure](https://lh3.googleusercontent.com/PfQc3hK_N9CbBSKFy4oXaulKJyNVitly72vl6zwK1F2DiXW8sp00MXDp9tzGt42z9qa3_5HbJXksMYPt3PrIVLVPZ9EALNFGMW7eHQ41aGAr4eHhL0zpJ2ge9gosQRoncQ5q8bm3d9ImlH67RKq4urHg6tv5nsrW_Il2Klcw4bRLNj16zeHP_D3in4wxkULDGEx_lrmgtvlbPGi-EBALcybaoscRtP4zhIQqMSjLeC-kSwFdRhABoPH9DG2xVbUxZAEVo8nDXZ_c_7gfOzD820_RK8zjD5nNoiAAl6dmVx3JNgQk47JWOFcJrJb4LplfAgUbmw6BzxsZJMQP9Rvz7SBjPyjbFkl-27lp28zhlpIMBH-3kLgeC4YAKfKi6JSRTD5_iUZhhjCgiRXdnJ4NBg5iR6D4StPgBRPogbZhmDkCoUj4fIWQu5XlJ10_MW25_6sSX6Ep902q5idvhi3WJYgWdBLcsRwr7MVQUyyE9qdTq_ZBu8kLmWDe4ju-0B65CH03aGIS0FbWgowT20jN28al5yUMrqkM7_soRqotOUpiPEk4yQcqDn0wpzHiYjEny8X6HYXV-BlPHB2rB8KmL9H6mRMJ-aYGH6FS7KSFq29ldss9Z8kKDX4fsAYmzBRRaikerHha5EuIN69dCfEf7jjKOXJA4oUL=w3304-h1924-no)



### Description

This a web application for showing clustering result. 

- #### Client Directory Path

  ```
  client/
  |__ public/
  |		|__ index.html
  |		|__ manifest.json
  |
  |__ src/
  |		|__ component/
  |		|		|__ Content.js
  |		|		|__ Header.js
  |		|
  |		|__ App.css
  |		|__ App.js
  |		|__ App.test.js
  |		|__ index.css
  |		|__ index.js
  |		|__ serviceWorker.js
  |
  |__ package.json
  |__ README.md
  |__ yarn.lock
  ```

- #### Storage Directory Path
	
    I had to move many large files from public directory to the storage directory to reduce Github size more than 100mb. **You can download all these files from an original link and can change all path by yourself for reducing latency**.
    
  ```
  storage/
  |__ GRHVkN5NwxcGmHUXsMOu3Q
  |	  	|__ css/
  |	  	|__ ico/
  |	  	|__ image/
  |			  |__ mike.png
  |			  |__ pantip.png
  |			  |__ mike.png
  |
  |__ KmLx7EM2GuwEeDQejBufJfgP+nXga5j8/
      	|__ notfidf/
      	|	  |__ apple.json
      	|	  |__ avenger.json
        |	  |__ ภูเก็ต.json
      	|__ tfidf/
        	  |__ apple.json
          	  |__ avenger.json
              |__ ภูเก็ต.json

	``` 

## Installation

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

#### Requirements

- NodeJS 10.15.3+
- Yarn 1.15.2

#### Instructions
Testing on MacOS Mojave 10.14.4, Windows 10, Ubuntu 18.04, CentOS 7

1. Change directory to **client** directory
	```
    $ cd client
    ```
    
2. Install dependencies for all modules
	```
    $ yarn
    ```
    
3. Start app - Let's play
	```
    $ yarn start
    ```
  
4. **[Optional]** Serving static files to server

    1. Install server dependencies
    2. Config server file
    3. Build app for production to a **build** directory.

        ```
        $ yarn build
        ```

    4. Move **build** directory to web directory or Create symbolic link to web directory