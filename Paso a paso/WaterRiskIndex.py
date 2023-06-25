from constantes import (
    JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER,
    OCTOBER, NOVEMBER, DECEMBER, ZONE12, ZONE3, ZONE4, ZONE5, ZONE6, ZONE7,
   #ZONA 12
    
    LIMIT_PR_JANUARY_ZONE12, TEMP_B_JANUARY_ZONE12, LIMIT_PR_FEBRUARY_ZONE12,
    TEMP_B_FEBRUARY_ZONE12, LIMIT_PR_MARCH_ZONE12, TEMP_B_MARCH_ZONE12,
    LIMIT_PR_APRIL_ZONE12, TEMP_B_APRIL_ZONE12, LIMIT_PR_MAY_ZONE12,
    TEMP_B_MAY_ZONE12, LIMIT_PR_JUNE_ZONE12, TEMP_B_JUNE_ZONE12,
    LIMIT_PR_JULY_ZONE12, TEMP_B_JULY_ZONE12, LIMIT_PR_AUGUST_ZONE12,
    TEMP_B_AUGUST_ZONE12, LIMIT_PR_SEPTEMBER_ZONE12, TEMP_B_SEPTEMBER_ZONE12,
    LIMIT_PR_OCTOBER_ZONE12, TEMP_B_OCTOBER_ZONE12, LIMIT_PR_NOVEMBER_ZONE12,
    TEMP_B_NOVEMBER_ZONE12, LIMIT_PR_DECEMBER_ZONE12, TEMP_B_DECEMBER_ZONE12,
    
    #ZONA 3
    
    LIMIT_PR_JANUARY_ZONE3, TEMP_B_JANUARY_ZONE3, LIMIT_PR_FEBRUARY_ZONE3,
    TEMP_B_FEBRUARY_ZONE3, LIMIT_PR_MARCH_ZONE3, TEMP_B_MARCH_ZONE3,
    LIMIT_PR_APRIL_ZONE3, TEMP_B_APRIL_ZONE3, LIMIT_PR_MAY_ZONE3,
    TEMP_B_MAY_ZONE3, LIMIT_PR_JUNE_ZONE3, TEMP_B_JUNE_ZONE3,
    LIMIT_PR_JULY_ZONE3, TEMP_B_JULY_ZONE3, LIMIT_PR_AUGUST_ZONE3,
    TEMP_B_AUGUST_ZONE3, LIMIT_PR_SEPTEMBER_ZONE3, TEMP_B_SEPTEMBER_ZONE3,
    LIMIT_PR_OCTOBER_ZONE3, TEMP_B_OCTOBER_ZONE3, LIMIT_PR_NOVEMBER_ZONE3,
    TEMP_B_NOVEMBER_ZONE3, LIMIT_PR_DECEMBER_ZONE3, TEMP_B_DECEMBER_ZONE3,
    
    #ZONA 4
    LIMIT_PR_JANUARY_ZONE4, TEMP_B_JANUARY_ZONE4, LIMIT_PR_FEBRUARY_ZONE4,
    TEMP_B_FEBRUARY_ZONE4, LIMIT_PR_MARCH_ZONE4, TEMP_B_MARCH_ZONE4,
    LIMIT_PR_APRIL_ZONE4, TEMP_B_APRIL_ZONE4, LIMIT_PR_MAY_ZONE4,
    TEMP_B_MAY_ZONE4, LIMIT_PR_JUNE_ZONE4, TEMP_B_JUNE_ZONE4,
    LIMIT_PR_JULY_ZONE4, TEMP_B_JULY_ZONE4, LIMIT_PR_AUGUST_ZONE4,
    TEMP_B_AUGUST_ZONE4, LIMIT_PR_SEPTEMBER_ZONE4, TEMP_B_SEPTEMBER_ZONE4,
    LIMIT_PR_OCTOBER_ZONE4, TEMP_B_OCTOBER_ZONE4, LIMIT_PR_NOVEMBER_ZONE4,
    TEMP_B_NOVEMBER_ZONE4, LIMIT_PR_DECEMBER_ZONE4, TEMP_B_DECEMBER_ZONE4,
    
    #ZONA 5
    LIMIT_PR_JANUARY_ZONE5, TEMP_B_JANUARY_ZONE5, LIMIT_PR_FEBRUARY_ZONE5,
    TEMP_B_FEBRUARY_ZONE5, LIMIT_PR_MARCH_ZONE5, TEMP_B_MARCH_ZONE5,
    LIMIT_PR_APRIL_ZONE5, TEMP_B_APRIL_ZONE5, LIMIT_PR_MAY_ZONE5,
    TEMP_B_MAY_ZONE5, LIMIT_PR_JUNE_ZONE5, TEMP_B_JUNE_ZONE5,
    LIMIT_PR_JULY_ZONE5, TEMP_B_JULY_ZONE5, LIMIT_PR_AUGUST_ZONE5,
    TEMP_B_AUGUST_ZONE5, LIMIT_PR_SEPTEMBER_ZONE5, TEMP_B_SEPTEMBER_ZONE5,
    LIMIT_PR_OCTOBER_ZONE5, TEMP_B_OCTOBER_ZONE5, LIMIT_PR_NOVEMBER_ZONE5,
    TEMP_B_NOVEMBER_ZONE5, LIMIT_PR_DECEMBER_ZONE5, TEMP_B_DECEMBER_ZONE5,

    #ZONA 6
    LIMIT_PR_JANUARY_ZONE6, TEMP_B_JANUARY_ZONE6, LIMIT_PR_FEBRUARY_ZONE6,
    TEMP_B_FEBRUARY_ZONE6, LIMIT_PR_MARCH_ZONE6, TEMP_B_MARCH_ZONE6,
    LIMIT_PR_APRIL_ZONE6, TEMP_B_APRIL_ZONE6, LIMIT_PR_MAY_ZONE6,
    TEMP_B_MAY_ZONE6, LIMIT_PR_JUNE_ZONE6, TEMP_B_JUNE_ZONE6,
    LIMIT_PR_JULY_ZONE6, TEMP_B_JULY_ZONE6, LIMIT_PR_AUGUST_ZONE6,
    TEMP_B_AUGUST_ZONE6, LIMIT_PR_SEPTEMBER_ZONE6, TEMP_B_SEPTEMBER_ZONE6,
    LIMIT_PR_OCTOBER_ZONE6, TEMP_B_OCTOBER_ZONE6, LIMIT_PR_NOVEMBER_ZONE6,
    TEMP_B_NOVEMBER_ZONE6, LIMIT_PR_DECEMBER_ZONE6, TEMP_B_DECEMBER_ZONE6,
    
    
    #ZONA 7
    LIMIT_PR_JANUARY_ZONE7, TEMP_B_JANUARY_ZONE7, LIMIT_PR_FEBRUARY_ZONE7,
    TEMP_B_FEBRUARY_ZONE7, LIMIT_PR_MARCH_ZONE7, TEMP_B_MARCH_ZONE7,
    LIMIT_PR_APRIL_ZONE7, TEMP_B_APRIL_ZONE7, LIMIT_PR_MAY_ZONE7,
    TEMP_B_MAY_ZONE7, LIMIT_PR_JUNE_ZONE7, TEMP_B_JUNE_ZONE7,
    LIMIT_PR_JULY_ZONE7, TEMP_B_JULY_ZONE7, LIMIT_PR_AUGUST_ZONE7,
    TEMP_B_AUGUST_ZONE7, LIMIT_PR_SEPTEMBER_ZONE7, TEMP_B_SEPTEMBER_ZONE7,
    LIMIT_PR_OCTOBER_ZONE7, TEMP_B_OCTOBER_ZONE7, LIMIT_PR_NOVEMBER_ZONE7,
    TEMP_B_NOVEMBER_ZONE7, LIMIT_PR_DECEMBER_ZONE7, TEMP_B_DECEMBER_ZONE7,

)



