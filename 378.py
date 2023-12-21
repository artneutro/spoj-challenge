#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 21/12/2023
# Updates:
# 
# SPOJ
# Problem 378
# SIZECON - Size Contest
# https://www.spoj.com/problems/SIZECON/
#

#
# Print the sum of all positive inputs
#

while True :
    # Get the number of cases
    case = int(input())
    if case == 0 :
        exit() ;
    # SUm all positive integers
    solution = 0
    while case > 0 :
        next = int(input())
        if next > 0 :
            solution = solution + next
        case = case - 1
    print(solution) ;
    exit() ;







