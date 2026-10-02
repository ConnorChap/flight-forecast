# Model Plan

## Goal
Build a simple model to predict flight delays using historical flight and weather data.

## Tasks
- Clean the data.
- Create useful features.
- Train a basic ML model.
- Save the trained model as a `.pkl` file.

## Notes
- Keep the model simple.
- Test it on a validation set.
- Make sure the backend can load the saved model.

## Historical weather
- Source: `https://mesonet.agron.iastate.edu/api/`
- 2022 - 2025
- Denver
- Columns:
    * station = airport code
    * valid = timestamp
    * tmpf = air tempture (F)
    * sknt = sustained wind speed
    * gust = peak wind gust
    * vsby = visibility
    * p01i = percipitation in the past hour
    * wxcodes = present weather codes
    * skyc1 = cloud cover of the lowest layer

### wxcodes
* Descriptors:	BC (Patches), BL (Blowing), DR (Low Drifting), FZ       (Freezing), SH (Showers), TS (Thunderstorm)

* Precipitation:	DZ (Drizzle), GR (Hail), IC (Ice Crystals), PL (Ice Pellets), RA (Rain), SN (Snow), SG (Snow Grains)

* Obstructions to Vision:	BR (Mist), DU (Widespread Dust), FG (Fog), FU (Smoke), HZ (Haze), VA (Volcanic Ash)

## Historical flight arrivals
- Source: `https://www.transtats.bts.gov/ontime/Arrivals.aspx`
- 2022 - 2025

### Airline map
- Southwest = wn
- Sprit = Kn
- 
