#Model

from django.db import models


class Redirect(models.Model):
    key = models.CharField("key", max_length=30, unique=True)
    url = models.CharField("url", max_length=100)
    active = models.BooleanField(default=False, verbose_name="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    readonly_fields = ["created_at", "updated_at"]
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.key

    
    @classmethod
    def get_redirects(cls):
        return cls.objects.all().filter(active=True)

    @classmethod
    def get_redirect_by_key(cls, key):
        try:
            return cls.objects.get(key=key,active=True)
        except Exception:
            return None

########################################
#Signal

#Como tenía un par de dudas con el enunciado hice dos verciones para el signal y el manejo de la cache
#Para probarlos sin inconvenientes, comentar uno y descomentar el otro

from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

#Al editarse un objeto, se borra toda la caché, se recuperan todos los que esten actives y se los guarda en la caché

@receiver([post_save,post_delete], sender=Redirect)
def actives_to_cache(sender,instance,**kwargs):
    cache.clear()

    redirects = list(Redirect.get_redirects())

    for re in redirects:
        cache.set( re.key, re.url )


#Al editarse un objeto, se saca ESE objeto de la caché y si se sigue active se lo vuelve a guardar actualizado en la caché

# @receiver([post_save,post_delete], sender=Redirect)
# def actives_to_cache_2(sender,instance,**kwargs):

#     cache.delete(instance.key)
#     redirect_object = Redirect.get_redirect_by_key(instance.key)

#     if redirect_object:
#         cache.set(redirect_object.key, redirect_object.url)
