This project analyzes the LINK open source global food prices dataset using Arkouda (a software package that allows a user to interactively issue massive parallel computations on distributed data using functions and syntax that mimic NumPy, the underlying computational library used in most Python data science workflows.)  

## Requirements

<aside>
💡

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
