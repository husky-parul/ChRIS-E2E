#!/usr/bin/env bash

if ! [ -d ChRIS-E2E ]; then
    echo "You must run this script from the parent directory to ChRIS-E2E"
    exit 1
fi

pushd ChRIS_ultron_backEnd
    sudo docker-compose down
popd
sudo oc cluster down
sudo rm -rf openshift.local.clusterup 2>/dev/null