from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_transaction(request):
    receiver_wallet = request.data.get('receiver_wallet')

    if receiver_wallet.startswith('0x423'):
        return Response({
            "status": "blocked",
            "message": "Fraudulent Wallet Detected!",
            "reason": "Known scam pattern detected in wallet address"
        })

    return Response({
        "status": "allowed",
        "message": "Transaction Allowed",
        "details": "No suspicious activity detected"
    })
