# 2) create a dictionary with pairs
#	soap:100
#	deo:300
#	perfume:400
# now accept a product name from user (in any case, so you have to handle "ignore case") and display its price. Also , if the product is not present in the dictionary display the error message " product not available "
#	Note:  you should not get "KeyError:" in the program.


products = {
    "soap": 100,
    "deo": 300,
    "perfume": 400
}
product_name_input = input("Enter product name: ")
product_name_lower = product_name_input.lower()

if product_name_lower in products:
    print(f"Price of {product_name_input}: {products[product_name_lower]}")
else:
    print("product not available")
