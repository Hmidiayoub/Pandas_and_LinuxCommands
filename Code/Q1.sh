awk -F, '{
   split($2, parts, " ")
   for(i in parts){
      print parts[i] "," $3
      }
}' ../data/synsets.txt > Q1.csv
