from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from manabi.apps.flashcards.models import Deck


def get_deck_or_404(user, pk, must_own=False):
    '''
    Returns the deck with the given pk. 404s, or raises an exception
    if the user doesn't own that deck and it's not shared.
    '''
    deck = get_object_or_404(Deck, pk=pk)

    # The user must either own it, or it must be a shared deck.
    if deck.owner != user and (must_own or not deck.shared):
        msg = 'You do not have permission to access this deck.'
        if not must_own:
            msg += ' This deck is not shared.'
        raise PermissionDenied(msg)

    return deck

