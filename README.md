# COMP-BIO-T3-2019-2

The purpose of this work is to explore the usage of the GCN algorithm in text

One of the ideias is to use the https://github.com/dmlc/dgl or the implementation from the author kipf: https://github.com/tkipf


## Installing

Python 3.X+ is required to maked it work.

We recommend that you use an virtual environment. 

You will need to install virtualenv using pip

```
pip install virtualenv
```

or 

```
pip3 install virtualenv
```

Once virtualenv is installed, you just need to run inside the in the root of this directory:

```
virtualenv env 
```


Now that you already have the virtual environment setted, all you have to do is initialize it. To do so run:


In Linux
```
source env/bin/activate
```

In Windows
```
env/Scripts/activate.[ps1|bat] # Note that ps1 or bat depends on which CLI you are using: Powershell or CMD
```

Now that it is activated, you can install the dependencies:


```
pip install -r requirements.txt 
```


Note: if you want to deactivate the virtual environment, simply run `deactivate`

-----------

