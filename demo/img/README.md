# Copy to Grafana

`export grafana_pod_id=( kubectl get pod -n monitoring | grep 'grafana' | awk 'END {print $1}' | xargs echo)`

`kubectl cp -n monitoring openart-bob-ross-lake-cabin.png $grafana_pod_id:/usr/share/grafana/public/img/bg/openart-bob-ross-lake-cabin.png`

`kubectl cp -n monitoring fireplace.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/fireplace.svg`

`kubectl cp -n monitoring fishes.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/fishes.svg`

`kubectl cp -n monitoring fishing_basket.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/fishing_basket.svg`

`kubectl cp -n monitoring thermometer.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/thermometer.svg`

# blog

https://volkovlabs.io/blog/pizzeria-canvas-20230723/

# Tools

figma.com
svgator
https://openart.ai/

