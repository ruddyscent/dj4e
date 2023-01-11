import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso
    # Cultural Landscape and Archaeological Remains of the Bamiyan Valley,"<p>The cultural landscape and archaeological remains of the Bamiyan Valley represent the artistic and religious developments which from the 1st to the 13th centuries characterized ancient Bakhtria, integrating various cultural influences into the Gandhara school of Buddhist art. The area contains numerous Buddhist monastic ensembles and sanctuaries, as well as fortified edifices from the Islamic period. The site is also testimony to the tragic destruction by the Taliban of the two standing Buddha statues, which shook the world in March 2001.</p>","<p><em>Criterion (i):</em> The Buddha statues and the cave art in Bamiyan Valley are an outstanding representation of the Gandharan school in Buddhist art in the Central Asian region.</p> <p><em>Criterion (ii)</em> : The artistic and architectural remains of Bamiyan Valley, and an important Buddhist centre on the Silk Road, are an exceptional testimony to the interchange of Indian, Hellenistic, Roman, Sasanian influences as the basis for the development of a particular artistic expression in the Gandharan school. To this can be added the Islamic influence in a later period.</p> <p><em>Criterion (iii):</em> The Bamiyan Valley bears an exceptional testimony to a cultural tradition in the Central Asian region, which has disappeared.</p> <p><em>Criterion (iv):</em> The Bamiyan Valley is an outstanding example of a cultural landscape which illustrates a significant period in Buddhism.</p> <p><em>Criterion (vi):</em> The Bamiyan Valley is the most monumental expression of the western Buddhism. It was an important centre of pilgrimage over many centuries. Due to their symbolic values, the monuments have suffered at different times of their existence, including the deliberate destruction in 2001, which shook the whole world.</p>",2003,67.82525,34.84694,158.9265,Cultural,Afghanistan,Asia and the Pacific,af
    # Minaret and Archaeological Remains of Jam,"<p>The 65m-tall Minaret of Jam is a graceful, soaring structure, dating back to the 12th century. Covered in elaborate brickwork with a blue tile inscription at the top, it is noteworthy for the quality of its architecture and decoration, which represent the culmination of an architectural and artistic tradition in this region. Its impact is heightened by its dramatic setting, a deep river valley between towering mountains in the heart of the Ghur province.</p>",<p><em>Criterion (ii):</em> The innovative architecture and decoration of the Minaret of Jam played a significant role in the development of the arts and architecture of the Indian sub-continent and beyond.</p> <p><em>Criterion (iii): </em>The Minaret of Jam and its associated archaeological remains constitute exceptional testimony to the power and quality of the Ghurid civilization that dominated its region in the 12th and 13th centuries.</p> <p><em>Criterion (iv): </em>The Minaret of Jam is an outstanding example of Islamic architecture and ornamentation in this region and played a significant role in their further dissemination.</p>,2002,64.51588889,34.39641667,70,Cultural,Afghanistan,Asia and the Pacific,af


    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        
        site = Site(
            name=row[0], description=row[1], justification=row[2], 
            year=None if row[3] == '' else row[3], 
            longitude=None if row[4] == '' else row[4], 
            latitude=None if row[5] == '' else row[5], 
            area_hectares=None if row[6] == '' else row[6], 
            category=c, state=s, region=r, iso=i
            )
        site.save()
        
