# Copy to Grafana

`export grafana_pod_id=( kubectl get pod -n monitoring | grep 'grafana' | awk 'END {print $1}' | xargs echo)`

`kubectl cp -n monitoring openart-bob-ross-lake-cabin.png $grafana_pod_id:/usr/share/grafana/public/img/bg/`

`kubectl cp -n monitoring bob-ross-smiling-at-you.png $grafana_pod_id:/usr/share/grafana/public/img/bg/`

`kubectl cp -n monitoring fireplace.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`

`kubectl cp -n monitoring fishes.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`

`kubectl cp -n monitoring fishing_basket.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`

`kubectl cp -n monitoring thermometer.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`

`kubectl cp -n monitoring bob_ross.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`

`kubectl cp -n monitoring ./kube/api.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`
`kubectl cp -n monitoring ./kube/c-m.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`
`kubectl cp -n monitoring ./kube/kubelet.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`
`kubectl cp -n monitoring ./kube/sched.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`
`kubectl cp -n monitoring ./kube/k-proxy.svg $grafana_pod_id:/usr/share/grafana/public/img/icons/unicons/`


# blog

https://volkovlabs.io/blog/pizzeria-canvas-20230723/

# Tools

figma.com
svgator
https://openart.ai/

