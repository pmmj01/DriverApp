from datetime import datetime
def my_cp(request):
    ctx = {
        'now': datetime.now(),
    }
    return ctx