from django.http import (
    HttpRequest,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponse,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "question_list"

    def get_queryset(self):
        """
        Return all published poll questions, sorted by question text.
        """
        return [
            q
            for q in Question.objects.all().order_by("question_text")
            if q.is_published()
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        question = get_object_or_404(Question, id=kwargs["pk"])
        if not question.is_published():
            return HttpResponseNotFound()
        # get user's previously selected choice
        if request.user.is_authenticated:
            vote = get_vote_for_user(question, request.user)
            choice = vote.choice if vote and vote.choice else None
        else:
            choice = None
        # pass the question and user's choice to the template as named variables
        context = {"question": question, "selected_choice": choice}
        return render(request, "polls/detail.html", context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request: HttpRequest, question_id):
    """Vote for a choice on a poll. Must be a POST request."""
    question = get_object_or_404(Question, id=question_id)
    context_data = {"question": question}
    if not question.can_vote():
        messages.error(request, "Voting not allowed for this question")
        return render(request, "polls/detail.html", context_data)
    if request.method != "POST":
        # this view accepts only POST
        return HttpResponseNotAllowed(["POST"], "Only POST method is allowed")
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "Please select a choice.")
        return render(request, "polls/detail.html", context_data)

    # Create a vote or update an existing vote
    vote = get_vote_for_user(question, request.user)
    if vote:
        vote.choice = selected_choice
        messages.info(request, "Your vote was successfully updated.")
    else:
        vote = Vote(user=request.user, choice=selected_choice)
        messages.info(request, "Your vote was successfully recorded.")
    vote.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def get_vote_for_user(question: Question, user) -> Vote:
    """Return the vote by the user for a specific poll question.

    :param question: a Question to get user's vote for
    :param user: the User whose vote to find and return
    :returns: an existing vote for the user, or None if no vote for this question.
    """
    if not user.is_authenticated:
        return None
    try:
        return Vote.objects.get(user=user, choice__question=question)
    except Vote.DoesNotExist:
        # no vote yet
        return None


def remove_vote(request: HttpRequest, question_id) -> HttpResponse:
    """Remove a user's vote for a poll question. Must be POST Request"""
    question = get_object_or_404(Question, id=question_id)

    vote = get_vote_for_user(question, request.user)
    if not vote:
        return HttpResponseNotFound("You didnt vote yet")
    vote.delete()
    messages.info(request, "Your vote was successfully removed")
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
