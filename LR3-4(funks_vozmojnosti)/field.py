def field(items, *args):
 assert len(args) > 0
 for item in items:
    for arg in args:
        if item[arg]:
            print(item[arg], end = ' ')
 print()
def main():
 goods = [
 {'title': 'Carpet', 'price': 2000, 'color': 'green'},
 {'title': 'Sofa', 'price': 5300, 'color': 'black'}
 ]
 field(goods, 'title')
 field(goods, 'title', 'price')

if __name__ == "__main__":
 main()
