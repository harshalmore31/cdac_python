colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = [{'color_name': c, 'color_code': d} for c, d in zip(colors, codes)]
print(result)