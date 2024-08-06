day1=3.65
day2=5.65
day3=3.52
day4=4.52
avg=(day1+day2+day3+day4)/4
Day1=day1-avg
Day2=day2-avg
Day3=day3-avg
Day4=day4-avg
sq=Day1**2+Day2**2+Day3**2+Day4**2
var=sq/4
stddev=var**0.5
print("Variance:", var)
print("Standard Deviation:", stddev)

