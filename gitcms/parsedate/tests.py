import parsedate
def test_parsedate():
    assert parsedate.parsedate('4 April 2010') == parsedate.parsedate('April 4 2010')
    assert parsedate.parsedatetime('4 April 2010 19:02') == parsedate.parsedatetime('April 4 2010 19:02')

