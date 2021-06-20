import validictory
from bmi_calculator_manager import BMI_Manager

VALIDATION_MAP = {'bmi': {
    'type': 'dict',
    'properties': {
                   'HeightCm': {'type': 'integer', 'required': True},
                   'WeightKg': {'type': 'integer', 'required': True},
                   'Gender': {'type': 'string', 'required': False},
                   
                   }}}

class BMI_Calculator_Api():
    """
    THe controller get the data fro enduser and validates the data, and call the
    manager class to do the required calculation
    """
    def __init__(self, data):
        self.data = data
#         self.validate()
    
    def bmi_calculate(self):
        """
        This function call the manager function
        """
        try:
            manager_obj  = BMI_Manager(self.data)
            manager_obj.bmi_calculation()
        except Exception as ex:
            print("Exception in bmi_calculate function")
    
    def validate(self):
        """
        This function validates the given data
        """
        validictory.validate(self.data, VALIDATION_MAP["bmi"])
    
if __name__ == "__main__":
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167,"WeightKg": 82}]
    obj = BMI_Calculator_Api(data)
    obj.bmi_calculate()