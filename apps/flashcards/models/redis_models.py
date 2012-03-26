from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete

from apps.utils.utils import unix_time
from apps.manabi_redis.models import redis
from apps.flashcards.models import Card


class RedisCard(object):
    def __init__(self, card):
        self.card = card

    #def update_due_at(self):
    #    ''' Records the earliest due card per fact. '''
    #    key = 'next_due_at:fact:{0}'.format(self.card.fact_id)
    #    score = unix_time(self.card.due_at)
    #    existing = redis.get(key)
    #    if existing is None or int(existing) > score:
    #        redis.zadd(key, score, self.card.id)

    #def _update_review_date(self):
    #    ''' Records the most recently reviewed card per card. '''
    #    key = 'last_reviewed_at:fact:{0}'.format(self.card.fact_id)
    #    score = unix_time(card.last_reviewed_at)
    #    existing = redis.get(key)
    #    if existing is None or int(existing) < score:
    #        redis.zadd(key, score, card.id)

    #def _add_failed_review(self):
    #    ''' Which cards were failed in their last review, per user. '''
    #    if self.card.last_review_grade != GRADE_NONE:
    #        return
    #    key = 'failed_cards:user:{0}'.format(self.card.owner)
    #    redis.sadd(key, self.card.id)

    def update_deck(self):
        key = 'cards:deck:{0}'.format(self.card.fact.deck_id)
        redis.sadd(key, self.card.id)

    def update_ease_factor(self):
        key = 'ease_factor:deck:{0}'.format(self.card.fact.deck_id)
        if self.card.active and self.card.ease_factor:
            score = self.card.ease_factor
            redis.zadd(key, score, self.card.id)
        else:
            redis.zrem(key, self.card.id)

    def after_review(self):
        ''' Call after a card is reviewed. '''
        #self._update_review_date()
        #self._add_failed_review()
        #self.update_due_at()
        self.update_ease_factor()

    def update_all(self):
        self.update_deck()
        self.update_ease_factor()

    def delete(self):
        deck_id = card.fact.deck_id
        redis.srem('cards:deck:' + deck_id, card.id)
        redis.zrem('ease_factor:deck:' + deck_id, card.id)



# Listeners

@receiver(post_save, sender=Card, dispatch_uid='card_saved_redis')
def card_saved(sender, card, created, **kwargs):
    if not created:
        return
    card.update_deck()

@receiver(post_delete, sender=Card, dispatch_uid='card_deleted_redis')
def card_deleted(sender, card, **kwargs):
    redis.
