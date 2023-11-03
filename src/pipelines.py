from chalk import online, Now, _
from src.models import Driver, Averages


@online
def get_driver_age(dob: Driver.dob, now: Now) -> Driver.age_days:
    """The age of the driver in days.
    This feature is computed relative to `Now`, which changes based
    on whether we're computing a training set or doing inference."""
    return (now.date() - dob).days


@online
def get_rides_vs_avg(
    rides: Driver.rides[_.id],
    avg: Averages.num_total_rides,
) -> Driver.rides_vs_average:
    """The number of rides that this driver has given, relative to the
    average number of rides given by all drivers.
    Note that here we're taking in features from two namespaces:
    `Driver.rides` and `Averages.num_total_rides`.
    We can do this because `Averages` is a singleton feature class,
    and so it's always available to us.
    """
    return rides.count() / avg
