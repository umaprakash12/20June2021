import pandas as pd
import timeit


class BMI_Manager():
    
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def calculate_bmi(self):
        """
        This function creates a new column in data frame called bmi
        and to get the bmi value internally it called get_bmi function for each record
        """
        self.df['bmi'] = self.df.apply(self.get_bmi, axis=1)
          
    def get_bmi(self,df):
        """
        This function is used to calculate the bmi using formula
        """
        return df['WeightKg'] / (df['HeightCm']/100)**2
    
    def catagarize_over_weight(self):
        """
        This function creates a new column in data frame called is_over_weight
        and to get the is_over_weight flag  internally it called is_over_weight function for each record
        """
        self.df['is_over_weight'] = self.df.apply(self.is_over_weight, axis=1)
        
        
    def is_over_weight(self,df):
        """
        This function set the value in is_over_weight flag , if the bmi is between 25 and 29.9
        """
        return int(df['bmi'] > 25 and df['bmi'] < 29.9)
#   
    
    def count_no_of_over_weight(self):
        """
        This function is used to count the number of over weight people
        """
        return self.df['is_over_weight'].sum()
    

    def bmi_calculation(self):
        self.calculate_bmi()
        self.catagarize_over_weight()
        count=self.count_no_of_over_weight()
        print("Number of people in over weight")
        print(count)
    

# def bmi(data):
#     count =0
#     for df in data:
#         val = df['w'] / df['h']**2  
#         if val > 25 and val < 29.9:
#             count+=1
# #     print(count)
#   
# data = [
#   { 'h': 1.80, 'w': 80 },
#   { 'h': 1.70, 'w': 90 },
#   { 'h': 1.60, 'w': 60 },
# ]
# start = timeit.repeat("bmi(data)", setup = "from __main__ import bmi, data")
# print(start)
# bmi(data)  
# end = timeit.timeit()
# print(end - start)
        
        
# if __name__ == "__main__":
#     data = [
#   { 'h': 1.80, 'w': 80 },
#   { 'h': 1.70, 'w': 90 },
#   { 'h': 1.60, 'w': 60 },
# ]
# #     start = timeit.repeat("method(data)", setup = "from __main__ import method, data")
#  
#     
#     obj = BMI_Manager(data)
#     obj.calculate_bmi()
#     obj.catagarize_over_weight()
#     count=obj.count_no_of_over_weight()
#     print(count)
#     print(obj.df)
        
        
        
        
