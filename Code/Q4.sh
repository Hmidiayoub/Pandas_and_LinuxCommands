awk -F',' ' 
$3 == 1 {count[$1]++}
END {
  for (country in count) {
      print country "," count[country]
    }
}' Q3.csv | sort -t',' -k2 -nr > Q4.csv