import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_increase_salary_vectorized(self):
        """Test if salary is increased correctly by 10% using vectorized operations."""
        try:
            original_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary before increment
            self.analysis.increase_salary_vectorized()
            increased_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary after increment
            obj = increased_salary == original_salary * 1.10  # Check if the salary increased by 10%
            self.test_obj.yakshaAssert("TestIncreaseSalaryVectorized", obj, "functional")
            print("TestIncreaseSalaryVectorized = Passed" if obj else "TestIncreaseSalaryVectorized = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIncreaseSalaryVectorized", False, "functional")
            print("TestIncreaseSalaryVectorized = Failed")

    def test_increase_salary_loop(self):
        """Test if salary is increased correctly by 10% using loop-based operation."""
        try:
            original_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary before increment
            self.analysis.increase_salary_loop()
            increased_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary after increment
            obj = increased_salary == original_salary * 1.10  # Check if the salary increased by 10%
            self.test_obj.yakshaAssert("TestIncreaseSalaryLoop", obj, "functional")
            print("TestIncreaseSalaryLoop = Passed" if obj else "TestIncreaseSalaryLoop = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIncreaseSalaryLoop", False, "functional")
            print("TestIncreaseSalaryLoop = Failed")

    def test_compare_performance(self):
        """Test if performance comparison works correctly."""
        try:
            data = {"Employee_ID": range(1, 10001), "Name": ["Employee"] * 10000, "Department": ["HR"] * 10000, "Salary": [50000] * 10000}
            self.analysis = EmployeeDataAnalysis(file_path='employee_data.csv', data=data)
            vectorized_time, loop_time = self.analysis.compare_performance()
            obj = vectorized_time < loop_time  # Vectorized operation should be faster
            self.test_obj.yakshaAssert("TestComparePerformance", obj, "functional")
            print(f"TestComparePerformance = Passed" if obj else f"TestComparePerformance = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestComparePerformance", False, "functional")
            print("TestComparePerformance = Failed")
