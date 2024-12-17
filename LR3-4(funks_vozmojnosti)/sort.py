def main():
 data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
 result = sorted(data, key = lambda x: abs(x), reverse = True)
 print(result)

 def sort_by_abs(x):
    return abs(x)
 result_with_lambda = sorted(data, key = sort_by_abs, reverse = True)
 print(result_with_lambda)
if __name__ == "__main__":
 main()