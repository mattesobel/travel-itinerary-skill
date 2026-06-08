# How to publish this to GitHub

Two ways: the no-terminal way (easiest) and the command-line way.

## Option A — No terminal (drag and drop)

1. Go to https://github.com/new and create a new **public** repository named `travel-itinerary-skill`. Don't add a README or license (this folder already has them).
2. On the new empty repo page, click **uploading an existing file**.
3. Drag the contents of this folder in: `README.md`, `LICENSE`, `.gitignore`, `travel-itinerary.skill`, and the `travel-itinerary/` folder.
4. Click **Commit changes**.

That's it. Your share link is `https://github.com/<your-username>/travel-itinerary-skill`. People can read the README, download `travel-itinerary.skill`, or clone the repo.

## Option B — Command line

From inside this folder:

```bash
git init
git add .
git commit -m "Travel Itinerary Skill"
git branch -M main
# create the repo first at https://github.com/new (public, no README), then:
git remote add origin https://github.com/<your-username>/travel-itinerary-skill.git
git push -u origin main
```

## After publishing

- Edit the clone URL in `README.md` to point at your real repo.
- Add a few example screenshots of a finished dashboard to the README so people see what they get. (GitHub renders images you drop into the repo.)
- Pin the repo on your GitHub profile, and link it from wherever you announce it.

## Tip: a direct download link for the .skill

Once pushed, anyone can download the skill directly from:

```
https://github.com/<your-username>/travel-itinerary-skill/raw/main/travel-itinerary.skill
```

Handy to paste into a post or a message.
