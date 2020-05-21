import settings


def determine_tracking_action(request):
    tracking_setting = request.cookies.get("tracking")

    if tracking_setting is None:

        return {"action": "demand_consent"}

    elif tracking_setting == "track":

        return {"action": "track", "tracking_id": settings.CARTOGRAM_GA_TRACKING_ID}

    else:

        return {"action": "do_not_track"}
