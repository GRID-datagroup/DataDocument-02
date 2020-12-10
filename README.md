# GRID Document

## Introduction
This project is written to help the use of GRID Science Data Products, and is constantly being improved; if you encounter any problems or have suggestions, please contact GRID Team  

## Environment
This project is built with [Sphinx](https://www.sphinx-doc.org/en/master/), supported markdown file and use [ReadtheDocs](https://readthedocs.org) for hosting  

#### Development environment
```
Python 3.9.1rc1
Sphinx 
```

#### Dependent package
```
sphinx
sphinx-autobuild
sphinx_rtd_theme
recommonmark
sphinx-markdown-tables
```

#### Config
* `conf.py` :
```python
extensions = ['sphinx_markdown_tables', 'recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
```

The following operations will support local Chinese search:
* `jieba package` :
```python
pip3 install jieba
```
* `zh_CN.py` : move the `zh_CN.py` file in the `sphinx/search` directory
* `sphinx/search/__init.py__` :
```python
from sphinx.search import en, ja, zh_CN
languages = {
    'en': en.SearchEnglish,
    'zh_CN': zh_CN.SearchChinese
}
```

#### Local test
* `Server` : use `en/zh_server.py` with `Flask` module
* `Makefile` : Custom `make html` command

## Category
1. Science Data Product Document

## Reference
* [使用ReadtheDocs托管文档](https://www.xncoding.com/2017/01/22/fullstack/readthedoc.html)
* [ReadthrDocs](https://docs.readthedocs.io/en/stable/index.html)
* [Sphinx](https://www.sphinx-doc.org/en/master/)