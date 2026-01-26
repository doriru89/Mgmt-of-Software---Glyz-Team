# Oxfam income inequality slides

This folder contains a short slide deck and two figures for the
"Trends in Global Income" conference prompt.

## Files

- `slides.md` - Slide content in Markdown.
- `generate_figures.py` - Script that renders the charts.
- `data/` - CSV inputs used by the script.
- `figures/` - Exported PNG and SVG images.

## Regenerate figures

```bash
python3 docs/oxfam_income_inequality/generate_figures.py
```

## Data note

The current CSV values are stylized for discussion. Replace them with
the latest official values (e.g., WID.world or World Bank) before final
submission if required.
