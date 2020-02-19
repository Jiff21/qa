#!/bin/bash

# Can confirm setup after policy with gcloud alpha monitoring policies list > ~/Downloads/policy.yaml
# Need to install 
# pip install google-cloud-monitoring
# pip install tabulate

emails="example1@example.com example2@example.com"
HOST='gweb-example.appspot.com'
PROJECT='gweb-example'
CHECK_NAME='Static Uptime Check'

CreateChannel(){
    gcloud --quiet alpha monitoring channels create \
        --type=email \
        --display-name="Email $1" \
        --description="E-mail channel for $1" \
        --channel-labels=email_address="$1" \
        --format="value(name)"
}

channels=''
i=0

for email in $emails
do
    channel=$(CreateChannel $email)
    if [ $i = 0 ]; then
        channels+=$channel
        i=i+1
    else
        channels+=,$channel
    fi
done


gcloud alpha monitoring policies create \
    --notification-channels=$channels \
    --aggregation='{"alignmentPeriod": "60s","perSeriesAligner": "ALIGN_MEAN"}' \
    --condition-display-name='CPU Utilization >0.80 for 10m'\
    --condition-filter='metric.type="appengine.googleapis.com/flex/instance/cpu/utilization" resource.type="gae_instance"' \
    --combiner='AND' \
    --duration='10m' \
    --if='> 0.2' \
    --documentation="You are receiving this alert because CPU Utilization has been high for 10 minutes." \
    --display-name='CPU Utilization'


gcloud alpha monitoring policies create \
    --notification-channels=$channels \
    --aggregation='{"alignmentPeriod": "60s","perSeriesAligner": "ALIGN_MEAN"}' \
    --condition-display-name='Memory Utilization >0.20 for 10m'\
    --condition-filter='metric.type="appengine.googleapis.com/flex/instance/cpu/utilization" resource.type="gae_instance"' \
    --combiner='AND' \
    --duration='10m' \
    --if='> 0.2' \
    --documentation="You are receiving this alert because Memory Utilization is above 20% for 10 minutes." \
    --display-name='Memory Utilization'


gcloud alpha monitoring policies create \
    --notification-channels=$channels \
    --aggregation='{"alignmentPeriod": "60s","perSeriesAligner": "ALIGN_RATE"}' \
    --condition-display-name='>=1 Quota Error in 10 Min'\
    --condition-filter='metric.type="appengine.googleapis.com/http/server/quota_denial_count" resource.type="gae_app"' \
    --combiner='OR' \
    --duration='10m' \
    --if='> 0' \
    --trigger-count=1 \
    --documentation="Checks every 10 minutes to see if we're over Quota on an API." \
    --display-name='Over Quota'


# Need to make sure this is https and firing

GCLOUD_PROJECT=$PROJECT python3 uptime-check-client.py create-uptime-check --host_name $HOST --display_name "$CHECK_NAME"

check_name_sanitized="${CHECK_NAME// /_}"

gcloud alpha monitoring policies create \
    --notification-channels=$channels \
    --aggregation='{"alignmentPeriod": "60s","crossSeriesReducer": "REDUCE_COUNT_FALSE", "groupByFields": [ "resource.*" ], "perSeriesAligner":ALIGN_NEXT_OLDER}' \
    --condition-display-name='Uptime Health Check on HTTPS'\
    --condition-filter='metric.type="monitoring.googleapis.com/uptime_check/check_passed" resource.type="uptime_url" metric.label."check_id"="$check_name_sanitized"' \
    --combiner='OR' \
    --duration='10m' \
    --if='< 1.0' \
    --trigger-count=1 \
    --documentation="Checks every 10 minutes make sure uptime checks are not failing" \
    --display-name='Static Uptime Check'
