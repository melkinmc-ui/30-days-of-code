#!/bin/python3

import math
import os
import random
import sys
import re

if __name__ == '__main__':
    N = int(input().strip())
    
    gmail_users = []
    # Patron que busca correos finalizados en @gmail.com
    pattern = r'@gmail\.com$'
    
    for _ in range(N):
        first_name, email_id = input().rstrip().split()
        if re.search(pattern, email_id):
            gmail_users.append(first_name)
            
    # Ordenar alfabeticamente
    gmail_users.sort()
    
    for name in gmail_users:
        print(name)