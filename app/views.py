from django.shortcuts import render


def index(request):
    """
    Display an individual :model:`app.SampleTable`.

    **Context**

    ``message``
        sample message :model:`app.SampleTable`.

    **Template:**

    :template:`app/index.html`
    """
    message = "This is Index Page."
    params = {
        "message": message,
    }
    return render(request, 'app/index.html', params)