from django.shortcuts import render

PORTFOLIO_ITEMS = [
    {
        'name': 'scholarly_editions',
        'label': 'Brill\'s Scholarly Editions',
        'href': 'https://dh.brill.com/scholarlyeditions',
        'dark_mode': True,
        'no_slides': 3,
    },
    {
        'name': 'vincent_jacob',
        'label': 'Vincent Jacob',
        'href': 'https://vincentjacobmusic.com',
        'no_slides': 3,
    },
    {
        'name': 'nco',
        'label': 'Natuurkundige Commissie Archives Online',
        'href': 'https://dh.brill.com/nco',
        'dark_mode': True,
        'no_slides': 3,
    },
    {
        'name': 'levensfilosofie',
        'label': 'Colloquium Levensfilosofie',
        'href': 'https://levensfilosofie.nu',
        'dark_mode': True,
        'no_slides': 3,
    }
]


def _get_slide_names(name, no_slides):
    return [f'images/{name}_{i + 1}.png' for i in range(no_slides)]


def home(request):
    portfolio_items = [
        {**item, 'slides': _get_slide_names(item['name'], item['no_slides'])}
        for item in PORTFOLIO_ITEMS
    ]
    return render(
        request, 'index.html', context={'portfolio_items': portfolio_items}
    )
