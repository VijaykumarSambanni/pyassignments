# Modulue with with pytest naming convention created

import pytest

class Test_Task:
# Class with pytest naming convention in above module
    @pytest.mark.smoke
    def test_function1(self):
        print("Function 1")

    @pytest.mark.skip
    def test_function2(self):
        print("Function 2")


    def test_cognizant_function3(self):
        print("Function 3")


    def test_cognizant_function4(self):
        print("Function 4")


    def test_cognizant_function5(self):
        print("Function 5")


    def test_function6(self):
        print("Function 6")


    def test_function7(self):
        print("Function 7")


    def test_function8(self):
        print("Function 8")

    @pytest.mark.xfail
    def test_function9(self):
        print("Function 9")

    @pytest.mark.smoke
    def test_function10(self):
        print("Function 10")

# 10 functions created