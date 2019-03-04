# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:36:59 2019

@author: Naveen Gunasekaran
"""
input_file = "A-small-practice.in";
#input_file = "A-large-practice.in";
output_file = "Output_small_set.txt";
#output_file = "Output_large_set.txt";

file_in = open (input_file, "r");
file_out = open (output_file, "w");
line = " ";
line = file_in.readline();
no_test_cases = int(line);
test_case_no = 1;
while no_test_cases != 0:
    line = file_in.readline();
    no_Gbus = int(line);
    
    line = file_in.readline();
    list_bus = [];
    for every_bus in line.split():
        list_bus.append (int(every_bus));
    
    line = file_in.readline();
    no_cities = int (line);
    
    dict_city_need = {};
    while no_cities != 0:
        line = int (file_in.readline());
        dict_city_need[line] = 0;
        no_cities = no_cities - 1;
    
    for keys in dict_city_need.keys():
        for i in range (0,len(list_bus),2):  
            if keys >= list_bus[i]:  
                if keys <= list_bus [i + 1]:
                    dict_city_need[keys] = dict_city_need[keys] + 1;    

    file_out.write("Case #" + str(test_case_no) + ": ");
    for value in dict_city_need.values():
        file_out.write(str(value));
        file_out.write(" ");
    file_out.write ("\n");
    test_case_no = test_case_no + 1;
    no_test_cases = no_test_cases -1 ;
    line = file_in.readline();

file_in.close();
file_out.close();
