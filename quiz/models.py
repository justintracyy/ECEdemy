import re
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator
from django.db import models

from django.core.exceptions import ValidationError


# Create your models here.


class ECEManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())
        new_category.save()
        return new_category


class ECESubject(models.Model):
    ece_subject = models.CharField(
        verbose_name=_('ECE Subject'),
        max_length=255, blank=True,
        unique=True, null=True)

    objects = ECEManager()

    class Meta:
        verbose_name = _('ECE Subject')
        verbose_name_plural = _('ECE Subjects')

    def __str__(self):
        return self.ece_subject


class ECEtopic(models.Model):
    ece_topic = models.CharField(
        verbose_name=_('ECE Topic'),
        max_length=255, blank=True,
        unique=True, null=True)

    ece_subject = models.ForeignKey(
        ECESubject, null=True, blank=True,
        verbose_name=_('ECE Subject'), on_delete=models.CASCADE
    )

    objects = ECEManager()

    class Meta:
        verbose_name = _('ECE Topic')
        verbose_name_plural = _('ECE Topics')

    def __str__(self):
        return self.ece_topic


class ECESubtopic(models.Model):
    ece_subtopic = models.CharField(
        verbose_name=_('ECE Subtopic'),
        max_length=255, null=True, blank=True,
        unique=True)

    ece_topic = models.ForeignKey(ECEtopic,
                                  null=True, blank=True, verbose_name=_('ECE Topic'), on_delete=models.CASCADE)

    objects = ECEManager()

    class Meta:
        verbose_name = _('ECE Subtopics')
        verbose_name_plural = _('ECE Subtopics')

    def __str__(self):
        return self.ece_subtopic


class QuizECESubject(models.Model):
    ece_subjects = models.ForeignKey(ECESubject, related_name='quiz_ecesubjects',
                                     max_length=90, blank=False, verbose_name=_('ECE Subject'),
                                     on_delete=models.CASCADE)

    description = models.CharField(max_length=255,
                                   verbose_name=_('Description'),
                                   blank=True, help_text=('a description of the quiz')
                                   )
    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    number_question = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('Number of questions'),
        help_text=_('Number of question to be answered')
    )

    stored_score = models.BooleanField(
        blank=False, default=False,
        help_text=_('If yes, the result of eact attempt by the user will be stored'),
        verbose_name=_('Score')
    )

    pass_mark = models.SmallIntegerField(
        blank=True, default=0,
        verbose_name=_('Pass Mark'),
        help_text=_('Percentage required to pass exam.'),
        validators=[MaxValueValidator(70)]
    )

    success_mark = models.TextField(
        blank=True, help_text=_('Displayed if user passes'),
        verbose_name=_('Success Text')
    )

    fail_mark = models.TextField(
        blank=True, help_text=_('Displayed if use fails.'),
        verbose_name=_('Fail Text')
    )

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.url = re.sub('\s+', '-', self.url).lower()

        self.url = ''.join(letter for letter in self.url if
                           letter.isalnum() or letter == '-')

        if self.pass_mark > 70:
            raise ValidationError('% is above 70' % self.pass_mark)

        super(QuizECESubject, self).save(force_insert, force_update, *args, **kwargs )

    class Meta:
        verbose_name = _('Quiz in ECE Subject'),
        verbose_name_plural = _('EXAM IN ECE SUBJECTS')

    def __str__(self):
        return str(self.ece_subjects)

    def get_questions(self):
        return self.question_set.all().select_subclasses()

    def get_max_score(self):
        return self.get_questions().count()

    def anon_score_id(self):
        return str(self.id) + "_score"

    def anon_q_list(self):
        return str(self.id) + "_q_list"

    def anon_q_data(self):
        return str(self.id) + "_data"


class QuizECETopics(models.Model):

    ece_subject = models.ForeignKey(ECESubject, related_name='quiz_ece_subjects',
                                     max_length=90, blank=False, null=True,  verbose_name=_('ECE Subject'),
                                     on_delete=models.CASCADE)

    ece_topic = models.ForeignKey(ECEtopic,related_name='quiz_ecetopics',
        max_length=90, blank=False,verbose_name=_('ECE Topics'),
                                     on_delete=models.CASCADE)

    description = models.CharField(max_length=255,
        verbose_name=_('Description'),
        blank=True, help_text=('a description of the quiz')
    )

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    number_question = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('Number of questions'),
        help_text=_('Number of question to be answered')
    )

    stored_score = models.BooleanField(
        blank=False, default=False,
        help_text=_('If yes, the result of eact attempt by the user will be stored'),
        verbose_name=_('Score')
    )

    pass_mark = models.SmallIntegerField(
        blank=True, default=0,
        verbose_name=_('Pass Mark'),
        help_text=_('Percentage required to pass exam.'),
        validators=[MaxValueValidator(70)]
    )

    success_mark = models.TextField(
        blank=True, help_text=_('Displayed if user passes'),
        verbose_name=_('Success Text')
    )

    fail_mark = models.TextField(
        blank=True, help_text=_('Displayed if use fails.'),
        verbose_name=_('Fail Text')
    )

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.url = re.sub('\s+', '-', self.url).lower()

        self.url = ''.join(letter for letter in self.url if
                           letter.isalnum() or letter == '-')

        if self.pass_mark > 70:
            raise ValidationError('% is above 70' % self.pass_mark)

        super(QuizECETopics, self).save(force_insert, force_update,)

    class Meta:
        verbose_name =_('EXAM IN ECE TOPICS'),
        verbose_name_plural =_('EXAM IN ECE TOPICS')

    def __str__(self):
        return str(self.ece_topic)

    def get_questions(self):
        return self.question_set.all().select_subclasses()

    @property
    def get_max_score(self):
        return self.get_questions().count()

    def anon_score_id(self):
        return str(self.id) + "_score"

    def anon_q_list(self):
        return str(self.id) + "_q_list"

    def anon_q_data(self):
        return str(self.id) + "_data"