g1:{seq:til x; sum seq[where 0=(seq mod 3)& seq mod 5]}
g1 1000

g2:{n3:(x-1) div 3; n5:(x-1) div 5; n15:(x-1) div 15; s3:3*n3*(n3+1)%2; s5:5*n5*(n5+1)%2; s15:15*n15*(n15+1)%2; s3+s5-s15}
g2 1000
