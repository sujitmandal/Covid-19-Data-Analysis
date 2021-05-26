## Covid-19-Data-Analysis
covid-19(coronavirus) data analysis 


## Argument 
```
-dose = Number Of Dose 
    Example : one or two or both

-d = Date 
    Example : 26-05-2021 [dd/mm/yy]

-p = Pincode 
    Example : 735101

-o = Output 
    Example : csv or html 
```

## How To Run Vaccine Information In India
```
Step 1 : git clone https://github.com/sujitmandal/Covid-19-Data-Analysis.git

Step 2 : pip install -r requirements.txt or pip3 install -r requirements.txt

Step 3 : cd Covid-19-Data-Analysis/vaccine-info-india

Step 4 : python vaccine.py -dose [dose] -d [date] -p [pincode] -o [output]

    Example 1 : python vaccine.py -dose one -d 26-05-2021 -p 735101 -o csv

    Example 2 : python vaccine.py -dose one -d 26-05-2021 -p 735101 -o html

    Example 3 : python vaccine.py -dose two -d 26-05-2021 -p 735101 -o csv

    Example 4 : python vaccine.py -dose two -d 26-05-2021 -p 735101 -o html

    Example 5 : python vaccine.py -dose both -d 26-05-2021 -p 735101 -o csv

    Example 6 : python vaccine.py -dose both -d 26-05-2021 -p 735101 -o html
```

## Required Package's or Librarie's:
```
pip install pandas
```
[pandas Link](https://pypi.org/project/pandas/)