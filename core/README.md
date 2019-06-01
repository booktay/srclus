# Core
All backend part. Srclus Library, Collect datas, Word Prepraration, TF-ID, Make a Word2vec model and API Server

## Directory Structure
  ```
  core/
  |__ datas/
  |   |__ corpus/  
  |   |   |__ customwords.json
  |   |   |__ stopwords.json
  |   |
  |   |__ model/
  |   |__ tfidf/
  |   |__ token/
  |   |__ raw/
  |
  |__ srcluslib/
  |   |__ corpus/
  |   |   |__ customwords.py
  |   |   |__ pantip.py
  |   |   |__ stopwords.py
  |   |
  |   |__ utility/
  |   |   |__ iorq.py
  |   |
  |   |__ model/
  |       |__ tfidf.py
  |       |__ tokenize.py
  |       |__ word2vec.py
  |
  |__ envsrclus/
  |
  |__ 1.getdata.py
  |__ 2.wordcut.py
  |__ 3.tfidf.py
  |__ 4.model.py
  |__ server.py
  |__ README.md
  |__ requirements.txt 
  ```

## Installation

* ### Requirements
    - Python 3.7
    - Ram 8 GB+
    
* ### Instructions
    Testing on MacOS Mojave 10.14.4, Windows 10, Ubuntu 18.04, CentOS 7

    1. Change directory to **_client/_** directory
    
        ```
        $ cd core
        ```
    
    2. **[Optional]** If you want to use a **```Virtual environment```**.
    
        - **Init** virtual environment
        
        ```
        $ virtualenv envsrclus
        ```
        
        - **Activate** virtual environment
        
            * **_Linux OS_**
        
                ```
                $ source envsrclus/bin/activate
                ```
        
            * **_Windows OS_**
            
                ``` 
                $ .\envsrclus\Scripts\activate 
                ```
        
        - **Deactivate** virtual environment
        
        ```
        $ deactivate
        ```
        
    3. Install Dependencie Modules
    
        ```
        $ pip install -r requirements.txt 
        ```
        
        * Note: **Windows 10 OS**, Please install this **first** ``` $ pip install https://github.com/wannaphongcom/artagger/tarball/master#egg=artagger ```
        
        NLTK POS Tagger 
        
        ``` 
        $ python -c "import nltk; nltk.download('averaged_perceptron_tagger');"
        ```
   
    4. Download example datas directory from this [**link**](https://drive.google.com/open?id=1NjvARd1gyEdhEpQX9zUi_OUsnLfXhz68) 
        and Extract it in **core** directory (You can see a guideline in directory structure.)

## File Description
_``` Please read command description in each file ```_
  
* Srclus Library : **srcluslib/corpus/, srcluslib/utility/ and srcluslib/model/**
* Collect datas from pantip.com : **1.getdata.py**
* Word Prepraration : **2.wordcut.py**
* TF-IDF Process : **3.tfidf.py**
* Make a Word2vec model : **4.model.py**
* API Server [Test by running with [client](../client)] : **server.py**
    *  For Test result clustering API 
        *   Select a Search Word : "Apple"
        *   Want to use TF-IDF Model : "false"
        *   go to [http://localhost:5000/api/cluster/apple?tfidf=false](http://localhost:5000/api/cluster/apple?tfidf=false) on your browser
    
<!--## Centos 7 Server Configuration-->
<!--See howto on this [howto-setup-centos7server](https://mike.cpe.ku.ac.th:65443/gitlab/books/srclus/wikis/howto-setup-centos7server) wiki-->
