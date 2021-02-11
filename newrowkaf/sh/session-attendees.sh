# Newrow API
# ----------
# GET /analytics/session-attendees
# https://smart.newrow.com/backend/api/analytics/session-attendees
# *** populate session_id with valid value (this is a newrow session Id, so need to run sessions.sh first)
apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "analytics/session-attendees",
	"params": {
        "session_id": 7687842,
        "include_third_party_data": 1
	}
}
EOF
)

# Call Newrow API
./newrowkaf.sh "$apiJson"
