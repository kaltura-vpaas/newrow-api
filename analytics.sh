# Newrow API
# ----------
# GET /analytics/sessions
# https://smart.newrow.com/backend/api/analytics/sessions

apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "analytics/sessions",
	"params": {
        "room_id": 190909
	}
}
EOF
)

# Call Newrow API
./newrowkaf.sh "$apiJson"