# Newrow API
# ----------
# GET /analytics/sessions
# https://smart.newrow.com/backend/api/analytics/sessions
# *** populate room_id with valid value (this is a newrow room Id, so need to run rooms.sh first)
apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "analytics/sessions",
	"params": {
        "room_id": 198995
	}
}
EOF
)

# Call Newrow API
./newrowkaf.sh "$apiJson"
