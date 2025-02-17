# 📝 TPC2

In this TPC  we were asked to create a program that reads a CSV file and prints its content as desired.
The trick is that we could not use the `csv` module from Python and a line on the csv could have a multi-line description field so we had to implement our own CSV parser.

## Author
<p><strong>Name:</strong> Fábio Magalhães</p>
<p><strong>Number:</strong> A104365</p>

## Results

<!--
###### ⚠️ ATTENTION: To run the following commands you need to execute them from the root of the project and use at leat Python 3.10 (if not, you need to add the `__init__.py` file to the *utils* folder and every *TPC folder*.) 

To run the program you can use:
```bash
python -m TPC2.csvparser
```
-->

The code is able to detect when or not the description field is multi-line and print the content of the CSV file as desired. And deliver the expected results. And the CSV parser works with any CSV file. (It can be used without construction a class object).

To run the program you can use:
```bash
python .\csvparser.py
```

## Assets
![](https://i.imgur.com/bNqceAX.png)
![](https://i.imgur.com/Nv4VFD1.png)
![](https://i.imgur.com/fujTlFm.png)
![](https://i.imgur.com/qCx6KeI.png)