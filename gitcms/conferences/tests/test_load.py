import conferences.load
import conferences.models
def test_load():
    conferences.load.loaddir('conferences/tests/data/', clear=True)
    assert len(conferences.models.Conference.objects.all()) == 1

