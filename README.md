# rinobot-plugin-rebin

## Example

Call it with arguments:

## Options

```
rebin --bin_multiple=4 --xtime=True --algo=[avg, max, sum]
```

It will rebin xyyy data and resize the bin to whatever bin_multiple times the current bin size it.
So bin_multiple of 4 makes the bin 4 times bigger.

- `bin_multiple` whatever the new bin size is as a multiple of the old bin size.
- `algo` can be `avg`, `max` or `sum` to make the new values the average, max or sum of the values in the new bin.
- `xtime` (optional - default `false`) if set to true, the algorithm will treat the first column as
a time axis and only the values in the bin it.

## Output

File called `{filename}-rebin[{algo}-{bin_multiple}].txt`
