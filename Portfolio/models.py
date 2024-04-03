from django.db import models


# class Project(models.Model):
#     srno=models.IntegerField()
#     title=models.CharField(max_length=200)
#     client=models.CharField(max_length=200,null=True,blank=True)
#     short_description=models.TextField(null=True,blank=True)
#     description=models.TextField(null=True,blank=True)
#     vlink=models.CharField(max_length=200,null=True,blank=True)
#     glink=models.CharField(max_length=200,null=True,blank=True)
#     pic = models.ImageField(default="blank.png", null=True, blank=True)
    
    
#     def __str__(self):
#         return f'{self.title}'

class Project(models.Model):
    srno = models.IntegerField()
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    vlink = models.CharField(max_length=200, null=True, blank=True)
    glink = models.CharField(max_length=200, null=True, blank=True)
    pic = models.ImageField(default="blank.png", null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        # Check if srno is empty
        if not self.srno:
            last_project = Project.objects.order_by('-srno').first()
            if last_project:
                self.srno = last_project.srno + 1
            else:
                # If no existing projects, set srno to 1
                self.srno = 1

        # Check if the serial number is already in use
        elif Project.objects.filter(srno=self.srno).exists():
            # If the object already exists and its srno is the same, simply save it without changing other project's srno
            if self.pk:
                super(Project, self).save(*args, **kwargs)
                return
            else:
                # Increment the serial number of existing projects with greater numbers
                existing_projects = Project.objects.filter(srno__gte=self.srno).exclude(pk=self.pk)
                for project in existing_projects:
                    project.srno += 1
                    project.save()

        super(Project, self).save(*args, **kwargs)

class Certifications(models.Model):
    category=(
    ('programming','programming'),
    ('cloud','cloud'),
    ('networking','networking'),
    ('other','other'),
    )
    srno=models.IntegerField()
    title=models.CharField(max_length=200)
    filter=models.CharField(max_length=200,choices=category)
    pic = models.ImageField(default="blank.png", null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.title}'
        
    def save(self, *args, **kwargs):
        # Check if srno is empty
        if not self.srno:
            last_certificate = Certifications.objects.order_by('-srno').first()
            if last_certificate:
                self.srno = last_certificate.srno + 1
            else:
                # If no existing certificates, set srno to 1
                self.srno = 1

        # Check if the serial number is already in use
        elif Certifications.objects.filter(srno=self.srno).exists():
            # If the object already exists and its srno is the same, simply save it without changing other certifications' srno
            if self.pk:
                super(Certifications, self).save(*args, **kwargs)
                return
            else:
                # Increment the serial number of existing certificates with greater numbers
                existing_certificates = Certifications.objects.filter(srno__gte=self.srno).exclude(pk=self.pk)
                for certificate in existing_certificates:
                    certificate.srno += 1
                    certificate.save()

        super(Certifications, self).save(*args, **kwargs)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,)
    message = models.TextField(max_length=1000, default="")


    def __str__(self):
        return f'{self.name}'

class Resume(models.Model):
     resume_image = models.ImageField( null=True, blank=True)
     resume_pdf = models.FileField( null=True, blank=True)
     
