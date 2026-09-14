# HomeForge Home Assistant blueprints

Reusable starting points for practical automations. Review entity selections and test every automation before relying on it.

## Motion light with timeout

Import `motion-light-with-timeout.yaml`, choose a motion or occupancy sensor, choose a light, and set how long the area must stay clear before shutoff.

This blueprint intentionally keeps the first version simple. Add time-of-day brightness, illuminance conditions, and manual-override logic only after the basic behavior is reliable.

Full setup guide: https://estivonponcho.github.io/homeforge/guides/home-assistant-beginners-guide.html
