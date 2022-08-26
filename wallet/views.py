from urllib import request
from wallet.models import Wallet, Transaction
from wallet.serializers import FullWalletSerializer, TransactionSerializer
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import (
    DjangoObjectPermissions,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
)
from django.db.models import Q


# custom viewset with no PUT and PATCH methods
class WalletViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Wallet.objects.all()
    serializer_class = FullWalletSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticatedOrReadOnly]

    # Overriding method of getting queryset to display (only current user wallets)
    def get_queryset(self):
        owner = self.request.user
        return Wallet.objects.filter(owner=owner)


# custom viewset with no PUT, PATCH and DELETE methods
class TransactionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # getting all transactions where wallet is sender OR receiver
    def get_queryset(self):
        transactions = Transaction.objects.all()
        user_wallets = Wallet.objects.filter(owner=self.request.user)
        q = transactions.filter(
            Q(receiver__in=user_wallets) | Q(sender__in=user_wallets)
        )
        return q
