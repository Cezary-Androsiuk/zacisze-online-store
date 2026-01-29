from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from store.models import Cart

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_related_objects(sender, instance, created, **kwargs):
    """
    Ta funkcja uruchamia się za każdym razem, gdy zapisywany jest User.
    """
    # get cart associated with current user
    user_cart = Cart.objects.filter(user=instance).first()
    # if user do not have cart associated then
    #   create new cart for hom
    if not user_cart:
        if created:
            Cart.objects.create(user=instance)