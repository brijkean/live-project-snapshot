# Live Project 
## About the Project
During the last two weeks of my time at the Tech Academy, I worked with a team developing a web application in Python utilizing the Django framework. The website creates databases to help hobbyists manage collections of information relating to different hobbies— my section of the site tracks radio stations. 

We came into the project mid-lifecycle and expanded upon the basic structure of the site for each of our collection applications. This involved front-end stories creating new pages and setting their styling, and back end stories setting up the database and adding functions for the user to make changes to the database from the site. I've included in this repo some of the files that I created for my sections, other relevant code snippets that I created for the project, and screenshots displaying the app. 

<img src="community fm screenshot.png" alt="landing page of my app"> 

## Back End Stories
Setting up the database involved creating a model for the stations 
  
    class Station(models.Model):
      station_name = models.CharField(max_length=30)
      type = models.BooleanField()
      station_frequency = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
                                              help_text="<small>Leave blank for streaming-only</small>")  #allow blank=True and Null=True to account for streaming-only stations
      genre = models.CharField(max_length=30)
      country = models.CharField(max_length=30)
      state = models.CharField(max_length=30)
      station_url = models.URLField(max_length=300, default="http://")

      objects = models.Manager()

      def __str__(self):
          return self.station_name

        
and a model form that included all the inputs for the different sections of the model. 

    class StationForm(ModelForm):
      class Meta:
          model = Station
          fields = '__all__'
          labels = {'type': _('Streaming Only'),
                    }

      def clean(self):
          # allow for null and blank values if streaming-only choice is selected
          stream_only = self.cleaned_data.get('type')

          if stream_only:
              self.cleaned_data['station_frequency'] = None

          return self.cleaned_data

I created the other functions for displaying and working with the database in [views.py](https://github.com/brijkean/live-project-snapshot/blob/master/views.py).

<img src=".png" alt="">



