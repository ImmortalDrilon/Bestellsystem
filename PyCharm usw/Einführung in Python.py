for n in [1.1, 1.9, 3.4]:   
    variant_1 = n + (1 - n % 1) if n % 1 else n    
    variant_2 = n // 1 + 1.0 if n % 1 else n    
    variant_3 = n // 1 + (n % 1 > 0)   

print(f'{n} -> v1({variant_1}), v2({variant_2}), v3({variant_3})')