# rinobot-plugin-rebin

Rebin xyyy data and resize the bin to whatever binsize times the current bin size it.
So binsize of 4 makes the bin 4 times bigger.

## Options

- binsize whatever the new bin size is as a multiple of the old bin size.
- algo can be `avg`, `max` or `sum` to make the new values the average, max or sum of the values in the new bin.
- xtime (optional - default `false`) if set to true, the algorithm will treat the first column as
a time axis and only the values in the bin it.
