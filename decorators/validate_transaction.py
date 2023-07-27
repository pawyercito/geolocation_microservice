from flask import jsonify, request
from functools import wraps
from utils.transactions import generate_internal_transaction_id, is_hexadecimal


def validate_external_transaction_id(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        external_transaction_id = request.json.get("externalTransactionId")
        channel = request.json.get("channel")
        internal_transaction_id = generate_internal_transaction_id()

        if not external_transaction_id or not is_hexadecimal(external_transaction_id):
            return jsonify({
                "code": 500,
                "message": "Invalid externalTransactionId" if external_transaction_id else "Missing externalTransactionId",
                "external_transaction_id": external_transaction_id,
                "internal_transaction_id": internal_transaction_id,
            })
        
        return func(
            *args, 
            internal_transaction_id=internal_transaction_id, 
            external_transaction_id=external_transaction_id, 
            channel=channel, 
            **kwargs
        )

    return wrapper