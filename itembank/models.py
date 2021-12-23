import re
from django.core.validators import MaxValueValidator
from django.db import models
from quiz.models import ECEtopic, ECESubject, ECESubtopic, BaseModel

from model_utils.managers import InheritanceManager
from django.core.exceptions import ValidationError


# Create your models here.

class Item(BaseModel):

    question = models.CharField(max_length=1000,
                                blank=False,
                                help_text="Enter the question text that you want to displayed",
                                verbose_name='Question')
    figure = models.ImageField(upload_to='insert',
                               blank=True,
                               null=True,
                               verbose_name='Figure')

    optionA = models.CharField(max_length=200, blank=False, null=True)
    optionB = models.CharField(max_length=200, blank=False, null=True)
    optionC = models.CharField(max_length=200, blank=False, null=True)
    optionD = models.CharField(max_length=200, blank=False, null=True)
    cat = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))

    answer = models.CharField(max_length=1000,
                              blank=False, null=True,
                              help_text='Enter the answers that you want to displayed',
                              verbose_name='ANSWER', choices=cat)

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text='Is this a correct answer?',
                                  verbose_name='Correct')

    solution = models.TextField(max_length=2000,
                                blank=True,
                                help_text='Explanation to be shown after the question has been answered.',
                                verbose_name='Explanation')

    subject = models.ForeignKey(ECESubject,
                                verbose_name='ECE Subject',
                                blank=True,
                                null=True, on_delete=models.CASCADE)

    topic = models.ForeignKey(ECEtopic,
                              blank=True,
                              null=True,
                              verbose_name='ECE Topic', on_delete=models.CASCADE
                              )

    subtopic = models.ForeignKey(ECESubtopic,
                                 blank=True,
                                 null=True,
                                 verbose_name='ECE Subtopic', on_delete=models.CASCADE)

    solution = models.TextField(max_length=2000,
                                blank=True,
                                help_text='Explanation to be shown after the question has been answered.',
                                verbose_name='Explanation')

    difficulty_level = (
        (0, ('Easy')),
        (1, ('Medium')),
        (2, ('Hard')),
    )

    difficulty = models.IntegerField(default=0, choices= difficulty_level, verbose_name='Difficulty Level')

    optionA = models.CharField(max_length=200, blank=False, null=True)
    optionB = models.CharField(max_length=200, blank=False, null=True)
    optionC = models.CharField(max_length=200, blank=False, null=True)
    optionD = models.CharField(max_length=200, blank= False, null=True)
    cat = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))

    answer = models.CharField(max_length=1000,
                            blank=False,null=True,
                            help_text='Enter the answers that you want to displayed',
                            verbose_name='ANSWER', choices=cat)

    solution = models.TextField(max_length=2000,
                                blank=True,
                                help_text='Explanation to be shown after the question has been answered.',
                                verbose_name='Explanation')


    objects = InheritanceManager()

    class Meta:
        verbose_name = 'Exam Item',
        verbose_name_plural = 'Exam items'

    def __str__(self):
        return self.question












