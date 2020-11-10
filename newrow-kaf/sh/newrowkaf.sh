# Populate these values prior to running any of the scripts.
PARTNER_ID="INSERT_VALID_PARTNER_ID"
USER_SECRET="INSERT_VALID_USER_SECRET"
DEFAULT_RESOURCE_ID="INSERT_VALID_RESOURCE_ID"
KAF_DOMAIN="https://INSERT_VALID_KAF_DOMAIN.kaf.kaltura.com"

if [ $# -eq 0 ]
  then
    echo "ERROR: no apiJson arg passed to newrowkaf.sh"
    exit
  else
    apiJson=$1
fi

if [ -z "$2" ]
  then
    # resourceId needs to be populated with a valid value for this API to work
    resourceId=$DEFAULT_RESOURCE_ID
  else
    resourceId=$2
fi

# URL encode "apiJson" and output it to "api" variable
urlencode() {
	local LANG=C i c
	for ((i=0;i<${#1};i++)); do
                c=${1:$i:1}
		[[ "$c" =~ [a-zA-Z0-9\.\~\_\-] ]] || printf -v c '%%%02X' "'$c"
                api+="$c"
	done
}

api=''
urlencode "$apiJson"

#echo "$api"
#echo ""
#echo "$apiJson"


KALTURA_SESSION=`curl -X POST https://www.kaltura.com/api_v3/service/session/action/start \
    -d "secret=$USER_SECRET" \
    -d "partnerId=$PARTNER_ID" \
    -d "type=0" \
    -d "expiry=86400" \
    --data-urlencode "privileges=resourceId:$resourceId,role:viewerRole,api:$api" \
    -d "format=1" | sed 's@"@@g'`
#echo $KALTURA_SESSION
echo ""
curl -X GET $KAF_DOMAIN/newrowkaf/index/api?ks=$KALTURA_SESSION
echo ""
echo ""