def get_index_month_zone(tprom, pr, mes, zona):
    limit_pr = 0.0
    limit_temp_b = 0.0

    if mes == JANUARY:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_JANUARY_ZONE12
            limit_temp_b = TEMP_B_JANUARY_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_JANUARY_ZONE3
            limit_temp_b = TEMP_B_JANUARY_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_JANUARY_ZONE4
            limit_temp_b = TEMP_B_JANUARY_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_JANUARY_ZONE5
            limit_temp_b = TEMP_B_JANUARY_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_JANUARY_ZONE6
            limit_temp_b = TEMP_B_JANUARY_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_JANUARY_ZONE7
            limit_temp_b = TEMP_B_JANUARY_ZONE7
            
    elif mes == FEBRUARY:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE12
            limit_temp_b = TEMP_B_FEBRUARY_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE3
            limit_temp_b = TEMP_B_FEBRUARY_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE4
            limit_temp_b = TEMP_B_FEBRUARY_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE5
            limit_temp_b = TEMP_B_FEBRUARY_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE6
            limit_temp_b = TEMP_B_FEBRUARY_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_FEBRUARY_ZONE7
            limit_temp_b = TEMP_B_FEBRUARY_ZONE7
            
    elif mes == MARCH:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_MARCH_ZONE12
            limit_temp_b = TEMP_B_MARCH_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_MARCH_ZONE3
            limit_temp_b = TEMP_B_MARCH_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_MARCH_ZONE4
            limit_temp_b = TEMP_B_MARCH_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_MARCH_ZONE5
            limit_temp_b = TEMP_B_MARCH_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_MARCH_ZONE6
            limit_temp_b = TEMP_B_MARCH_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_MARCH_ZONE7
            limit_temp_b = TEMP_B_MARCH_ZONE7
            
    elif mes == APRIL:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_APRIL_ZONE12
            limit_temp_b = TEMP_B_APRIL_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_APRIL_ZONE3
            limit_temp_b = TEMP_B_APRIL_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_APRIL_ZONE4
            limit_temp_b = TEMP_B_APRIL_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_APRIL_ZONE5
            limit_temp_b = TEMP_B_APRIL_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_APRIL_ZONE6
            limit_temp_b = TEMP_B_APRIL_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_APRIL_ZONE7
            limit_temp_b = TEMP_B_APRIL_ZONE7
            
    elif mes == MAY:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_MAY_ZONE12
            limit_temp_b = TEMP_B_MAY_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_MAY_ZONE3
            limit_temp_b = TEMP_B_MAY_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_MAY_ZONE4
            limit_temp_b = TEMP_B_MAY_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_MAY_ZONE5
            limit_temp_b = TEMP_B_MAY_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_MAY_ZONE6
            limit_temp_b = TEMP_B_MAY_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_MAY_ZONE7
            limit_temp_b = TEMP_B_MAY_ZONE7
            
    elif mes == JUNE:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_JUNE_ZONE12
            limit_temp_b = TEMP_B_JUNE_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_JUNE_ZONE3
            limit_temp_b = TEMP_B_JUNE_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_JUNE_ZONE4
            limit_temp_b = TEMP_B_JUNE_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_JUNE_ZONE5
            limit_temp_b = TEMP_B_JUNE_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_JUNE_ZONE6
            limit_temp_b = TEMP_B_JUNE_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_JUNE_ZONE7
            limit_temp_b = TEMP_B_JUNE_ZONE7
            
    elif mes == JULY:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_JULY_ZONE12
            limit_temp_b = TEMP_B_JULY_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_JULY_ZONE3
            limit_temp_b = TEMP_B_JULY_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_JULY_ZONE4
            limit_temp_b = TEMP_B_JULY_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_JULY_ZONE5
            limit_temp_b = TEMP_B_JULY_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_JULY_ZONE6
            limit_temp_b = TEMP_B_JULY_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_JULY_ZONE7
            limit_temp_b = TEMP_B_JULY_ZONE7

    elif mes == AUGUST:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_AUGUST_ZONE12
            limit_temp_b = TEMP_B_AUGUST_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_AUGUST_ZONE3
            limit_temp_b = TEMP_B_AUGUST_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_AUGUST_ZONE4
            limit_temp_b = TEMP_B_AUGUST_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_AUGUST_ZONE5
            limit_temp_b = TEMP_B_AUGUST_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_AUGUST_ZONE6
            limit_temp_b = TEMP_B_AUGUST_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_AUGUST_ZONE7
            limit_temp_b = TEMP_B_AUGUST_ZONE7
            
    elif mes == SEPTEMBER:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE12
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE3
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE4
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE5
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE6
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_SEPTEMBER_ZONE7
            limit_temp_b = TEMP_B_SEPTEMBER_ZONE7
            
    elif mes == OCTOBER:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_OCTOBER_ZONE12
            limit_temp_b = TEMP_B_OCTOBER_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_OCTOBER_ZONE3
            limit_temp_b = TEMP_B_OCTOBER_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_OCTOBER_ZONE4
            limit_temp_b = TEMP_B_OCTOBER_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_OCTOBER_ZONE5
            limit_temp_b = TEMP_B_OCTOBER_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_OCTOBER_ZONE6
            limit_temp_b = TEMP_B_OCTOBER_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_OCTOBER_ZONE7
            limit_temp_b = TEMP_B_OCTOBER_ZONE7

    elif mes == NOVEMBER:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE12
            limit_temp_b = TEMP_B_NOVEMBER_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE3
            limit_temp_b = TEMP_B_NOVEMBER_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE4
            limit_temp_b = TEMP_B_NOVEMBER_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE5
            limit_temp_b = TEMP_B_NOVEMBER_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE6
            limit_temp_b = TEMP_B_NOVEMBER_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_NOVEMBER_ZONE7
            limit_temp_b = TEMP_B_NOVEMBER_ZONE7
            
    elif mes == DECEMBER:
        if zona == ZONE12:
            limit_pr = LIMIT_PR_DECEMBER_ZONE12
            limit_temp_b = TEMP_B_DECEMBER_ZONE12
        elif zona == ZONE3:
            limit_pr = LIMIT_PR_DECEMBER_ZONE3
            limit_temp_b = TEMP_B_DECEMBER_ZONE3
        elif zona == ZONE4:
            limit_pr = LIMIT_PR_DECEMBER_ZONE4
            limit_temp_b = TEMP_B_DECEMBER_ZONE4
        elif zona == ZONE5:
            limit_pr = LIMIT_PR_DECEMBER_ZONE5
            limit_temp_b = TEMP_B_DECEMBER_ZONE5
        elif zona == ZONE6:
            limit_pr = LIMIT_PR_DECEMBER_ZONE6
            limit_temp_b = TEMP_B_DECEMBER_ZONE6
        elif zona == ZONE7:
            limit_pr = LIMIT_PR_DECEMBER_ZONE7
            limit_temp_b = TEMP_B_DECEMBER_ZONE7


    # Continue similarly for each month and each zone

    if pr == -9999.0:
        index = 0
    else:
        if pr < limit_pr and tprom > limit_temp_b:
            index = 4  # high risk
        else:
            if pr < limit_pr and tprom < limit_temp_b:
                index = 3  # risk
            else:
                if pr > limit_pr and tprom > limit_temp_b:
                    index = 2  # moderate risk
                else:
                    index = 1  # no risk
                    
    return index
