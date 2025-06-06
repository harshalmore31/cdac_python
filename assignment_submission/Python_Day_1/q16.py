# 16) print the following pattern
# *   *   *   *   *   
#   *   *   *   *   
#     *   *   *   
#       *   *   
#         *   

for i in range(5):
    print('  ' * i + '*   ' * (5 - i))