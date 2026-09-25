# Frontend Plan

## Goal
Create a simple page where a user can enter flight info and see a delay prediction.

## Flight Entry
Users manually enter details for a flight arriving at Denver International Airport (DEN). The app uses these inputs to estimate the likelihood of an arrival delay based on historical flight data.

| Form label | Example | Historical data field |
|---|---|---|
| Airline | United Airlines | `Reporting_Airline` |
| Departure airport | Chicago O'Hare (ORD) | `Origin` |
| Flight date | October 15, 2026 | `FlightDate` |
| Scheduled departure time | 2:30 PM | `CRSDepTime` |
| Scheduled arrival time at DEN | 4:10 PM | `CRSArrTime` |
| Arrival airport | Denver International (DEN) | `Dest` — fixed to `DEN` |

Prediction: Likelihood that the flight arrives at DEN at least 15 minutes late (`ArrDel15`).

The app does not look up or verify the flight's current status. Its result is a historical delay estimate, not a live flight update.

## Tasks
- Build a form with airline, airport, and day inputs.
- Send the data to the backend API.
- Show the prediction result on the page.

## Notes
- Keep the design simple.
- Validate input fields.
- Test that the frontend works with the backend.
