# Install Python Dependencies

####Base
```
pip install tensorflow[tensorflow-gpu] gensim deepcut pythainlp sklearn pprint nltk
```

* Note: **Windows OS**, please install this first
```
pip install https://github.com/wannaphongcom/artagger/tarball/master#egg=artagger
```

####NLTK POS Tagger
```
import nltk
nltk.download('averaged_perceptron_tagger')
```

####Test Embedded Graph
```
pip install matplotlib scipy
```

####Use Virtual Environment on Jupyter 
```
pip install --user ipykernel
python -m ipykernel install --user --name=envsrclus
```

* Check Virtual Environment on Jupyter  ```jupyter kernelspec list```

* Remove Virtual Environment on Jupyter  ```jupyter kernelspec uninstall myenv```