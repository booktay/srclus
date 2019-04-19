## Module

### Install Python Dependencies

#### Base
```
pip install gensim pythainlp sklearn pprint nltk cython
```

```
pip tensorflow[tensorflow-gpu] deepcut
```

* Note: **Windows OS**, please install this first
```
pip install https://github.com/wannaphongcom/artagger/tarball/master#egg=artagger
```

#### NLTK POS Tagger
```
import nltk
nltk.download('averaged_perceptron_tagger')
```

### Web Server
```
pip install flask flask_cors paramiko
```

#### Test Embedded Graph
```
pip install matplotlib scipy
```

#### Use Virtual Environment on Jupyter 
```
pip install ipykernel
python -m ipykernel install --user --name=envsrclus
```

* Check Virtual Environment on Jupyter  ```jupyter kernelspec list```

* Remove Virtual Environment on Jupyter  ```jupyter kernelspec uninstall myenv```