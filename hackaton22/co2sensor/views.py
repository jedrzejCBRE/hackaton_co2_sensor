from django.shortcuts import render
from rest_api.models import MotorSpeed
import random
# Create your views here.
import environ

# Initialise environment variables
env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent

#environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


def main_calculation(request):
    sensor_ppm = random.randrange(500,1000)
    max_speed = 61
    min_speed = 30
    ppm_leap = 4
    speed_leap = 0.4
    if sensor_ppm >= 1000:
        fan_speed = max_speed
    elif sensor_ppm <= 700:
        fan_speed = min_speed
    else:
        ppms = (1000-sensor_ppm)/ppm_leap
        fan_speed = round(max_speed-(speed_leap*ppms),2)
    MotorSpeed.objects.filter(pk = 1).update(hz_speed = fan_speed)
    return render(request, "home_info.html",{"level_of_co2": sensor_ppm, "fan_speed":fan_speed})