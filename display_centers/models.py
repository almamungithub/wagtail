from django.db import models

# Create your models here.
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel


from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel


from streams import blocks



class DisplayCentersListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""
    # template = "blog/blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = DisplayCentersDetailPage.objects.live().public()
        return context

class DisplayCentersDetailPage(Page):

    center_name= models.CharField(max_length=100, blank=False, null=False,  help_text='Center Name')
    # center_address= models.TextField(help_text='Center Address')
    # center_business_hours= models.TextField(help_text='Center Business Hours')

    center_address = RichTextField(features=["bold", "italic"], null=True, help_text='Center Address')
    center_business_hours = RichTextField(features=["bold", "italic"], null=True, help_text='Center Business Hours')

    center_contact_no = models.CharField(max_length=100, blank=False, null=False, help_text='Center Contact No')



    center_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("center_name"),
        FieldPanel("center_address"),
        FieldPanel("center_business_hours"),
        FieldPanel("center_contact_no"),
        ImageChooserPanel("center_image"),
    ]



    # panels = [
    #     FieldPanel("center_name"),
    #     FieldPanel("center_address"),
    #     FieldPanel("center_business_hours"),
    #     FieldPanel("center_contact_no"),
    #     ImageChooserPanel("center_image"),
    #
    # ]


    # def __str__(self):
    #     return self.center_name

    class Meta:  # noqa
        verbose_name = "Display Center"
        verbose_name_plural = "Display Centers"