# Live Assets

## Build

`cd cabin`
`podman build . -t cabin-app:v3`

## Create namespaces if not exist

`kubectl create ns drawing`

`kubectl create ns studio`

## Deploy

`kubectl -n drawing apply -f lake_deploy.yaml`
`kubectl -n drawing apply -f cabin_deploy.yaml`
`kubectl -n drawing apply -f fisherman_deploy.yaml`

`kubectl -n studio apply -f bob_deploy.yaml`

## Expose fisherman api

Add this entry in your /etc/hosts

`fisherman.localhost 127.0.0.1`



