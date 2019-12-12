from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/')

# Create your models here.

class Berita(models.Model):
    judul = models.CharField(max_length=50)
    # link = judul[:15]
    # link = '-'.join(link.split(' ').lower)
    createdat = models.DateTimeField(auto_now_add=True)
    # ini jadi pertanyaan ngehandle media uploadannya laopo
    # sementara placeholder pakai link nanti jadi upload, nanti jadi handle upload video
    media = models.ImageField(storage=fs)
    content = models.CharField(max_length=1000)
    SPORT = (('Football','Football'),('NBA','National Basketball Association'),('NFL','National Football League'))
    sport = models.CharField(max_length=11, choices=SPORT)
    #pass

    def __str__(self):
        return str(self.id) + " -- " + str(self.createdat) + " -- " + self.judul

class Team(models.Model):
    # TEAM_NAME = (
    #     ('SMCU','Manchester United'),
    #     ('SRMA','Real Madrid'),
    #     ('SBAR','Barcelona'),
    #     ('SMUN','Bayern Munich'),
    #     ('SMCI','Manchester City'),
    #     ('FDAL','Dallas Cowboys'),
    #     ('FNEP','New England Patriots'),
    #     ('FNYG','New York Giants'),
    #     ('FLAR','Los Angeles Rams'),
    #     ('FWAS','Washington Redskins'),
    #     ('BNYK','New York Knicks'),
    #     ('BLAL','Los Angeles Lakers'),
    #     ('BGSW','Golden State Warriors'),
    #     ('BCHI','Chicago Bulls'),
    #     ('BBOS','Boston Celtics'),
    # ) code S - Football/Soccer, F - Football, B - Basketball followed by three
    # letter initials for said team
    team_abbr = models.CharField(max_length=4, unique=True)
    team_name = models.CharField(max_length=50)
    #pass

    def __str__(self):
        return (f"{self.team_abbr} {self.team_name}")

class Detail(models.Model):
    berita_id = models.ForeignKey(Berita, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Berita ID: {self.berita_id} Team ID: {self.team_id}")