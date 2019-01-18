# Install Python Dependencies

```
pip install tensorflow[tensorflow-gpu] deepcut pythainlp sklearn pprint nltk
```
* Note: standard ```artagger``` package from PyPI will not work on Windows, please ```pip install https://github.com/wannaphongcom/artagger/tarball/master#egg=artagger```

```
import nltk
nltk.download('averaged_perceptron_tagger')
```