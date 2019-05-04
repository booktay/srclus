## Core


### Directory Structure


  ```
  core/
  |__ srcluslib/
  |		|__ corpus/
  |		|	|__ customwords.py
  |		|	|__ pantip.py
  |		|	|__ stopwords.py
  |		|
  |		|__ utility/
  |		|	|__ iorq.py
  |		|
  |		|__ model/
  |			|__ tfidf.py
  |			|__ tokenize.py
  |			|__ word2vec.py
  |
  |__ datas/
  |		|__ corpus/  
  |		|	|__ customwords.json
  |		|	|__ stopwords.json
  |		|
  |		|__ model/
  |		|__ tfidf/
  |		|__ token/
  |		|__ raw/
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
     
    Jupyter Notebook
    	 
       ```
       $ pip install ipykernel
       $ python -m ipykernel install --user --name=envsrclus
       ```

      * Check Virtual Environment on Jupyter  ```jupyter kernelspec list```

      * Remove Virtual Environment on Jupyter  ```jupyter kernelspec uninstall myenv```
  
4. Download files in **datas** directory from this [link](https://github.com/facebook/create-react-app) and Extract it in **core** directory
   
7. Start program - Let's play
	```
    $ python server.py
    ```
  