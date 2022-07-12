def gallon_used(start_p,end_p):
    if end_p < start_p:
        calc_used = (999999999-start_p) + end_p + 1
    else:
        calc_used = end_p - start_p
    return calc_used/10

def code_residential(code,g_used):
    billed = (g_used * 0.0005) + 5
    return round (billed,2)

def code_commercial(code,g_used):
    if g_used > 4000000:
        billed = (g_used * 0.00025) + 1000
    else:
        billed = 1000 
    return round (billed,2)

def code_industrial(code,g_used):
    if g_used >= 4000000 and g_used < 10000000:
        billed = 2000
    elif g_used >= 10000000:
        billed = (g_used * 0.00025) + 2000
    else:
        billed = 1000
    return round (billed,2)



print ("Enter customer code: ")
code = str(input())
print ("Enter beginning meter reading: ")
start_p = int(input())
print ("Enter ending meter reading: ")
end_p = int(input())

if code.lower() == 'r':
    used = gallon_used(start_p,end_p)
    print ("Gallons of water used: ", used)
    print ("Amount billed: $", code_residential(code,used))
elif code.lower() == 'c':
    used = gallon_used(start_p,end_p)
    print ("Gallons of water used: ", used)
    print ("Amount billed: $", code_commercial(code,used))
elif code.lower() == 'i':
    used = gallon_used(start_p,end_p)
    print ("Gallons of water used: ", used)
    print ("Amount billed: $", code_industrial(code,used))
else:
    print("Wrong customer code")
