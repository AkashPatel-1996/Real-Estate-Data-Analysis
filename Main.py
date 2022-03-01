import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)

df1 = pd.read_csv('Bengaluru_House_Data.csv')


df2 = df1.drop(['area_type','society','balcony','availability'],axis='columns')
df2.head()


df3 = df2.dropna()
df3.isnull().sum()

df3['bhk'] = df3['size'].apply(lambda x :int(x.split(' ')[0]))

def is_float(x):
    try:
        float(x)
    except:
        return False
    return True


df3[~df3['total_sqft'].apply(is_float)].head()

df4 = df3.copy()


def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)


df1.groupby('area_type')['area_type'].agg('count')
def locations_wise_flats():

    area = df1.value_counts('size').index.tolist()
    max_flat = df1.value_counts('size').index[0]
    min_flat = df1.value_counts('size').index[-1]
    count= df1.value_counts('size').tolist()
    plt.bar(area, count, color ='green', width = .2)
 
    plt.xlabel("Types of Flats")
    plt.ylabel("No. of homes available")
    plt.title("Different types of flats that available in market for purchase")
    plt.show()
    print("here are my analysis of the data")
    print("Maxium number of flats that are available :", max_flat )
    print("Minimum number of flats that are available :", min_flat)

answer = input("Do you want to show the graph of homes in different areas :")

if answer == "yes":
    locations_wise_flats()
    print("Graph shows that maximum numbers of flats that are available in city is in range of 2-BHK to 5-Bhk")
    
else:
    print("Ok, Thanks for visiting here!")


df5 = df4.copy()
df5.head(10)

df5['price_per_sqft'] = df5[('price')]*100000/df5[('total_sqft')]
df5.head()

df5.location = df5.location.apply(lambda x : x.strip())
locations_stats = df5.groupby('location')['location'].agg('count').sort_values(ascending = False)


def show_graph(answer):
    whitefield_data = df5[df5["location"]== answer]
    print( whitefield_data.value_counts("bhk").size)
    print(whitefield_data.value_counts("bhk"))
    lis= []
    lis_data = []
    if whitefield_data.value_counts("bhk").size >= 1:
        home__1_whitefield_ind = whitefield_data.value_counts("bhk").index[0]
        home__1_whitefield = whitefield_data.value_counts("bhk").values[0]
        lis.append(str(home__1_whitefield_ind) + " bhk")
        lis_data.append(home__1_whitefield)
      
    
    if whitefield_data.value_counts("bhk").size >= 2:
        home__1_whitefield_ind = whitefield_data.value_counts("bhk").index[1]
        home__1_whitefield = whitefield_data.value_counts("bhk").values[1]
        lis.append(str(home__1_whitefield_ind) + " bhk")
        lis_data.append(home__1_whitefield)
      
    
    if whitefield_data.value_counts("bhk").size >= 3:
        home__1_whitefield_ind = whitefield_data.value_counts("bhk").index[2]
        home__1_whitefield = whitefield_data.value_counts("bhk").values[2]
        lis.append(str(home__1_whitefield_ind) + " bhk")
        lis_data.append(home__1_whitefield)
    

    
    plt.bar(lis,lis_data ,width = 0.1)
    plt.title('title name')
    plt.xlabel('xAxis name')
    plt.ylabel('yAxis name')
    plt.show()
    print("This is my analysis of different sizes of homes that are available in Whitefield.")
    
checkIt = input("Do you want to show the graph of different size of homes that are available in different locations: ")
answer = input("Enter the loation name for which you want to see the graph for flats : ")

if checkIt == "yes":
    show_graph(answer)
else:
    print("Ok, Thanks for visiting here!")
    
answer = input("Do you want to show the graph of different size of homes that are available in Whitefield: ")

if answer == "yes":
    show_graph()
else:
    print("Ok, Thanks for visiting here!")
    

       

value = int(input('enter the size of flat to know the price :'))
df5 = df5.dropna()

if value == 3:
    df5 = df5[(df5["location"]== "Whitefield") & (df5['bhk'] == 3)]
    df5["price_per_sqft"] = pd.to_numeric(df5["price_per_sqft"])
    mean_3 = df5["price_per_sqft"].mean()
    print('Average price of 3 BHK flat that are available is :',mean_3)
elif value == 2:
    df5 = df5[(df5["location"]== "Whitefield") & (df5['bhk'] == 2)]
    df5["price_per_sqft"] = pd.to_numeric(df5["price_per_sqft"])
    mean_2 = df5["price_per_sqft"].mean()
    print('Average price of 2 BHK flat that are available is :',mean_2)
elif value == 4:
    df5 = df5.loc[(df5["location"]== "Whitefield") & (df5['bhk'] == 4)]
    df5["price_per_sqft"] = pd.to_numeric(df5["price_per_sqft"])
    mean_4 = df5["price_per_sqft"].mean()
    print('Average price of 4 BHK flat that are available is :',mean_4)
else:
    print("okay! Thanks")
