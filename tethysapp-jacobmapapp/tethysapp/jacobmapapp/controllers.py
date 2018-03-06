from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, ToggleSwitch, RangeSlider, DatePicker

@login_required()
def home(request):
    """
        Controller for the app home page.
        """
    toggle_switch = ToggleSwitch(
        display_text='Styled Toggle',
        name='toggle2',
        on_label='Yes',
        off_label='No',
        on_style='success',
        off_style='danger',
        initial=True,
        size='large'
    )

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
        'toggle_switch': toggle_switch,
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
    toggle_switch_DEM = ToggleSwitch(
        display_text='Utah DEM',
        name='DEM_toggle',
        on_label='Yes',
        off_label='No',
        on_style='success',
        off_style='danger',
        initial=True,
        size='large'
    )

    toggle_switch_road = ToggleSwitch(
        display_text='Roads',
        name='road_toggle',
        on_label='Yes',
        off_label='No',
        on_style='success',
        off_style='danger',
        initial=True,
        size='large'
    )

    date_picker = DatePicker(
        name='date1',
        display_text='Prediction Date',
        autoclose=True,
        format='MM d, yyyy',
        start_date='3/6/2018',
        start_view='month',
        today_button=True,
        initial='March 6, 2018'
    )

    distance_slider = RangeSlider(
        display_text='Distance of Interest (km)',
        name='distance_slider',
        min=0,
        max=50,
        initial=25,
        step=5
    )

    context={
        'toggle_switch_DEM': toggle_switch_DEM,
        'toggle_switch_road': toggle_switch_road,
        'date_picker': date_picker,
        'distance_slider': distance_slider
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