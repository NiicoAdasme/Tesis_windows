# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:54:35 2023

@author: Nico
"""

# ENERO
def enero(tprom, pr):
    if tprom > 21.15 and pr < 11.15:
        indice = 4
    else:
        if tprom > 21.15 and pr > 11.15:
            indice = 3
        else:
            if tprom <= 21.15 and tprom > 18.15 and pr < 11.15:
                indice = 3
            else:
                if tprom <= 21.15 and tprom > 18.15 and pr > 11.15:
                    indice = 2
                else:
                    if tprom <= 18.15 and tprom > 15.15 and pr < 11.15:
                        indice = 2
                    else:
                        if tprom <= 18.15 and tprom > 15.15 and pr > 11.15:
                            indice = 1
                        else:
                            if tprom < 15.15 and tprom > 0 and pr < 11.15:
                                indice = 1
                            else:
                                indice = 0

    return indice

# FEBRERO
def febrero (tprom, pr):
    if tprom > 20.4 and pr < 16.59:
        indice = 4
    else:
        if tprom > 20.4 and pr > 16.59:
            indice = 3
        else:
            if tprom <= 20.4 and tprom > 17.4 and pr < 16.59:
                indice = 3
            else:
                if tprom <= 20.4 and tprom > 17.4 and pr > 16.59:
                    indice = 2
                else:
                    if tprom <= 17.4 and tprom > 14.4 and pr <16.59:
                        indice = 2
                    else:
                        if tprom <= 17.4 and tprom > 14.4 and pr > 16.59:
                            indice = 1
                        else:
                            if tprom < 14.4 and tprom > 0 and pr < 16.59:
                                indice = 1
                            else:
                                indice = 0
                                
    return indice
    
# MARZO
def marzo (tprom, pr):
    if tprom > 18.5 and pr < 24.28:
        indice = 4
    else:
        if tprom > 18.5 and pr > 24.28:
            indice = 3
        else:
            if tprom <= 18.5 and tprom > 15.5 and pr < 24.28:
                indice = 3
            else:
                if tprom <= 18.5 and tprom > 15.5 and pr > 24.28:
                    indice = 2
                else:
                    if tprom <= 15.5 and tprom > 12.5 and pr < 24.28:
                        indice = 2
                    else:
                        if tprom <= 15.5 and tprom > 12.5 and pr > 24.28:
                            indice = 1
                        else:
                            if tprom < 12.5 and tprom > 0 and pr < 24.28:
                                indice = 1
                            else:
                                indice = 0
                    
    return indice

# ABRIL
def abril (tprom, pr):
    if tprom > 15.3 and pr < 96.2:
        indice = 4
    else:
        if tprom > 15.3 and pr > 96.2:
            indice = 3
        else:
            if tprom <= 15.3 and tprom > 12.3 and pr < 96.2:
                indice = 3
            else:
                if tprom <= 15.3 and tprom > 12.3 and pr > 96.2:
                    indice = 2
                else:
                    if tprom <= 12.3 and tprom > 9.3 and pr < 96.2:
                        indice = 2
                    else:
                        if tprom <= 12.3 and tprom > 9.3 and pr > 96.2:
                            indice = 1
                        else:
                            if tprom < 9.3 and tprom > 0 and pr < 96.2:
                                indice = 1
                            else:
                                indice = 0
    return indice                        
                        

# MAYO
def mayo (tprom, pr):
    if tprom > 11.8 and pr < 271.8:
        indice = 4
    else:
        if tprom > 11.8 and pr > 271.8:
            indice = 3
        else:
            if tprom <= 11.8 and tprom > 8.8 and pr < 271.8:
                indice = 3
            else:
                if tprom <= 11.8 and tprom > 8.8 and pr > 271.8:
                    indice = 2
                else:
                    if tprom <= 8.8 and tprom > 5.8 and pr < 271.8:
                        indice = 2
                    else:
                        if tprom <= 8.8 and tprom > 5.8 and pr > 271.8:
                            indice = 1
                        else:
                            if tprom < 5.8 and tprom > 0 and pr < 271.8:
                                indice = 1
                            else:
                                indice = 0        
    return indice

# JUNIO
def junio (tprom, pr):
    if tprom > 8.75 and pr < 335.11:
        indice = 4
    else:
        if tprom > 8.75 and pr > 335.11:
            indice = 3
        else:
            if tprom <= 8.75 and tprom > 5.75 and pr < 335.11:
                indice = 3
            else:
                if tprom <= 8.75 and tprom > 5.75 and pr > 335.11:
                    indice = 2
                else:
                    if tprom <= 5.75 and tprom > 2.75 and pr < 335.11:
                        indice = 2
                    else:
                        if tprom <= 5.75 and tprom > 2.75 and pr > 335.11:
                            indice = 1
                        else:
                            if tprom < 2.75 and tprom > 0 and pr < 335.11:
                                indice = 1
                            else:
                                indice = 0
        
    return indice
    
# JULIO
def julio (tprom, pr):
    if tprom > 7.55 and pr < 317.89:
        indice = 4
    else:
        if tprom > 7.55 and pr > 317.89:
            indice = 3
        else:
            if tprom <= 7.55 and tprom > 4.55 and pr < 317.89:
                indice = 3
            else:
                if tprom <= 7.55 and tprom > 4.55 and pr > 317.89:
                    indice = 2
                else:
                    if tprom <= 4.55 and tprom > 1.55 and pr < 317.89:
                        indice = 2
                    else:
                        if tprom <= 4.55 and tprom > 1.55 and pr > 317.89:
                            indice = 1
                        else:
                            if tprom < 1.55 and tprom > 0 and pr < 317.89:
                                indice = 1
                            else:
                                indice = 0
            
    return indice

# AGOSTO
def agosto(tprom, pr):
    if tprom > 8.75 and pr < 201:
        indice = 4
    else:
        if tprom > 8.75 and pr > 201:
            indice = 3
        else:
            if tprom <= 8.75 and tprom > 5.75 and pr < 201:
                indice = 3
            else:
                if tprom <= 8.75 and tprom > 5.75 and pr > 201:
                    indice = 2
                else:
                    if tprom <= 5.75 and tprom > 2.75 and pr < 201:
                        indice = 2
                    else:
                        if tprom <= 5.75 and tprom > 2.75 and pr > 201:
                            indice = 1
                        else:
                            if tprom < 2.75 and tprom > 0 and pr < 201:
                                indice = 1
                            else:
                                indice = 0
            
    return indice

# SEPTIEMBRE
def septiembre (tprom, pr):
    if tprom > 10.4 and pr < 122.86:
        indice = 4
    else:
        if tprom > 10.4 and pr > 122.86:
            indice = 3
        else:
            if tprom <= 10.4 and tprom > 7.4 and pr < 122.86:
                indice = 3
            else:
                if tprom <= 10.4 and tprom > 7.4 and pr > 122.86:
                    indice = 2
                else:
                    if tprom <= 7.4 and tprom > 4.4 and pr < 122.86:
                        indice = 2
                    else:
                        if tprom <= 7.4 and tprom > 4.4 and pr > 122.86:
                            indice = 1
                        else:
                            if tprom < 4.4 and tprom > 0 and pr < 122.86:
                                indice = 1
                            else:
                                indice = 0
            
    return indice
# OCTUBRE
def octubre (tprom, pr):
    if tprom > 12.6 and pr < 92.46:
        indice = 4
    else:
        if tprom > 12.6 and pr > 92.46:
            indice = 3
        else:
            if tprom <= 12.6 and tprom > 9.6 and pr < 92.46:
                indice = 3
            else:
                if tprom <= 12.6 and tprom > 9.6 and pr > 92.46:
                    indice = 2
                else:
                    if tprom <= 9.6 and tprom > 6.6 and pr < 92.46:
                        indice = 2
                    else:
                        if tprom <= 9.6 and tprom > 6.6 and pr > 92.46:
                            indice = 1
                        else:
                            if tprom < 6.6 and tprom > 0 and pr < 92.46:
                                indice = 1
                            else:
                                indice = 0
            
    return indice
# NOVIEMBRE
def noviembre (tprom, pr):
    if tprom > 12.6 and pr < 46.28:
        indice = 4
    else:
        if tprom > 12.6 and pr > 46.28:
            indice = 3
        else:
            if tprom <= 12.6 and tprom > 9.6 and pr < 46.28:
                indice = 3
            else:
                if tprom <= 12.6 and tprom > 9.6 and pr > 46.28:
                    indice = 2
                else:
                    if tprom <= 9.6 and tprom > 6.6 and pr < 46.28:
                        indice = 2
                    else:
                        if tprom <= 9.6 and tprom > 6.6 and pr > 46.28:
                            indice = 1
                        else:
                            if tprom < 6.6 and tprom > 0 and pr < 46.28:
                                indice = 1
                            else:
                                indice = 0
 
    return indice
# DICIEMBRE
def diciembre (tprom, pr):
    if tprom > 15.4 and pr < 28.87:
        indice = 4
    else:
        if tprom > 15.4 and pr > 28.87:
            indice = 3
        else:
            if tprom <= 15.4 and tprom > 12.4 and pr < 28.87:
                indice = 3
            else:
                if tprom <= 15.4 and tprom > 12.4 and pr > 28.87:
                    indice = 2
                else:
                    if tprom <= 12.4 and tprom > 9.4 and pr < 28.87:
                        indice = 2
                    else:
                        if tprom <= 12.4 and tprom > 9.4 and pr > 28.87:
                            indice = 1
                        else:
                            if tprom < 9.4 and tprom > 0 and pr < 28.87:
                                indice = 1
                            else:
                                indice = 0
    return indice
