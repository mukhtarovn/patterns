from wavy import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
}


def secret_controller(request):
    request['secret_key'] = 'This is FrontController'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)

