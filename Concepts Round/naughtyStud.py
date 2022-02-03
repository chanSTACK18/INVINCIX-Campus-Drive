""" 
A class room is infamous for naughty students. The principal had asked their class teacher to note
down names of the candidates that are caught disturbing during a class. At the end of every month,
the principal would want to see the naughtiest candidate by looking at who’s name has occurred in
the list the highest number of times. Also the principal would like to know if any one is doing better
and would want to know who’s the least naughty.

"""
"""
Input
1. N – number of entries in the list
2. For each I in N
    a. Name of the candidate

Output
1. Most Naughty candidate’s name
2. Least Naughty candidate’s name

"""

# Write a program that can tell the principal both the least and the most naughty candidate in the list.


n = 10

def nameCounter(n, list):
    count = []
    for i in range(n):
        count.append(0)
    for i in range(n):
        for j in range(n):
            if list[i] == list[j]:
                count[i] += 1
    return count

def mostNaughty(n, list):
    mostNaughty = nameCounter(n, list)
    most = 0
    for i in range(n):
        if mostNaughty[i] > mostNaughty[most]:
            most = i
    return list[most]

def leastNaughty(n, list):
    leastNaughty = nameCounter(n, list)
    least = 0
    for i in range(n):
        if leastNaughty[i] < leastNaughty[least]:
            least = i
    return list[least]

if __name__ == '__main__':
    list = []
    for i in range(n):
        list.append(input())
    mostNaughty = mostNaughty(n, list)
    leastNaughty = leastNaughty(n, list)

    print('Most naughty-',mostNaughty)
    print('Least naughty-',leastNaughty)
    

#Example
"""
N – 10
Neil
John
Shilpa
Neil
KT
Jack
Shilpa
KT
John
KT
"""

# Output
# Most naughty- KT
# Least naughty- Jack