# Installation

Seulement pour Grafana < v.11

`kubectl -n monitoring cp agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT.zip grafana-6d966b5cc4-khrn9:/var/lib/grafana/plugins/agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT.zip`

`kubectl -n monitoring exec -it grafana-6d966b5cc4-khrn9 -- unzip /var/lib/grafana/plugins/agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT.zip -d /var/lib/grafana/plugins/agenty-flowcharting-panel-1.0.0d.220606199-SNAPSHOT`

`kubectl -n monitoring exec -it grafana-6d966b5cc4-khrn9 -- chmod 777 -R /var/lib/grafana/plugins`