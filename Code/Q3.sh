awk '
BEGIN {
    positions[1] = "1"; positions[2] = "2"; positions[3] = "3"; positions[4] = "4" 
}
/^\|-/ { next } 
/^[A-Z]+$/ {team=$1;  line_count=0; next}                  
/^[|]/ {  
    if (/^[|1385624]*$/)  next  
    line_count++  
    if ($0 ~ /^[|0]*$/) next                    
    n=split($0, nums, ",")             
    for (i = 1; i <= n; i++)  { 
        gsub(/^\|/, "", nums[i])        
        print team "," nums[i] "," positions[line_count]      
    }   
}' worldcup-semiclean.txt > Q3.csv
