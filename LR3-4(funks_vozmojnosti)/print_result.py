def print_result(input_func):
 def output_func():
    print(input_func.__name__)

 result = input_func()
 if (isinstance(result, list)):
    for elem in result:
        print(elem)
 elif (isinstance(result, dict)):
    for key in result:
        print(f"{key} = {result[key]}")
    else:
        print(result)
 return output_func
@print_result
def test_1():
 return 1
@print_result
def test_2():
 return 'iu5'
@print_result
def test_3():
 return {'a': 1, 'b': 2}
@print_result
def test_4():
 return [1, 2]
def main():
 print('!!!!!!!!')
 test_1()
 test_2()
 test_3()
 test_4()
if __name__ == "__main__":
 main()