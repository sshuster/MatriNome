# Generated by Django 2.2.6 on 2019-12-24 09:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InterestChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField(null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('state', models.IntegerField(choices=[(1, 'Andra Pradesh'), (2, 'Arunachal Pradesh'), (3, 'Assam'), (4, 'Bihar'), (5, 'Chhattisgarh'), (6, 'Goa'), (7, 'Gujarat'), (8, 'Haryana'), (9, 'Himachal Pradesh'), (10, 'Jammu and Kashmir'), (11, 'Jharkhand'), (12, 'Karnataka'), (13, 'Kerala'), (14, 'Madya Pradesh'), (15, 'Maharashtra'), (16, 'Manipur'), (17, 'Meghalaya'), (18, 'Mizoram'), (19, 'Nagaland'), (20, 'Orissa'), (21, 'Punjab'), (22, 'Rajasthan'), (23, 'Sikkim'), (24, 'Tamil Nadu'), (25, 'Telagana'), (26, 'Tripura'), (27, 'Uttaranchal'), (28, 'Uttar Pradesh'), (29, 'West Bengal')], null=True)),
                ('city', models.CharField(max_length=30)),
                ('bio', models.TextField(max_length=150)),
                ('address', models.TextField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('interests', models.ManyToManyField(to='users.InterestChoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
