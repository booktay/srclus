## Client 

![ProjectStructure](https://lh3.googleusercontent.com/iNWDz1VHEM9AApicbuW5ZhsT6SfPMys2unKnBS4w6AliCmEOz_a8NlNArtxu5JkpyHqrvPD0GR2MHQKLLpfzBw6s99Gr9OatXGiVUBDDO4CVXRsRBFzxZZ_YdvsGSG3ypxxjroxtWOLKFX-e-OPWQBavYjUOxO49mOM47HYTF5y9ar9_kwk9pB3VQz9To9bpbksDNs2Eg2yFmoU7pNwW37nqpt-lGwbfsXBJC9dJ2mNMr6gl5zm36klid9pVHSijWMLDgSIGOlOmB2RjAgbD0vKnh_HHOJ2c0MeJIAOhOX98fXnn3kbkC4Lac33Y1odNFZLGB6pnxwqF8Dr0_Le2abP1dk27OOjWtPb898ItL1WH-Xy3Y3ZvdeOGpMhCVeX9dH46bXUzUaQHYXkaBYqG39avF_bInyiMClkZ5LjQxVxr85nUgaSxlxImHytIhhr94BkHP24etDZkSlKFiVWgA52OO1WQnBaXVS85_6jWakKOD6xKpTsfCpnRfDApHllpmL1_K36sSoE3fuy1N-q6u4hMl2LMxFeCQHAAbc9hg7BIk1XXa2Fe5A_yjqGpFJo2l7_3HY29vXOafaHFUvMpvkFgVaY8RFIGW1_EfJgak1R0akzCvEvIHAJc4_RgpBB4G8MG_0JA3KrmdN2pGUJyVERJ0NcOMJ3XKwtCorCt5Z3CMhOb4306aVWUHFJQqAyLXG-SvzRHgKljnuEO4nhykiBQnQ=w3304-h1924-no)



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