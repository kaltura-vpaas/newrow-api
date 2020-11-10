# Newrow API
# ----------
# GET /users/<id>
# https://smart.newrow.com/backend/api/users/<id>

apiJson=$(cat <<EOF
{
	"method": "GET",
	"action": "users/245855",
	"params": {
	}
}
EOF
)

# Call Newrow API
./newrowkaf.sh "$apiJson"
