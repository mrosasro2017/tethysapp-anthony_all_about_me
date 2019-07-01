from tethys_sdk.base import TethysAppBase, url_map_maker


class AnthonyAllAboutMe(TethysAppBase):
    """
    Tethys app class for Anthony All About Me.
    """

    name = 'Anthony All About Me'
    index = 'anthony_all_about_me:home'
    icon = 'anthony_all_about_me/images/icon.gif'
    package = 'anthony_all_about_me'
    root_url = 'anthony-all-about-me'
    color = '#a80306'
    description = 'Place a brief description of your app here.'
    tags = ''
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
                url='anthony-all-about-me',
                controller='anthony_all_about_me.controllers.home'
            ),
        )

        return url_maps
