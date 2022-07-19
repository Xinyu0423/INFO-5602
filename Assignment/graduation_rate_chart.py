import numpy as np
import matplotlib.pyplot as plt

# x_axis=["2007-08","2008-09","2009-10","2010-11","2011-12","2012-13","2013-14"]
# y_axis=[0.75,0.75,0.78,0.79,0.80,0.81,0.82]
# fig = plt.figure(figsize = (10, 5))
 
# # creating the bar plot
# plt.bar(x_axis, y_axis,
#         width = 0.4)
 
# for a,b in zip(x_axis,y_axis):
#     plt.text(a, b, "%.0f%%"%(b*100), ha='center', va= 'bottom',fontsize=12)

# plt.xlabel("Year")
# plt.ylabel("Percentage")
# plt.title("High School Graduation Rate Under President Obama")
# plt.show()

x_axis=[0.43,0.57]
y_axis=["milk","soda"]
plt.barh(y_axis, x_axis)
for i, v in enumerate(x_axis):
    plt.text(v , i , "%.0f%%"%(v*100), color='blue', fontweight='bold')
 
# setting label of y-axis
plt.ylabel("Product Categories")
 
# setting label of x-axis
plt.xlabel("Percentage")
plt.title("What should cost less: a cup of milk or a cup of soda")
plt.show()



