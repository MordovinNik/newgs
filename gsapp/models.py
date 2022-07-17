from django.db import models


class Reports(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    closing_date = models.DateField(null=True)
    status = models.BooleanField()
    description = models.TextField()
    report_type = models.ForeignKey('ReportTypes', on_delete=models.PROTECT, null=False)
    submitter = models.ForeignKey('Users', on_delete=models.PROTECT, null=False, related_name='submitter')
    assigned_user = models.ForeignKey('Users', on_delete=models.PROTECT, null=False, related_name='assigned_user')
    added_users = models.ManyToManyField('Users', verbose_name='Добавленные пользоваетели', related_name='added_users', blank=True)
    dept = models.ForeignKey('Depts', on_delete=models.PROTECT, null=False)
    subdept = models.ForeignKey('SubDepts', on_delete=models.PROTECT, null=True)
    files = models.ManyToManyField('Files', verbose_name='Прикрепленные файлы', blank=True)


class SubDepts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    dept = models.ForeignKey('Depts', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Depts(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    concern_permission_class = models.DecimalField(max_digits=1, decimal_places=0)
    concern_additional_permissions = models.ManyToManyField('ConcernPermissions', verbose_name='Дополнительные права', null=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    dept = models.ForeignKey('Depts', on_delete=models.PROTECT, null=False)
    subdept = models.ForeignKey('SubDepts', on_delete=models.PROTECT, null= True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ReportTypes(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Files(models.Model):
    name = models.CharField('Имя файла', max_length=255, unique=True)
    filepath = models.FileField('Файл', upload_to='media/')

    def __str__(self):
        return self.name + ": " + str(self.filepath)


class ConcernPermissions(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
