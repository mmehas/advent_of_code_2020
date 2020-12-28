from collections import defaultdict
from sys import stdin

stdin = open("input.txt", "r")

product_cnt = defaultdict(int)
all_products = set()
solution = dict()
ing2p = dict()

for line in stdin:
    products, ingredients = line.replace(')', '').split('(contains')
    products = list(map(str.strip, products.split()))
    all_products.update(products)
    ingredients = list(map(str.strip, ingredients.split(',')))
    for product in products:
        product_cnt[product] += 1
    for ingredient in ingredients:
        if ingredient in ing2p:
            ing2p[ingredient] = ing2p[ingredient].intersection(set(products))
        else:
            ing2p[ingredient] = set(products)

another_try = True
while another_try:
    another_try = False
    resolved_product = None
    for ingredient, products in ing2p.items():
        if len(products) == 1:
            resolved_product = next(iter(products))
            solution[ingredient] = resolved_product
            break
    for ingredient, products in ing2p.items():
        if resolved_product in products:
            products.remove(resolved_product)
    another_try = resolved_product is not None

res = 0
for product in all_products:
    if not product in solution.values():
        res += product_cnt[product]

print(res)
print(solution.values())
print(','.join([v[1] for v in sorted(solution.items())]))
