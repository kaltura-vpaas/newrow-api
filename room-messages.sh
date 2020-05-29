# Newrow API
# ----------
# GET /analytics/room-messages
# https://smart.newrow.com/backend/api/analytics/room-messages

apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "analytics/room-messages",
	"params": {
	}
}
EOF
)

if [ $# -eq 0 ]
  then
    echo "ERROR: no resourceId arg passed to room-messages.sh"
    exit
  else
    resourceId=$1
fi

# Call Newrow API
./newrowkaf.sh "$apiJson" $resourceId
