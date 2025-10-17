#Import all libraries needed for the exercise
import csv #this library was not actually used
import pandas as pd
import matplotlib.pyplot as plt
import argparse

#Make the file a CLI input argument to avoid hardcoding
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--csv_file', help='Input the csv file') #the flags -f or --csv_file can be used to input the file
args = parser.parse_args() #I parse the argument

#2.1 Read the file into a pd dataframe
csv_file = pd.read_csv(args.csv_file, sep=',') #the csv file is read into a pandas dataframe. args.csv_file is used to get the argument for the file given by the user

#2.2.1 Create a function that creates a histogram and saves the figure as fpkm_distributions.png
def hist_fpkm(data): #I define the function and make it have one parameter, data, which should be a dataframe
#It is not necessary to assign the plt. outputs to a variable (hist_plt = plt.) but I prefer it since I feel like I can keep track of my plots better this way
    hist_plt = plt.hist(data['fpkm_log2']) #I plot the fpkm_log2 data into ahistogram using matplotlib
    hist_plt = plt.title('Distribution of gene expression') #I add a plot title
    hist_plt = plt.xlabel('Expression') #I add an x-axis label
    hist_plt = plt.ylabel('Number of genes') #I add an y-axis label
    hist_plt.figure.savefig('fpkm_distribution.png') #I save the figure as a png file 

#2.2.2 Call the function
hist_fpkm(csv_file) #I call the function with my pandasa dataframe as input
