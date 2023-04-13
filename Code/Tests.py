from TestLib import test, affirm, affirm_eq, affirm_ne

class FunnyFunctions:
    def funny_function(square):
        return square[0] * 2

    def funny_function_2(a, b):
        return a**2 + b**2

class TestFunnyFunctions:

    @test
    def test_find_square_circumference():
        result = FunnyFunctions.funny_function([4, 4, 4])
        affirm(result >= 0)

    def pitagoras(a, b):
        result = FunnyFunctions.funny_function_2(a, b)
        affirm(result <= 0)
    
def not_wrapped():
    return None

if __name__ == "__main__":
    #Will become: TestFunnyFunctions.test_all()
    TestFunnyFunctions.test_find_square_circumference()
    TestFunnyFunctions.pitagoras(2, 3)