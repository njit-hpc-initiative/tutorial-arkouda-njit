This project analyzes the open source global food prices [dataset](https://www.kaggle.com/datasets/jboysen/global-food-prices) using Arkouda (a software package that allows a user to interactively issue massive parallel computations on distributed data using functions and syntax that mimic NumPy, the underlying computational library used in most Python data science workflows.)  


The project has a set of basic computations done on the food dataset which cn be listed as:

**1. Conversion and cleaning of data**
- For analyzing any dataset into Arkouda, we need to make sure the dataset is in HDF5 format. For this we have few different methods but the preferable one is to use a formatter file and convert the existing CSV dataset.

- Cleaning of the dataset involved not having any advanced datatypes in the dataset

**2. Currency Conversion**
- Since we are using currency as a comparison parameter in this project we have converted all the currencies into 

**3. **
-  

**4.dd**
dd
**5.ddd**


## Requirements

<aside>
💡 Basic knowledge of python and some linux commands

</aside>

## How to run the code

**Step 1:**

Install Arkouda 

The steps for the same can be found at Click here

**Step 2:**

Single-locale startup:

```bash
./arkouda_server
```

**Step 3:**

Head to the respective Jupyter Notebook, where you have your project code

Import Arkouda

```bash
import arkouda as ak
```

Connect Arkouda to your Jupyter Notebook

```bash
#replace MacBook-Pro-7 with your device name
ak.connect(connect_url='tcp://MacBook-Pro-7.local:5555 ') #connecting to arkouda server
```

**Step 4:**

Run your respective source code
