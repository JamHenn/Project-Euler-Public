/ algorithm:
/ convert start and end dates to months
/ make a list of months from the start to the end
/ convert each month to a date: the 1st day of that month
/ Use modular arithmetic to count the Sundays
/ 2000.01.01 (0) is a Saturday
/ 2000.01.02 (1) is a Sunday, so Sundays are 1 mod 7

f:{[start;end] start:`month$start; end:`month$end; months:start+til 1+end-start; dates:`date$months; sum 1=dates mod 7}

f[1901.01.01;2000.12.31]
