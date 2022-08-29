#1 Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from datetime import datetime

# getting the timestamp
#ts = datetime.timestamp(dt)

#print("Date and time is:", dt)
#print("Timestamp is:", ts)

o=1
while o==1:
    # Getting the current date and time
    dt = datetime.now()
    #str_date_time = dt.strftime("%d-%m-%Y, %H:%M:%S")
    str_day = dt.strftime("%d")
    #day = int(str_date_time[0:2])
    day=int(str_day)
    index_car_entry = 0
    index_car_exit = 0
    index_truck_entry = 0
    index_truck_exit = 0
    index_bus_entry = 0
    index_bus_exit = 0
    car_plate_entry = []
    car_date_entry=[]
    car_plate_exit=[]
    car_date_exit=[]
    car_duration=[]
    car_cost=[]
    car_plate_entry_exit=[]
    truck_plate_entry = []
    truck_date_entry = []
    truck_plate_exit = []
    truck_date_exit = []
    truck_duration = []
    truck_cost = []
    truck_plate_entry_exit=[]
    bus_plate_entry = []
    bus_date_entry = []
    bus_plate_exit = []
    bus_date_exit = []
    bus_duration = []
    bus_cost = []
    bus_plate_entry_exit=[]
    flag_car_entry_exit=0
    flag_bus_entry_exit=0
    flag_truck_entry_exit=0
    dt8 = datetime.now()
    str_day2 = dt8.strftime("%d")
    day2 = int(str_day2)
    while day2==day:
        flag_car_entry=input("Enter 1 if a car enters else enter 0:")
        if flag_car_entry=='1':
            index_car_entry+=1
            car_plate_entr=input("Enter the car plate of the car it enters:")
            col = []
            for i in range(0,2):
                if i==0:
                  col.append(index_car_entry)
                else:
                  col.append(car_plate_entr)
            car_plate_entry.append(col)
            col1=[]
            for i in range(0,2):
                if i == 0:
                    col1.append(index_car_entry)
                else:
                    dt1 = datetime.now()
                    entry_time = dt1.strftime("%H:%M:%S")
                    col1.append(entry_time)
            car_date_entry.append(col1)
        flag_car_exit = input("Enter 1 if a car exits else enter 0:")
        if flag_car_exit == '1':
            index_car_exit += 1
            car_plate_exi = input("Enter the car plate of the car it exits:")
            col2=[]
            for i in range(0,2):
                if i==0:
                  col2.append(index_car_exit)
                else:
                  col2.append(car_plate_exi)
            car_plate_exit.append(col2)
            col3=[]
            for i in range(0,2):
                if i == 0:
                    col3.append(index_car_exit)
                else:
                    dt2 = datetime.now()
                    exit_time = dt2.strftime("%H:%M:%S")
                    col3.append(exit_time)
            car_date_exit.append(col3)
        flag_truck_entry = input("Enter 1 if a truck enters else enter 0:")
        if flag_truck_entry == '1':
            index_truck_entry += 1
            truck_plate_entr = input("Enter the truck plate of the truck it enters:")
            col4 = []
            for i in range(0, 2):
                if i == 0:
                    col4.append(index_truck_entry)
                else:
                    col4.append(truck_plate_entr)
            truck_plate_entry.append(col4)
            col5 = []
            for i in range(0, 2):
                if i == 0:
                    col5.append(index_truck_entry)
                else:
                    dt3 = datetime.now()
                    entry_time1 = dt3.strftime("%H:%M:%S")
                    col5.append(entry_time1)
            truck_date_entry.append(col5)
        flag_truck_exit = input("Enter 1 if a truck exits else enter 0:")
        if flag_truck_exit == '1':
            index_truck_exit += 1
            truck_plate_exi = input("Enter the truck plate of the truck it exits:")
            col6 = []
            for i in range(0, 2):
                if i == 0:
                    col6.append(index_truck_exit)
                else:
                    col6.append(truck_plate_exi)
            truck_plate_exit.append(col6)
            col7 = []
            for i in range(0, 2):
                if i == 0:
                    col7.append(index_truck_exit)
                else:
                    dt4 = datetime.now()
                    exit_time1 = dt4.strftime("%H:%M:%S")
                    col7.append(exit_time1)
            truck_date_exit.append(col7)
        flag_bus_entry = input("Enter 1 if a bus enters else enter 0:")
        if flag_bus_entry == '1':
            index_bus_entry += 1
            bus_plate_entr = input("Enter the bus plate of the bus it enters:")
            col8 = []
            for i in range(0, 2):
                if i == 0:
                    col8.append(index_bus_entry)
                else:
                    col8.append(bus_plate_entr)
            bus_plate_entry.append(col8)
            col9 = []
            for i in range(0, 2):
                if i == 0:
                    col9.append(index_bus_entry)
                else:
                    dt5 = datetime.now()
                    entry_time2 = dt5.strftime("%H:%M:%S")
                    col9.append(entry_time2)
            bus_date_entry.append(col9)
        flag_bus_exit = input("Enter 1 if a bus exits else enter 0:")
        if flag_bus_exit == '1':
            index_bus_exit += 1
            bus_plate_exi = input("Enter the bus plate of the bus it exits:")
            col10 = []
            for i in range(0, 2):
                if i == 0:
                    col10.append(index_bus_exit)
                else:
                    col10.append(bus_plate_exi)
            bus_plate_exit.append(col10)
            col11 = []
            for i in range(0, 2):
                if i == 0:
                    col11.append(index_bus_exit)
                else:
                    dt6 = datetime.now()
                    exit_time2 = dt6.strftime("%H:%M:%S")
                    col11.append(exit_time2)
            bus_date_exit.append(col11)

        car_plate_entry_exit = []
        car_duration = []
        car_cost = []
        for i in range(0, index_car_exit):
            for j in range(0, index_car_entry):
                if car_plate_exit[i][1]==car_plate_entry[j][1] and car_date_exit[i][1]>car_date_entry[j][1]:
                    flag_car_entry_exit=1
                    col12=[]
                    col13=[]
                    col14=[]
                    for k in range(0, 2):
                        if k == 0:
                            col12.append(index_car_exit)
                            col13.append(index_car_exit)
                            col14.append(index_car_exit)
                        else:
                            duration_car_min=((int(car_date_exit[i][1][0:2])-int(car_date_entry[j][1][0:2]))*60)+(int(car_date_exit[i][1][3:5])-int(car_date_entry[j][1][3:5]))+((int(car_date_exit[i][1][6:8])-int(car_date_entry[j][1][6:8]))/60)
                            col12.append(round(duration_car_min))
                            if round(duration_car_min)>=0 and round(duration_car_min)<=30:
                                car_cost_euros=0
                            elif round(duration_car_min)>30 and round(duration_car_min)<=60:
                                car_cost_euros=3
                            elif round(duration_car_min)>60 and round(duration_car_min)<=120:
                                car_cost_euros=5
                            elif round(duration_car_min)>120 and round(duration_car_min)<=240:
                                car_cost_euros=7
                            else:
                                car_cost_euros=(round(duration_car_min)/60)*1
                            col13.append(car_cost_euros)
                            col14.append(car_plate_exit[i][1])
                    car_duration.append(col12)
                    car_cost.append(col13)
                    car_plate_entry_exit.append(col14)

        truck_plate_entry_exit = []
        truck_duration = []
        truck_cost = []
        for i in range(0, index_truck_exit):
            for j in range(0, index_truck_entry):
                if truck_plate_exit[i][1]==truck_plate_entry[j][1] and truck_date_exit[i][1]>truck_date_entry[j][1]:
                    flag_truck_entry_exit=1
                    col15=[]
                    col16=[]
                    col17=[]
                    for k in range(0, 2):
                        if k == 0:
                            col15.append(index_truck_exit)
                            col16.append(index_truck_exit)
                            col17.append(index_truck_exit)
                        else:
                            duration_truck_min=((int(truck_date_exit[i][1][0:2])-int(truck_date_entry[j][1][0:2]))*60)+(int(truck_date_exit[i][1][3:5])-int(truck_date_entry[j][1][3:5]))+((int(truck_date_exit[i][1][6:8])-int(truck_date_entry[j][1][6:8]))/60)
                            col15.append(round(duration_truck_min))
                            if round(duration_truck_min)>=0 and round(duration_truck_min)<=30:
                                truck_cost_euros=0
                            elif round(duration_truck_min)>30 and round(duration_truck_min)<=60:
                                truck_cost_euros=5
                            elif round(duration_truck_min)>60 and round(duration_truck_min)<=120:
                                truck_cost_euros=9
                            elif round(duration_truck_min)>120 and round(duration_truck_min)<=240:
                                truck_cost_euros=11
                            else:
                                truck_cost_euros=(round(duration_truck_min)/60)*2
                            col16.append(truck_cost_euros)
                            col17.append(truck_plate_exit[i][1])
                    truck_duration.append(col15)
                    truck_cost.append(col16)
                    truck_plate_entry_exit.append(col17)

        bus_plate_entry_exit=[]
        bus_duration=[]
        bus_cost=[]
        for i in range(0, index_bus_exit):
            for j in range(0, index_bus_entry):
                if bus_plate_exit[i][1]==bus_plate_entry[j][1] and bus_date_exit[i][1]>bus_date_entry[j][1]:
                    flag_bus_entry_exit=1
                    col18=[]
                    col19=[]
                    col20=[]
                    for k in range(0, 2):
                        if k == 0:
                            col18.append(index_bus_exit)
                            col19.append(index_bus_exit)
                            col20.append(index_bus_exit)
                        else:
                            duration_bus_min=((int(bus_date_exit[i][1][0:2])-int(bus_date_entry[j][1][0:2]))*60)+(int(bus_date_exit[i][1][3:5])-int(bus_date_entry[j][1][3:5]))+((int(bus_date_exit[i][1][6:8])-int(bus_date_entry[j][1][6:8]))/60)
                            col18.append(round(duration_bus_min))
                            if round(duration_bus_min)>=0 and round(duration_bus_min)<=30:
                                bus_cost_euros=0
                            elif round(duration_bus_min)>30 and round(duration_bus_min)<=60:
                                bus_cost_euros=7
                            elif round(duration_bus_min)>60 and round(duration_bus_min)<=120:
                                bus_cost_euros=16
                            elif round(duration_bus_min)>120 and round(duration_bus_min)<=240:
                                bus_cost_euros=19
                            else:
                                bus_cost_euros=(round(duration_bus_min)/60)*3
                            col19.append(bus_cost_euros)
                            col20.append(bus_plate_exit[i][1])
                    bus_duration.append(col18)
                    bus_cost.append(col19)
                    bus_plate_entry_exit.append(col20)





        dt8 = datetime.now()
        str_day2 = dt8.strftime("%d")
        day2 = int(str_day2)
        if (day2-day)==1:
            break
        end1 = input("If you want the program to stop running the day type number 5:")
        if end1 == '5':
            break
    if flag_car_entry_exit==1:
     for i in range(0, index_car_exit):
        print('The plate of the ',i+1,'st car that had first entry and then exit today was:',car_plate_entry_exit[i][1])
        print('The costs of the ',i+1,'st car that had first entry and then exit today was:',car_cost[i][1])
        print('The duration in minutes of the ',i+1,'st car that had first entry and then exit today was:',car_duration[i][1])
    print('The number of cars that had entry first and exited then today were', index_car_exit)
    if flag_truck_entry_exit==1:
     for i in range(0, index_truck_exit):
        print('The plate of the ',i+1,'st truck that had first entry and then exit today was:',truck_plate_entry_exit[i][1])
        print('The costs of the ',i+1,'st truck that had first entry and then exit today was:',truck_cost[i][1])
        print('The duration in minutes of the ',i+1,'st truck that had first entry and then exit today was:',truck_duration[i][1])
     print('The number of trucks that had entry first and exited then today were', index_truck_exit)
    if flag_bus_entry_exit==1:
     for i in range(0, index_bus_exit):
        print('The plate of the ',i+1,'st bus that had first entry and then exit today was:',bus_plate_entry_exit[i][1])
        print('The costs of the ',i+1,'st bus that had first entry and then exit today was:',bus_cost[i][1])
        print('The duration in minutes of the ',i+1,'st bus that had first entry and then exit today was:',bus_duration[i][1])
     print('The number of buses that had entry first and exited then today were', index_bus_exit)
    total_vehicles=index_car_exit + index_truck_exit + index_bus_exit
    print('The total number of cars,trucks and buses that had entry first and exited then today were',total_vehicles)
    end = input("If you want the program to stop running type number 5:")
    if end=='5':
        break