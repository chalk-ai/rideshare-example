from datetime import date

from chalk import DataFrame, has_one, feature, has_many
from chalk import _
from chalk.features import features


@features(singleton=True, max_staleness="2d")
class Averages:
    num_total_rides: float


@features
class RiderReview:
    """A review left by a Rider on a Ride"""

    id: int

    # The ID of the driver that left the review.
    ride_id: int

    # The rating that the driver left for the ride.
    rating: int = feature(min=1, max=5)

    # Note that we don't need to specify the relationship here,
    # because the relationship is already specified on the other
    # side of the relationship (Ride.rider_review).
    ride: "Ride"


@features
class Driver:
    id: int

    # The full name of the driver.
    name: str

    # The birthdate of the driver.
    dob: date

    # The age of the driver in days. Note that this feature value should
    # change with the current time, which may be different when we're
    # computing a training set vs. when we're doing inference.
    age_days: int

    # Rides completed by this driver.
    rides: "DataFrame[Ride]"

    # Here, we define the feature directly on the class, rather than
    # creating an explicit resolver. This is useful when the feature
    # is simple and doesn't require any additional logic. This definition
    # can be used both for generating training data and for inference.
    num_5_star_reviews: int = _.rides[_.rider_review.rating == 5].count()

    rides_vs_average: float


@features
class Ride:
    """A ride provided by a Driver to a Rider in a Vehicle"""

    id: int

    # The ID of the vehicle that was reserved.
    vehicle_id: int

    # The ID of the driver that reserved the vehicle.
    driver_id: int
    driver: Driver = has_one(lambda: Ride.driver_id == Driver.id)

    vehicle_id: int
    vehicle: "Vehicle"

    rider_review: RiderReview = has_one(lambda: RiderReview.ride_id == Ride.id)


@features
class VehicleModel:
    """This class allows us to implement a self-join pattern"""

    # The model of the vehicle (e.g. "Ford F-150" or "Toyota Prius").
    id: str

    vehicles: "DataFrame[Vehicle]"

    average_review: int = _.vehicles[_.average_review].mean()


@features
class Vehicle:
    id: str

    # The model of the vehicle (e.g. "Ford F-150" or "Toyota Prius").
    kind: str

    average_review: int = _.rides[_.rating].mean()
    difference_from_average_of_model: float = _.average_review - _.model.average_review

    model: VehicleModel = has_one(lambda: VehicleModel.id == Vehicle.kind)
    rides: DataFrame[Ride] = has_many(lambda: Ride.vehicle_id == Vehicle.id)
