# Newrow API
# ----------
# GET /rooms
# https://smart.newrow.com/backend/api/rooms

apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "rooms",
	"params": {
	}
}
EOF
)

# Call Newrow API
./newrowkaf.sh "$apiJson"
