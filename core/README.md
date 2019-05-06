## Core


### Directory Structure
  ```
  core/
  |__ srcluslib/
  |     |__ corpus/
  |     |   |__ customwords.py
  |     |   |__ pantip.py
  |     |   |__ stopwords.py
  |     |
  |     |__ utility/
  |     |   |__ iorq.py
  |     |
  |     |__ model/
  |         |__ tfidf.py
  |         |__ tokenize.py
  |         |__ word2vec.py
  |
  |__ datas/
  |     |__ corpus/  
  |     |   |__ customwords.json
  |     |   |__ stopwords.json
  |     |
  |     |__ model/
  |     |__ tfidf/
  |     |__ token/
  |     |__ raw/
  |
  |__ envsrclus/
  |__ 1.getdata.py
  |__ 2.wordcut.py
  |__ 3.tfidf.py
  |__ 4.model.py
  |__ server.py
  |__ README.md
  |__ requirements.txt 
  ```

## Installation

#### Requirements

- Python 3.6+

#### Instructions
Testing on MacOS Mojave 10.14.4, Windows 10, Ubuntu 18.04, CentOS 7

1. Change directory to **client** directory

	```
    $ cd core
    ```
 
2. **[Optional]** If you want to use a virtual environment.
	
    ```
    $ virtualenv envsrclus
    $ source envsrclus/bin/activate
    ```
    
3. Install Modules

	Requirement Modules
 
	```
    $ pip install -r requirements.txt 
    ```
    
    * Note: **Windows OS**, Please install this first
    ```$ pip install https://github.com/wannaphongcom/artagger/tarball/master#egg=artagger```
      
    NLTK POS Tagger

      ```
      $ python -c "import nltk; nltk.download('averaged_perceptron_tagger');"
      ```
  
4. Download files in **datas** directory from this [link](https://drive.google.com/open?id=1NjvARd1gyEdhEpQX9zUi_OUsnLfXhz68) and Extract it in **core** directory
   
#### Description
* Collect datas from pantip.com
  ```
  $ python 1.getdata.py 
  ```
* Word Prepraration
  ```
  $ python 2.wordcut.py 
  ```
* TF-IDF
  ```
  $ python 3.tfidf.py 
  ```
* Make a model
  ```
  $ python 4.model.py 
  ```
* Run API Serve
  1. Run this command ``` $ python server.py ```
  2. Go to [http://localhost:5000/api](http://localhost:5000/api)
