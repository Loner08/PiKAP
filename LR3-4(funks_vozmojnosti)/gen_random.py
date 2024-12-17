import random
def gen_random(num_count, begin, end):
 for _ in range(num_count):
    print(random.randrange(begin, end))
def main():
 gen_random(5, 1, 3)
if __name__ == "__main__":
 main()