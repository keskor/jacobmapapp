from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'jacobmapapp/home.html', context)

def mapview(request):
    """
    map view page for my app
    """
    context={


    }

    return render(request, 'jacobmapapp/mapview.html', context)

def about(request):
    """
    about page for my app
    """
    context={


    }

    return render(request, 'jacobmapapp/about.html', context)


def data(request):
    """
    data service page for my app
    """
    context={

    }

    return render(request, 'jacobmapapp/data.html', context)

def proposal(request):
    """
    proposal page for my app
    """
    context={


    }

    return render(request, 'jacobmapapp/proposal.html', context)

def mockups(request):
    """
    mockups page for my app
    """
    context={


    }

    return render(request, 'jacobmapapp/mockups.html', context)