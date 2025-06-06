# 17) print the following

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# * * * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 

for i in range(6):
    spaces = ' ' * (5 - i)
    stars = '* ' * (i + 1)
    print(spaces + stars)

for i in range(4, -1, -1):
    spaces = ' ' * (5 - i)
    stars = '* ' * (i + 1)
    print(spaces + stars)