# USAGE
# python bmi_calculator.py -i data/data.json

# import the necessary packages
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--filename", required=True, type=str)
args = parser.parse_args()

with open(args.filename) as json_data:
    data = json.load(json_data)
    

count = 0
Underweight = 0
Normal_Weight = 0
Overweight = 0
Moderately_Obese = 0
Severely_Obese = 0
Very_Severely_Obese =0



# iterate over the list
for i in data:
    
    locals().update(i) 
    #Calculate the BMI (Body Mass Index) using Formula 1
    BMI = WeightKg / (HeightCm/100)**2  
    

    if BMI <= 18.4:  
        BMI_Category = "underweight"
        Health_risk =  "Malnutrition risk"
        Underweight+= 1
        print("Detailed Report :",Gender,BMI, BMI_Category,Health_risk)  
    elif  18.5 <= BMI <= 24.9:  
        BMI_Category = "Normal weight"
        Health_risk =  " Low risk"
        Normal_Weight+= 1
        print("Detailed Report :",Gender,BMI,BMI_Category, Health_risk)  
    elif  25 <= BMI <= 29.9 :
        BMI_Category = " Overweight"
        Health_risk =   " Enhanced risk"
        Overweight+=1
        count+= 1
        print("Detailed Report :",Gender, BMI,BMI_Category, Health_risk)  
    elif 30 <= BMI <= 34.9 :  
        BMI_Category = "Moderately obese"
        Health_risk =  "Medium risk"
        Moderately_Obese+=1
        count+= 1
        print("Detailed Report :",Gender,BMI,BMI_Category, Health_risk)  
    elif 35 <= BMI <= 39.9 : 
        BMI_Category = " Severely obese"
        Health_risk = " High risk"
        Severely_Obese+=1
        count+= 1
        print("Detailed Report :",Gender,BMI ,BMI_Category, Health_risk)  
    elif BMI <= 40:  
        BMI_Category = " Very severely obese"
        Health_risk = "  Very high risk"
        count+= 1
        Very_Severely_Obese+= 1
        print("Detailed Report :",Gender,BMI ,BMI_Category, Health_risk)  

#print count of each category, if required.
'''
print("Total number of Underweight people",Underweight)
print("Total number of Normalweight people",Normal_Weight)
print("Total number of Overweight people",Overweight)
print("Total number of Moderately obese people",Moderately_Obese)
print("Total number of Severely Obese people",Severely_Obese)
print("Total number of Very Severely Obese people",Very_Severely_Obese)
'''


#print count of total number of overweight people. 
print("Total number of Overweight people from all categories",count)
