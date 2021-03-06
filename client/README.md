## Client 

![ProjectStructure](https://lh3.googleusercontent.com/iNWDz1VHEM9AApicbuW5ZhsT6SfPMys2unKnBS4w6AliCmEOz_a8NlNArtxu5JkpyHqrvPD0GR2MHQKLLpfzBw6s99Gr9OatXGiVUBDDO4CVXRsRBFzxZZ_YdvsGSG3ypxxjroxtWOLKFX-e-OPWQBavYjUOxO49mOM47HYTF5y9ar9_kwk9pB3VQz9To9bpbksDNs2Eg2yFmoU7pNwW37nqpt-lGwbfsXBJC9dJ2mNMr6gl5zm36klid9pVHSijWMLDgSIGOlOmB2RjAgbD0vKnh_HHOJ2c0MeJIAOhOX98fXnn3kbkC4Lac33Y1odNFZLGB6pnxwqF8Dr0_Le2abP1dk27OOjWtPb898ItL1WH-Xy3Y3ZvdeOGpMhCVeX9dH46bXUzUaQHYXkaBYqG39avF_bInyiMClkZ5LjQxVxr85nUgaSxlxImHytIhhr94BkHP24etDZkSlKFiVWgA52OO1WQnBaXVS85_6jWakKOD6xKpTsfCpnRfDApHllpmL1_K36sSoE3fuy1N-q6u4hMl2LMxFeCQHAAbc9hg7BIk1XXa2Fe5A_yjqGpFJo2l7_3HY29vXOafaHFUvMpvkFgVaY8RFIGW1_EfJgak1R0akzCvEvIHAJc4_RgpBB4G8MG_0JA3KrmdN2pGUJyVERJ0NcOMJ3XKwtCorCt5Z3CMhOb4306aVWUHFJQqAyLXG-SvzRHgKljnuEO4nhykiBQnQ=w3304-h1924-no)

## Description

This a web application for showing clustering result. It has 3 part

1. Search Part : Top side
2. Cluster Name Part : Left side
3. Thread cluster Part : Right side

You can input a search word and put a search button. A clustering process may take approximately **1 minute** then show a result on the web. If you don't want to wait, You can input **apple** or **avenger**. I prepared these words for showing my example clustering.
You should follow the instruction from [core](../core) before read this. 

I explain this structure in this video.

[![Video](https://img.youtube.com/vi/eMprd8Fwt80/0.jpg)](https://youtu.be/eMprd8Fwt80?t=413)

### Directory Structure

- #### Client Directory

    This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

  ```
  client/
  |__ public/
  |   |__ GRHVkN5NwxcGmHUXsMOu3Q/
  |   |   |__ css/
  |   |   |__ ico/
  |   |   |__ image/
  |   |
  |   |__ KmLx7EM2GuwEeDQejBufJfgP+nXga5j8/
  |   |   |__ notfidf/
  |   |   |   |__ apple.json
  |   |   |   |__ avenger.json
  |   |   |
  |   |   |__ tfidf/
  |   |       |__ apple.json
  |   |       |__ avenger.json
  |   |
  |   |__ index.html
  |   |__ manifest.json
  |
  |__ src/
  |   |__ component/
  |   |   |__ Content.js
  |   |   |__ Header.js
  |   |
  |   |__ App.css
  |   |__ App.js
  |   |__ App.test.js
  |   |__ index.css
  |   |__ index.js
  |   |__ serviceWorker.js
  |
  |__ package.json
  |__ README.md
  |__ yarn.lock
  ```

## Installation

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
    
3. Download files in public from this [link](https://drive.google.com/open?id=1Nm-K8-fAwZ5Bs4wE_rYc7U_M-DEW-ZOB) and Extract it in **public** directory

4. Start app - Let's play
	```
    $ yarn start
    ```

5. Open your browser (Testing on **Chrome**) without CORS Policy and Go to [http://localhost:3000/](http://localhost:3000/)

    * MacOS 10.14.4, run this command in Terminal
    ```
    $ open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
    ```

    * Windows 10, run this command in CMD or Powershell
    ```
    $ "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-web-security --disable-gpu --user-data-dir=~/chromeTemp
    ```

#### Serving static files to server

1. Install server dependencies and Config server file 
<!--see in this [howto-setup-centos7server](https://mike.cpe.ku.ac.th:65443/gitlab/books/srclus/wikis/howto-setup-centos7server) wiki-->
2. Build app for production to a **build** directory.

    ```
    $ yarn build
    ```

4. Move **build** directory to web directory or Create symbolic link to web directory
