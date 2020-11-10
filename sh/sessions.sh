# Newrow API
# ----------
# GET /analytics/sessions
# https://smart.newrow.com/backend/api/analytics/sessions
# *** No params needed since passing resourceId and filtering by it.

apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "analytics/sessions",
	"params": { }
}
EOF
)

if [ $# -eq 0 ]
  then
    echo "ERROR: no resourceId arg passed to sessions.sh"
    exit
  else
    resourceId=$1
fi

# Call Newrow API
./newrowkaf.sh "$apiJson" $resourceId
