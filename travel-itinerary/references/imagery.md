# Imagery

The photos are a signature part of this dashboard. A plan with the right pictures stops feeling like a spreadsheet and starts feeling like a preview of the trip. Two image elements matter most: the **hero** and the **per-day photos**.

## The hero image

One wide, iconic shot of the destination sits behind the title, with a gradient wash over it so the text stays readable.

- Choose the single most evocative, recognizable image of the trip (the harbor at golden hour, the volcano, the skyline). When the trip has multiple bases, pick the one that best captures the whole.
- Save it as `itinerary-images/hero.jpg`. Landscape orientation, at least ~1600px wide so it stays crisp on big screens.
- It is set in CSS on `header.hero` as a layered background: a `linear-gradient(...)` on top of `url("itinerary-images/hero.jpg")`. Retint the gradient `rgba()` values toward your palette, and adjust the `center 55%` to frame the shot.
- If you don't have a hero yet, the gradient alone still looks good. Drop the `url()` line and add the photo later.

## One photo per day

Each day card gets a real photo of where the traveler will actually be that day.

- Match the photo to the day's place or activity: the town they're based in, the site they're visiting, the boat day, the winery. A travel day can show the next destination they're heading to.
- Use the `.day-photo` figure already in the template: an `<img>` plus a short, evocative `<figcaption>`.
- **Frame the subject** with a positioning helper class on the `<img>`: `.pos-top`, `.pos-mid`, `.pos-low`, `.pos-left`, `.pos-right`. Because images are cropped to a fixed height (`object-fit:cover`), the right class keeps the landmark in view instead of cropping it out. Default to `.pos-mid` and adjust per image.
- Always write meaningful `alt` text describing the photo, and keep `loading="lazy"` so the page stays fast.
- Save each as `itinerary-images/descriptive-name.jpg` in kebab-case (e.g. `taormina-isola-bella.jpg`, `etna-wine-estate.jpg`). Descriptive names make the file easy to swap later.

## Sourcing images

Find real, openly-licensed photos. Good sources: **Wikimedia Commons**, **Unsplash**, **Pexels**, and official tourism boards. Prefer images that are clearly licensed for reuse, and capture the source so you can credit it.

Practical workflow for the agent building the dashboard:

1. For the hero and each day, decide the specific subject (place or landmark).
2. Find a high-quality, openly-licensed image of that subject and download it into `itinerary-images/` with a descriptive name. Use whatever image-search or download tools are available in the environment; respect the web and content rules of the host.
3. Note the source and photographer for the credits block.
4. Reference the file from the hero CSS or the day's `.day-photo` figure.

Keep a short, honest **credits block** at the bottom of the dashboard (the `.credits` div in the template) listing sources, photographers, and licenses where the license requires attribution. When in doubt about a license, choose a different image rather than guessing.

## Two output modes

- **Working version** (`Dashboard.html`) links to the `itinerary-images/` folder. Lighter and easy to keep editing.
- **Shareable version** (`Dashboard (Shareable).html`) embeds every image as a base64 data URI so the whole dashboard is one self-contained file that works with no folder and no internet, perfect for emailing or AirDropping to a partner or family.

Generate the shareable copy with the helper script:

```
python3 scripts/embed_images.py "path/to/Dashboard.html"
```

It reads the working HTML and its `itinerary-images/` folder, inlines every local image (including the hero's CSS `url(...)`), and writes `Dashboard (Shareable).html` next to it. Re-run it whenever the images or the dashboard change. Produce this version any time the traveler wants to share the dashboard.

## Quality bar

- Hero is sharp, well-composed, and unmistakably the destination.
- Every day has a photo that matches that day, framed so the subject is centered.
- Captions are short and warm, not just labels.
- Alt text is real and descriptive.
- Credits are present and accurate.
- The shareable version opens correctly as a single file with no broken images.
