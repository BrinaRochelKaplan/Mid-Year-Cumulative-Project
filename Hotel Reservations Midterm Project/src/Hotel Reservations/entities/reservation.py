from guest import Guest
from enums.distribution_channel import DistributionChannel
from enums.hotel import Hotel
from enums.meal import Meal
from enums.market_segmant import MarketSegment

class Reservation:
    def __init__(self, row):
        self.is_canceled = row['is_canceled']
        self.lead_time = row['lead_time']
        self.arrival_date_week_number = row['arrival_date_week_number']
        self.stays_in_weekend_nights = row['stays_in_weekend_nights']
        self.stays_in_week_nights = row['stays_in_week_nights']
        self.meal = Meal(row['meal'])
        self.country = row['country']
        self.market_segment = MarketSegment(row['market_segment'])
        self.distribution_channel = DistributionChannel(row['distribution_channel'])
        self.is_repeated_guest = row['is_repeated_guest']
        self.previous_cancellations = row['previous_cancellations']
        self.previous_bookings_not_canceled = row['previous_bookings_not_canceled']
        self.reserved_room_type = row['reserved_room_type']
        self.assigned_room_type = row['assigned_room_type']
        self.booking_changes = row['booking_changes']
        self.deposit_type = row['deposit_type']
        self.agent = row['agent']
        self.company = row['company']
        self.days_in_waiting_list = row['days_in_waiting_list']
        self.customer_type = row['customer_type']
        self.adr = row['adr']
        self.required_car_parking_spaces = row['required_car_parking_spaces']
        self.total_of_special_requests = row['total_of_special_requests']
        self.reservation_status = row['reservation_status']
        self.reservation_status_date = row['reservation_status_date']
        self.arrival_date = row['arrival_date']
        self.direct_booking = row['direct_booking']
        self.guest = Guest(row)
        self.hotel = Hotel(row.hotel)

    def __str__(self):
        s = str(self.guest)
        s += self.guest
        return s