from django.db import models

class Customer(models.Model):
    """Model definition for Customer."""
    name = models.CharField( max_length=50, blank=False, null=False)
    customer_id = models.CharField(max_length=50, blank=False, null=False)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        return self.name

class usageQueryset(models.QuerySet):
    def querysetUsage(self):
        return self.filter(usage=1)
    
    def get_usage(self):
        return self.filter(usage_gte=1)
    
class UageManger(models.Manager):
    def is_Usages(self):
        return usageQueryset(self.model, using=self._db)
    
    def equalDate(self):
        return self.filter(date__range=["2011-01-01", "2024-01-31"])
    
    def is_Usage(self):
        return self.filter(usage=2)

class Usage(models.Model):
    """Model definition for Usage."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    usage = models.IntegerField()

    # TODO: Define fields here
    #items= models.Manager()
    usage_items= UageManger()

    class Meta:
        """Meta definition for Usage."""

        verbose_name = 'Usage'
        verbose_name_plural = 'Usages'

    def __str__(self):
        """Unicode representation of Usage."""
        return str(self.customer)


