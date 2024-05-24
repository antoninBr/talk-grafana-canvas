# Installation

Seulement pour Grafana < v.11

`export grafana_pod_id=( kubectl get pod -n monitoring | grep 'grafana' | awk 'END {print $1}' | xargs echo)`


`kubectl -n monitoring cp agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT.zip $grafana_pod_id:/var/lib/grafana/plugins/`

`kubectl -n monitoring exec -it $grafana_pod_id -- unzip /var/lib/grafana/plugins/agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT.zip -d /var/lib/grafana/plugins/agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT`

`kubectl -n monitoring exec -it $grafana_pod_id -- chmod 777 -R /var/lib/grafana/plugins`