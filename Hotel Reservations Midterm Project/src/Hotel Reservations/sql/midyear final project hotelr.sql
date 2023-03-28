--Write a query that shows whether the number of children impacts the number of nights. (group by children, get avg nights)
select children, (avg(stays_in_weekend_nights))+ (avg(stays_in_week_nights))nights
from Reservation
group by children
order by 1;

--Choose any year and choose a range of values for the adr column (average daily rate). Write a query that selects all the Reservations + Guests for that year that are
--within the chosen range and were not canceled.

select r.*, g.*
from Reservation r
join guest g
on r.GuestId = g.GuestId
where is_canceled = 0 
and arrival_date like '%2016%'
and (adr> 30 and adr<35);

--Write a query that gets the agent id with the most bookings in a given country (choose any country). Select the top 10 Reservations for that agent and country along
--with the Guest information for that row.
WITH cte AS (
SELECT TOP 1 agent, COUNT(agent) countagent
FROM Reservation
WHERE country LIKE 'IRL'
GROUP BY agent
ORDER BY 2 DESC
)
SELECT TOP 10 g.*
FROM Reservation AS r
JOIN Guest as g
ON g.GuestId = r.GuestId
JOIN cte 
ON cte.agent = r.agent
WHERE r.country LIKE 'IRL'
AND r.agent = cte.agent
