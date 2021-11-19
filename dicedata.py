import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

dice_result = []
file = csv.DictReader('StudentsPerformance.csv')
for i in range(0,1000):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    dice_result.append(d1+d2)

mean = sum(file)/len(file)
standard_deviation = statistics.stdev(file)
mode = statistics.mode(file)
median = statistics.median(file)

print("Mean : - ",mean)
print("Mode : - ",mode)
print("Median : - ",median)
print("SD : - ",standard_deviation)

graph = ff.create_distplot([file],["results"],show_hist = False)

first_std_deviation_start,first_std_deviation_end = mean - standard_deviation,mean + standard_deviation
second_std_deviation_start,second_std_deviation_end = mean - 2*standard_deviation,mean + 2*standard_deviation
third_std_deviation_start,third_std_deviation_end = mean - 3*standard_deviation,mean + 3*standard_deviation

print('First SD = ', first_std_deviation_start,first_std_deviation_end)
print('Second SD = ', second_std_deviation_start,second_std_deviation_end)
print('Third SD = ', third_std_deviation_start,third_std_deviation_end)

graph.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name  ='mean'))
graph.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0,0.17],mode = 'lines',name  ='STD 1 Start'))
graph.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0,0.17],mode = 'lines',name  ='STD 1 End'))
graph.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start],y = [0,0.17],mode = 'lines',name  ='STD 2 Start'))
graph.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0,0.17],mode = 'lines',name  ='STD 2 End'))

list_of_data_within_1_std_deviation = [result for result in dice_result if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result>second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result>third_std_deviation_start and result<third_std_deviation_end]
graph.show()
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result))) 
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result))) 
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))