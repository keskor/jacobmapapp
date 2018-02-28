from tethys_sdk.base import TethysAppBase, url_map_maker


class Jacobmapapp(TethysAppBase):
    """
    Tethys app class for Jacobs Map App.
    """

    name = 'Jacobs Map App'
    index = 'jacobmapapp:home'
    icon = 'jacobmapapp/images/icon5.png'
    package = 'jacobmapapp'
    root_url = 'jacobmapapp'
    color = '#64b5f6'
    description = 'This is the start of a tethys app that will predect the air quality of Utah county.'
    tags = '&quot;Air Quality&quot;, &quot;ArcGIS&quot;, &quot;Tethys&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='jacobmapapp',
                controller='jacobmapapp.controllers.home'
            ),

            UrlMap(
                name='mapview',
                url='jacobmapapp/mapview',
                controller='jacobmapapp.controllers.mapview'
            ),

            UrlMap(
                name='about',
                url='jacobmapapp/about',
                controller='jacobmapapp.controllers.about'
            ),

            UrlMap(
                name='data',
                url='jacobmapapp/data',
                controller='jacobmapapp.controllers.data'
            ),

            UrlMap(
                name='proposal',
                url='jacobmapapp/proposal',
                controller='jacobmapapp.controllers.proposal'
            ),

            UrlMap(
                name='mockups',
                url='jacobmapapp/mockups',
                controller='jacobmapapp.controllers.mockups'
            ),
        )

        return url_maps

