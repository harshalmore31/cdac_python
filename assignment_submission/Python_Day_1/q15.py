# 15) print the following pattern

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)